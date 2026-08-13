---
name: google-ads
description: Google Ads-strategie, diagnose en optimalisatie volgens Aaron Young (Define Digital Academy), gedestilleerd uit 100 video's uit 2026. Gebruik deze skill bij alles rond Google Ads: campagnes die geen of te weinig conversies opleveren, verspilde besteding, rommelleads, stijgende CPC's, een account dat niet verder wil schalen, keuzes tussen search, shopping, Performance Max, Demand Gen en AI Max, biedstrategieën (maximize clicks/conversions, tCPA, tROAS), matchtypes en negatieve keywords, accountstructuur, advertentieteksten en landingspagina's, conversietracking en offline conversies, Merchant Center en productfeeds, budgetberekening, een account doorlichten, scripts en AI-tools. Ook bij de vraag of je een bureau inhuurt of het zelf doet, wat je van je Google-vertegenwoordiger moet aannemen, lokale dienstverleners en reactiesnelheid op leads, Local Service Ads, Black Friday en agentic commerce. Niet voor Meta/Facebook-advertenties — daarvoor is /meta-ads.
---

# Google Ads volgens Aaron Young

Gedestilleerd uit 100 video's van het YouTube-kanaal van Aaron Young (Define Digital Academy),
opgenomen tussen ongeveer februari en augustus 2026. Aaron draait Google Ads sinds 2010, voor
accounts van onder de $500 per maand tot ver boven zes cijfers per maand. Waar zijn coaches (Johan
voor leadgen, Brent voor e-commerce, Daniel, Ashley) of gasten (Andrew Lok, Mike Rhodes, Mike Ryan,
Mike Mancini, Fred) aan het woord zijn, staat dat erbij — vooral omdat ze het niet altijd met hem
eens zijn.

Alle bedragen in dit document zijn in dollars, zoals in de transcripties. Reken ze om naar euro's
als dat relevant is; de verhoudingen kloppen wel.

---

## Hoe hij denkt

Eén zin vat het samen: **je accountstructuur en je conversiedata zijn belangrijker dan welke
optimalisatie dan ook.**

Dat is geen relativering van optimaliseren, maar een volgorde. De klassieke Google Ads-vaardigheid —
keywords uitkiezen, biedaanpassingen fijnslijpen, honderden negatieven toevoegen — leverde jarenlang
het meeste op. Nu niet meer, om twee redenen:

1. **Google target de betekenis, niet de woorden.** Ook exact match pikt close variants op waar je
   keyword niet eens in voorkomt. Google's eigen taal is verschoven van keyword*targeting* naar
   keyword*signalen*. Een signaal is een suggestie ("kijk daar eens"); vindt Google daar niets, dan
   gaat het er ver voorbij.
2. **Zoekgedrag wordt gesprekachtig.** AI overviews, AI mode, Lens, spraak. Je kunt niet targeten op
   een prompt van dertig woorden.

Wat overblijft als stuurmiddel is de conversiedata die je Google voert, en de campagnestructuur die
bepaalt waar het budget heen kan.

Daaruit volgt de rest: **minder campagnes, betere conversiedefinities, en pas splitsen als je tegen
een plafond loopt.**

### De vier kernprincipes

**1. Follow the money.** De simpelste en meest verwaarloosde regel: geef meer uit waar het werkt,
stop met uitgeven waar het niet werkt. Praktisch als een kwadrantenkaart van besteding × conversies:

| | Weinig conversies | Veel conversies |
|---|---|---|
| **Veel besteding** | **Verliezers** — stoppen. Is het een kernproduct, dan eerst een optimalisatieronde bij lager budget. | **Winnaars** — budget erbij. |
| **Weinig besteding** | **Zombies** — onbekend. Klein testbudget om erachter te komen wat ze zijn. | **Potentials / sidekicks** — hier maak je een breakout-campagne voor. |

De potentials zijn de kern van het hele schaalverhaal: thema's of producten die converteren maar te
weinig zoekvolume hebben, waardoor Google ze naast de volumewinnaars laat liggen.

**2. Begrijp eerst het bedrijf, dan pas het account.** Zie de onboardingvragen verderop. De meeste
mensen plakken Google Ads-kennis op een bedrijf; het moet andersom.

**3. Elke campagne moet een reden hebben om te bestaan.** Zijn openingsvraag bij een audit: "je hebt
zes campagnes — vertel me het doel van elk." Kun je het niet uitleggen, dan consolideren.

**4. Er zijn maar twee manieren om te schalen.** Meer geld waar het al werkt, of koudere doelgroepen
en nieuwe netwerken. Al het andere is een variant daarvan.

### De Google Ads success loop

Het ritme waar bijna alles in dit document op teruggrijpt:

> data bekijken → optimaliseren → **wachten** → nieuwe data → optimaliseren → wachten

De belangrijkste stap is die derde. Concrete wachttijden:

- Advertentietekst-splittest: minimaal 30 dagen, in de praktijk 8–10 weken
- Na een wissel van biedstrategie: 3–4 weken, en de eerste 1–2 weken worden de resultaten vaak
  eerst *slechter*
- Biedstrategieën herzien: hooguit elke 4 weken, realistisch elke 6–9 weken
- Demand Gen-creatietest: 30 dagen, soms 6 weken tot 2 maanden

Je hoeft **hooguit één keer per week** in je account te zitten. Dat is geen luiheid maar techniek:
wie dagelijks sleutelt, geeft het systeem nooit de kans om te leren.

---

## Diagnose

Begin altijd hier. Spring niet naar instellingen voordat je weet welk probleem je oplost.

> **Werk je voor een aannemer of installateur?** Voer dan éérst de tegenvraag uit `/aannemer` op:
> reken de break-even uit als overhead gedeeld door de brutomarge. Wie op 30% marge draait heeft bij
> gelijke overhead ongeveer tien leads per maand méér nodig dan wie op 50% draait. Meer advertentie-
> budget bij een kapotte prijs versnelt alleen het verlies. Klopt de marge, dan is dit hoofdstuk
> waar je bent.

### Diagnose 0 — ligt het aan Google Ads, of aan alles?

Ga naar GA4 → verkeersacquisitie → sessies per bron/medium. Zakt organisch óók, of alleen betaald?
Dalen alle bronnen, dan ligt het niet aan de campagne maar aan de site, het aanbod of de markt.

Sluit ook altijd eerst het triviale uit: is de landingspagina veranderd of offline geweest, is de
tracking kapot, zijn er marktomstandigheden die je gewoon moet uitzitten?

> **Casus.** Conversies vielen weg bij een klant. CTR was juist gestegen, zoektermen ongewijzigd,
> advertentieteksten ongewijzigd. Bleek: het bedrijf had zélf de landingspagina veranderd.
> Teruggezet, conversies terug.

### Diagnose 1 — de sessieduur-test

Het snelste onderscheid tussen een verkeersprobleem en een aanbodprobleem:

| Wat je ziet | Wat het betekent | Waar je repareert |
|---|---|---|
| Weg binnen 30 s (zeker onder 10 s) | Verkeerde mensen, of de bovenkant van de pagina klopt niet | Keywordtargeting; óf headline, subheadline, hero-afbeelding |
| Langer dan 60 s, geen conversie | Juiste mensen, verkeerde belofte | Aanbod, CTA, autoriteitsmarkers, checkoutfriction |

Hij formuleert het niet altijd hetzelfde: in de ene video is "weg binnen 30 seconden" een
**targeting**probleem, in de andere een **boodschap**probleem aan de bovenkant van de pagina. Beide
lezingen zijn bruikbaar — controleer eerst je zoektermen, en als die relevant zijn, is het de pagina.

### Diagnose 2 — de benchmarktabel (en de waarschuwing erbij)

Hij noemt in verschillende video's verschillende drempels. Behandel dit als **bandbreedtes**, niet
als constanten:

| Metric | Wat hij noemt |
|---|---|
| CTR search | tussen 6% en 10%; onder 5% is alarm, onder 8% een rode vlag |
| CTR shopping | 1% tot 3%; onder 1–1,5% een rode vlag |
| CTR display | ~1% |
| Conversieratio leadgen/search | minstens 5% |
| Conversieratio e-commerce/shopping | minstens 3% (branchebenchmark 2025: 3,22%) |

Hij relativeert ze ook zelf. Bij één klant lieten ze de CTR bewust zakken van 10% naar 6,5–7% door
een prijskwalificatie in de tekst te zetten — de conversieratio ging naar boven de 10%. **CTR is
geen doel; conversies zijn het doel.**

### Diagnose 3 — de datadrempels

Dit is de meest praktische tabel in dit hele document. Bijna elk "waarom werkt dit niet"-probleem bij
kleine accounts is een van deze drempels die niet gehaald wordt:

| Wat je wilt doen | Wat je nodig hebt |
|---|---|
| Maximize conversions / conversion value | **30 conversies per 30 dagen** (≈1 per dag) |
| tCPA of tROAS toevoegen | **50 conversies per maand**, én 4 weken stabiliteit |
| Performance Max starten | 30 conversies/30 dagen; leadgen: liefst pas met offline conversies |
| Een searchcampagne überhaupt laten werken | minstens ~300, liefst ~600 clicks/maand (≈10–20 per dag) |
| Startbudget bepalen | **gemiddelde CPC × 30**, per campagne |

De rekenregel achter dat laatste, uitgeschreven:

| Conversieratio | Clicks/dag nodig | Budget |
|---|---|---|
| 1% | ~100 | CPC × 100 |
| 3% | ~30 | CPC × 30 |
| 5% | ~20 | CPC × 20 |

Vijf campagnes van $10 per dag halen die drempel nooit. Dit is de belangrijkste reden waarom
versplinteren funest is voor kleine accounts.

> "Het is moeilijker geworden om met Google Ads te *starten*, maar veel makkelijker om te
> *schalen*." Zodra je genoeg conversiedata hebt, geven tROAS en tCPA je vangrails waarmee je
> agressief budget kunt toevoegen.

### Diagnose 4 — CPC-weerstand (het schaalplafond)

Signaal: je verhoogt het budget met 10–20% en de CPC springt 30–35% omhoog, of de conversiemetrics
breken — en het herstelt niet na een paar weken.

Kijk naar **search impression share**. Dat is een score op 100: 37% betekent dat je op 37 van elke
100 zoekopdrachten verschijnt.

| Impression share | Wat het betekent |
|---|---|
| Onder 40% | Budget met 20% verhogen kan meestal zonder verlies aan conversiekwaliteit |
| 45–50% | CPC begint hard op te lopen |
| 50–65% | Het gebruikelijke plafond. In sommige niches al bij 40%, in andere pas bij 75–80% |
| Boven 60% | Vrijwel altijd tijd voor een andere strategie |

Bij broad match ligt het plafond lager dan bij exact.

> **Casus.** Account geschaald van $2.000 naar $5.000 per maand. Boven 60% impression share spikete
> de CPC, daalden de conversies, steeg de CPA. Dat werd pas zichtbaar bij **zes maanden** data — bij
> 30 dagen leek het willekeurig. De markt was uitgeput; dat is geen optimalisatieprobleem maar een
> schaalprobleem.

### Diagnose 5 — verspilling opsporen

Zes instellingen die stilletjes geld kosten:

1. **Auto-apply recommendations uit.** Anders past Google zelf wijzigingen toe.
2. **Locatietargeting op "presence"**, niet "presence and interest". Google zet dit standaard
   verkeerd; het trekt mensen aan die alleen naar je gebied *zoeken*.
3. **AI Max niet aanzetten binnen een bestaande searchcampagne.** Wil je het testen, zet het in een
   aparte campagne met converterende keywords en je merk als negatief.
4. **Conversietelling op "one"** voor leadgen. Op "every" telt één lead die drie keer belt als drie
   conversies. (E-commerce is het omgekeerde — zie verderop.)
5. **Merkuitsluitingen op PMax.** Anders koopt PMax je eigen merkverkeer, want dat is de goedkoopste
   conversie die er is.
6. **Optimized targeting uit** bij specifieke doelgroeplijsten in Demand Gen, display en video.
   Anders negeert Google je lijst.

Daarnaast: exporteer je zoektermen en producten en laat er een **n-gram-analyse** of
**product labelizer** op los (zie het AI-hoofdstuk).

> **Casus e-commerce.** 23% van de besteding ($9.000 over 90 dagen) ging naar producten die samen
> $36 aan conversiewaarde opleverden.
> **Tweede casus.** 20% van de besteding ging naar 1.500 "under-index"-producten die $9.000 kostten
> en $27 opleverden. Alleen die uitsluiten bracht het account al bijna op zijn ROAS-doel.

### Diagnose 6 — het account is niet kapot, het is versnipperd

Symptomen: veel campagnes, weinig data per campagne, meerdere campagnes die op dezelfde keywords of
producten bieden, en niets dat de drempels haalt.

**Zet campagnes niet uit om opnieuw te beginnen.** Elke nieuwe campagne betekent een nieuwe
leerfase, en je lost het onderliggende probleem niet op. Renoveren is goedkoper dan slopen.

Gebruik in plaats daarvan de **stoplicht-audit**:

- **Groen** — wat werkt. Bijna elk account heeft thema's of producten waar je gewoon meer geld in
  kunt stoppen. Snelste winst, en de stap die auditors het vaakst vergeten omdat ze alleen naar
  kapotte dingen kijken.
- **Oranje** — belangrijk maar niet urgent. PMax of Demand Gen starten, conversietracking uitbreiden.
- **Rood** — nu veranderen. Dubbele campagnes op dezelfde keywords, verkeerde biedstrategie,
  vervuilde keywordtargeting. Effect binnen 7 tot 21 dagen.

> **Casus.** Account dat in een half jaar langs drie bureaus ging en 14 campagnes had geprobeerd.
> Het echte probleem was simpelweg te weinig verkeer: 136 clicks in 30 dagen. Oplossing: terug naar
> de ene dienst die converteerde, stadsegmentatie eruit, één campagne die genoeg clicks krijgt.

---

## STAB — het optimalisatieraamwerk

Alle honderden dingen die je in een account kunt doen, vallen in vier categorieën:

**S — Spending & segmentation.** Vind winnaars, geef ze meer budget. Vind verliezers, zet ze uit.
Werkt dat niet meer, dan **segmenteren**: budget zit op campagneniveau, dus een aparte campagne
*dwingt* Google geld uit te geven waar het al converteert.

**T — Targeting.** Vooral zoektermen opschonen. Bied-aanpassingen worden door smart bidding
overruled, dus daar zit de winst niet meer.

**A — Ads & landingspagina's.** De advertentie levert de klik, de pagina levert de conversie.
"Geef niet alleen Google de schuld — het kan je landingspagina zijn."

**B — Bidding.**

### De optimalisatievolgorde

1. **Follow the money** — triage. Begin bij de campagne met de hoogste besteding én slechte
   resultaten, niet bij de campagne die het makkelijkst te sleutelen is.
2. **Sluit uit dat het buiten Google Ads ligt.**
3. **90-60-30-14-dagen review** met vergelijkingsperiodes, om te zien of het probleem erger of
   beter wordt.
4. **Maak de juiste wijziging.**
5. **Wees geduldig.**

Voor e-commerce werkt hij met blokken van 4–6 weken, kalenderweek maandag–zondag, weergave op
wekelijks, en hij **negeert bewust de laatste 7 dagen** — het acquisitievenster van eerste klik tot
aankoop is 3 tot 7 dagen, dus die data is nog niet af. Daarna een **14-daagse vergelijking** met de
voorafgaande periode.

