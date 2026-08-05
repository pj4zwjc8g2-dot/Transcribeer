---
name: seo
description: SEO-strategie en AI-zichtbaarheid volgens de werkwijze van Nathan Gotch (Gotch SEO, Rankability, auteur van AI SEO for Dummies). Gebruik deze skill bij vragen over SEO, zoekmachineoptimalisatie, ranken in Google, zichtbaarheid in ChatGPT/Perplexity/AI Overviews, AI SEO, AEO of GEO, zoekwoordenonderzoek, contentstrategie, topical authority, on-page optimalisatie, technische SEO, interne links, backlinks en autoriteit, reviews, lokale SEO, e-commerce SEO, SEO-audits, of wanneer iemand zegt "waarom rankt deze pagina niet", "we worden niet genoemd door AI", "hoe krijg ik meer organisch verkeer", of "/seo" typt.
---

# SEO en AI-zichtbaarheid

De werkwijze van Nathan Gotch — vijftien jaar SEO, honderden campagnes, oprichter van Gotch SEO
en Rankability, auteur van *AI SEO for Dummies*. Gedistilleerd uit 56 van zijn recente video's (2026).

Zelfdragend: alles staat hier, er is geen externe kennismap nodig.

## De kernstelling

Er zijn nu twee scoreborden, en ze bewegen onafhankelijk.

- **Apple** komt niet voor in de traditionele resultaten voor "best laptops" en domineert
  tegelijk vrijwel elk AI-antwoord op die vraag.
- Een merk in gezonde beef jerky staat **plek 3 in Google** en wordt door **geen enkel**
  AI-platform aanbevolen — 4 vermeldingen in 82 citaties, waarvan 3 op de eigen site.

In één zin: **SEO optimaliseert een pagina, AEO optimaliseert een entiteit.** SEO is de basislaag,
AEO staat daarbovenop. Goede SEO maakt AEO makkelijker maar vervangt het niet.

## De belangrijkste rankingfactor voor AI

HubSpot domineert de AI-antwoorden voor "beste CRM's", maar hun eigen domein komt **niet eens voor
in de citaties**. Wat wél zo is: **HubSpot wordt genoemd in 89% van de bronnen die AI citeert.**

> Als je merk consistent verschijnt in de belangrijkste zoekresultaten, is de kans groot dat je
> ook in de AI-antwoorden verschijnt. Echt geen magie.

En de vondst die de klassieke SEO-reflex onderuithaalt: **72% van die merkvermeldingen bevat geen
link.** Nofollow, gesponsord, advertentielabel — AI maakt geen onderscheid. Het gaat om de
vermelding.

Daaruit volgt de formule: **haal de vermeldingen op voor je commerciële zoekwoorden, en dat is je
prospectlijst.**

**Geciteerd worden is niet hetzelfde als aanbevolen worden.** Staat jouw URL in de bronnen, dan is
die informatie alleen gebruikt; de AI beslist zelf welk merk in het antwoord komt. Zelfvermelding
telt bovendien steeds minder mee — AI herkent steeds beter dat een merk dat zichzelf aanbeveelt
bevooroordeeld is.

### Verdiende versus eigen media, geschaald op concurrentie

| Concurrentie | Zwaartepunt |
|---|---|
| **Hoog** (CRM, SaaS, juridisch) | Vrijwel alles op verdiende media. Je site is één bron van de tien tot honderd die de AI raadpleegt. |
| **Midden** | Eigen kanalen krijgen meer invloed. |
| **Laag / lokaal** | Ongeveer gelijk. Bij lokale commerciële queries zijn de lokale bedrijven zélf vaak de geciteerde bronnen. |

Zijn stelregel: **80% van je tijd buiten je eigen website**, en voor AI eerder 90%. Begin met het
externe werk op **dag één**, niet in maand drie.

## De zeven rankingfactoren

Zijn expliciete rangorde voor traditioneel zoeken én AI-overzichten.

