#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["youtube-transcript-api>=1.0.0", "yt-dlp>=2024.0.0", "requests>=2.31"]
# ///
"""Haal de tekst (ondertitels) op van de laatste video's van een YouTube-kanaal of playlist.

Wat het doet:
  1. Pakt de N nieuwste video's van een kanaal/playlist (yt-dlp, alleen de lijst - geen download).
  2. Haalt per video de ONDERTITELS op via youtube-transcript-api (YouTube heeft die al).
     Geen video/audio-download, geen ffmpeg, geen Whisper. Gratis.
  3. Schrijft per video een leesbaar .md-bestand met de tekst.
  Al-opgehaalde video's worden overgeslagen (herkenbaar aan het video-ID in de naam).

Blokkade-bescherming (v3, 4 augustus 2026):
  - Random jitter (8-20s) tussen video's in plaats van een vaste pauze.
    Kleine batches (t/m 15 nog op te halen video's) krijgen automatisch een
    snelpad met korte jitter (2-4s): de blokkade komt pas na ~30 snelle
    verzoeken, dus daar is de lange pauze onnodig. Expliciete --min-pauze/
    --max-pauze/--pauze winnen altijd; --pauze N is de oude vaste pauze (alias).
  - Drie lokale routes achter elkaar, elk met een andere client-handtekening;
    bij een block gaat 'ie door naar de volgende:
      1. youtube-transcript-api
      2. yt-dlp caption-route
      3. InnerTube (rechtstreeks youtubei.googleapis.com/youtubei/v1/player
         met de mobiele ANDROID/IOS-clients - de handtekening waar YouTube
         het minst streng op is)
  - Rustpauze (5 min) na elke 15 lokale fetches.
  - Bij een block op alle drie de routes: 15 min cooldown, dan opnieuw proberen.
  - Lukt het na de cooldown nog niet en is er een Apify-key: overschakelen
    naar de Apify-afvanger voor de rest.
  - State file (.transcript_state.json) in de doelmap: hervat altijd waar
    het bleef, ook na een ctrl-c of een blokkade.

Gebruik (via uv, dat installeert de pakketjes zelf):
    uv run transcribeer.py "https://www.youtube.com/@kanaalnaam"
    uv run transcribeer.py "https://www.youtube.com/playlist?list=..." --max 10
    uv run transcribeer.py "<url>" --taal nl --vertaal        # ondertitels vertalen naar NL
    uv run transcribeer.py "<url>" --bouw-skill meta-ads       # + kennis-skill bouwen (Claude maakt 'm af)
    uv run transcribeer.py "<url>" --apify                     # direct via Apify (~$0,01/video)
    uv run transcribeer.py "<url>" --geen-apify                # puur lokaal, nooit Apify

Standaard-opslagplek: als config.json (naast dit script) een 'kennis_map' bevat, komen de
transcripties in <kennis_map>/<kanaal>. De installatie-wizard vraagt daarnaar bij het installeren.

Taal: standaard zoekt 'ie een Nederlandse ondertitel; bestaat die niet, dan pakt 'ie de beste
beschikbare in de oorspronkelijke taal. Met --vertaal laat je YouTube 'm naar --taal vertalen.
Via de Apify-route is de taalcode een schatting (stopwoorden-heuristiek).

Gemaakt door Bart Boonstra (Slim Werken AI).
"""
from __future__ import annotations
import argparse, json, os, random, re, subprocess, sys, time
from pathlib import Path

YTDLP = [sys.executable, "-m", "yt_dlp"]
SCRIPT_DIR = Path(__file__).resolve().parent
APIFY_ACTOR = "pintostudio~youtube-transcript-scraper"
STATE_FILE = ".transcript_state.json"

NL_WOORDEN = {"de", "het", "een", "en", "van", "dat", "je", "niet", "ook", "maar", "voor", "zijn", "dus", "wel", "gaan", "naar"}
EN_WOORDEN = {"the", "and", "that", "you", "not", "for", "this", "with", "are", "have", "going", "what", "about", "just"}

# Defaults voor rate-limit-bescherming
MIN_DELAY = 8
MAX_DELAY = 20
REST_EVERY = 15
REST_SECS = 300
COOLDOWN_SECS = 900