> Voorbeeld: besteding +18%, conversiewaarde +21% ⇒ prima, laten staan.
> Besteding omlaag én conversiewaarde omlaag ⇒ rode vlag.

### Rode vlaggen

- CTR search < 8% / shopping < 1% → advertentietekst, producttitels, productafbeeldingen
- Conversieratio leadgen < 5% / e-com < 3% → landingspagina of aanbod, niet keywords
- Campagne geeft budget niet meer uit → biedstrategie te agressief, óf impression share zit tegen
  het plafond
- PMax springt heen en weer per maand → kanaalverdeling controleren
- Campagne met < 20–30 clicks per dag én < 30 conversies per maand → samenvoegen of laten groeien

---

## Een bestaand account doorlichten: de audit in drie stappen

Gebruik dit als je een account overneemt of als je niet weet waar je moet beginnen. STAB is de
optimalisatielus; dit is de nulmeting eronder.

### Stap 1 — technische audit

**Accountniveau**

- **Auto-apply recommendations uit.** Google verandert doelen te vaak en te veel. Het systeem is niet
  dom, het mist alleen de context van jouw bedrijf — welke marges je draait, welke diensten je
  werkelijk levert, hoe druk je bent.
- **Automatische assets uit** bij gereguleerde branches (medisch, financieel, juridisch), waar Google
  iets kan bijverzinnen dat je niet mag beweren.

**Campagneniveau**

- Locatietargeting op **presence only**.
- **Zoekpartners en display uit** bij searchcampagnes.
- Biedstrategie tegen het **doel van de klant** houden. Een tCPA van $15 terwijl de klant $40–50
  prima vindt, is een rem — niet een prestatie.
- Advertentieschema's controleren: draai je op uren waarop niemand opneemt?

**Keyword- en advertentiegroepniveau**

- Kwaliteitsscore boven 5 (daarboven diminishing returns, zie hieronder).
- **Kruisbestuiving controleren.** Filter je zoektermenrapport op één woord en kijk of het opduikt in
  campagnes of advertentiegroepen waar het niet hoort. Verschijnt dezelfde term op drie plekken, dan
  concurreer je met jezelf om data.

### Stap 2 — resultatenaudit

Drie soorten vondsten, in deze volgorde:

1. **Makkelijke winst** — converteert goed, lage impression share ⇒ budget erbij. Dit doe je eerst,
   want het levert direct op.
2. **Bloedingen stoppen** — veel besteding, geen rendement ⇒ pauzeren of het budget knijpen terwijl
   je optimaliseert. Kijk hierbij óók naar de landingspagina en het aanbod; de oorzaak zit vaak niet
   in Google Ads.
3. **Kansen** — weinig besteding, goede conversies ⇒ uitbreken naar een eigen campagne. **De best
   presterende advertentiegroep blijft in de oorspronkelijke campagne staan**, anders sloop je de
   campagne die het werk deed.

### Stap 3 — het stoplicht

Zet elke bevinding op groen, oranje of rood:

- **Groen** — dit werkt, hier gaat meer geld in.
- **Oranje** — belangrijk, maar niet deze week.
- **Rood** — nu veranderen.

En dan: **follow the money.** Begin bij waar het meeste geld doorheen loopt, niet bij wat het
makkelijkst te repareren is.

> **Resultaten die hij bij dit proces noemt.** Een e-commerceaccount van 20 naar 40 verkopen per dag
> in zes weken. Een Amerikaanse aannemer die $5.000 per maand mínder uitgaf en méér gekwalificeerde
> leads kreeg. Een therapeut van 3 naar 6 nieuwe klanten per dag.

---

## Accountstructuur

### Het uitgangspunt: één campagne, één advertentiegroep

Bijna nooit haalbaar, maar het is het startpunt waar je vanaf moet beargumenteren. Elke extra laag
moet je verantwoorden.

Dit is geen theorie. Voorbeelden uit zijn eigen accounts:

- Klant van $400 → $4.000 per maand: **één searchcampagne, één advertentiegroep**. Drie
  advertentiegroepen samengevoegd omdat ze naar dezelfde landingspagina gingen, met dynamic keyword
  insertion voor de relevantie.
- Klant op $33.000 per maand: drie campagnes (search, PMax, remarketing via Demand Gen).
- Klant op $150.000 per maand: één searchcampagne met twee advertentiegroepen, PMax erover, wat
  display.
- Klant op $2.700 per dag: vier campagnes.

Hij kent geen enkele campagne in zijn beheer met meer dan vier of vijf advertentiegroepen; meestal
twee of drie.

### Wanneer een extra advertentiegroep

**Alleen als de advertentietekst of de landingspagina niet meer aansluit bij de betekenis van de
zoekopdracht.**

Wat wél splitsen rechtvaardigt: airco-installatie versus airco-onderhoud (twee verschillende
problemen). Eenslaapkamer- versus tweeslaapkamervilla (stellen zonder kinderen versus gezinnen).
Hardloopschoenen versus trailschoenen. Bikini versus badpak.

Wat níét meer splitsen rechtvaardigt: matchtypes, of woordvolgorde.

> **Casus.** Een klant had aparte advertentiegroepen voor *acupunctuur* en *dry needling*. Google
> toonde bij beide zoekopdrachten advertenties uit beide groepen. Samengevoegd — andere woorden,
> dezelfde intentie. Voorwaarde: tekst en pagina moeten voor beide kloppen.
> **Casus.** Een enterprise-klant had aparte groepen voor "sale", "buy" en "available". Eén intentie,
> dus samengevoegd.

**Single-theme ad groups, geen single-keyword ad groups.** Heb je 10–15 advertentiegroepen in
SKAG-stijl, dan krijgt waarschijnlijk maar 30% daarvan noemenswaardig verkeer. Draai een
zoektermenrapport, kijk welke groepen op dezelfde zoektermen afvuren, en voeg ze samen.

### Wanneer een extra campagne

Vier geldige redenen, en niet meer:

1. **Sterk verschillende winstmarges** — vooral een product met **laag volume en hoge marge**, dat
   anders ondergesneeuwd raakt door de volumewinnaars.
2. **Een ander netwerk** (YouTube, display, shopping, kaarten).
3. **Bestedingscontrole per locatie** — landen, staten, postcodes, franchises.
4. **Resultaatsturing** — geld forceren naar een product of locatie die converteert maar te weinig
   krijgt.

De rode draad: **je budget zit op campagneniveau.** Elke besteding die je apart wilt kunnen sturen,
heeft een eigen campagne nodig. Dat is de enige mechanische reden dat campagnes bestaan.

### De spanning die je moet begrijpen

Compact beginnen en segmenteren om te schalen lijken tegenstrijdig. De volgorde lost dat op:

> **Begin compact om conversiedata te concentreren. Splits pas als je CPC-weerstand ziet.**

Meer campagnes is geen strategie; het is een reactie op een plafond.

### Naamgeving

Zet geen budgetten, doelen, lanceerdata of laatste optimalisatiedatum in je campagnenamen — die
staan al in kolommen. Namen veranderen heeft **nul effect op prestaties**, maar wel op je vermogen
om je eigen account te lezen. Houd een apart optimalisatiejournaal.

> **Casus.** Een account had een PMax-campagne en een shoppingcampagne op exact dezelfde producten
> met exact dezelfde tROAS. Vermoedelijke oorzaak: de namen waren zo overladen dat niemand doorhad
> dat het dubbelop was.

---

## Bedrijfsstrategie vóór accountstructuur

Zijn onboardinginterview, in de volgorde waarin hij het stelt. Dit gaat vooraf aan elke technische
keuze.

- **Wat is je bedrijfsmodel — hoe verdien je geld?** Zit de winst in de eerste verkoop of in een
  onderhouds- of abonnementscontract erna? In dat laatste geval mag je ROAS-doel omlaag en je CPA
  omhoog.
- **Wat is het doel van de campagnes? Wat wil je over zes maanden bereikt hebben?**
- **In welke fase zit het bedrijf: groei of efficiëntie?** Een groeifase rechtvaardigt Demand Gen en
  top-of-funnel; een efficiëntiefase juist niet.
- **Wat zijn je break-evencijfers — AOV, LTV, CAC — en hoe kom je aan dat getal?** Die vervolgvraag
  is de belangrijkste: hij opent het gesprek over marges en over welk product de hoogste marge heeft.
- **Hoe ziet je marketingteam eruit?** Bepaalt het tempo waarin je kunt veranderen.
- **Welke gebieden, seizoensinvloeden, branchevoorschriften?**
- **Welke hefbomen wil je kunnen bedienen?**

Toegang die hij vraagt: Google Ads, Analytics, Tag Manager, Merchant Center, plus CRM of
trackingsoftware (Triple Whale, Salesforce, HubSpot).

### Platformdata is geen bedrijfsdata

Dit is misschien zijn belangrijkste enkele principe.

Een gerapporteerde ROAS van 500% betekent **niet** dat je bedrijf 500% verdient. De dashboardcijfers
zijn een **optimalisatie-instrument** — schalen, remmen, prioriteren — geen boekhouding. De enige
vraag die telt: *is dít cijfer winstgevend voor mijn bedrijf?*

> **Casus.** Klant wilde 500% ROAS. Uit de cijfers bleek dat 200% al winstgevend was. Ze konden
> agressief gaan schalen.
> **Casus.** Klant dacht $100 CPA nodig te hebben; in werkelijkheid kon $150–200 uit.
> **Casus.** E-commerce merk van $100.000–250.000 per maand joeg een tROAS van 350% na. In gesprek
> bleek dat de winst niet in het apparaat zat maar in een **24-maands onderhoudsplan** dat erna
> verkocht werd. Doel verlaagd naar 200% — de eerste verkoop hoefde alleen quitte te spelen — en het
> bedrijf ging naar een nieuw winstniveau. Het doel van 350% bestond alleen omdat men dacht dat het
> haalbaar was.
> **Casus.** Bij een leadgenklant zakten de conversies in het dashboard van 600+ naar onder 200 per
> maand. Het aantal **betalende klanten** per week ging van ~20 naar 30–48. Het vorige bureau
> optimaliseerde op een getal dat niets betekende. Opgelost met offline conversies.

### Je doel verschuift naarmate je schaalt

Op $10.000 per maand haal je misschien 600% ROAS. Op $25.000 is 400% realistischer. Boven $100.000
weer anders. Op een gegeven moment kun je alleen nog verder groeien door je **offline
verkoopproces, average order value of lifetime value** te verbeteren — niet door de campagne.

> **Casus.** Zelfde budget, zelfde conversies, maar een fulltime closer aangenomen: van 23 naar
> boven de 40 nieuwe klanten per week.

Rekenlogica: met een LTV van $100 valt er nauwelijks te schalen. Bij $500 of $1.000 mag je ROAS-doel
veel lager en kun je veel meer markt kopen.

### De incrementaliteitstest

*Betaal je Google voor verkopen die je toch al had gekregen?*

Klassiek voorbeeld: merkzoektermen. Stop je die besteding, dan ziet je dashboard er slechter uit,
maar kun je dat geld inzetten om écht nieuwe klanten te kopen — die duurder zijn en langer doen over
converteren. Voor e-commerce adviseert hij acquisitie-trackingsoftware; voor leadgen het CRM in met
offline conversies.

---

## Een bureau inhuren, of het zelf doen

**Onder ongeveer $10.000 advertentiebudget per maand is een bureau weggegooid geld.** Zijn stelling:
in 2026 zou je met de beschikbare hulpmiddelen zelf tot $30.000–50.000 per maand moeten kunnen
schalen voor je die hulp echt nodig hebt.

### De twee soorten bureaus die misgaan

- **De onervaren operator.** Begon een bureau na een video over hoe je een bureau begint. Huurt
  freelancers in, besteedt zijn eigen tijd aan verkoop, belooft te veel omdat hij niet weet hoe
  Google Ads werkt. Niet kwaadaardig, wel schadelijk.
- **Het gevestigde bureau.** Hier zitten geen slechte mensen, maar er is een **modelprobleem**: een
  paar grote klanten slurpen de capaciteit op. Betaal jij $1.000–2.000 beheerfee en een ander
  $20.000–50.000, wie krijgt de aandacht als het druk wordt? Daar bovenop gaat **40 tot 60% van elke
  beheerfee** op aan overhead — kantoor, HR, boekhouding, verkoop — vóór er iemand naar jouw campagne
  kijkt.

### De vragen die je stelt vóór je tekent

1. Hoeveel ervaring heb je?
2. **Wie draait mijn account werkelijk** — jij, een teamlid, of een freelancer?
3. **Wat zijn de resultaten bij klanten die evenveel uitgeven als ik?** Niet de vitrinecases met
   twintig keer jouw budget.

### Wanneer wél een bureau

- Als je niet verder kunt schalen. In leadgen ligt dat meestal rond $20.000–30.000 per maand, soms
  $50.000; in e-commerce vaker $50.000–60.000.
- Als je creatiebehoefte (video, beeld) te groot wordt voor je eigen team.

Wat hij wél zou uitbesteden, en dan **eenmalig**: het opzetten van conversietracking en de
koppelingen — Shopify ↔ Google Ads ↔ Merchant Center, of CRM ↔ Google Ads. *"Dat is iets waar ik
zeker voor zou betalen om te zorgen dat het klopt."*

Zijn rekensom: 10–30% beheerfee op $10.000 besteding is $1.000–3.000 per maand, en die fee stijgt
mee als je meer uitgeeft. En het werk is minder dan je denkt: **je kunt een account in 1 tot 3 uur
per week optimaliseren.** Het idee dat een bureau dagelijks in je account zit is onjuist — en zou
ook slecht zijn, want dagelijks sleutelen is precies wat smart bidding kapotmaakt.

> Weeg dit tegen zijn eigen positie: hij verkoopt coaching aan mensen die het zelf doen. Dat maakt
> het argument niet fout, maar het is geen neutrale bron.

---

## Wat je van een Google-vertegenwoordiger moet aannemen

Voor elke slechte rep is er een goede. Maar sommigen vinken vooral hun quota af, en **alles wat een
rep zegt is een aanbeveling, geen voorschrift** — ook als het gepresenteerd wordt als "Google's best
practice".

**Twee vragen die je altijd stelt:**

1. *"Hoeveel ervaring heb je met het beheren van Google Ads-campagnes bùiten je rol bij Google?"*
   In Australië kun je als account strategist beginnen met **één jaar** ervaring in digitale
   marketing — niet eens per se in Google Ads. En bij kleinere budgetten bel je vaak niet met Google
   zelf, maar met een extern bedrijf dat namens Google mag opereren.
2. *"Kun je me twee of drie casussen geven van vergelijkbare bedrijven in mijn niche die ongeveer
   evenveel uitgeven, en wat daar het resultaat was?"* Namen hoeven niet. Het gaat erom of de data
   iets over jouw situatie zegt.

> **Waarom die tweede vraag ertoe doet.** Bij de lancering van AI Max noemde Google een verdubbeling
> van de conversieratio bij 31% lagere kosten per conversie. Dat cijfer kwam van **L'Oréal** — een
> bedrijf dat ook op Meta, billboards en tv adverteert, met een budget in een compleet andere orde.
> Hij betwist de data niet; hij betwist dat je er iets aan hebt bij $1.500–2.000 per maand.

---

## Keywords, matchtypes en negatieven