### 1. Indexering

Zonder index geen ranking, en traditionele zoekresultaten zijn de belangrijkste voedingsbron voor
AI-platforms.

- **Controleer met een `site:`-zoekopdracht** of de site überhaupt geïndexeerd is.
- **robots.txt**: laat crawlers toe. Let ook op `CCBot` (Common Crawl, voedt onder meer OpenAI en
  Anthropic) en `PerplexityBot`. Sitemap actueel, geen `noindex` op pagina's die moeten ranken.
- **Maximaal drie kliks diep.** Zet belangrijke commerciële pagina's in de navigatie en link van
  daaruit door. Meet met Screaming Frog: kolommen *crawl depth* en *unique inlinks*.
- **HTML, geen JavaScript.** Vibe-codingplatforms als Lovable en Replit leveren standaard
  JavaScript, en AI-platforms verwerken dat slecht tot niet. ChatGPT slaat je site dan over ten
  gunste van een site die makkelijker te lezen is. WordPress en de meeste CMS'en zijn standaard goed.
- **Laadtijd onder 3 seconden.** Crawlers hebben geen geduld; boven die grens kunnen LLM's je
  overslaan.

### 2. Zoekintentie matchen

Verplaats je in de zoeker. Bij een kopterm als "SEO" is de intentie niet te raden — dat maakt het
een slecht doelwit. Meer context maakt het scherper: "beste SEO-tools voor bureaus" heeft een
duidelijke intentie en laat zich vertalen naar één relevante pagina.

Bij twijfel: google de term en kijk welk format er domineert. Zijn het lijstjes, maak dan een lijstje.

### 3. Contentrelevantie

Informatiewinst telt — Google en LLM's belonen pagina's die iets toevoegen. Maar **te uniek zijn
werkt averechts.** Begin met relevantie, denk daarna pas aan differentiatie.

- Dek zoveel mogelijk dezelfde onderwerpen af als de concurrenten die ranken.
- **Aantal woorden = de mediaan van de concurrenten**, als richtpunt voor de schrijver. Het is geen
  rankingfactor.
- Zet het hoofdzoekwoord in: **URL, titel, meta-omschrijving, H1, de eerste zin**, een variant in de
  **eerste H2**, en nog één keer in de **conclusie**.
- Richt op dekking, niet op zoekwoorden strooien.

### 4. Topical authority

Geen losse acties. Elke stuk content hoort in een cluster.

Pijlerpagina → ondersteunende pagina's. Een beproefd patroon voor commerciële clusters:
*"[concurrent] alternatieven"* → *"[concurrent A] versus [concurrent B]"* → *"[concurrent] versus ons"*.
Herhaal dat voor je **vijf tot tien belangrijkste concurrenten**.

Meer ondersteuning geeft ook meer interne links, en dat betekent: **krijgt één pagina in de cluster
een backlink, dan profiteert de hele cluster.**

### 5. Backlinkkwaliteit

Eén link van een vertrouwde partij is meer waard dan honderd middelmatige. Drie tests:

1. **Autoriteit** — heeft die site zelf een goed backlinkprofiel? Een link van Forbes is het waard,
   ook als hij nofollow is.
2. **Is het een AI-bron?** Heeft die site zelf AI-citaties? Zo ja, dan wordt hij gebruikt bij
   retrieval — en een vermelding daar vergroot je kans om in AI-antwoorden te komen. Dit is de test
   die de meeste mensen missen.
3. **Relevantie** — lokaal kan dat een softbalcompetitie in je stad zijn; landelijk zijn het blogs
   en nieuwssites in je niche.

Alle drie is ideaal. Relevantie mag ontbreken als de site extreem betrouwbaar is (Wikipedia is voor
vrijwel niemand 100% relevant, maar een vermelding is enorm waardevol).

### 6. Domeinsterkte

