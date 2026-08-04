# Transcribeer

Claude Code-skills, met als eerste `/transcribeer`: haal de kennis van een YouTube-kanaal
binnen als tekst en bouw er optioneel een kennis-skill van.

De skill pakt van de nieuwste video's van een kanaal of playlist de ondertitels die YouTube
zelf al heeft. Er wordt niets gedownload — geen video, geen audio, geen ffmpeg, geen model.
Snel en gratis.

> `/transcribeer` is gemaakt door Bart Boonstra (Slim Werken AI).

## Wat je nodig hebt

| Onderdeel | Check | Installeren |
|---|---|---|
| Python 3 | `python3 --version` | zit meestal al op je Mac; anders `brew install python` of via python.org |
| uv | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` (Mac/Linux) · `powershell -c "irm https://astral.sh/uv/install.ps1 \| iex"` (Windows) |

Meer is er niet. `uv` haalt de Python-pakketjes (`yt-dlp`, `youtube-transcript-api`,
`requests`) de eerste keer vanzelf op.

## Installeren

Clone deze repo en koppel de skill met een symlink. Zo werkt `git pull` meteen door en
hoef je niets te kopiëren:

```bash
git clone https://github.com/pj4zwjc8g2-dot/transcribeer.git ~/repos/transcribeer
mkdir -p ~/.claude/skills
ln -s ~/repos/transcribeer/transcribeer ~/.claude/skills/transcribeer
```

Op Windows werkt een symlink ook, maar dan vanuit PowerShell als administrator:

```powershell
New-Item -ItemType SymbolicLink -Path "$HOME\.claude\skills\transcribeer" -Target "$HOME\repos\transcribeer\transcribeer"
```

Kopiëren mag natuurlijk ook — dan mis je alleen de automatische updates.

## Instellen waar je kennis heen gaat

Kopieer het voorbeeldbestand en vul je eigen pad in (een volledig pad, dus zonder `~`):

```bash
cp ~/repos/transcribeer/transcribeer/config.example.json ~/repos/transcribeer/transcribeer/config.json
```

```json
{ "kennis_map": "/Users/jouwnaam/Documents/YouTube-Kennis" }
```

Transcripties komen dan in `<kennis_map>/<kanaalnaam>/`. Zonder `config.json` gebruikt het
script `./transcripties/<kanaal>` in de map waar je staat.

`config.json` staat in `.gitignore`, want dat pad verschilt per machine.

## Gebruiken

Start Claude Code en typ:

```
/transcribeer https://www.youtube.com/@eenkanaalnaarkeuze
```

Of plak een kanaal- of playlist-link en zeg *"haal de tekst van de laatste 20 video's op"*.
Wil je er meteen een skill van bouwen die werkt volgens de kennis van dat kanaal:

```
/transcribeer https://www.youtube.com/@eenkanaal — en bouw er een skill van om advertenties te schrijven
```

Het script kan ook los:

```bash
uv run ~/.claude/skills/transcribeer/transcribeer.py "<URL>" --max 10
```

| Optie | Wat het doet |
|---|---|
| `--max N` | de N nieuwste video's (default 20) |
| `--out "<map>"` | een andere doelmap voor deze keer |
| `--taal nl` | voorkeurstaal van de ondertitels |
| `--vertaal` | ondertitels laten vertalen naar `--taal` |
| `--min-pauze` / `--max-pauze` | rustiger tempo tussen video's |
| `--apify` / `--geen-apify` | gedrag van de afvanger (zie hieronder) |
| `--bouw-skill "<naam>"` | na het ophalen een kennis-skill bouwen |

## Blokkades bij grote kanalen

YouTube blokkeert je IP tijdelijk bij te veel ondertitel-verzoeken achter elkaar — in de
praktijk vanaf zo'n 30 video's in één keer. Het script vangt dat in lagen op: random pauzes,
een tweede ophaalroute via `yt-dlp`, en een afkoelperiode met nieuwe poging. Een
`.transcript_state.json` in de doelmap onthoudt wat al gedaan is, dus opnieuw draaien hervat
altijd waar het bleef.

Wil je grote kanalen in één keer doorlopen, dan is er een optionele afvanger via
[Apify](https://apify.com) (~$0,01 per video). Zet je token in een `.env` naast de skill:

```
APIFY_API_KEY=apify_api_JOUW_TOKEN_HIER
```

`.env` staat in `.gitignore` — die hoort nooit in git terecht te komen.

## Let op

- Werkt op openbare video's met ondertitels (bijna alles heeft auto-ondertitels).
- De omgeving waarin je draait moet YouTube kunnen bereiken. Sommige cloud- of
  bedrijfsomgevingen blokkeren dat; draai de skill dan lokaal.
- Respecteer auteursrecht: gebruik dit voor eigen research en output, niet om andermans
  content letterlijk te herpubliceren.