### Waarom broad match niet meer optioneel is

Om in AI overviews en AI mode te verschijnen zijn er **drie** manieren:

1. **AI Max** — hij raadt dit voorlopig af (zie het tijdgebonden hoofdstuk)
2. **Performance Max** — niet als startpunt
3. **Broad match keywords**

Voor de meeste bedrijven blijft dus alleen broad match over. Google zelf zegt inmiddels dat
keyword*targeting* niet meer bestaat, alleen keyword*signalen*.

De reden dat dit dringend is: de CTR bij AI overviews daalde volgens Seer Interactive van 14%
(oktober 2024) naar iets boven 6% (oktober 2025) — elders noemt hij "tot 68% daling". Eind 2024
gebruikten ~350 miljoen zoekopdrachten AI overviews of AI mode; begin 2026 meer dan **2 miljard per
maand**. In sommige branches verschijnt bij meer dan 80% van de zoekopdrachten een AI-element.

### Hoe je broad match veilig inzet

- **Broad match keywords van minstens drie woorden, liever vier tot zes.** Niet
  "airco-installatie" maar "split system airconditioning installatie voor woningen". Google target
  de **context** van het keyword, niet de losse woorden — dus hoe meer context je meegeeft, hoe
  strakker de match. Kort broad match keyword = alle kanten op.
- **Samen met exact match keywords in dezelfde advertentiegroep.** Dit is de sleutel: een van de
  kernsignalen die Google gebruikt voor een broad match keyword zijn **de andere keywords in
  diezelfde advertentiegroep**. Exact match houdt broad match in het gareel. Zijn verhouding:
  **twee of drie long-tail broad keywords plus 5 tot 25 exact match keywords.** Soms werken twee
  broad keywords in hun eentje ook.
- **De landingspagina moet echt aansluiten.** Geen keyword stuffing, wel inhoud die het thema
  daadwerkelijk behandelt — de pagina is óók een targetingsignaal.
- **Negatieven als vangrails**: blokkeer de thema's die je niet levert, niet meer dan dat.

Over "near me": hij is er geen fan van, maar bij één lokale klant werkte het en was er geen bruikbaar
alternatief.

**Phrase match** gebruikt hij bewust niet — "ik denk gewoon niet dat het nu relevant is". Zie het
volgende hoofdstuk voor de onderbouwing.

> **Casus die zijn eigen tegenwerping ondergraaft.** Online begeleiding specifiek voor zwangere
> vrouwen — een niche binnen een niche, precies het geval waarvan iedereen zegt dat broad match er
> onmogelijk kan werken. Van 12–15 leads per week naar structureel boven de 30, met een piek van 50.
> Het bedrijf had er 30 nodig om te draaien.

*"Had je me dit in 2022 gevraagd, dan had ik je uitgelachen."* Hij is hier van mening veranderd, en
zegt dat er ook bij.

### Negatieve keywords: hij is hierin van mening veranderd

Een à twee jaar geleden sloten ze agressief uit: concurrenten, how-to's, doe-het-zelf,
symptoomzoekopdrachten.

**Nu bewust conservatief.** Reden: AI overviews en AI mode draaien juist op vragende en
symptoomzoekopdrachten, en je wilt daar vroeg in de zoekreeks zichtbaar zijn.

De regel nu:

- **Wél uitsluiten**: concurrenten, en diensten of producten die je werkelijk niet levert. Lever je
  alleen de herenvariant, dan sluit je de damesvarianten uit.
- **Niet uitsluiten**: vragen, symptoomzoekopdrachten, how-to's.
- **Geen zoektermen uitsluiten waar nog geen klik op is geweest.** Zonde van de tijd.

Meer algemeen: **hoe meer conversiedata je hebt, hoe minder vangrails je nodig hebt.** Campagnes
draaien vaak beter met mínder negatieven. Honderden negatieven toevoegen is achterhaald werk.

### Keywordonderzoek in de praktijk

Tools → planning → keyword planner → discover new keywords. Plak je URL en typ de woorden die je
zélf zou zoeken.

Wat je zoekt zijn **thema's**, geen losse keywords. "toothpaste for gingivitis", "best toothpaste
for gingivitis", "bleeding gums" en "toothpaste to reverse gum disease" horen in dezelfde
advertentiegroep — zelfs als exact match pikt Google al die varianten op.

Wat je verder meeneemt: de biedrange die Google toont (bijvoorbeeld $1,20–$4,00 ⇒ reken met $3) en
het maandelijkse zoekvolume. Google's eigen CPC-schatting kan er flink naast zitten — in één
voorbeeld schatte Google $3,23 waar eigen onderzoek $1,50 liet zien.

### Kannibalisatie versus redundantie

Brent maakt een onderscheid dat de meeste mensen door elkaar halen:

- **Redundantie** is het echte probleem: vijftien keywords die feitelijk hetzelfde zeggen. "Badmat"
  en "blauwe badmat" leest Google als dezelfde intentie. "Blauwe katoenen badmat" is wél
  onderscheidend. Varianten maken door te herschikken of andere interpunctie splitst je
  prestatiedata over te veel keywords, waardoor Google trager leert.
- **Kannibalisatie** tussen een PMax- en een searchcampagne op dezelfde dienst is géén probleem,
  zolang beide presteren. De veiling kiest per gebruiker.

Aarons bezwaar tegen kannibalisatie is een ander: **budgetcontrole.** Zit een thema in meerdere
campagnes, dan kun je er niet gericht meer geld in stoppen of het gericht stoppen. Dat maakt zowel
schalen als verspilling stoppen onmogelijk.

Johans nuance: overlap tussen twee verschillende *diensten* (gazonverzorging en bomen snoeien bij
één hovenier) is wél een probleem, want dan kloppen de advertentie en de landingspagina niet meer.

---

## Zes strategieën die niet meer werken

De onderliggende reden dat deze allemaal tegelijk verlopen: het **zoekvolume stijgt, maar het aantal
clicks daalt**, omdat mensen hun antwoord al in het AI-overzicht krijgen. Technieken die uitgingen
van veel, goedkoop, fijnmazig te sturen verkeer zijn daardoor stuk voor stuk verzwakt.

1. **SKAG's — single keyword ad groups — zijn dood.** Al sinds ongeveer 2022, en ze duiken nog steeds
   op. Reden: **exact match werkt nu zoals phrase match vroeger werkte.** Google's eigen voorbeeld:
   een exact match op "furniture store" toont ook bij "home furnishing store". Controleer het in je
   zoektermenrapport — duiken dezelfde termen in meerdere advertentiegroepen op, dan heb je het
   probleem. Vervang door **STAG's: single theme ad groups.**
2. **Phrase match is dood.** Hij gebruikt alleen nog exact en broad. Twee redenen: exact doet nu wat
   phrase deed, én **broad match is het enige matchtype dat alle zes targetingsignalen gebruikt** —
   waaronder de andere keywords in de advertentiegroep, de landingspagina en de verwachte CTR. Phrase
   en exact delen een kleinere set. **Draaien je phrase-keywords goed? Zet ze niet uit** — faseer ze
   uit door varianten in broad en exact toe te voegen en pas te stoppen als die het overnemen.
3. **Honderden of duizenden negatieve keywords toevoegen.** Ze halen die nu weg in batches van
   **10–20%**, wachten op data, en halen weer weg. *"In alle gevallen zagen we betere prestaties."*
   De nieuwe rationale: negatieven bestaan niet om de perfecte zoekterm te vinden, maar om **thema's
   uit de testpoel te halen die je niet levert** — alleen installatie en geen onderhoud, alleen
   split-units en geen kanaalsystemen, alleen producten voor volwassenen.
4. **IP-blokkers.** Hij heeft er nooit waarde voor geld in gezien. Standaardwerkwijze bij een nieuw
   account: pauzeren, de lijst eruit halen (bewaren voor het geval dat), 4–6 weken wachten. De
   uitkomst is óf niets, óf **betere** resultaten. Daarna zeggen ze het abonnement op.