# Klein-batch-snelpad: de blokkade komt in de praktijk pas na ~30 snelle verzoeken,
# dus bij weinig op te halen video's kan de jitter fors korter. De dual-route- en
# cooldown-bescherming blijven ook dan gewoon actief als vangnet.
SMALL_BATCH = 15
SMALL_MIN = 2.0
SMALL_MAX = 4.0


# ---------- helpers ----------

def die(msg, code=1):
    print(f"\n[FOUT] {msg}", file=sys.stderr)
    sys.exit(code)


def safe_name(text, maxlen=80):
    text = re.sub(r'[\\/:*?"<>|]', "", text).strip()
    text = re.sub(r"\s+", " ", text)
    return text[:maxlen].strip() or "video"


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "kanaal"


def load_config():
    cfg = SCRIPT_DIR / "config.json"
    if cfg.exists():
        try:
            return json.loads(cfg.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def apify_token():
    if os.environ.get("APIFY_API_KEY"):
        return os.environ["APIFY_API_KEY"].strip()
    for kandidaat in (SCRIPT_DIR / ".env", SCRIPT_DIR.parents[2] / ".env", Path.cwd() / ".env"):
        if kandidaat.exists():
            for line in kandidaat.read_text(encoding="utf-8").splitlines():
                if line.strip().replace(" ", "").startswith("APIFY_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip()
    return None


def taal_heuristiek(text):
    woorden = re.findall(r"[a-zà-ÿ']+", text.lower()[:8000])
    nl = sum(1 for w in woorden if w in NL_WOORDEN)
    en = sum(1 for w in woorden if w in EN_WOORDEN)
    return "nl (geschat)" if nl >= en else "en (geschat)"


# ---------- state (resume-ondersteuning) ----------

def load_state(out_dir):
    p = out_dir / STATE_FILE
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"done": {}, "failed": {}}


def save_state(out_dir, state):
    (out_dir / STATE_FILE).write_text(json.dumps(state, indent=1), encoding="utf-8")


def already_done(out_dir, vid, state):
    if vid in state["done"]:
        return True
    # Glob for files containing [VIDEO_ID] in the name
    pattern = "*[[]" + vid + "[]]*"
    if any(out_dir.glob(pattern)):
        state["done"][vid] = vid
        return True
    return False


# ---------- yt-dlp: alleen de lijst ophalen (geen download) ----------

def normalize_channel_url(url):
    u = url.split("?")[0].rstrip("/")
    is_channel = any(s in u for s in ("/@", "/channel/", "/c/", "/user/"))
    already_tab = u.endswith(("/videos", "/streams", "/shorts", "/featured"))
    if is_channel and not already_tab:
        return u + "/videos"
    return url


def list_latest(url, n):
    candidates = [normalize_channel_url(url)]
    if candidates[0] != url:
        candidates.append(url)
    proc = None
    for cand in candidates:
        cmd = YTDLP + ["--flat-playlist", "--playlist-end", str(n),
                       "--dump-json", "--no-warnings", cand]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0 and proc.stdout.strip():
            break
    if proc is None or proc.returncode != 0:
        die("yt-dlp kon de video-lijst niet ophalen. Klopt de URL?\n"
            + (proc.stderr.strip() if proc else ""))
    entries = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        vid = d.get("id")
        if not vid:
            continue
        entries.append({
            "id": vid,
            "title": d.get("title") or vid,
            "url": d.get("url") or "https://www.youtube.com/watch?v=" + vid,
        })
    if not entries:
        die("Geen video's gevonden op die URL.")
    return entries[:n]


def channel_label(url):
    m = re.search(r"@([A-Za-z0-9._-]+)", url)
    if m:
        return safe_name(m.group(1), 60)
    try:
        out = subprocess.run(
            YTDLP + ["--flat-playlist", "--playlist-end", "1",
                     "--print", "%(channel|playlist_title|uploader)s", "--no-warnings",
                     normalize_channel_url(url)],
            capture_output=True, text=True, timeout=60)
        name = (out.stdout.strip().splitlines() or [""])[0]
        if name and name != "NA":
            return safe_name(name, 60)
    except Exception:
        pass
    return "kanaal"


# ---------- ondertitels ophalen: route 1 (youtube-transcript-api) ----------

class IpBlockedError(Exception):
    pass


BLOK_NAMEN = ("IpBlocked", "RequestBlocked", "TooManyRequests", "YouTubeRequestFailed")
# YouTube blokkeert tegenwoordig vaker met een bot-check dan met een kale 429.
# Die komt via alle routes binnen als een gewone foutmelding, dus herkennen we 'm
# aan de tekst - anders boeken we een blokkade weg als 'video zonder ondertitels'
# en slaat de cooldown nooit aan.
# google.com/sorry is de bot-muur waar YouTube je naartoe stuurt bij verdacht
# verkeer; die redirect komt per route in een ander jasje naar buiten.
BLOK_TEKSTEN = ("429", "too many requests", "blocking requests from your ip",
                "sign in to confirm", "confirm you're not a bot",
                "confirm you are not a bot", "bevestigen dat je geen bot bent",
                "google.com/sorry", "/sorry/index")


def lijkt_op_blokkade(exc):
    return type(exc).__name__ in BLOK_NAMEN or any(s in str(exc).lower() for s in BLOK_TEKSTEN)


def fetch_captions(video_id, taal, vertaal):
    """Route 1: youtube-transcript-api.
    Geeft (tekst, taalcode, vertaald_bool) of (None, reden, False).
    Gooit IpBlockedError bij een rate-limit-block."""
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()
    try:
        tl = api.list(video_id)
    except Exception as e:
        if lijkt_op_blokkade(e):
            raise IpBlockedError(str(e)) from e
        return None, "geen ondertitels (" + type(e).__name__ + ")", False

    transcript = None
    try:
        transcript = tl.find_transcript([taal, "en", "en-US", "en-GB"])
    except Exception:
        transcript = None
    translated = False
    if transcript is None:
        available = list(tl)
        if not available:
            return None, "geen ondertitels beschikbaar", False
        generated = [t for t in available if t.is_generated]
        transcript = (generated or available)[0]

    if vertaal and transcript.language_code != taal and getattr(transcript, "is_translatable", False):
        try:
            transcript = transcript.translate(taal)
            translated = True
        except Exception:
            translated = False

    try:
        fetched = transcript.fetch()
    except Exception as e:
        if lijkt_op_blokkade(e):
            raise IpBlockedError(str(e)) from e
        return None, "ophalen mislukt (" + type(e).__name__ + ")", False

    snippets = getattr(fetched, "snippets", fetched)
    parts = []
    for s in snippets:
        t = (getattr(s, "text", None) or (s.get("text") if isinstance(s, dict) else "") or "").strip()
        if t:
            parts.append(t)
    text = " ".join(parts).strip()
    if not text:
        return None, "lege ondertitel", False
    return text, transcript.language_code, translated


# ---------- ondertitels ophalen: route 2 (yt-dlp caption-URL's) ----------

def fetch_captions_ytdlp(video_id, taal):
    """Route 2: yt-dlp's caption-URL's (andere client-handtekening).
    Werkt vaak nog als de transcript-api al geblokkeerd is.
    Geeft (tekst, taalcode, False) of (None, reden, False).
    Gooit IpBlockedError bij een 429."""
    import urllib.error, urllib.request
    from yt_dlp import YoutubeDL
    # De bot-check komt hier als een gewone DownloadError naar buiten, niet als 429.
    try:
        with YoutubeDL({"quiet": True, "no_warnings": True, "skip_download": True}) as ydl:
            info = ydl.extract_info("https://www.youtube.com/watch?v=" + video_id, download=False)
    except Exception as e:
        if lijkt_op_blokkade(e):
            raise IpBlockedError(str(e)[:200]) from e
        raise
    tracks = {}
    for source in (info.get("subtitles") or {}, info.get("automatic_captions") or {}):
        for lang, formats in source.items():
            tracks.setdefault(lang, formats)
    formats = None
    chosen_lang = None
    for lang in (taal, "en", taal + "-orig", "en-orig"):
        if lang in tracks:
            formats = tracks[lang]
            chosen_lang = lang
            break
    if not formats and tracks:
        chosen_lang, formats = next(iter(tracks.items()))
    if not formats:
        return None, "geen ondertiteling beschikbaar (yt-dlp)", False
    fmt = next((f for f in formats if f.get("ext") == "json3"), formats[0])
    req = urllib.request.Request(fmt["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise IpBlockedError("429 op caption-URL (yt-dlp-route)") from e
        return None, "yt-dlp caption HTTP " + str(e.code), False
    data = json.loads(raw)
    parts = []
    for event in data.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in event.get("segs", [])).strip()
        if text and text != "\n":
            parts.append(text.replace("\n", " "))
    text = " ".join(parts).strip()
    if not text:
        return None, "caption-bestand was leeg (yt-dlp)", False
    lang_clean = chosen_lang.replace("-orig", "") if chosen_lang else taal
    return text, lang_clean, False


# ---------- ondertitels ophalen: route 3 (InnerTube, rechtstreeks) ----------

# De mobiele clients krijgen een player-antwoord met caption-tracks zonder PO-token;
# de WEB-client geeft daar tegenwoordig UNPLAYABLE op. Op volgorde van betrouwbaarheid.
INNERTUBE_URL = "https://youtubei.googleapis.com/youtubei/v1/player"
INNERTUBE_KEY = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
TIMEDTEXT_BACKOFF = [(8, 12), (25, 35)]
INNERTUBE_CLIENTS = [
    ({"clientName": "ANDROID", "clientVersion": "20.10.38", "androidSdkVersion": 30},
     "com.google.android.youtube/20.10.38 (Linux; U; Android 11) gzip"),
    ({"clientName": "IOS", "clientVersion": "20.10.4", "deviceModel": "iPhone16,2"},
     "com.google.ios.youtube/20.10.4 (iPhone16,2; U; CPU iOS 18_3 like Mac OS X)"),
    ({"clientName": "ANDROID_VR", "clientVersion": "1.62.27", "deviceModel": "Quest 3",
      "androidSdkVersion": 32},
     "com.google.android.apps.youtube.vr.oculus/1.62.27 (Linux; U; Android 12; Quest 3) gzip"),
]


def _is_botcheck(status, reason):
    """LOGIN_REQUIRED betekent hier niet 'privevideo' maar de bot-check
    ('Log in om te bevestigen dat je geen bot bent') - oftewel een blokkade
    op het IP, geen video die er niet is. De reden-tekst is vertaald naar --taal,
    dus de status is leidend en de tekst alleen een vangnet."""
    if status == "LOGIN_REQUIRED":
        return True
    low = (reason or "").lower()
    return any(s in low for s in BLOK_TEKSTEN)


def _innertube_player(video_id, client, user_agent, taal):
    """Eén player-call. Geeft (data, status, reden); data is None als deze
    client de video niet mag zien."""
    import urllib.error, urllib.request
    ctx = dict(client)
    ctx["hl"] = taal
    ctx["gl"] = "NL"
    body = json.dumps({
        "context": {"client": ctx},
        "videoId": video_id,
        "contentCheckOk": True,
        "racyCheckOk": True,
    }).encode("utf-8")
    req = urllib.request.Request(
        INNERTUBE_URL + "?key=" + INNERTUBE_KEY, data=body,
        headers={"Content-Type": "application/json", "User-Agent": user_agent,
                 "X-Youtube-Client-Name": client["clientName"],
                 "X-Youtube-Client-Version": client["clientVersion"]})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="ignore"))
    except urllib.error.HTTPError as e:
        if e.code in (429, 403):
            raise IpBlockedError("HTTP " + str(e.code) + " op de InnerTube-player") from e
        raise
    ps = data.get("playabilityStatus") or {}
    status, reason = ps.get("status"), ps.get("reason")
    if status != "OK":
        return None, status, reason
    return data, status, reason