Eén goede link is mooi, maar je hebt **consistente groei op lange termijn** nodig. Vergelijk je DR
of autoriteitsscore én je aantal verwijzende domeinen met je drie belangrijkste concurrenten. Dat
verschil is je doel.

### 7. Merksignalen

Verzamel **recensies op de platforms die er in jouw niche toe doen.**

- **Lokaal: 90% van je tijd op het Google Bedrijfsprofiel**, plus twee tot drie nicheplatforms
  (thuisdiensten: Angi, Thumbtack; juridisch: Avvo, Super Lawyers).
- **Diversiteit is cruciaal, want ChatGPT gebruikt Google Bedrijfsprofielen niet voor retrieval.**
  Het put uit gezaghebbende directories zoals Yelp. Rank je perfect in het lokale pakket en sta je
  nergens in de directories, dan blijf je onzichtbaar in AI.
- **Hoe vind je de jouwe?** Draai een commerciële query ("beste letselschadeadvocaten in [stad]"),
  klik door naar de citaties en kijk welke platforms daar worden gebruikt. Dat zijn je doelen.

## De audit

Zijn volledige auditproces. Opzet: een Google Sheet met een tabblad per onderdeel, en een
**Screaming Frog**-crawl als basis (die beveelt hij expliciet aan zonder commissie). Koppel in
Screaming Frog de API's van **GA4, Search Console en PageSpeed Insights** — dan heb je gedrag,
vertoningen en snelheid naast elke URL staan. Zet bij de configuratie *near duplicates* aan.

### Technisch

- **Crawldiepte** — markeer alles dat meer dan **drie kliks** diep zit.
- **Unieke interne links** — markeer pagina's met minder dan een handvol inkomende interne links.
  Weinig interne links is meestal een symptoom: óf je hebt het linkwerk nooit gedaan, óf er is te
  weinig omliggende content om vanaf te linken.
- **Laadsnelheid** — markeer een performancescore onder de 80; daarboven treedt de wet van de
  afnemende meeropbrengst in. Verbeter je één pagina, dan tilt dat meestal de hele site.
- **404's** — niet elke 404 is fout. Bewust verwijderde pagina's zijn prima. **De kwaadaardige
  404's zijn die mét positieve KPI's**: verkeer, vertoningen, kliks, betrokkenheid. Sorteer daarop
  en redirect die.

### Inhoudelijk

- **Dunne content** — onder de 500 woorden markeren, maar dat is een signaal om te onderzoeken,
  geen opdracht om te schrappen. Dun is trouwens niet alleen woordental: een lange pagina die niets
  toevoegt is ook dun.
- **Dubbele content** — kijk naar bijna-duplicaten. Onder de 30% overlap is geen zorg.
- **Irrelevante content** — filter de titels die je kernonderwerp **niet** bevatten. Pagina's buiten
  je expertisegebied verwateren je autoriteit. Wees meedogenloos, maar kijk eerst of ze KPI's hebben
  die je wilt behouden.
- **Zwakke clusters** — een cluster is een groep pagina's rond één onderwerp. Presteert een onderwerp
  slecht, kijk dan naar de ondersteuning eromheen in plaats van naar de pagina zelf. Twintig pagina's
  is redelijk; zijn sterkste pijler krijgt uiteindelijk 75 tot 100 ondersteunende stukken.
- **Wegwerkcriterium** — geen verkeer, geen vertoningen, geen backlinks: die pagina hoort er niet te
  zijn. Weg ermee, tenzij hij nieuw is. Een compacte site verspilt geen crawlbudget.

### Kansen

- **Laaghangend fruit (positie 2-15)** — filter in Search Console op cluster, sorteer op positie.
  **Check eerst in incognito**: sta je er al eerste, dan is heroptimaliseren zonde. Doe daarna drie
  dingen tegelijk: heroptimaliseren op relevantie, interne links toevoegen, laadsnelheid verbeteren.
  Die drie samen leveren bijna gegarandeerd verbetering. Helpt dat niet, dan pas backlinks.