5. **Producttitels volstoppen met keywords.** Niet drie keer hetzelfde zeggen ("kussen voor
   zijslapers, zijslaapkussen, kussen tegen nekpijn"). Wel: **één sterke keywordfocus vooraan, dan
   het merk, dan modifiers** (latex, veren, bamboehoes). De attributen in je feed doen de rest.
6. **Alleen search draaien als leadgenbedrijf.** Search blijft je basis, maar op enig moment heb je
   PMax nodig. *"Dat PMax slecht is voor leadgen is simpelweg niet waar"* — mits je offline
   conversies op orde hebt (zie het PMax-hoofdstuk).

---

## Je CPC verlagen: vier manieren

1. **Kwaliteitsscores — met een belangrijke nuance.** Een goede kwaliteitsscore zet alleen
   **neerwaartse druk** op je CPC; het lost niets op. Je kunt betere scores hebben dan drie maanden
   geleden en tóch meer betalen, omdat het een live veiling is met nieuwe concurrenten en steeds meer
   smart bidding. En er zijn **diminishing returns**: van 2–3 naar 5–6 scheelt veel, van 5–6 naar
   9–10 nauwelijks. Let wel op je **landingspagina-score** — een trage site drijft je CPC echt op.
2. **Broad match testen.**
   > **Casus, 11 maanden data, accreditatiebedrijf.** Exact match $11+ per klik, broad match $6,50.
   > Conversieratio exact 23%, broad 11–12%. CPA exact $48, broad $52–55 — en de klant had $70 nodig.
   > **Broad won op volume tegen acceptabele kwaliteit.** De les: staar je niet blind op de CPC, kijk
   > naar de balans met de conversiemetrics. Was de klantbehoefte $45 geweest, dan was de conclusie
   > omgekeerd.
3. **Probleem- of oplossingsgerichte keywords**, hoger in de funnel.
   > **Casus acnécrème.** Het koopintentie-keyword kostte **$7,19** per klik; "beste
   > huidverzorgingsroutine voor vette huid" kostte **$3**.

   Zet dit in een **aparte campagne**, want de conversie duurt langer en je wilt het budget en de
   beoordeling gescheiden houden van je bottom-of-funnel campagne.
4. **Diversifiëren naar andere netwerken** — YouTube, Demand Gen, display. Begin met **5 tot 10% van
   je searchbudget**, en beoordeel op **accountniveau**, niet per campagne. De losse campagne kan
   break-even draaien terwijl het hele account beter presteert doordat je searchcampagnes goedkoper
   converteren.

---

## Biedstrategieën

### Vijf gouden regels

1. **Twijfel je, wacht.** De grootste fout is te vaak veranderen. Hooguit elke 4 weken, realistisch
   elke 6–9 weken.
2. **Kijk naar trends over 30, 60 en 90 dagen.** Bij een lang acquisitievenster (21 dagen van klik
   tot conversie) zegt zelfs twee weken data niets.
3. **Kijk per week, niet per dag.** Zet je kalenderweek op maandag–zondag; anders klopt Google's
   weekindeling niet.
4. **Verander biedstrategie en budget nooit tegelijk.** Twee grote ingrepen, apart houden — niet in
   dezelfde week, vaak zelfs niet in dezelfde maand.
5. **Vergeet je CPC.** Je CPC gáát omhoog. Je vertelt Google dat conversies belangrijker zijn dan
   clicks. 20% duurdere klikken met dubbel zoveel conversies is winst.

> **Casus.** Overstap van maximize clicks naar maximize conversions: CPC van $3,00 naar $4,80, maar
> de kostprijs per conversie daalde fors. tCPA pas vier maanden later toegevoegd, op $75 — het
> niveau waarop het account al presteerde, niet een wensgetal.
> **Casus.** Na diezelfde overstap zakten de conversies de eerste anderhalve week; daarna 20, 21, 25
> per week. Mensen draaien zo'n wijziging na één slechte week terug. Geef het 3 tot 4 weken.

### Checklist: is deze campagne klaar voor smart bidding?

- 30 conversies in 30 dagen?
- Wekelijkse conversies over 4 weken stabiel, met **niet meer dan 20% variatie**? (vooral van belang
  vóór een tCPA)
- Biedstrategie of doel niet in de afgelopen 6 weken al veranderd?
- Budget niet recent veranderd?

Alles groen ⇒ overstappen.

### Wat als je die 30 conversies niet haalt?

Conversiedata reikt 90 dagen terug, maar de laatste 30 dagen wegen het zwaarst. Haal je consequent
**15 conversies per maand** gedurende twee à drie maanden (≈30 over 60 dagen, ≈45 over 90 dagen), en
zijn je andere metrics goed (CTR boven 10%, conversieratio boven 5% search / 3% shopping), dan
stapt hij tóch over. Daarna vier weken niets aanraken.

### Mag een nieuwe campagne meteen op maximize conversions?

- **Nieuw account, nieuwe campagne: nee.** Begin met **maximize clicks**. Goedkoper verkeer, sneller
  testen van teksten, pagina's en keywords. Overstappen binnen 60–90 dagen. Bij een overstap kan het
  bovendien 7 tot 14 dagen duren voor je advertenties überhaupt vertonen.
- **Volwassen account met campagnes die al op smart bidding draaien: ja**, als je een campagne
  uitbreekt voor dezelfde keywords of producten in een andere locatie — mits het budget een
  **30× multiplier van je huidige CPA** is. CPA $10 ⇒ $300 per dag.

### Wanneer een tCPA of tROAS toevoegen

Pas als de kostprijs per conversie **4 tot 6 weken** stabiel is, met minder dan ~20% variatie.

> **Voorbeeld.** Wekelijkse CPA van 285 → 87 → 485 → 111: veel te wild. Pas toen er vier weken
> achtereen 140, 166, 135 stond, zetten ze een tCPA rond 170–175.
> **Tegenvoorbeeld van wat je niet moet doen.** Zie je 150 → 120 → 100 en Google stelt een tCPA van
> 100 voor, dan zet je hem daar níét op — je kunt misschien naar 50. Wacht tot je vier weken 55, 52,
> 48, 51 ziet.

Zet het doel op wat het account **doet**, niet op wat je wilt. Een verkeerd gezet doel is een rem.

### tROAS: twee casussen die elkaar tegenspreken

Bewaar beide; welke van toepassing is, hangt af van of je te weinig data hebt of te veel prijs
weggeeft.

> **Casus A — verlagen hielp.** PMax-campagne met te weinig verkeer. tROAS verlaagd ⇒ méér
> conversiewaarde, want er kwam eindelijk data binnen. Later de tROAS helemaal verwijderd ⇒
> conversiewaarde en clicks weer omhoog. Een te hoge tROAS wurgt het account.
> **Casus B — verlagen was rampzalig.** tROAS van 200 naar 175 naar 170 om te schalen. Gevolg:
> mínder clicks én lagere conversiewaarde. Terug naar 200: beide hersteld.
> **Casus C — de mechaniek achter B.** E-commerce account verlaagde de tROAS van 200 naar 180 bij
> gelijk budget. Google ging **veel agressiever bieden op precies dezelfde veilingen en producten**
> — geen betere posities, geen ander verkeer, alleen bijna dubbel zo dure klikken. Bij gelijk
> budget dus fors minder clicks, en impressies en impression share zakten mee. Advies: terugzetten,
> 14 dagen geven.

De les: **een tROAS verlagen is geen schaalknop.** Het verandert met wie Google biedt.

Praktisch: de gemiddelde tROAS is zichtbaar in het overzicht van een PMax-campagne. Bij **standaard
shoppingcampagnes zie je die alleen met een portfolio-biedstrategie** — daarom raadt Brent portfolio
aan zodra je meerdere standaardcampagnes hebt.

### De risico's van smart bidding

*"Van alle optimalisaties die je kunt doen, draagt deze het meeste risico."* Vier dingen die
misgaan:

- **De tCPA/tROAS-mythe: het dashboardcijfer is geen bedrijfsgezondheid.** Het doel is een
  optimalisatie-instrument, geen winstmeting.
  > Zijn bekendste voorbeeld: een clip waarin een ROAS van 200% te zien is, waar iedereen op
  > reageerde met "waarom adverteer je überhaupt". Voor dát bedrijf was het de beste beslissing ooit,
  > want de winst zat niet in de eerste verkoop maar in een **onderhoudscontract van 24 maanden**
  > erna. Ze verlaagden het doel bewust om volume te kopen.
- **De klokcurve.** Er is een optimale waarde, geen "hoe hoger hoe beter". Zet je de tROAS te hoog
  (of de tCPA te laag), dan wordt het **restrictief**: minder clicks, minder impressies, minder
  omzet. Te laag en je koopt rommel. *"Er zijn meer mensen die converteren bij 300% ROAS dan bij
  800%."*
- **Een doel is geen gaspedaal maar een rem.** Zet het op de **ondergrens** van wat je nodig hebt,
  niet op je ambitie.
- **Zet het doel op de huidige data, niet op je wens.** Wil je 600% terwijl je 300% draait, dan
  gebeurt er simpelweg niets — je uitgaven vallen stil. Je klimt de trap op via optimalisatie:
  300 → 350 → 400.

> **Casus die alle vier samenvat.** Nieuwe e-commercecampagne. Ze wachtten **acht weken** voor ze
> überhaupt een tROAS toevoegden, en zetten hem toen op 600 terwijl het account 700+ draaide —
> bewust láger, omdat de klant wilde opschalen. Later zelfs naar 500. *"Bij schalen is het altijd
> veiliger je doel lager te zetten dan wat je werkelijk presteert."*

### De laddermethode

Staat je doel hoger dan wat het account werkelijk doet (doel 350, werkelijk 188)? Zet het doel dan
op de werkelijke prestatie (200), verzamel 3–4 weken data, en verhoog met **10–20% per stap**.

---

## Schalen

### De drie hefbomen

1. **Meer budget in bestaande campagnes.** De 20%-regel: verhoog met stappen van 20% elke 5–7 dagen.
   Meestal lukken twee tot drie snelle verhogingen, daarna 1–2 weken wachten. Zakken de resultaten
   iets, geef het een week of twee — het trekt meestal bij. Vanaf een heel lage basis ($5–10) mogen
   absolute stappen van $5–10 ook al is dat meer dan 20%.
2. **Segmentatie / breakout-campagnes.** Budget zit op campagneniveau, dus een aparte campagne
   dwingt Google geld uit te geven waar het al converteert. Op locatie, op product- of
   dienstcategorie, of (lastiger) op doelgroep.
3. **Koudere doelgroepen.** Nieuwe netwerken (YouTube, display, Gmail, Demand Gen) en nieuwe
   keywordthema's — benefit- of probleemgericht in plaats van product- of dienstgericht.

*Terminologie is niet consistent*: in de ene video heet hefboom 1 "verticaal" en hefboom 2
"horizontaal"; in een andere noemt hij segmentatie eerst verticaal en in de samenvatting horizontaal.
Benoem de mechaniek, niet het etiket.

### Vier vinkjes vóór je gaat schalen

1. CTR search ≥ 8%, shopping ≥ 1,5%
2. Conversieratio search ≥ 5%, shopping ≥ 3%
3. Minstens 50 conversies per maand, liefst binnen één campagne
4. Bestaande PMax besteedt ≥ 90% aan search + shopping

Waarom: als je met slechte fundamenten gaat schalen, bouw je die problemen straks opnieuw op maar met
meer geld. En bij koudere doelgroepen wil je **niet** nog je landingspagina zitten testen.

Waarom CTR er hier toe doet: Google verdient aan clicks, dus een hogere CTR dan je concurrenten in
dezelfde veiling verlaagt de premie die je moet betalen voor dezelfde zichtbaarheid. Bij een klein
budget merk je dat nauwelijks; bij een groot budget wel.

### De belangrijkste regel bij het uitbreken

**De categorie of het keywordthema met de meeste besteding en conversies blijft in de originele
campagne.** Je breekt de *tweede* categorie uit. Anders saboteer je je eigen kerncampagne.

En: **gefaseerd.** Eén of twee campagnes tegelijk, niet alles ineens.

### Casussen

> **E-commerce, 50.000 SKU's, 10 productcategorieën.** Eén PMax + één shopping → in fasen uitgebreid
> naar zes PMax-campagnes, gesegmenteerd op productcategorie. $32.000 → $75.000 per maand met
> gelijke ROAS.
> **Leadgen.** Eén searchcampagne met drie duidelijke keywordthema's waarvan Google er maar één
> bediende. Twee extra searchcampagnes op de andere thema's, plus PMax erover. $12.000 → $20.000
> per maand.
> **Locatiesegmentatie VS.** Pennsylvania kostte $800 en leverde 10 conversies met een impression
> share onder 30%. Eigen campagne. Het mooie hiervan: keywords, tekst en landingspagina zijn al
> bewezen — je opent alleen het budgetkanaal. Idem voor Georgia, Illinois, Washington ($1.000 voor
> 424 conversies).
> **Search-only leadgen.** Impression share van 20% naar 64%, CPC van $2 naar $7,60. Ze hielden het
> lang vol omdat de conversieratio van 1% naar 8–10% ging — de rekensom bleef kloppen. Maar bij
> twee kerndiensten is er geen nieuwe searchcampagne meer te bouwen, dus PMax erbij.
> **Regionaal Australië.** Campagnes uitgebroken voor regionaal New South Wales en Queensland, waar
> weinig concurrentie was maar veel vraag — Google gaf al het geld uit in Brisbane, Sydney en
> Melbourne.

### Sidekicks vinden

Exporteer je zoektermen of productlijst en draai er een **n-gram-analyse** of **product labelizer**
op. Vroeger via scripts; nu net zo goed door de export in een taalmodel te gooien. Je zoekt het
kwadrant *lage besteding, goede conversies*.

### Het bodybuilder-concept

Volume en winstgevendheid tegelijk laten groeien is heel moeilijk. Werk in cycli van 3–4 maanden,
zoals een bodybuilder bulkt en cut: een periode gericht op **volume** (je accepteert wat vet), dan
een periode gericht op **rendement** (tROAS omhoog, tCPA omlaag, vet eraf). Plan die cycli om je
seizoenspieken heen — een e-commerce merk dat in Q4 verkoopt, bulkt in Q4.

---

## Advertentieteksten

### Vier verplichte onderdelen

1. **Keywordfocus.** De headline moet aansluiten bij wat er gezocht is. Dynamic keyword insertion is
   hier nog steeds nuttig — en efficiënt: één van je vijftien headlines dekt daarmee je hele
   keywordfocus af, zodat de andere veertien vrij zijn voor USP's en CTA's.
2. **Sterke call-to-action met een getal.** Geen "bel nu" maar "bel nu en bespaar $49" of "verhoog je
   productiviteit met 20%". Moet waar en onderbouwd zijn.
3. **Iets zeggen wat je concurrent niet kan of niet wil zeggen.** Cruciaal als je duurder bent:
   waarom zou iemand op jouw advertentie klikken als er goedkoper bestaat? Blijf weg van "wij zijn
   nummer één" — zoek objectieve feiten.
4. **Een emotionele trigger.** De fout die bijna iedereen maakt is schrijven vanuit het bedrijf.
   Elke zoekopdracht komt voort uit **pijn** of **verlangen**.
   - Niet "professionele boekhouddiensten" maar "bespaar 12 uur op je aangifte"
   - Niet "beste projectmanagementtool" maar "lever je product twee keer zo snel op"

Verdeling van de 15 headlines: één met dynamic keyword insertion, drie tot vijf USP's, drie tot vijf
call-to-actions. Vier beschrijvingen. Google toont er meestal twee (soms drie) en twee beschrijvingen.

### Het USP-werkblad

Schrijf de USP op, en zoek dan **vijf andere manieren om hetzelfde te zeggen** — met de emotie erin.
Boor aan wat mensen **haten**.

> **Privézwembadvilla.** Niet "privézwembad" (dat schrijft iedereen), maar: "skinny dip in your own
> pool" · "no sunbed wars, it's yours" · "no shared pools, just yours". Wat ze aanboren: vechten om
> ligbedden, kinderen die bommetjes maken.
> **Butlerservice** werd "app je butler wanneer je wilt".
> **Onderhoudsdienst** werd "alle huisonderhoudscontroles in één bezoek" — in plaats van vier losse
> afspraken voor airco, ventilatoren, ongedierte en rookmelders.
> **Babygehoorbescherming**: het enige merk dat zowel de Amerikaanse als de Europese veiligheidsnorm
> haalde, én in de VS geproduceerd. Dat stond in elke advertentie en op elke productpagina.

Een taalmodel is hier nuttig: "dit zijn onze USP's, schrijf het emotioneler."

### Splittesten

- **Twee advertenties tegelijk** per advertentiegroep, niet drie of vier. Bij 3+ duwt Google het
  budget toch naar de bovenste twee.
- **Eén verschil per test.** Zijn eerste test is altijd dezelfde: twee identieke advertenties,
  waarvan er één een dynamic-keyword-insertion-headline op positie 1 gepind heeft. Wint die, dan
  varieer je vervolgens de andere headlines; verliest die, dan test je in ronde twee
  call-to-actions op positie 2.
- **Looptijd**: minimaal 4 weken, in de praktijk 8–10 weken, en minstens **1.000 impressies** per
  advertentie.
- **Beslis op conversieratio en CPA, niet op CTR.**
- Blijft Google een advertentie voortrekken die volgens jouw data slechter converteert? Harde test:
  de andere pauzeren.
- Cyclus: winnaar houden, verliezer pauzeren, winnaar dupliceren, opnieuw testen.

> **Voorbeeld.** De advertentie met de *lagere* CTR won, omdat de conversieratio 5 procentpunt hoger
> lag en de CPA $34 was.
> **Voorbeeld.** CTR van 4,5% naar bijna 9% binnen een maand, daarna structureel boven 10%.

Tactiek die hij aanraadt: **werk eerst je CTR boven de 10%**, zodat je daarna een prijs- of
dienstkwalificatie in de tekst kunt zetten. Zakt de CTR daarvan met 2 punten, dan zit je nog altijd
op 7–8% en dus boven het branchegemiddelde.

### Ad strength: negeren

Puur een diagnosetool van Google, bedoeld voor de setup. Hij laat een advertentie met beoordeling
"poor" zien die de hoogste CTR, hoogste conversieratio en laagste CPA van het hele account heeft.
Gepinde headlines drukken de score. Kijk naar CTR en conversie.

### Continuïteit

De dollar- of procentbelofte in je advertentie moet terugkomen op de pagina, zodat de bezoeker weet
wat hij daar aantreft.

---

## Landingspagina's

**De landingspagina weegt zwaarder dan de campagne.** Een middelmatige campagne met targetingfouten
en zwakke teksten haalt op een goed converterende pagina nog steeds resultaat. Andersom niet: een
perfecte campagne die naar een slechte pagina stuurt, converteert niet.

Ook: stuur **nooit naar je homepage**. Altijd de specifiekste relevante pagina.

### Vijf elementen

Niet zijn eigen mening: het Australische **Test Mate** draaide ruim 10.000 gebruikerstests.

1. **Sterke headline en subheadline** die bevestigen dat de bezoeker op de juiste plek is. Gaat over
   de klant, niet over het bedrijf. Haalt de pagina de "5-secondentest" niet, dan is de boodschap
   niet duidelijk.
2. **Duidelijke call-to-action boven de vouw.** Meerdere contactopties mogen, mits ze bij elkaar
   horen; je belangrijkste conversieactie moet direct zichtbaar zijn.
3. **Rustig, leesbaar ontwerp.** Er zijn twee soorten websites: een opzichtig visitekaartje en een
   probleemoplossende site. De tweede wint altijd. Te veel animaties en pop-ups verpesten het.
4. **Autoriteitsmarkers.** Reviews, prijzen, keurmerken — voor wie je nog niet kent.
5. **Simpel afrekenen of aanvragen.** Geen drempels.

> **Casus.** Een pagina herschreven op basis van pijnpuntonderzoek. 126 weergaven leverden **drie
> directe verkopen** van een programma van $1.500 per jaar; de 1.100 weergaven daarvóór leverden
> vier conversieacties met samen $141 omzet. Sessieduur van 47 seconden naar 1:15. **Aanbod en prijs
> waren ongewijzigd** — alleen de pagina.

---

## Leadgeneratie

### Drie leadproblemen en waar je eerst kijkt

**1. Spamleads en rommelleads** ⇒ conversie-instellingen of het verkeerde campagnetype.

- **Belduur.** Google start de teller zodra de telefoon *overgaat*, niet zodra je opneemt. Standaard
  staat op 30 seconden. Zet hem op **45 tot 90 seconden**, soms 2 minuten of meer. Langer gesprek =
  waarschijnlijk betere lead.
- **Conversietelling op "één"**, niet "elke".
- **Meerstapsformulier** in plaats van naam, e-mail, telefoon. Het formulier ís je kwalificatiestap:
  wie geen 30–60 seconden over heeft voor je formulier, koopt waarschijnlijk toch niet. Vraag naar
  het type klus, onderhoud of installatie, eigen materiaal, budget. Hang er automatische antwoorden
  aan: budget onder een drempel ⇒ "wij zijn waarschijnlijk niet de juiste partij".
- **Campagnetype.** Hij is fan van PMax voor leadgen, maar **nooit als startpunt**.

**2. "Tire kickers" — echte maar verkeerde leads** ⇒ een boodschapprobleem, geen targetingprobleem.

Voorbeelden: B2B die B2C-leads krijgt, sollicitanten in plaats van klanten, prijs-mismatch.

Oplossing: kwalificeer in de **headline en op de landingspagina**. Wie duurder is, zet de prijs erin:
"vanaf $199". Bij e-commerce doet de prijs op de productpagina dat signaleringswerk vanzelf en leert
Google ervan; bij leadgen zit er **geen prijssignaal in de conversieactie**, dus moet de tekst het
doen.

Minder clicks en minder conversies is hier de bedoeling. *Google wordt betaald bij de klik; jij pas
als het geld op je rekening staat.*

**3. Leads lopen maand na maand terug zonder dat je iets veranderde** ⇒ de verschuiving naar
inferred intent. Doe een audit van keywords en zoektermen, met n-gram-analyse. Behandel de uitkomst
als **diagnose, niet als opdrachtenlijst**.

> **Casus.** In één account bleek 30% van het budget naar nieuwe keywordthema's te gaan die niet
> converteerden. Vangrails aangescherpt, prestaties keerden terug.
> **Casus.** Veel besteding aan concurrentmerken. Negatieven toegevoegd (8 van de 10 voorstellen
> overgenomen), broad match presteerde met 5% conversieratio prima, tCPA ongewijzigd gelaten.

### "Garbage in, garbage out"

PMax volgt altijd de weg van de minste weerstand en levert precies de goedkope conversies die je hem
voert.

> **Casus (Johan).** Klant met een PMax die de verkeerde conversieactie najoeg. PMax **uitgezet**,
> search het werk laten doen, offline conversies geïmplementeerd, en PMax daarna pas opnieuw aan.
> In het dashboard zag het eruit als een ramp: conversies meer dan gehalveerd (336 → 257), CPA
> omhoog. In werkelijkheid was november de **beste maand in zes jaar bedrijfsvoering**.

Aarons formulering, die hij zelf voorzichtig noemt:

> **Je conversiedata moet de laagst mogelijke kwaliteit conversie zijn die nog echte business
> oplevert.** Zet je de lat te hoog, dan krijg je te weinig data om te schalen. Te laag, en je voert
> Google rommel.

Kan een klant geen offline conversies aan? Dan een meerstapsformulier of een afspraakboeking — iets
dat **moeite** kost, zodat PMax harder moet werken.

### De volgorde in een leadgenaccount

1. Conversietracking goed zetten en controleren dat die conversies echte business zijn
2. **Twee tot drie maanden** die basis laten draaien (conversiehistorie op accountniveau reikt ~3
   maanden terug)
3. Pas dan tCPA — bij ongeveer 20% variatie over vier weken
4. Budget omhoog tot de searchcampagne verzadigd raakt: duurdere conversies, niet méér conversies
5. Dán pas PMax als tweede kanaal

> **Casus.** Lokale dienstverlener in één niet-grote Amerikaanse stad, van $20 naar $110 per dag, op
> **één campagne met één advertentiegroep**: twee broad match keywords van drie à vier woorden plus
> een set exact match. Impression share nog maar 30% — dus nog volop ruimte, en dus geen PMax.
> **Casus.** Account op >$5.000 per maand met 47 conversies in 30 dagen. PMax draait, maar krijgt
> $120 van de $575 per dag (≈20%); de rest zit in search. Ze schuiven niet verder op omdat de
> impression share nog maar 31% is en naar 60–70% kan — het budget kan ruim boven $200 per dag vóór
> PMax nodig is. En ze meten alleen telefoongesprekken.
> **Casus.** Van $150–160 naar bijna $900 per week met stijgende conversies, op één campagne met één
> advertentiegroep en zonder PMax.

Over de overlap tussen search en PMax: die is er, en dat is oké. Geen kannibalisatie zolang de
conversies goed zijn. Wel iets om op te lossen door bijvoorbeeld staatscampagnes toe te voegen op
plekken waar geen van beide kwam.

### Structuur voor dienstverleners

Vier factoren bepalen welke hefbomen je nodig hebt: dienst of product, **seizoen** (airco in het
voorjaar), locatie, en winst- of conversiemetrics (dat laatste pas later).

Adverteer niet al je diensten in al je gebieden. Concentreer op je kerndienst in je kerngebied, maak
dat winstgevend, en bouw daarna uit.

> **Casus.** Lokale dienstverlener met airco-reiniging, ventilatoren, ongediertebestrijding en
> rookmelders, én een franchisemodel over vier regio's ⇒ **vier campagnes op franchisegebied**, met
> advertentiegroepen per dienst. Kustplaatsen bleken meer airco te vragen, het binnenland meer
> ongedierte. Zónder franchisemodel had hij grotere gebieden genomen en per **dienst** gesplitst.

Betrek de ondernemer bij het meekijken, ook als de tracking niet perfect is: "$100 extra uitgegeven,
drie telefoontjes meer" is een sterker signaal dan het dashboard.

---

## E-commerce

### Merchant Center is het brein

> "Je Google Ads-account is het lichaam, Merchant Center is het brein."

Ontbrekende attributen en zwakke titels maken je **onzichtbaar**. Dit geldt voor shoppingcampagnes,
maar net zo goed voor PMax en voor shopping-assets in Demand Gen.

- **Producttitel.** De belangrijkste informatie moet in de **eerste 50 tekens**. Niet
  "Merk — tandpasta voor tandvleesontsteking" maar **product eerst, merk in het midden, modifiers
  achteraan**. Niet "zwart shirt" maar "zwart Egyptisch katoenen T-shirt, maat L, comfortabele
  pasvorm".
- **GTIN's** — het belangrijkste productattribuut. Het vertelt Google exact welk product dit is; het
  zoekt specificatie, kleur, materiaal en maat op in zijn eigen database in plaats van af te gaan op
  jouw titel. Ontbreekt het, dan is dat óf omdat het product uniek is (niets aan te doen), óf omdat
  het simpelweg niet is aangeleverd. Toevoegen via een **supplemental feed** gemapt op product-ID
  (pleister — dekt geen nieuwe producten) of, beter, via je productattributen in Shopify zodat het
  automatisch meegaat.
- **Productafbeeldingen**: geen drukke achtergronden, product centraal.
- **Store quality**: Merchant Center → product and store → store quality. Mik op **"exceptional"**,
  niet "good". Verzending, retouren, afbeeldingen, sitesnelheid — alles invullen.

### Conversie-instellingen: e-commerce is het omgekeerde van leadgen

| | E-commerce | Leadgen |
|---|---|---|
| Primair doel | **Aankoop.** Add-to-cart mag secundair — dat telt wel mee maar stuurt het bieden niet | Telefoongesprek of formulier |
| Telling | **"every"** (je stuurt de omzetwaarde mee) | **"one"** |
| Klikvenster | 90 dagen | — |
| Extra | enhanced conversions aan | belduur 45–90 s, meerstapsformulier |

De klassieke fout is add-to-cart als primair doel zetten. Dan optimaliseert maximize conversion value
op mensen die dingen in een winkelwagen leggen.

### Startstructuur en budget

Eén niet-merkgebonden **searchcampagne** + één standaard **shoppingcampagne**. Eventueel een derde,
kleine merkcampagne — maar als startend merk is dat vaak weggegooid geld op zoekopdrachten die je
toch al wint.

Budget: **gemiddelde CPC × 30, per campagne**. Bij een CPC van $3 is dat $90 per dag per campagne,
dus ruim $180 in totaal.

**Concentreer je budget.** Niet al je SKU's.

> **Voorbeeld.** Merk met vijf productcategorieën adverteert er twee (handdoeken en badjassen).
> **Voorbeeld.** Merk met tandpasta, mondwater en tandenborstels ging **volledig op tandpasta** — de
> winstgevendste en makkelijkst te verkopen — en verkocht de rest via bundels.

### Waarom search en shopping eerst, en niet PMax

PMax werkt alleen met een goede feed. Is de feed slecht, dan zakt je ranking in shopping en gaat PMax
het geld uitgeven in Discover, Gmail en display. Met search en shopping krijg je bovendien een veel
snellere terugkoppeling: welke advertentietekst werkt niet, kloppen je producttitels en attributen.

Brent (e-commerce coach) begint liever met een **feed-only PMax-campagne dan met een klassieke
shoppingcampagne**, omdat feed-only ook doelgroepsignalen en zoekopdrachtsignalen meeneemt. Daarna
pas een volledige PMax erover, en searchcampagnes voor controle.

Zijn drempel voor PMax: conversiedata is nummer één, én hij wil zien dat **meerdere producten
converteren**, niet één kampioensproduct terwijl de rest niets doet. Bij een kleiner account ~30+
aankopen per maand. Hij wil zo snel mogelijk naar PMax — geen drie jaar data afwachten.

### De product labelizer

Producten worden op basis van je noordster-KPI (bijvoorbeeld 2× ROAS) automatisch ingedeeld:

- **Over-index** — presteren consequent ruim boven doel, veel clicks én aankopen
- **Index** — rond het doel, bewezen
- **Near-index** — op of boven het doel, maar te weinig data om bewezen te heten
- **No-index** — te weinig data voor welk oordeel dan ook (meestal het gros van je SKU's)
- **Under-index** — presteren slecht

De snelste ingreep: **sluit de under-index-producten uit van je grootste en schalende campagnes.**
Geef ze wel een **kleine restcampagne** met laag budget — sommige zijn seizoensgebonden, of hadden
gewoon een slechte periode.

Het label werkt dynamisch en actualiseert zichzelf, dus de eerste opzet is belangrijk. Hij gebruikt
de gratis versie van Flow Boost.

### Wanneer shopping en PMax naast elkaar mogen draaien

Alleen met een **reden**. Ofwel de PMax zit sterk op het zoeknetwerk, ofwel de shoppingcampagne
draait op een **duidelijk hogere tROAS** en bedient specifieke attribuutzoekopdrachten (materiaal,
maat) met een lange converteergeschiedenis.

Zonder zo'n verschil — zelfde producten, zelfde netwerken, zelfde tROAS — is het gewoon dubbelop.
Pauzeer er één.

**Campagneprioriteit** is alleen relevant als een shoppingcampagne en een PMax-campagne dezelfde feed
en producten bedienen; dan geef je Google een signaal welke voorgaat.

### Als het na 60 dagen niet loopt

Diagnose op sessieduur (zie Diagnose 1). Is het zoektermverkeer aantoonbaar relevant — te
controleren via insights & reports → search terms in je shoppingcampagne — en komt het toch niet
rond, dán is dat het moment om de **shoppingcampagne uit te zetten en PMax te proberen** terwijl
search blijft draaien.

Reden om niet meteen met PMax te beginnen: de shoppingcampagne levert je in die 60 dagen juist de
zoektermdata die je nodig hebt om dit te kúnnen beoordelen.

### Realistische verwachtingen

**Reken op drie tot zes maanden voordat je rendement ziet.** Merken komen te vaak bij Google Ads als
laatste redmiddel, met nog $2.000 op de bank, en geven het platform drie weken om het bedrijf te
redden. Dat gebeurt niet. Google kan een zwak aanbod of een verkeerde prijsstelling niet oplossen,
hoe gericht het verkeer ook is.

---

## Performance Max

### De optimalisatiehiërarchie

Conversiedata staat bovenaan; al het andere is ondergeschikt. PMax zit vast op maximize conversions
of maximize conversion value, dus je hebt minder knoppen. Alles hangt aan *welke conversieactie je
Google laat najagen*.

Google zegt zelf dat de andere signalen — assets, doelgroepen, zoekopdrachtsignalen — **suggesties**
zijn, geen harde regels.

### Instapdrempel

30 conversies per 30 dagen. Startbudget = genoeg voor **minstens één conversie per dag**. CPA $50 ⇒
$50 per dag.

### Instellingen die je moet controleren

- **Merkuitsluitingen.** Eigen merk, eventueel een tweede lijst met concurrentmerken. Kan een paar
  dagen duren voor het actief is.
- **Page feeds** om PMax tot bepaalde producten of diensten te beperken.
- **Demografische uitsluitingen** — alleen met harde data.
- **Locatie op "presence".**
- **Data-uitsluitingen** om bestaande kopers uit te sluiten. PMax is voor nieuwe klanten.

Voeg je een merkuitsluiting toe aan een campagne die veel merkverkeer converteerde? Haal dan ook de
tCPA/tROAS weg zodat de campagne kan resetten op de nieuwe regels.

### Kanaalverdeling — de belangrijkste PMax-diagnose

Insights & reports → channel performance, met alléén de PMax-campagne geselecteerd.

Goede PMax-campagnes besteden **~95% aan search + shopping**. Meer dan 5% naar display, YouTube of
discovery is een zwakke campagne. (In een andere video noemt hij de drempel 90% — gebruik het als
bandbreedte.)

Wat het betekent als het scheef staat: te weinig conversiedata, of bij e-commerce een vuile
productfeed. Er zijn betere kanalen om op display en YouTube te adverteren — Demand Gen en
videocampagnes geven je controle over de creaties, PMax niet.

### Negatieve keywords in PMax

> "Just because you can doesn't mean you should."

Alleen hele **thema's** blokkeren die je echt niet levert (kinderkleding als je die niet verkoopt,
installaties als je alleen onderhoud doet) of concurrenten. Veel irrelevant verkeer betekent te
weinig conversiedata, niet te weinig negatieven.

### Assets

Assets → performance, filteren op assettype. Vervang de headlines waar Google geen geld aan besteedt.
Follow the money.

Landingspaginarapport: insights & reports → report editor → landing pages.

### Zou je ooit alléén PMax draaien?

Johan: **nee.** Zolang searchcampagnes bestaan blijven ze het fundament, omdat ze de enige plek zijn
waar je zegt "dít wil ik". Aaron beaamt dat: search voedt continu accurate data terwijl PMax zijn
gang gaat.

---

## Demand Gen en creatietesten

### Demand Gen

Draait niet op keywords maar op **plaatsing, doelgroep, creatie**. Beoordeel het ook anders.

Meestal een **tweede of derde golf** campagne. Uitzondering: een educatief bedrijf of een product dat
de markt nog niet kent — dan mag Demand Gen vooraan.

**Halo-effect.** Meet het niet als "budget in, conversies uit binnen 30 dagen". Kijk of merk-,
organisch en direct verkeer stijgen, en of search, shopping en PMax na 90 dagen een lagere CPC of
CPA laten zien.

**Twee functies, kies er expliciet één per campagne:** remarketing (bezoekers of kijkers van de
laatste 60 dagen) of expansie (top of funnel, nieuwe markten).

**Structuur.** Advertentiegroepen per plaatsing — shorts, in-stream, in-feed, display — zodat je de
besteding tussen die formaten kunt sturen. In-feed is je advertentie bij een zoekopdracht *binnen*
YouTube.

**Doelgroepen.** Audiences, keywords & content → audience segments. Look-alikes en interesses apart
houden. Doelgroepen die veel geld kosten zonder data: uitzetten. Demografie pas uitsluiten na
**60–90 dagen** data.

**Creatie is make-or-break.** 3 tot 5 *verschillende hoeken* per advertentiegroep, niet alles in één
advertentie — dan kun je niets snel uitzetten. Groepeer meerdere beelden onder dezelfde hoek, zodat
je data op hoekniveau leest.

**Video play-through** als kolom toevoegen. Hoge kijkstart = goede hook. Snel afhaken = het aanbod.
Wel uitkijken maar niet converteren = aanbodprobleem.

Testduur ~30 dagen, soms 6 weken tot 2 maanden. Display minstens **2.500 impressies** per hoek.

**Realistisch: elke 4–6 weken nieuwe creaties.** Kun je dat niet volhouden, begin dan niet aan Demand
Gen. Vooraf batchen werkt niet, want je maakt de volgende ronde op basis van de data.

### Drie kaders voor creatietesten (Brent)

Randvoorwaarde die hij drie keer herhaalt: **dit is niet voor je eerste jaar.** Search, shopping en
PMax moeten al winstgevend draaien; je landingspagina en je aanbod mogen geen open vragen meer zijn.

Uitgangspunt: **zachte metrics (CTR, view rate, watch time) meten aandacht, niet impact.**

**Kader 1 — Cost Curve Response.** Draai dezelfde creatie op **drie bestedingsniveaus**.

- **Hero**: CPA blijft gelijk bij hogere besteding ⇒ schaalbaar over elk publiek
- **Center**: houdt het redelijk vol, maar niet publiek-onafhankelijk
- **Audience locked**: breekt bij schaal ⇒ werkt alleen bij één publiek of fase

Gebruik dit vooral bij accounts met veel budget.

**Kader 2 — Creative Decay Rate.** Hoe lang tot je CPA verdubbelt?

- Sterke **beeld**creatie: 60–90 dagen half-life
- Sterke **video**creatie: 90–180 dagen

Eerder is een zwakke creatie — tenzij de context iets anders zegt (een Black Friday-creatie draai je
geen 180 dagen). Gebruik dit vooral bij accounts die het van beeld moeten hebben; display verslijt
sneller omdat mensen er blind voor worden.

**Kader 3 — Cross Audience Portability Score.** Draai dezelfde creatie tegen 3–4 doelgroepen:
retargeting, look-alikes, koude prospectie, brede demografie.

De vraag die dit beantwoordt: **werkte die creatie, of ging die persoon toch al kopen?**

Retargeting geeft altijd een lagere CPA; dat zegt op zichzelf niets. Is het verschil met koud en
breed extreem groot, dan is de creatie niet schaalbaar — en dat is prima, dan weet je dat het een
bodem-van-de-funnel-creatie is. Kost wel ongeveer vier keer je testbudget. Gebruik dit vooral bij
video-gedreven accounts.

### Boodschap per funnelfase

- **Koud** — kent je niet, weet misschien niet eens dat er een probleem is. Niet verkopen.
  Introduceren op een manier die niet afschrikt, en de gedachte "dit zou ik kunnen gebruiken"
  oproepen. Een korting van 10% betekent niets voor wie je niet kent.
- **Midden** — probleembewust, nog niet oplossingsbewust. Hier werken oprichtersverhalen: waarom
  besta je, waarom doe jij het anders.
- **Retargeting** — kent je en kent het aanbod. Herinneren, drempels wegnemen, sociale bewijskracht,
  reviews, eventueel een aanbod om ze over de streep te trekken. Ook educatie en waarde werken hier.

Dezelfde creatie mag in alle fasen draaien — de test vertelt je juist in welke fase hij het sterkst
is.

### Van Meta naar Google

Zeker testen — je hebt honderden bestaande creaties. Maar **neem niet aan dat wat op Meta werkt ook
op Google werkt.** Merken discounten de Google-cijfers ("onze CPA is normaal $40, hier $250, maar op
Meta werkt het, dus het zal wel goed zijn") en negeren zo echte underperformance. Brents eerlijke
kanttekening: meten is het zwakste punt van Google in dit domein, en het duurt tijd voordat Google
leert.

Twee aanvullingen van Aaron: schrijf creaties die het op Meta *niet* deden niet af, en let op het
**halo-effect** — kijk niet alleen naar de campagnedata maar ook of je CPC's en CPA's in search en
shopping veranderen.

---

## AI als gereedschap

### De hoofdregel

**Diagnose-instrument, geen bestuurder.** Hij krijgt wekelijks aanbiedingen om AI-tools te promoten
die "je Google Ads optimaliseren". Zijn beeld: bij een goudkoorts worden de mensen rijk die schoppen
verkopen. Hij weigert ze allemaal — maar is uitgesproken vóór het gebruik van de modellen zelf.

Drie regels:

1. **Geef het geen controle.** Geen koppeling die live wijzigingen in je account doorvoert.
2. **Volg niet elke uitkomst.** Het hallucineert, en het kent je bedrijfsdoelen niet volledig.
3. **Vergeet je eigen inzicht niet.** Niemand kent je bedrijf zoals jij.

> **Jij bent de strateeg; het model is je onderzoekspartner.**

### Waarom geen live koppeling

Niet uit angst voor techniek, maar vanwege de **success loop**. Een tool die dagelijks wijzigt, breekt
die lus. Zo'n tool mist bovendien de context van de veiling: een concurrent die er $300.000 in dumpt,
seizoen, geopolitiek.

> **Casus.** Een bedrijf koppelde zo'n tool. Die voegde in **zeven dagen 498 phrase match keywords**
> toe plus een eindeloze negatievenlijst.

Twee risico's die zijn coaches noemen: **accounttoegang** (één tool gekoppeld aan duizenden accounts
is een aantrekkelijk doelwit, zoals WordPress-plugins) en het feit dat er al voorbeelden zijn van
**Meta-accounts die geblokkeerd werden** omdat een AI te veel wijzigingen doorvoerde.

Aaron voegt toe dat hij zelfs de aanbevelingen ín het Google Ads-dashboard niet vertrouwt — ook AI,
ook zonder bedrijfscontext.

### Context is alles

Zeven invoeren die hij meegeeft: **merkstem · transcripten van verkoopgesprekken · opnames van
optimalisatiesessies · klantreviews · klantpersona's · doelen en winstmarges · conversiehiërarchie.**

Daarnaast: exporteer altijd je échte accountdata, en beschrijf hoe je zelf werkt.

**Nooit algemene vragen stellen** ("wat raad je aan voor Google Ads?"). Zonder context krijg je een
plausibel maar fout antwoord.

### Overlay-analyse — de sterkste toepassing

Leg **Google Ads-data** naast **echte bedrijfsdata**. Waar ze elkaar overlappen, zit de strategie.

> **Casus.** Juridische dienstverlener met een groot offline verkoopproces; ze meten niet leads maar
> de omvang van de schuld die ze binnenhalen. Ze legden het aantal echte klanten per staat naast de
> clicks en conversies per staat uit Google Ads. Uitkomst: hun **waardevolste klanten kwamen uit
> staten waar nauwelijks budget heen ging** — onzichtbaar in Google Ads alleen. Gevolg:
> staatsgerichte campagnes uitgebroken.

### Concrete toepassingen

- **SWOT- en n-gram-analyse** op keyword- en zoektermenexports (1-, 2- of 3-woordgroepen). Waar zit
  omzet, waar zit verspilling, waar is een thema met weinig besteding en veel conversies. Ook
  geschikt voor 12 maanden data bij een audit.
- **Verandergeschiedenis exporteren**, gesegmenteerd per week of maand, en laten samenvatten.
- **Vergelijk oude en nieuwe zoektermen** (niet de keywords — de zoektermen) om te zien hoe Google
  anders is gaan matchen.
- **Compliance-controle.** Account in de financiële sector met 50+ advertenties van 15 headlines.
  Alles geëxporteerd en laten controleren op wat wel en niet gezegd mag worden. Een week werk werd
  een paar uur, en het ving menselijke fouten af die eerder door het compliance-team werden gepakt.
- **Advertentieteksten opzetten** en in een Ads Editor-uploadsjabloon laten zetten.
- **Week-op-week segmentatie** in Google Ads als datavorm voor analyse over campagnes heen.

### Pijnpuntonderzoek

Laat het model Reddit-fora, Facebookgroepen, Google reviews, Yelp en TripAdvisor afstruinen op de
pijn- en verlangenspunten van jouw klant, en koppel headlines daaraan. Een bevriende tekstschrijver
deed dit onderzoek in **twee dagen**; nu in vijf minuten tot een uur.

> **Casus.** Sterk gereguleerde juridische niche in de VS, klant schaalt naar $200.000 per maand.
> Advertentierapport plus alle verkoopgesprekken ingevoerd. Resultaat: **25 headlines om over drie
> tot vier maanden te testen, waarvan het juridische team er slechts twee afkeurde.** Thema's die
> eruit kwamen: angst voor telefoontjes van incassobureaus, schaamte, isolement, opluchting, hoop op
> een uitweg.

Dit soort onderzoek was voorbehouden aan grote bedrijven met consultants. Nu ligt het binnen bereik
van iedereen die een fatsoenlijke prompt draait.

### Management by exception (Mike Rhodes)

Hiërarchie: **data → informatie → inzicht → actie → bedrijfsuitkomst.** Klanten willen geen dashboard
en zelfs geen inzichten; ze willen weten wat er in hun bedrijf verandert.

Stap 1 (data → informatie) is scripts die exports automatiseren — meestal direct ~5 uur per week.
Stap 2 (informatie → inzicht) vereist context.

> **Casus.** Een smart-bidding-script gaf per campagne een rood/groen/wacht-signaal. Rood klopte
> altijd; groen controleerde hij zelf. Over vijf accounts en veertig campagnes wees het de twee aan
> die aandacht nodig hadden. De winst zat niet alleen in tijd maar in **mentale energie**: je begint
> je dag niet uitgeput door bezigheidswerk.

### Praktische adviezen

- **Vraag het model hoe jij de data het best kunt aanleveren.**
- Loop je vast: laat het in een apart gesprek eerst de prompt voor je schrijven, en plak die in een
  nieuw gesprek.
- Dicteren werkt vaak beter dan typen.
- Bouw vertrouwen stapsgewijs: laat het eerst tonen wat het deed, geef feedback, en pas als het tien
  of twintig keer achtereen klopt laat je het doorlopen.
- **Kies op systeem, niet op model.** ChatGPT, Claude en Gemini liggen qua intelligentie dicht bij
  elkaar. Kies op integratie (Google Docs/Sheets ⇒ Gemini) en use case. Aaron en zijn coach Daniel
  gaven in mei 2026 de voorkeur aan **Claude** voor keyword- en tekstanalyse, omdat het terugduwt in
  plaats van te pleasen. Ze zeggen er expliciet bij dat dat over drie maanden anders kan zijn.

### Drie scripts die hij onmisbaar noemt

Zijn selectiecriteria: makkelijk op te zetten, veel tijdwinst, en het moet iets geven dat **niet al
in het dashboard staat**. Een script dat een bestaande rapportage nabouwt, is werk voor niets.

1. **n-gram-keywordanalyse.** Groepeert je zoektermen op los woord in plaats van op hele zoekopdracht.
   Levert drie soorten optimalisaties tegelijk: negatieve keywords, nieuwe keywordthema's, en
   segmentatie.
   > **Casus militaire uitrusting.** Alles met het woord "dive" erin converteerde veel beter dan de
   > zoekopdrachten met alleen "snorkel".
   > **Casus airco-bedrijf.** Alles met het woord "calculator" presteerde fors beter — daar hebben ze
   > vervolgens een eigen campagne voor gemaakt.
2. **Smart bidding-analyse.** Draait de ja/nee/wacht-checklist uit het biedhoofdstuk automatisch over
   al je campagnes: 30 conversies per maand? · wekelijkse conversies stabiel binnen 20% variatie? ·
   biedstrategie in de laatste 6 weken gewijzigd? · budget recent gewijzigd? Zes campagnes in 10–15
   seconden, waar hij er handmatig 5–10 minuten per campagne over doet. Bij een "ja" controleert hij
   het altijd zelf na — het script is een filter, geen beslisser. (Hij liet dit bouwen omdat het niet
   bestond.)
3. **Een PMax-script.** Nog steeds onmisbaar ondanks de betere rapportage in het dashboard, om drie
   dingen: scheiding tussen het search- en het shoppingnetwerk, vergelijking tussen meerdere
   PMax-campagnes (overlappen ze in producten?), en een kwadrantweergave die je **zombieproducten**
   toont — producten die in je feed zitten maar geen enkele besteding krijgen.

De scripts die hij noemt komen grotendeels van Mike Rhodes. Het punt hier is niet welk script, maar
welke drie analyses je mist als je alleen naar het dashboard kijkt.

### Wat je bewust níét hoeft te automatiseren

Met de juiste structuur en data hoef je veel minder te optimaliseren dan je denkt:

- Advertentietekst-tests: maandelijks. Boven zes cijfers besteding elke 2–3 weken. Kleine accounts
  elke 6–8 weken.
- Biedstrategieën: elke 2–3 maanden.
- Negatieve keywords: alleen vangrails voor wat je écht niet levert.

Terugkerende reactie van klanten na twee tot drie maanden in zijn programma: *"wat deed mijn vorige
bureau eigenlijk?"* — omdat de winst in structuur en data zat, niet in wekelijks sleutelen.

---

## Lokale dienstverleners en aannemers

Uit een gesprek met **Mike Mancini**, die uitsluitend met home-servicebedrijven werkt (loodgieters,
elektriciens, dakdekkers, hoveniers). Hij is het op een paar punten oneens met Aaron; die
meningsverschillen staan hieronder zoals ze in het materiaal staan.

### Waar Mancini afwijkt

- **Hij houdt formulieren juist kort.** *"Mensen gaan veel te diep en vragen zich dan af waarom ze
  geen conversies krijgen. Je vraagt naar hun bloedgroep."* Zelfs om een adres vragen is volgens hem
  al een drempel: ze hebben je nog niet ingehuurd. Dit staat **haaks op Aarons meerstapsformulier**
  uit het leadgenhoofdstuk. Aaron laat het staan zonder het glad te strijken.
- **Hij start met ongeveer 2.000 negatieve keywords** uit branche-ervaring, vóór de campagne
  überhaupt draait. Dat wringt met "voeg niet honderden negatieven toe".
- **Geen display remarketing bij spoedeisend werk.** *"Mijn wc lekt"* vraagt niet om iemand die je
  twee weken achtervolgt. Aaron nuanceert: bij lange aankooptrajecten — zijn voorbeeld is zakelijke
  IT — werkt remarketing wél.
- **PMax pas met offline conversies**: daar zijn ze het over eens, maar Mancini is strenger. Hij test
  het alleen in zeer competitieve markten en heeft er zelf nog geen goede resultaten mee.

### Waar het bij kleine dienstverleners echt om draait: reactiesnelheid

Dit is het punt waar beiden het hardst op drukken, en het ligt buiten Google Ads.

- Onderzoek dat Mancini aanhaalt: **341% meer kans** op een lead bij reageren binnen 5 minuten, en
  **400%** binnen 60 seconden.
- Zijn eigen test: vier aannemers gebeld via hun advertenties, allemaal voicemail. De eerste belde na
  10 minuten terug, daarna 4 uur, 8 uur, de volgende dag. **De eerste kreeg de klus van $1.700.**
- Ze bellen klanten op via het tracking-nummer: *"Jullie hebben de laatste tien telefoontjes niet
  opgenomen. Hoe moet dit dan werken?"*
- *"Je kunt tegenwoordig een antwoorddienst inhuren voor onder de $200 per maand. Levert die één klus
  op, dan heb je hem voor zes maanden terugverdiend."*
- Wat ze het vaakst horen in gespreksopnames: **"O, je neemt op."** En die krijgt de klus.

### De rest van het beeld

- **Een conversie is de eerste winst, niet het einde.** Niemand sluit 100% van zijn leads. Voorbeeld:
  één elektricien die hij inhuurde leverde via twee doorverwijzingen ruim $5.000 op.
- **Wat je meet als je geen CRM hebt**: een simpele spreadsheet waarin de ondernemer 10–20 minuten
  per week de werkelijke omzet per lead invult. Waarschuwing erbij: *"is het niet geautomatiseerd,
  dan gebeurt het niet"* — Aaron zegt dat je 3–6 maanden nodig hebt voor bruikbare data, Mancini zegt
  meestal sneller.
- **Twee waarschuwingen over lead*kwaliteit*.** Beiden vertellen een casus waarin de klant klaagde
  over slechte leads en het probleem **buiten Google Ads** lag: bij Aaron een nieuwe receptioniste,
  bij Mancini een verkoper die was gepasseerd voor promotie en bewust deals liet klappen. Controleer
  wie de leads aanneemt voor je aan de campagne sleutelt.
- **Verwachtingen**: maand twee is beter dan maand één, maand drie beter dan twee. *"Google Ads is
  geen Hail Mary."* Is het je laatste redmiddel omdat het bedrijf omvalt, dan is het geen goede
  match.

> **Werk je aan een aannemersbedrijf?** Reken dan eerst met `/aannemer` na of de marge en de
> break-even kloppen. Meer leads bij een kapotte prijs versnelt alleen het verlies.

---

## Local Service Ads

Alleen relevant waar Google ze aanbiedt; in Nederland en België niet of nauwelijks. (Interview met
Ashley.)

- **Positie boven de gewone zoekadvertenties**, daarboven niets. Daaronder pas ads, kaartresultaten,
  organisch. Ziet eruit als een bedrijfsprofiel: sterren, reviews, bedrijfsinfo.
- **Betaling per lead**, niet per klik. Klikken en rondkijken is gratis; je betaalt bij bellen of
  berichten.
- **Veel minder controle.** Geen keywords, geen zoektermen, geen uitsluitingen, geen eigen headlines
  of beschrijvingen. Je vinkt diensten aan, verder doet Google het.
- **Verificatie en achtergrondcontrole** met licenties. Dat vinkje is het vertrouwenssignaal.
- **Rankingfactoren**: reviews (aantal, instroom, en of je erop reageert) en **reactiesnelheid**.
  Voicemail en onbeantwoorde berichten zijn negatieve signalen die je positie omlaag duwen.
- **Optimalisatie**: leads markeren (goed, slecht, geboekt, buiten servicegebied, dienst die je niet
  levert). Biedstrategie: maximize leads, eventueel met een maximum kosten per lead.
- **Locatietargeting strak houden.** Te breed ⇒ leads van 30 minuten verderop die je niet kunt
  bedienen ⇒ negatief signaal ⇒ slechtere posities.
- **Begin er niet mee** als je nieuw bent, geen reviews hebt, of geen systeem hebt om snel op leads
  te reageren. Dan eerst search, ondertussen een reviewsysteem opbouwen — een geautomatiseerd
  sms'je 2–3 dagen na de klus dat eerst vraagt of ze tevreden zijn, en pas dan om een review — en na
  drie à vier maanden LSA erbij.
- Wil je een specifieke niche binnen je vak targeten: dat kan alleen met searchads.
- Terugkoppeling: de telefoongesprekken worden opgenomen. Hoor je steeds hetzelfde type klus goed
  converteren, test dat dan ook in je searchcampagne.

---

## Black Friday (kalenderafhankelijk, maar de logica is duurzaam)

**Black Friday is geen evenement dat je in oktober begint.**

De onderliggende logica: tijdens Black Friday stijgen **terugkerende** klanten het hardst — e-mail,
merken die men al kent, aantrekkelijke korting — en die zijn ook het efficiëntst. Dus iedere nieuwe
klant die je nú binnenhaalt, vergroot de kans op een herhaalaankoop in november.

- **Augustus + september — nieuwe klantacquisitie.** Merkbekendheid opbouwen kost tijd. September
  zakt vaak wat weg; gebruik die maand **analytisch**: welke creaties werken, en plan de creatieve
  productie voor de twee maanden erna.
- **Oktober — generiek, niet-merkgebonden verkeer opschalen.** Google's eigen data laat elk jaar
  hetzelfde patroon zien: generieke zoekopdrachten lopen op vanaf **eind oktober**, storten in
  **precies op de dag dat de sale begint**, en merkzoekopdrachten schieten dan omhoog. Mensen doen
  hun onderzoek vóór Black Friday en leggen lijstjes aan.
  Zet in op search, shopping, Demand Gen en vooral YouTube, met **educatieve** content, niet met
  harde CTA's. Shorts bewaar je voor de sale zelf.
  Verwacht dat je gerapporteerde resultaten **niet mooi** zijn. Aanvaard ~20% minder ROAS dan
  normaal, eventueel break-even. Stuur op **engagementsignalen**: sessieduur, pagina's per sessie,
  add-to-carts, begin-checkouts, e-mailinschrijvingen.
- **November** — eerste twee weken nog steeds niet-merkgebonden opbouwen. Derde week: Demand Gen
  aanzetten met **waardegedreven, evergreen creaties** (die presteren tijdens sales vaak juist het
  best) om die campagnes warm te draaien. Vierde week: merkcreaties en de sale.

**Wanneer je je aanbod naar buiten brengt**: twee tot drie weken vóór Black Friday is het maximum.
Brent heeft merken hun sale in oktober zien aankondigen — "dat mislukte verschrikkelijk". Test je
aanbod niet vooraf op je markt; test je *creaties*.

**Eerlijke kanaalopmerking.** Brent zegt onomwonden dat **Meta Google in negen van de tien gevallen
verslaat tijdens verkoopperiodes** en stuurt vaak het grootste deel van het salebudget daarheen.
Google verdient zijn plek in de opbouwmaanden.

Brents analogie: augustus en september is je marketingteam dat leads binnenhaalt, oktober en begin
november is kwalificeren, en Black Friday is je verkoopteam dat oogst.

Rode draad: **verwacht niet dat klanten zich anders gedragen dan jijzelf.** Bijna niemand ziet een
advertentie en koopt dezelfde dag; producten blijven dagen of weken in een winkelwagen. "Omdat je het
niet kunt meten, betekent niet dat het niet gebeurt."

Bouw jaar op jaar een **playbook** met de lessen van vorig jaar.

---

## Een campagne opzetten: de checklist

De instellingsvallen, verzameld. Google's defaults staan op meerdere plekken tegen je in.

- Google's onboarding zet je campagne standaard op **Performance Max**. Klik door naar "view other
  campaign types" en kies **search**.
- Google dumpt automatisch keywords in je campagne. In zijn eigen voorbeeld (villa's met alleen 1-
  en 2-slaapkamers) stelde Google *vier*- en *drie*slaapkamervilla's voor, plus "goedkope villa's".
  Verwijderen.
- Beschrijf je producten en diensten **specifiek**, niet breed.
- **Locatie op "presence"**, niet "presence or interest".
- **Eén taal per campagne.**
- **20–30 doelgroepsegmenten, als observatie** — geen targeting, alleen data-opbouw voor later
  (YouTube, Demand Gen, remarketing). Detailed demographics is nuttig bij dienstverlening
  (huiseigenaar versus huurder); zie je later dat huurders alleen geld kosten, dan kun je ze
  uitsluiten.
- **Zoekpartnernetwerk én displaynetwerk uit.** Het partnernetwerk omvat honderden niet-Google-sites
  en geparkeerde domeinen, en sommige biedstrategieën werken er sowieso niet. Displayadvertenties
  wil hij wél, maar in een eigen campagne met controle over de creaties — hier grijpt Google zomaar
  afbeeldingen van je site en gebruikt het restbudget voor verkeer van lagere kwaliteit.
- **AI Max uit** — en na publicatie nóg een keer controleren, want Google zet het soms zelf aan.
- Google's automatische keyword- en assetgeneratie **overslaan**.
- **Landingspagina: nooit je homepage.**
- **Matchtypes: exact + broad, geen phrase.**
- **Biedstrategie: maximize clicks** om te beginnen. Een max-CPC-limiet alleen bij extreme spreiding
  ($5 tot $70 per klik), niet bij $2–$4.
- **Advertentieschema** als je alleen tijdens kantooruren gebeld wilt worden.
- **Sitelinks, callouts, prijspromoties, display path** invullen.
- **Budget berekenen vanuit clicks, niet vanuit een bedrag.** Zie de datadrempels hierboven.
- Het dagbudget wordt maandelijks verrekend (×30,4): sommige dagen $50–60, andere $10–20. Niet
  dagelijks op staren.
- Bij shoppingcampagnes: geen keywords, geen advertentieteksten. Advertentiegroepen indelen op
  producttype (of item-ID bij weinig producten).

---

## Tijdgebonden — controleer dit voor je erop vertrouwt

Alles in dit hoofdstuk is een momentopname uit 2026. De onderliggende redeneringen blijven bruikbaar;
de feiten en data's vrijwel zeker niet.

### AI Max en het einde van Dynamic Search Ads

**Tijdlijn zoals bekend in 2026:**

- Mei 2025: AI Max uitgebracht (beta)
- 15 april 2026: uit beta, officieel live
- Daarna: je kunt **geen nieuwe Dynamic Search Ads of DSA-advertentiegroepen meer aanmaken**
- **September 2026: gedwongen migratie.** Bestaande DSA's gaan over naar AI Max.

Aarons advies: migreer zelf, maar **in een aparte campagne** — niet door AI Max aan te zetten binnen
je bestaande searchcampagne.

**Zijn positie, en hoe die verschuift.** Kernanalogie die hij consequent gebruikt: **AI Max staat nu
waar Performance Max in 2022 stond.** PMax kwam in 2022 uit maar werd pas eind 2023/2024 breed
bruikbaar; nu draait 90%+ van zijn accounts erop. Hij verwacht dat AI Max die weg sneller aflegt.

- Mei 2026: **geen enkel account in zijn coachingprogramma's gebruikt AI Max.**
- Kort daarna: "voor de meeste bedrijven nog steeds een groot nee."
- Na Google Marketing Live 2026: **"2026 wordt het jaar waarin een flink deel van de bedrijven naar
  AI Max zal moeten."** Nog niet deze week of deze maand, maar het komt snel.

Dat is een verschuiving binnen enkele maanden, geen tegenspraak.

**Zijn drie bezwaren:**

1. **Geen aantoonbare incrementele reikwijdte.** Audit van een account dat AI Max per ongeluk had
   aangezet (het is heel makkelijk aan te klikken), 5 weken, opzet met twee broad match en drie
   exact match keywords: **83% van de zoektermen** die AI Max opeiste werd al door broad of exact
   geraakt, goed voor **92% van de clicks en 100% van de conversies**. In een eerdere test: 87% van
   de zoektermen, 92–93% van de conversies.
2. **Hij vertrouwt de gegenereerde teksten niet.** Voorbeeld: headlines die midden 2026 naar 2025
   verwijzen. Je kúnt regels toevoegen, maar zoiets basaals zou het systeem zelf moeten afvangen.
3. **Google publiceert geen drempels.** Voor PMax wisten we het: 30 conversies voor smart bidding,
   50 voor tCPA/tROAS. Voor AI Max is er alleen een belofte — en die belofte verschilt per bron:
   in februari 2026 citeert hij Google met **"14% meer conversies"**, in mei met **"+7%
   conversieratio bij gelijke CPA/ROAS"**. Twee verschillende getallen voor twee verschillende
   metrics. Hij zegt herhaaldelijk om minimumdrempels gevraagd te hebben en ze niet gekregen te
   hebben.

**Extra argument:** heb je een search impression share **onder 60%**, dan heb je AI Max niet nodig.
Bij 10–20% zit al je groei nog gewoon in budget verhogen → broad match → smart bidding → segmentatie
→ PMax.

**Technische verschillen DSA → AI Max:**

- **Zoekopdrachten vinden.** DSA scrapte de URL's die je opgaf. AI Max gebruikt daarnaast je
  headlines, de keywords in de advertentiegroep en realtime intentiesignalen. Google heeft niet
  uitgelegd hoe dat verschilt van broad match of PMax.
- **Teksten.** DSA schreef alleen headlines; AI Max laat Gemini ook de beschrijvingen schrijven.
- **Landingspagina's.** AI Max kiest zelf de best passende pagina. Dus óf al je pagina's zijn klaar,
  óf je stelt stevige regels in zodat het niet naar blogpagina's stuurt.
- **AI Max staat op campagneniveau** en raakt dus álle advertentiegroepen in die campagne. Precies
  daarom wil hij een aparte campagne: bij PMax kon je het testen afschermen van search en shopping,
  hier niet.

**AI briefs** (aangekondigd op Google Marketing Live 2026) waren voor hem de eerste stap die
vertrouwen gaf: je kunt tot **25 termuitsluitingen** opgeven (zeg niet "gratis", zeg geen bepaalde
kleuren) en tot **4.300 tekens aan boodschapuitsluitingen**. Door Google zelf "experimenteel"
genoemd.

### Het tegengeluid: Andrew Lok (Savvy Revenue)

Bewaren als een echt meningsverschil, niet als ruis. Andrew runt een boutique e-commerce Google
Ads-bureau, 15 jaar ervaring, eerder een bureau met 200 medewerkers. Hij staat op bijna elk punt
tegenover Aaron:

- **Hij is fel tegen PMax als concept**, maar **enthousiast over AI Max**. Precies andersom.
- **Hij gebruikt nauwelijks broad match.** Zijn stelling: de heilige graal is zoekterm → advertentie
  → landingspagina, en broad match breekt die keten. Pauzeer je "racefietsen", dan neemt
  "mountainbikes" die zoekterm over via broad match, en toon je de verkeerde advertentie: lagere
  CTR, lagere conversie.
- Hij verwacht dat **AI Max broad match gaat doden** — de broad-matchfunctionaliteit zit erin
  ingebakken, en AI Max kan er bovenop een betere headline schrijven en naar een beter passende
  pagina sturen.
- **Hij gebruikt geen negatieve keywords.**
- **Zijn drempel voor AI Max ligt veel hoger.** Onder 100 conversies per maand wordt hij nerveus;
  voor sommige dingen wil hij 300–500+. Reden: smart bidding biedt binnen AI Max per zoekterm; zonder
  conversies op die nieuwe zoektermen weet het niet wat goed of slecht is.

**Zijn drie experimenten** (zelfde account in meerdere landen, dus vergelijkbare trendlijnen):

1. Aparte AI Max-campagne náást losse searchcampagnes én een draaiende DSA ⇒ **AI Max deed niets.**
   Zolang DSA draait, weegt DSA intern zwaarder.
2. De DSA-campagne "upgraden" door AI Max aan te zetten ⇒ AI Max als matchtype kreeg **nul clicks**
   (logisch: geen keywords), URL-expansie gebeurde nauwelijks.
3. AI Max volledig aan (URL-expansie én tekstaanpassing, zonder page feed of uitsluitingen) en **DSA
   gepauzeerd** ⇒ AI Max nam het binnen een dag over. DSA was 20–30% van de searchbesteding; hij
   verwachtte een terugval en die kwam niet. Prestaties bleven gelijk. Zijn eerlijke conclusie: hij
   **kan niet verklaren waarom**, want de rapportage rond AI Max is ondoorzichtig.

**Waar ze het wél over eens zijn:** zet AI Max niet zomaar aan binnen een bestaande searchcampagne;
bouw eerst een fatsoenlijke searchstructuur (AI Max breidt uit wat er al staat); test het gescheiden
— ander land, andere staat, of een custom experiment.

**Andrews beste vuistregel — wanneer AI Max wél zin heeft:** heb je iets om *in uit te breiden*?

> Verkoop je één type marathonschoen, dan is er niets uit te breiden en gaat AI Max naar
> zoekopdrachten die niet converteren. Zijn juwelenklant verkoopt herensieraden: het keyword
> "armbanden" is een rampidee, want 98% van dat zoekvolume is vrouwelijk. Maar een klant met
> **500.000 SKU's** is gebouwd voor AI Max — daar kun je onmogelijk genoeg keywords bouwen en
> bijhouden. "Dat is wat DSA zo goed deed, en wat AI Max nog beter gaat doen."

Brent (e-commerce) is nog scherper: hij heeft er geen zinvol resultaat mee gehaald en schat dat het
**nog twee jaar** duurt. "Als je AI Max nódig hebt, is dat omdat je volledig bent uitgeput — dan geef
je meer dan een miljoen per maand uit op YouTube."

### Ads in AI overviews en AI mode

De advertentieposities veranderen. Vroeger vier bovenaan plus zes onderaan; nu vaak nog **één**.

> Zijn eigen zoekopdracht "physiotherapy in Brisbane" gaf één advertentie, daarna de kaarten, daarna
> organisch. Bij "physiotherapy near me" kwam een *sponsored* kaartvermelding boven — waarschijnlijk
> een adverteerder met PMax.

Minder plekken betekent dat je dekking nodig hebt over meerdere plaatsingstypes.

Zijn kernboodschap na Google Marketing Live 2026: **dit is niet het moment om je account om te
gooien.** Blijf draaien wat werkt en voeg pas iets toe als je metrics gaan zakken. Signalen om op te
letten: je CTR zakt verder, of je ziet bij je eigen zoekopdrachten steeds meer advertenties in AI
overviews.

Relativering die hij er zelf bij zet: **begin 2026 gaat 90–95% van de internetgebruikers nog steeds
eerst naar Google Search.** De markt loopt op twee snelheden en die spanning blijft nog jaren.
Daarom: voorbereid zijn, niet omschakelen.

### Agentic commerce (e-commerce)

**UCP — Universal Commerce Protocol**, ontwikkeld door Google en Shopify. Inmiddels hebben Amazon,
Microsoft en vrijwel iedereen zich aangesloten — **behalve OpenAI**.

Het probleem dat het oplost: de twee alternatieven waren allebei onwerkbaar. Óf AI's die letterlijk
door je website klikken en afrekenen (traag, riskant, duur), óf miljoenen losse API-koppelingen
tussen elke agent en elke webshop-backend. UCP is de tussenlaag.

Mike Ryan hekelt de term "agentic shopping" — hij noemt het liever **AI-assisted shopping**.

**Geen klif en geen muur.** De angst is dat de traditionele acquisitie te snel wegvalt of de nieuwe
te snel opkomt. Zijn inschatting: het wordt een overgang, mede omdat Google er alle belang bij heeft
adverteerders mee te nemen. Beide strategieën draaien voorlopig naast elkaar.

**De relevantiedriehoek krijgt er twee punten bij.** Klassiek was het zoekterm ↔ advertentietekst ↔
landingspagina. Nieuw: **de AI-inhoud waar je advertentie naast of ín staat** (je advertentie moet
er inheems aanvoelen, anders klikt niemand) en **de landingspaginakeuze**, die het systeem doet. En:
zoekopdrachten worden prompts, mogelijk **drie keer zo lang**.

**Je krijgt geen nette zoektermenlijsten meer terug.** Bij duizenden verschillende gesprekken past
dat niet meer in individuele zoektermen, en Google heeft privacydrempels. Wat eraan komt: **search
term insights** (clustering, al bekend van PMax), **synthetische keywords** (een lange prompt
distilleren tot iets wat op een keyword lijkt) en **Smart Bidding Exploration** om tegen meer
diverse zoekopdrachten te matchen.

**Nieuwe advertentieformaten**: conversational discovery ads, highlighted answers, en **AI-powered
shopping ads** — is een zoekopdracht specifiek genoeg, dan vervangt Google de klassieke
productcarrousel door een formaat met veel meer beschrijvende tekst, wat volledig afhangt van je
feed. Buy box-ervaringen verschijnen ook al in organische resultaten. **Dit is niet beperkt tot AI
mode.**

> **Waarom dit ertoe doet.** Twee mensen zoeken dezelfde koffiemachine. De een verhuist naar een
> kleiner appartement, dus **afmetingen** zijn allesbepalend. De ander wil weten wat de
> **maalcapaciteit en boilerdruk** zijn. Zelfde product, twee volstrekt verschillende advertenties
> nodig. Met AI Max voor shopping kan Google zelfs je **producttitel herschrijven** om bij de
> zoekopdracht te passen — je statische feedtitel kan die twee behoeftes onmogelijk allebei
> bedienen.

**Wat e-commerce merken nu moeten doen:**

- **Conversationele attributen in je feed.** Er zijn er **zes wereldwijd beschikbaar** en Google zegt
  dat er tientallen bijkomen. Voorbeelden: **vraag-en-antwoorddata** en **document-URL's** —
  handleidingen, specsheets, PDF's. Het model leest die en bepaalt daarmee of je product relevant
  is. Hier ligt het eerstkomende voordeel voor wie er vroeg bij is.
- **Opt-in voor de native checkout** vanuit je feed, plus wat werk op je website voor UCP. Let op
  geschiktheid: maatwerkproducten en leeftijdsbeperkte producten geven problemen, producten moeten
  op voorraad zijn, verzending en btw moeten kloppen. Strategische vraag: welke producten wil je
  hier juist *niet* in hebben?
- **Controleer je bot-instellingen.** Veel merken blokkeerden bots vanuit de gedachte "dat is een
  concurrent die scrapt". Nu vertegenwoordigen bots **echte klanten die willen kopen**.
- **Tag je website** zodat een agent die niet naar je feed kijkt tóch beschikbaarheid, werkelijke
  prijs, kortingen en verzendkosten begrijpt.
- Ben je marketplace-verkoper of zit je op Shopify: sluit aan bij hun feedformaten; op Shopify is het
  vaak één schakelaar. Bouw **geen eigen agent** — consumenten kiezen één agent die hen kent.

**Wat er met kortingspsychologie gebeurt.** Een agent trapt niet in ankerprijzen, drie-opties-nudges
of kunstmatig opgeblazen adviesprijzen. Hij kijkt naar data: beschikbaar, passend, binnen het
prijspunt? Dan koopt hij. Gemini-voorbeeld: een lopende opdracht, "koop dit parfum als het onder de
$50 komt" — feitelijk een limietorder. Aaron trekt de conclusie die daaruit volgt: dit versterkt
juist de waarde van een **sterk merk** dat een hogere prijs kan rechtvaardigen.

Cruciale nuance van Fred: er is **minder advertentieruimte** dan vroeger. Als de agent er niet zeker
van is dat jouw product écht beschikbaar is tegen die prijs, kiest hij een concurrent die de
implementatie wél op orde heeft — **ook als jouw product beter paste.**

### De wijziging van 17 augustus 2026 in doelgericht bieden

Tot dan presteerden campagnes met "beperkt door budget" én een tCPA/tROAS vaak *beter* dan hun doel:
Google plukte de goedkoopste conversies. Vanaf 17 augustus 2026 mikt Google **consistent op het
opgegeven doel**, ook bij beperkt budget. Gevolg: staat je tROAS op 340 en draait je account 430,
dan zakt je werkelijke ROAS richting 340.

Drie opties per campagne: terug naar maximize conversions/value, budget verhogen, of het doel
aanpassen.

Zijn beslisboom:

- **Prestatie ruim boven het doel en al lang stabiel** ⇒ haal het doel er gewoon af, en zet het later
  eventueel opnieuw.
- **Prestatie ongeveer gelijk aan het doel** ⇒ doel laten staan, wél gaan schalen met 20% per 5–7
  dagen.
- **Doel hoger dan de werkelijke prestatie** ⇒ **laddermethode** (zie het biedhoofdstuk).

Waarschuwing die hij expliciet maakt: dit is géén wenspaal. Je hebt nog steeds ~50 conversies per
maand nodig en een doel dat aansluit bij de werkelijke prestatie van de laatste 30–60 dagen.

---

## Waar hij het oneens is met Google zelf

Niet met **wat** Google zegt, maar met **wanneer** Google het aanraadt.

Google duwt PMax, smart bidding en AI Max naar bedrijven die er de data niet voor hebben — en dat
gaat in tegen Google's eigen documentatie (30 conversies per maand voor smart bidding, 50 voor
tCPA/tROAS). PMax zet je vast op smart bidding; als startpunt schendt dat dus Google's eigen regel.