def _kies_innertube_track(tracks, taal):
    """Voorkeur: gevraagde taal, dan Engels; binnen een taal handmatig boven automatisch."""
    def zelfde_taal(track, code):
        lc = track.get("languageCode") or ""
        return lc == code or lc.split("-")[0] == code.split("-")[0]

    for code in (taal, "en"):
        kandidaten = [t for t in tracks if zelfde_taal(t, code)]
        handmatig = [t for t in kandidaten if t.get("kind") != "asr"]
        if handmatig:
            return handmatig[0]
        if kandidaten:
            return kandidaten[0]
    return tracks[0]


def _timedtext_url(base_url, **extra):
    """fmt en tlang staan niet in 'sparams', dus die mogen we herschrijven
    zonder de signature in de URL ongeldig te maken."""
    import urllib.parse
    parts = urllib.parse.urlparse(base_url)
    query = urllib.parse.parse_qs(parts.query)
    for key, value in extra.items():
        query[key] = [value]
    return urllib.parse.urlunparse(parts._replace(query=urllib.parse.urlencode(query, doseq=True)))


def fetch_captions_innertube(video_id, taal, vertaal):
    """Route 3: rechtstreeks de InnerTube-player bevragen.
    Zelfde contract als fetch_captions: (tekst, taalcode, vertaald_bool)
    of (None, reden, False). Gooit IpBlockedError bij een rate-limit-block."""
    import urllib.error, urllib.request

    # Elke client krijgt een kans: waar de een een bot-check vangt, komt de ander
    # er vaak nog gewoon langs. Pas als geen enkele client binnenkomt tellen we de
    # bot-check als blokkade - dan mag de cooldown zijn werk doen.
    data = None
    botcheck = False
    laatste = "geen speelbaar antwoord"
    for client, user_agent in INNERTUBE_CLIENTS:
        try:
            data, status, reason = _innertube_player(video_id, client, user_agent, taal)
        except IpBlockedError:
            raise
        except Exception as e:
            if lijkt_op_blokkade(e):
                raise IpBlockedError(str(e)[:200]) from e
            laatste = type(e).__name__
            continue
        if data is not None:
            break
        laatste = str(reason or status or laatste)
        if _is_botcheck(status, reason):
            botcheck = True
    if data is None:
        if botcheck:
            raise IpBlockedError("InnerTube-bot-check: " + laatste)
        return None, "innertube: " + laatste, False

    tracklist = (data.get("captions") or {}).get("playerCaptionsTracklistRenderer") or {}
    tracks = tracklist.get("captionTracks") or []
    if not tracks:
        return None, "geen ondertitels beschikbaar (innertube)", False

    track = _kies_innertube_track(tracks, taal)
    lang = track.get("languageCode") or taal
    translated = False
    params = {"fmt": "json3"}
    if vertaal and lang.split("-")[0] != taal.split("-")[0] and track.get("isTranslatable"):
        params["tlang"] = taal
        translated = True

    # De timedtext-endpoint knijpt snel af, maar laat net zo snel weer los. Drie
    # pogingen met oplopende backoff (~10s, ~30s) kost in het slechtste geval een
    # halve minuut; dat is een stuk goedkoper dan de cooldown van 15 minuten die
    # er anders achteraan komt. Pas als ook de laatste poging 429 geeft is het raak.
    url = _timedtext_url(track["baseUrl"], **params)
    raw = None
    for poging in range(len(TIMEDTEXT_BACKOFF) + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8", errors="ignore")
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                if poging < len(TIMEDTEXT_BACKOFF):
                    lo, hi = TIMEDTEXT_BACKOFF[poging]
                    time.sleep(random.uniform(lo, hi))
                    continue
                raise IpBlockedError("429 op de timedtext-URL (innertube-route)") from e
            return None, "innertube caption HTTP " + str(e.code), False
    if not raw:
        return None, "innertube: leeg caption-antwoord", False

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return None, "innertube: onverwacht caption-formaat", False
    parts = []
    for event in payload.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in event.get("segs", [])).strip()
        if text and text != "\n":
            parts.append(text.replace("\n", " "))
    text = " ".join(parts).strip()
    if not text:
        return None, "innertube: lege ondertitel", False
    return text, (taal if translated else lang), translated