- **Clustermogelijkheden (positie 50+)** — hier zit een subtiel maar belangrijk punt: **een
  gloednieuwe pagina die op 50-100 staat is normaal, negeer die.** Het gaat om gevestigde pagina's
  die niet presteren. Die vertoningen zijn **bewijs van vraag**: staat er een query met vertoningen
  waar je geen eigen pagina voor hebt, dan is dat het bewijs dat die pagina er moet komen.
- **Contentveroudering** — content die ooit goed geoptimaliseerd was verliest terrein doordat er
  nieuwe concurrenten bijkomen en de onderwerpenset verschuift. Herzie binnen een jaar. Een
  herwerking levert typisch twee tot vier posities op.
- **Concurrentframeworks** — kijk in Ahrefs of Semrush welke pagina's van je concurrent de meeste
  links trekken. Meestal zie je een patroon (vaak statistiekpagina's). Dat framework herhaal je.
  Je kunt een framework ook **uit een andere branche overplanten** waar jouw concurrenten het nog
  nooit gezien hebben.

### Zoekwoordkannibalisatie: het misverstand

Hier wordt volgens hem enorm overdreven. Kannibalisatie is **niet** twee pagina's met hetzelfde
zaadwoord — het is twee pagina's met hetzelfde zaadwoord **én dezelfde intentie**.

Een commerciële productpagina ("beste tool voor X", enkelvoud, een verkooppagina) en een kopersgids
("beste tools voor X", meervoud, onderzoekend) concurreren niet. **Ze tillen elkaar juist op.**
Dat is precies wat je wilt bouwen.

Problematisch wordt het pas bij twee pagina's met dezelfde intentie én dezelfde modifier — twee keer
"SEO-training in Baltimore". Vuistregel: **een nieuwe pagina mag, zolang hij een ander doel heeft.**

## Zoekwoordenonderzoek

### Het sjabloon

Per zoekwoord leg je vast: **prioriteit, bron, cluster, zoekwoord, SERP-functies, zoekvolume, KD,
CPC, huidige positie, huidige URL, intentie, kanscategorie.**

Drie kolommen worden vaak verkeerd begrepen:

- **CPC is geen SEO-metriek maar een waardemeter.** Betalen veel adverteerders voor een term, dan is
  die term waarschijnlijk waardevol. Filter op hogere CPC.
- **KD meet alleen hoeveel links je op paginaniveau nodig hebt.** Dat is de helft van het verhaal;
  je moet ook de **domeinsterkte van de concurrenten** meewegen. Pas die twee samen vertellen je hoe
  competitief een SERP is.
- **SERP-functies bepalen je verwachte CTR** — zie hieronder.

**Intentie** houd je bewust grof: informatief of commercieel. Dat onderscheid alleen brengt je al ver.

### Kanscategorieën op basis van je huidige positie

| Positie | Categorie | Wat het betekent |
|---|---|---|
| **2-15** | Laaghangend fruit | Hier zit je snelste winst. |
| **16-50** | Bestaand zoekwoord | Belangrijk, maar gewoon onderhoud. |
| **> 50** | Clusteringmogelijkheid | Vaak een **intentiemismatch**: de pagina is niet de juiste pagina voor die query. Kandidaat voor een eigen pagina. |

Bij die laatste groep: onderzoek waaróm hij niet presteert. Ontbrekende interne links, te dunne
onderwerpdekking, te weinig backlinks — maar het is vaak intentie.

Er zijn twee sporen: zoekwoorden waar je al voor in de top 100 staat, en volledig nieuwe zoekwoorden.

### Waar je zoekwoorden vindt

1. **Google Ads Keyword Planner** — volume en trends, gratis. Let op: de kolom *concurrentie* gaat
   over advertenties, **niet** over SEO. Verwar die niet.
2. **Google Search Console** — kliks, impressies, CTR, positie. Echte queries van je eigen site, maar
   geen concurrentiedata.
3. **Google zelf** — autosuggesties, "andere vragen", gerelateerde zoekopdrachten. Blijf doorklikken
   en label waar je ze vandaan hebt.
4. **Reddit** — onderwerpen waar mensen nú over praten. Meestal weinig tot geen volume, en juist
   daarom een voorsprong.
5. **YouTube** — suggesties, en de kanalen van concurrenten. **Sorteer op recent, niet op populair**:
   een video van vijf jaar geleden met veel views herhaalt zich niet, want dat onderwerp is inmiddels
   verzadigd.

### Zoekwoorden met nul volume zijn geen slechte zoekwoorden

Dit is een van zijn scherpste punten. De meeste queries zijn onbekend bij SEO-tools; zelfs Google
kent de overgrote meerderheid niet. En query's worden **langer en gespreksachtiger** door AI, dus dat
probleem groeit.

Kijk daarom naar de **groei jaar op jaar** in plaats van naar absoluut volume. Zijn voorbeeld: "AEO
services" had nauwelijks volume — en géén enkele concurrent die erop richtte. Publiceren, ranken,
voorsprong opbouwen, en tegen de tijd dat de term groeit sta je er al.

### SERP-analyse per zoekwoord

Open het zoekwoord in een incognitovenster en kijk **wat er verschijnt**, niet alleen naar de tien
blauwe links:

- **Welke SERP-functies staan er?** Een lokaal pakket betekent dat je twee posities wilt: het
  organische resultaat én je Google Bedrijfsprofiel.
- **Welke directories staan erin?** Yelp, Clutch en vergelijkbare platforms. Sta je daar niet in, dan
  is dat werk — en het is cruciaal voor AI, want die platforms worden gebruikt bij retrieval.
- **Wat staat er op YouTube voor deze term?** Zijn dat verouderde video's, dan ligt dat kanaal open.

### Prioriteer op verwachte klikken, niet op positie

Een derde plaats betekent niet meer wat het was. Klapt het AI-overzicht open, dan zakt resultaat drie
volledig onder de vouw. Bij "best laptops" duwen vier advertenties plus een AI-overzicht alles weg.

- Plek één haalt ruwweg **30% CTR** op de klassieke blauwe links.
- Buiten de top drie is een klik onwaarschijnlijk.
- **AI-overzichten schaden je CTR veel meer dan een forumblok**, want ze beantwoorden de vraag in
  plaats van tot doorzoeken aan te zetten.

**De SERP-functies zijn je concurrenten om de klik.**

Zijn verwachting: de blauwe links verdwijnen niet, maar worden vooral een bibliotheek die de
AI-platforms voedt. Reden te meer om er te staan — je wilt een van de bronnen zijn.

## Categoriefocus

**Eén categorie, 90 tot 180 dagen, volledig afdekken.** Dit is zijn hardste regel en zijn
verklaring voor waarom bedrijven verliezen: ze gaan overal een centimeter de diepte in.

- **E-commerce**: niet de hele webshop, maar één categorie. Scope ook je technische audit daarop.
- **Lokaal**: 25 tot 30 onderwerpen rond één stad voordat je verder gaat — en dan naar een
  **aangrenzende** stad, zodat je relevantie doorbouwt.

Sjabloonpagina's per stad werken niet: in zijn voorbeeld 41 pagina's met 83% overlap. Snoeien,
samenvoegen, redirecten — niet eerst optimaliseren.

## Content

### Eén pagina, één intentie — en conversie eerst

Eén pagina die drie doelgroepen bedient is drie intenties en drie koopmotieven. Zelfs als hij rankt,
converteert hij niet.

> Begin altijd met conversie. SEO komt daarna.

Fundamenteel verkeerd opgezet? Opnieuw bouwen, niet optimaliseren.

**Nieuwe pagina of bestaande?** Als de **intentie** anders is, een nieuwe. "Dakdekker in X" is breed;
"dakreparatie", "dakinspectie" en "stormschade" zijn aparte intenties.

### Structuur modelleren met swipe files

Niet kopiëren — **modelleren**. Kies vijf tot tien zoekwoorden, pak per zoekwoord de twee tot drie
best presterende pagina's, en zoek vooral URL's die **zowel ranken als geciteerd worden**. Destilleer
daar een herbruikbaar sjabloon per contenttype uit.

Een structuur die zich honderden keren bewees gooi je niet overboord voor iets onbewezens. Je unieke
bijdrage zit in inhoud en expertise, niet in de opbouw.

Beproefde opbouw lokale servicepagina: diensten, vertrouwensbalk, waarom voor dit bedrijf kiezen,
resultaten en sociaal bewijs, getuigenissen, hoe het werkt, werkgebied, veelgestelde vragen.

### De "paarse koe": 10% beter

Analyseer je vijf belangrijkste concurrenten en zoek de invalshoek die je pagina meetbaar beter maakt.
Niet radicaal anders — soms een betere gebruikerservaring, soms meer data, soms echte ervaring.

## Het merkverhaal beheersen

AI leert alleen wat het aangeboden krijgt. Beantwoord jij een merkvraag niet, dan zoekt de AI door tot
hij ergens iets vindt — en dat klopt lang niet altijd.

- **Bouw een "super-FAQ"** die álle merkvragen beantwoordt ("Heeft [merk] een API?", "Wat kost [merk]?").
  Uit onderzoek van duizenden merkqueries blijkt dat AI die informatie rechtstreeks bij de bron ophaalt.
- **Ruim je entiteit op**: naam, adres, telefoonnummer, merkomschrijvingen consistent in álle profielen
  en directories. Inconsistente bronnen leveren onjuiste AI-antwoorden op.

## Uitbreiden naar andere kanalen

Bepaal eerst welke van je eigen kanalen **indexeerbaar** zijn: plak de profiel-URL in Google en kijk of
recente berichten verschijnen. Zo ja, dan staat het kanaal op je lijst.

**YouTube is vrijwel altijd de beste volgende stap**: op één na grootste zoekmachine, video's ranken in
Google, en het is het op één na meest geciteerde sociale kanaal in AI-zoekopdrachten.

- **Lange video's worden wél als bron gebruikt** — de AI leest het transcript.
- **Shorts vrijwel niet**: te weinig context om uit te putten. Voor **SERP-dominantie** in klassiek
  zoeken zijn Shorts wél sterk. Verwar die twee doelen niet.
- **Lees je artikel niet voor** — zet het om naar een script met een eigen invalshoek.

**Bouw een funnel**: publiceer eerst je **conversievideo**, en laat alle latere video's daarnaar
verwijzen.

### Onderwerpdominantie in de praktijk

Begin bij een zoekwoord waar je **al goed op scoort** — daar is bewezen dat je mee kunt. Dan:

1. Verbeter eerst de pagina die er staat, als die niet bovenaan staat.
2. Kijk of je datzelfde onderwerp op **YouTube** hebt behandeld. Zo niet, dan ligt daar een open kans.
3. Kijk wat er **verder op pagina één staat**. Dat zijn geen obstakels maar kansen:
   - **Reddit-threads** — vaak gearchiveerd en dus onbruikbaar, maar noteer welke subreddit steeds
     terugkomt en zet een melding voor toekomstige threads over dat onderwerp.
   - **Lijstjes op branchesites** — kijk of jouw product of dienst erin staat. Zo niet, dan is dat
     je pitch.

Zo pak je zoveel mogelijk posities op één zoekresultatenpagina.

### Wat weet AI eigenlijk van je merk?

Een gratis nulmeting: vraag een AI-platform wat het over je merk weet **zonder webzoekopdracht** —
dan kijk je puur naar de trainingsdata in plaats van naar wat het ter plekke opzoekt. Bij een minder
bekend merk moet je wat context meegeven. Het antwoord is geen exacte wetenschap en kan hallucinatie
bevatten, maar het laat wel zien of het model überhaupt iets van je weet.

## Dagelijkse praktijk

**1. Optimaliseer één bestaand item.** Zoek in Search Console de zoekwoorden op **positie 2 tot 15**.
Controleer zoekwoord in titel, meta, H1 en eerste zin. **Wijzig de URL niet** als de pagina daar al
staat — te riskant. Vul daarna de onderwerpgaten aan en verbeter de interne links. Kun je nauwelijks
pagina's vinden die zouden moeten linken, dan heb je meer ondersteunende content nodig.

**2. Publiceer één nieuw item.** Neem een pagina die goed presteert en zoek de queries waarop diezelfde
pagina **slecht** scoort (onder positie 50). Die passen vaak niet bij de intentie van de pagina. Bouw
daar een eigen pagina voor: je ondersteunt het origineel én pakt bereik met een exacte intentiematch.

**3. Doe extern werk.** Vijf tot tien outreach-mails per dag, of vijf tot tien merkvermeldingen opschonen.

## Snel scoren op opkomende zoekwoorden

Een nieuw onderwerp in je branche heeft nauwelijks concurrentie. Zijn voorbeeld: HubSpot lanceerde een
AEO-tool, hij bouwde direct *"[product] alternatieven"* en *"[eigen product] versus [product]"* en stond
binnen zes uur op nummer één, inclusief vermelding in de AI-overzichten.

Houd lanceringen en trends in je niche in de gaten en bouw meteen de vergelijkingspagina's. De
zichtbaarheid groeit daarna door van Google naar ChatGPT en Perplexity over drie tot zes maanden; Grok
loopt achter.

## Lokale SEO

- **Google Bedrijfsprofiel eerst.** De vestigingsplaats moet kloppen met je werkelijke adres. Een bedrijf
  in Ballwin met een profiel geoptimaliseerd op Chesterfield: alleen dat corrigeren kan vijf tot zeven
  posities schelen.
- **Recensies structureel binnenhalen**, en op meerdere platforms — zie rankingfactor 7.
- **Directories**: profiel aanmaken, recensies verzamelen, plaatsentiteit expliciet noemen.
- **Lokale sponsoring**: klein budget, behandel het als advertentiekosten. Je koopt zichtbaarheid bij
  entiteiten die ter plaatse al vertrouwd zijn.

## Linkbait en linkbuilding

Wat vanzelf links en vermeldingen aantrekt is materiaal op basis van **onderzoek en data**. Laat een AI
ideeën genereren die **specifiek zijn voor jouw categorie** — "geef me linkbait-ideeën" levert niets op.
Kies er één, laat er diepgaand onderzoek op los, en zet dat om in een vormgegeven stuk. Het onderzoek is
grondstof, geen publicatie.

Blijf daarnaast **klassieke linkbuilding doen** voor domeinautoriteit. In honderden audits van slecht
presterende sites lag de oorzaak vrijwel altijd eerst buiten de site: geen backlinks, slechte backlinks,
of een zwak ankerprofiel.

## AI als werkwijze

Zijn kennisbasis ("SEO-superintelligentie"):

- **Merkintelligentie** — producten, aanbod, veelgestelde vragen, beleid, sociaal bewijs, merkstem, en
  expliciet de **aliassen** van het merk.
- **Een entity record** als **bron van waarheid**. Loop het regel voor regel na met menselijk inzicht.
- **Data** — Search Console (16 maanden), Analytics, Bing Webmaster Tools, gedragsdata, positie- en
  citatietracking. Label elke import met een datum. Een GSC-export geeft maar circa 1.000 queries; via
  de API haal je er tot 50.000 op.
- **Ervaring en expertise** — interview één tot drie experts, transcribeer, en **gooi het ruwe transcript
  er niet in**. Comprimeer tot een gestructureerd artefact; twee uur interview wordt ongeveer 2.900
  woorden. Streef naar **tien artefacten**.
- **Een uitvoeringslogboek** — leg elke actie vast, zodat je later kunt nagaan waarom iets werkte.

Twee praktische regels:

- **Sla artefacten lokaal op als markdown**, niet opgesloten bij één aanbieder.
- **Gebruik niet je zwaarste model voor deterministische klusjes.** Een transcript comprimeren vraagt geen
  redeneerwerk; daar verbrand je alleen tokens.

### Wat AI wel en niet kan

> AI kan geen strategie ontwikkelen zoals ik je laat zien. Het lukt gewoon niet. En geloof me, ik heb het
> geprobeerd.

Goed in onderzoek, data-analyse en eerste versies. Slecht in strategie, en zonder echte data geeft het
algemene aanbevelingen zonder onderbouwing.

> De magie zit in het redigeren.

Behandel content als een product: reken op twee tot vier revisies voor zowel tekst als ontwerp.

## Meten

- **Momentopname, geen dagelijkse tracking.** Dagelijks posities volgen heeft geen zin als je die week
  niet aan die categorie werkt. Een benchmarkrapport, een logboek van wat je publiceert, en periodiek een
  nieuwe scan.
- **Grijp niet meteen in** als je iets kapots ziet — zeker bij klantwerk. Leg eerst de nulmeting vast,
  anders kun je later niet aantonen wat je hebt opgeleverd.
- **Wees sceptisch over AI-rank-trackers.** Hij bestudeerde er meer dan dertig, gemiddeld $337 per maand,
  en ziet claims die niet kloppen. Meten is nodig, maar controleer wat een tool werkelijk meet.
- **Citaties zijn niet-deterministisch** — dezelfde vraag geeft een andere set. Maar het is geen
  draaideur: over maanden blijven doorgaans **vijf tot zeven bronnen structureel in de top staan**.

## Werkwijze

1. **Meet eerst per oppervlak** — traditioneel, AI-antwoorden, AI-citaties, video, sociaal — en leg de
   nulmeting vast vóór je iets verandert.
2. **Bepaal welk probleem speelt**: ranken we niet (klassiek), of ranken we wel maar wordt het merk niet
   genoemd (citatie- en autoriteitsprobleem)? Dat vraagt totaal verschillend werk.
3. **Loop de zeven rankingfactoren af** als iets niet rankt. Begin bij indexering — dat is de goedkoopste
   en meest overgeslagen oorzaak.
4. **Doe de citatie-analyse** voor je aan content begint. Daar komt de werklijst uit.
5. **Dwing focus af.** Eén categorie, 90 dagen.
6. **Weeg de klikwaarde**, niet alleen de positie.
7. **Controleer intentie en conversie** voor je aan optimalisatie begint.
8. **Wees concreet met aantallen**: 100+ onderwerpen per zaad, 25-30 per stad, 5-10 zoekwoorden voor je
   swipe file, 5-10 concurrenten voor je vergelijkingscluster, 10 kennisartefacten, 9 ondersteunende
   stukken per hoofdonderwerp, 5-10 outreach-mails per dag, 2-4 revisies.

## Let op

- **Zijn invalshoek is uitgesproken AI-eerst.** Dat is een standpunt, geen consensus. Benoem dat het zijn
  aanpak is als het afwijkt van wat de gebruiker elders leest.
- **Hij promoot zwaar zijn eigen software.** Die plugs zijn hier weggelaten; de methodes staan er
  tool-onafhankelijk in, wat kan omdat hij zelf steeds de handmatige route erbij geeft. Screaming Frog
  beveelt hij expliciet zonder commissie aan.
- **Platformdetails verouderen snel** — welke bots wat crawlen, hoe AI-overzichten eruitzien, welke
  directories worden geciteerd. Controleer dat voor je het als vaststaand presenteert.