Waar hij Google wél gelijk in geeft:

- **Van handmatige hendels naar strategische input.** Granulaire bied- en keywordaanpassingen zijn
  niet alleen minder effectief maar vaak schadelijk. De belangrijkste input is je conversiedata.
- **Keywords zijn signalen geworden, geen strikte triggers.**
- **Consolideer.** Omdat keywords veel breder triggeren heb je minder advertentiegroepen nodig, en
  je krijgt snellere datalussen voor smart bidding.

---

## Spanningen die je moet bewaren, niet gladstrijken

Deze staan zo in het materiaal. Doe niet alsof het één antwoord is.

| Spanning | De twee kanten |
|---|---|
| **Compact versus segmenteren** | Begin met zo min mogelijk campagnes om data te concentreren; maar segmenteer om te schalen. Opgelost door de volgorde: splits pas bij CPC-weerstand. |
| **tROAS verlagen** | Casus A: verlagen bracht méér conversiewaarde (te weinig data). Casus B en C: verlagen kostte clicks én waarde (Google ging agressiever bieden op dezelfde veilingen). |
| **CTR-benchmarks** | 6%, 8% of 10% voor search, afhankelijk van de video. Behandel als bandbreedte. |
| **PMax-kanaalverdeling** | 95% search+shopping in de ene video, 90% in de andere. |
| **Sessieduur onder 30 s** | Targetingprobleem óf boodschapprobleem aan de bovenkant van de pagina. |
| **Broad match** | Aaron: onmisbaar in 2026. Andrew Lok: breekt de relevantieketen en is een slechte ervaring. |
| **AI Max** | Aaron ziet potentie maar raadt het af; Andrew Lok is enthousiast. Brent schat twee jaar. Aaron zelf verschuift binnen enkele maanden van "nee" naar "2026 wordt het jaar". |
| **PMax als concept** | Aaron: 90%+ van zijn accounts draait erop. Andrew Lok: fel tegen. |
| **Negatieve keywords** | Vroeger agressief, nu conservatief; Andrew Lok gebruikt er helemaal geen; Mike Mancini start bij lokale dienstverleners met ~2.000 negatieven vóór de campagne draait. |
| **Formulierlengte** | Aaron: meerstapsformulier, meer velden filteren beter. Mancini: kort houden, *"je vraagt naar hun bloedgroep"*. Beiden werken met leadgen. |
| **Remarketing bij dienstverleners** | Mancini: zinloos bij spoedwerk. Aaron: waardevol bij lange aankooptrajecten. Het onderscheid zit in de urgentie van de klus, niet in de branche. |
| **Doel verlagen om te schalen** | Video 77: bij schalen is lager altijd veiliger dan je werkelijke prestatie. Casus B en C hierboven: verlagen kostte clicks én waarde. Verschil: nieuwe campagne met ruimte versus volwassen campagne op een verzadigde veiling. |
| **Zelf doen versus bureau** | Onder $10.000 per maand een bureau weggegooid geld — maar hij verkoopt coaching aan wie het zelf doet. |
| **Promotie-PMax tijdens Black Friday** | Aaron blijft voorstander, Brent is er terughoudender in geworden. |
| **Google's AI Max-belofte** | "+14% conversies" versus "+7% conversieratio" — twee verschillende claims. |