# ---------- ondertitels ophalen: route 4 (Apify-afvanger, ~$0,01/video) ----------

def fetch_apify(token, video_id):
    """Zelfde contract als fetch_captions: (tekst, taalcode, False) of (None, reden, False)."""
    import requests
    try:
        r = requests.post(
            "https://api.apify.com/v2/acts/" + APIFY_ACTOR + "/run-sync-get-dataset-items",
            params={"token": token, "timeout": 120},
            json={"videoUrl": "https://www.youtube.com/watch?v=" + video_id},
            timeout=150)
        r.raise_for_status()
        items = r.json()
    except Exception as e:
        detail = ""
        resp = getattr(e, "response", None)
        if resp is not None:
            try:
                detail = ": " + (resp.json().get("error", {}).get("message") or "HTTP " + str(resp.status_code))
            except Exception:
                detail = ": HTTP " + str(resp.status_code)
        return None, "apify mislukt (" + type(e).__name__ + detail + ")", False
    if not isinstance(items, list) or not items:
        return None, "apify: leeg antwoord", False
    segs = items[0].get("data")
    if not segs or not isinstance(segs, list):
        return None, "apify: geen transcript gevonden", False
    parts = [s.get("text", "").strip() for s in segs if s.get("text", "").strip()]
    text = " ".join(parts).strip()
    if not text:
        return None, "apify: lege transcript", False
    return text, taal_heuristiek(text), False


# ---------- de lokale routes achter elkaar ----------

class AllesGeblokkeerdError(Exception):
    """Elke lokale route liep op een blokkade - tijd voor de cooldown."""


def lokale_routes(taal, vertaal):
    """De routes op volgorde. Elk een andere client-handtekening richting YouTube,
    dus een blokkade op de een betekent lang niet altijd een blokkade op de ander."""
    return [
        ("transcript-api", lambda vid: fetch_captions(vid, taal, vertaal)),
        ("yt-dlp", lambda vid: fetch_captions_ytdlp(vid, taal)),
        ("innertube", lambda vid: fetch_captions_innertube(vid, taal, vertaal)),
    ]


def haal_lokaal(video_id, routes, head):
    """Loopt de routes af tot er één ondertitels teruggeeft.

    Geeft (tekst, taalcode, vertaald, routenaam, pogingen). Vond geen enkele route
    ondertitels, dan is tekst None en staat de laatste reden op de plek van de taalcode.
    Zijn ALLE routes geblokkeerd, dan volgt een AllesGeblokkeerdError."""
    reden = "geen ondertitels"
    geblokkeerd = 0
    pogingen = 0
    for naam, fetch in routes:
        pogingen += 1
        try:
            text, lang, translated = fetch(video_id)
        except IpBlockedError:
            geblokkeerd += 1
            print(head + " - " + naam + "-route geblokkeerd")
            continue
        except Exception as e:
            reden = naam + ": " + type(e).__name__
            continue
        if text is not None:
            return text, lang, translated, naam, pogingen
        reden = lang
    if geblokkeerd == len(routes):
        raise AllesGeblokkeerdError()
    return None, reden, False, None, pogingen