---

## De grens met /meta-ads

Beide skills gaan over betaald adverteren, maar het onderliggende mechanisme verschilt fundamenteel:

- **Google Ads vangt bestaande vraag.** Iemand zoekt iets. Je taak is aansluiten bij intentie:
  keywords, conversiedata, de match tussen zoekopdracht, advertentie en landingspagina.
- **Meta onderbreekt.** Niemand zocht je. Je taak is aandacht winnen: creatie, hoek, hook.

Praktische gevolgen die uit dit materiaal komen:

- **Creatieverslijting** is bij Meta een dagelijkse zorg; in Google alleen in Demand Gen, display en
  video — en dan met een half-life van 60–180 dagen, niet dagen.
- **Meta verslaat Google bijna altijd tijdens verkoopperiodes** (Brents observatie). Google verdient
  zijn plek in de opbouwmaanden ervoor.
- **Winnende Meta-creaties zijn het waard om in Google te testen**, maar neem niet aan dat ze werken.
  En: creaties die het op Meta níét deden kunnen in Google wél werken.
- **Meten is Google's zwakke punt** in het creatieve domein. Discounteer de Google-cijfers niet met
  "maar op Meta werkt het".

Werk je aan een creatieve of interruptiecampagne, gebruik dan /meta-ads. Werk je aan intentie,
zoekopdrachten, feeds of biedstrategieën, dan deze.