# ---------- output ----------

def write_transcript(out_dir, meta, text, index, lang, translated, route=None):
    title_safe = safe_name(meta["title"])
    vid = meta["id"]
    fname = str(index).zfill(2) + " - " + title_safe + " [" + vid + "].md"
    taal_regel = lang + (" (vertaald)" if translated else "")
    lines = [
        "# " + meta["title"],
        "",
        "- **Video:** https://www.youtube.com/watch?v=" + vid,
        "- **Ondertitel-taal:** " + taal_regel,
        "- **Bron:** YouTube-ondertitels" + (" (via " + route + ")" if route else ""),
        "",
        "---",
        "",
        text,
        "",
    ]
    (out_dir / fname).write_text("\n".join(lines), encoding="utf-8")
    return fname


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description="Haal de ondertitels van de laatste YouTube-video's op als tekst.")
    ap.add_argument("url", help="YouTube-kanaal- of playlist-URL")
    ap.add_argument("--max", type=int, default=20, help="aantal nieuwste video's (default 20)")
    ap.add_argument("--out", default=None,
                    help="doelmap (default: <kennis_map>/<kanaal> uit config.json, anders ./transcripties/<kanaal>)")
    ap.add_argument("--taal", default="nl", help="voorkeurstaal van de ondertitels (default nl)")
    ap.add_argument("--vertaal", action="store_true",
                    help="ondertitels naar --taal vertalen als ze in een andere taal zijn")
    ap.add_argument("--min-pauze", type=float, default=None,
                    help="minimale pauze tussen video's in seconden (default " + str(MIN_DELAY)
                         + "; kleine batches t/m " + str(SMALL_BATCH) + " video's: " + str(SMALL_MIN) + ")")
    ap.add_argument("--max-pauze", type=float, default=None,
                    help="maximale pauze tussen video's in seconden (default " + str(MAX_DELAY)
                         + "; kleine batches t/m " + str(SMALL_BATCH) + " video's: " + str(SMALL_MAX) + ")")
    ap.add_argument("--pauze", type=float, default=None,
                    help="vaste pauze in seconden (alias van vroeger; zet min- en max-pauze allebei op deze waarde)")
    ap.add_argument("--apify", action="store_true",
                    help="direct via Apify ophalen (~$0,01/video), zonder eerst lokaal te proberen")
    ap.add_argument("--geen-apify", dest="geen_apify", action="store_true",
                    help="nooit naar Apify overschakelen, ook niet bij een blokkade")
    ap.add_argument("--bouw-skill", dest="bouw_skill", nargs="?", const="__auto__", default=None,
                    help="bouw na het ophalen een kennis-skill van dit kanaal (optioneel: skill-naam)")
    args = ap.parse_args()
    cfg = load_config()

    label = channel_label(args.url)
    if args.out:
        out_dir = Path(args.out).expanduser()
    elif cfg.get("kennis_map"):
        out_dir = Path(cfg["kennis_map"]).expanduser() / label
    else:
        out_dir = Path.cwd() / "transcripties" / label
    out_dir.mkdir(parents=True, exist_ok=True)

    token = None if args.geen_apify else apify_token()
    modus = "apify" if (args.apify and token) else "lokaal"
    if args.apify and not token:
        die("--apify gevraagd maar geen APIFY_API_KEY gevonden (env-var of repo-.env).")

    state = load_state(out_dir)

    print("Kanaal/playlist : " + label)
    print("Doelmap         : " + str(out_dir))
    print("Modus           : " + modus + ("" if modus == "lokaal" else " (~$0,01/video)"))
    print("\nNieuwste " + str(args.max) + " video's ophalen...")
    videos = list_latest(args.url, args.max)
    nog_te_doen = sum(1 for v in videos if not already_done(out_dir, v["id"], state))
    print(str(len(videos)) + " video's gevonden, " + str(nog_te_doen) + " nog te doen.")

    # Pauze bepalen: expliciete vlaggen winnen; anders het klein-batch-snelpad; anders defaults.
    if args.pauze is not None:
        min_p = max_p = args.pauze
        pauze_label = "vast (--pauze)"
    elif args.min_pauze is None and args.max_pauze is None and nog_te_doen <= SMALL_BATCH:
        min_p, max_p = SMALL_MIN, SMALL_MAX
        pauze_label = "kleine batch, snelpad"
    else:
        min_p = MIN_DELAY if args.min_pauze is None else args.min_pauze
        max_p = MAX_DELAY if args.max_pauze is None else args.max_pauze
        pauze_label = "random jitter"
    if max_p < min_p:
        max_p = min_p
    routes = lokale_routes(args.taal, args.vertaal)
    if modus == "lokaal":
        print("Pauze           : " + str(min_p) + "-" + str(max_p) + "s (" + pauze_label + ")")
        print("Lokale routes   : " + ", ".join(naam for naam, _ in routes))
    print()

    done = skipped = failed = apify_calls = local_fetches = 0
    t_all = time.time()
    gestopt = False

    for i, v in enumerate(videos, 1):
        head = "[" + str(i) + "/" + str(len(videos)) + "] " + v["title"][:60]
        if already_done(out_dir, v["id"], state):
            print(head + " - al gedaan, overslaan"); skipped += 1; continue

        text = lang = route = None
        translated = False

        if modus == "lokaal":
            try:
                text, lang, translated, route, pogingen = haal_lokaal(v["id"], routes, head)
                local_fetches += pogingen
            except AllesGeblokkeerdError:
                # Alle routes geblokkeerd: cooldown en één keer opnieuw langs de hele rij
                print(head + " - alle lokale routes geblokkeerd. "
                      + str(COOLDOWN_SECS) + "s afkoelen...")
                save_state(out_dir, state)
                time.sleep(COOLDOWN_SECS)
                try:
                    text, lang, translated, route, pogingen = haal_lokaal(v["id"], routes, head)
                    local_fetches += pogingen
                except AllesGeblokkeerdError:
                    # Nog steeds geblokkeerd: naar Apify of stoppen
                    resterend = len(videos) - i + 1
                    print(head + " - nog steeds geblokkeerd na cooldown.")
                    if token:
                        print(">> Overschakelen naar Apify voor de resterende "
                              + str(resterend) + " video's (~$" + ("%.2f" % (resterend * 0.01)) + ").")
                        modus = "apify"
                    else:
                        print("\n>> GESTOPT om een IP-ban te voorkomen.")
                        print(">> Draai later hetzelfde commando opnieuw: hij hervat waar hij bleef.")
                        print(">> Tip: met APIFY_API_KEY in .env schakelt hij automatisch over.")
                        gestopt = True
                        save_state(out_dir, state)
                        break

        if modus == "apify" and text is None:
            text, lang, translated = fetch_apify(token, v["id"])
            route = "apify"
            apify_calls += 1

        if text is None:
            print(head + " - overslaan (" + str(lang) + ")")
            failed += 1
            state["failed"][v["id"]] = str(lang)[:200]
        else:
            fname = write_transcript(out_dir, v, text, i, lang, translated, route)
            print(head + " - " + str(len(text.split())) + " woorden (" + lang
                  + ", via " + str(route) + ") -> " + fname)
            done += 1
            state["done"][v["id"]] = fname
            state["failed"].pop(v["id"], None)

        save_state(out_dir, state)

        # Jitter + rustpauze
        if modus == "lokaal" and i < len(videos):
            delay = random.uniform(min_p, max_p)
            time.sleep(delay)
            if REST_EVERY and local_fetches and local_fetches % REST_EVERY == 0:
                print("Rustpauze van " + str(REST_SECS) + "s (na " + str(local_fetches) + " lokale fetches)...")
                time.sleep(REST_SECS)

    kosten = ", Apify-kosten ~$" + ("%.2f" % (apify_calls * 0.01)) if apify_calls else ""
    elapsed = "%.1f" % (time.time() - t_all)
    print("\nKlaar in " + elapsed + " sec. "
          + str(done) + " nieuw, " + str(skipped) + " overgeslagen, " + str(failed) + " zonder ondertitels" + kosten + ".")
    print("Alle transcripties staan in: " + str(out_dir))
    if state.get("failed"):
        print("Mislukte ID's staan in " + str(out_dir / STATE_FILE) + " onder 'failed'.")

    if args.bouw_skill is not None and not gestopt:
        slug = slugify(label if args.bouw_skill == "__auto__" else args.bouw_skill)
        print("\n" + "=" * 64)
        print("VOLGENDE STAP - KENNIS-SKILL BOUWEN (instructie voor Claude)")
        print("=" * 64)
        print("Kennisbron (transcripties): " + str(out_dir))
        print("Nieuwe skill: /" + slug + "  ->  ~/.claude/skills/" + slug + "/SKILL.md")
        print("Claude: volg nu de procedure 'Een kennis-skill bouwen' uit de SKILL.md")
        print("van /transcribeer. Kort:")
        print("  1. Lees een representatieve selectie van de transcripties hierboven.")
        print("  2. Distilleer de kernprincipes, frameworks, do's/don'ts en voorbeelden")
        print("     van deze expert.")
        print("  3. Schrijf ~/.claude/skills/" + slug + "/SKILL.md die die kennis toepast en")
        print("     naar de kennisbron-map hierboven verwijst voor de details.")
        print("  4. Bevestig en laat een gebruiksvoorbeeld zien.")


if __name__ == "__main__":
    main()