---

## Wat snel veroudert

Behandel het volgende als momentopname en controleer het:

- **Alles in het tijdgebonden hoofdstuk** — AI Max, de DSA-migratie, Google Marketing Live 2026, de
  wijziging van 17 augustus 2026, agentic commerce.
- **Benchmarkgetallen.** CTR's, conversieratio's, CPC's, de e-commerce conversieratio van 3,22%.
- **De datadrempels (30 en 50 conversies)** komen uit Google's documentatie plus zijn eigen data.
  Google kan die documentatie wijzigen.
- **Welk taalmodel het beste is.** Ze zeggen er zelf bij dat dit binnen drie maanden anders kan zijn.
- **Namen van functies en menupaden.** Google hernoemt en verplaatst voortdurend.
- **Het percentage gebruikers dat nog eerst naar Google Search gaat** (90–95% begin 2026) is precies
  het cijfer dat gaat schuiven.
- **Local Service Ads-beschikbaarheid** per land.
- **De budgetgrenzen waarboven een bureau zinvol wordt** ($10.000 / $30.000 / $50.000) — die
  verschuiven met wat je zelf met hulpmiddelen aankunt.
- **Welke scripts bestaan en wat het dashboard inmiddels zelf toont.** Google haalt functionaliteit
  in; een script dat vandaag onmisbaar is, kan volgend jaar overbodig zijn.
- **De reactiesnelheidscijfers** (341% / 400%) komen uit aangehaald onderzoek waarvan de bron en het
  jaar in het materiaal niet worden genoemd. De richting is aannemelijk, het precieze getal niet
  controleerbaar.

Wat waarschijnlijk lang meegaat: de success loop, follow the money, de kwadrantenkaart, het
onderscheid tussen platformdata en bedrijfsdata, de mechaniek van budget-op-campagneniveau, de
sessieduur-diagnose, de vier redenen voor een extra campagne, de drie stappen van de accountaudit,
de klokcurve onder biedstrategieën, en de vier onderdelen van een goede advertentietekst.

---

## Voorbehouden

- Dit is **één praktijk**, niet de industrie. Aaron Young runt een opleidings- en coachingbedrijf;
  zijn accounts zijn overwegend Australisch en Amerikaans, in leadgeneratie en e-commerce. Zijn
  advies is gevormd door wat hij in die accounts ziet.
- **Zijn eigen coaches en gasten zijn het regelmatig met hem oneens.** Die meningsverschillen staan
  hierboven bewaard omdat ze informatiever zijn dan een gladde consensus.
- **Casussen zijn zijn casussen.** De getallen zijn wat hij in zijn video's laat zien; ze zijn niet
  onafhankelijk geverifieerd en de resultaten zijn niet zonder meer overdraagbaar.
- **Dit document bevat geen commerciële verwijzingen** naar zijn programma's, kortingscodes of
  tools. Waar een tool onmisbaar was voor het principe (product labelizer, keyword planner) staat
  hij genoemd; waar het een productplug was, is alleen het onderliggende principe overgebleven.
- **Waar het materiaal dun is, staat dat er.** Er is bijvoorbeeld weinig over YouTube-campagnes als
  aparte discipline, weinig over B2B met lange verkoopcycli, en niets specifieks over de Europese
  of Nederlandstalige markt — de matchtype-, LSA- en agentic-commercepraktijk kan hier anders liggen.
- **Bedragen staan in dollars.** Reken om waar relevant.
