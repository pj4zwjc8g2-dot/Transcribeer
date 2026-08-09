---
name: lokale-seo
description: Lokale SEO en Google Bedrijfsprofiel volgens de werkwijze van Sterling Sky (Joy Hawkins). Gebruik deze skill bij vragen over Google Bedrijfsprofiel, Google Business Profile of GBP, het lokale pakket of de kaartresultaten, Google Maps-rankings, verificatie en bulkverificatie, eigendom en beheerders van een profiel, geschorste, uitgeschakelde of gefilterde vermeldingen, recensies die verdwijnen of niet gepubliceerd worden, recensieblokkades, het lokale filter of possum-filter, servicegebiedbedrijven, categorieën, openingstijden, lokale citaties, "near me"-zoekopdrachten, meerdere vestigingen, AI-lokale pakketten, of wanneer iemand zegt "mijn rankings op Maps zijn ineens weg", "mijn recensies verschijnen niet", "mijn profiel is geschorst", "iemand heeft mijn pin verplaatst", of "/lokale-seo" typt.
---

# Lokale SEO en Google Bedrijfsprofiel

De werkwijze van **Sterling Sky** — het bureau van Joy Hawkins, gespecialiseerd in lokale SEO, dat
zijn advies op eigen tests en klantcases baseert. Gedistilleerd uit 34 recente video's (2024–2026)
van een corpus van 98, inclusief gesprekken met twee ex-Googlers die elk ruim elf jaar aan Google
Bedrijfsprofiel werkten (Brad Weatherall, Joel Headley) en met recensie-specialist Claudia Tomina.

Zelfdragend: alles staat hier, er is geen externe kennismap nodig.

**Verhouding tot `/seo`:** die skill is strategisch en AI-eerst (Nathan Gotch). Deze is operationeel
en testgedreven. Ze spreken elkaar op één punt hard tegen — zie [Waar deze skill botst met
`/seo`](#waar-deze-skill-botst-met-seo). Strijk dat niet glad.

---

## Kernstelling: lokaal en organisch zijn verschillende spellen

Het lokale pakket draait op een **eigen algoritme**. Dat is het fundament onder bijna alles hier:

- **Core updates raken de kaartresultaten meestal niet.** Lokaal heeft eigen updates: openness,
  vicinity, possum, diversity.
- **Algoritmische strafmaatregelen op links werken alleen organisch door.** Sterling Sky zag sites
  die ruim **90% van hun organische verkeer** verloren terwijl hun lokale-pakketposities volledig
  intact bleven — bij één site schoten die zelfs omhoog.
- **Links doen bijna alles voor organisch en bijna niets voor lokaal.** Zie [Links](#links).
- **Citaties doen vrijwel niets voor het lokale pakket.** Zie [Citaties](#citaties).

En sinds 2024 is er een koppeling bijgekomen die de verkeerde kant op werkt: **staan in het lokale
pakket kan je organische positie omlaag duwen** (de diversity update). Zie
[Diagnose 5](#diagnose-5-organisch-zakt-terwijl-het-lokale-pakket-goed-staat).

Diagnose begint dus altijd met: **welk scorebord is stuk?** Een probleem in het ene zegt weinig over
het andere, en een maatregel die het ene helpt kan het andere schaden.

---

## Diagnose 1: de rankings op Maps zijn ineens weg

Loop deze oorzaken na vóór je iets optimaliseert. Meestal is het er één van.

### 1. Een servicegebiedbedrijf dat verhuisd is

Bij verificatie slaat Google het adres **verborgen op in het systeem**, ook als het niet zichtbaar is
op de vermelding. De vermelding blijft ranken op die oude locatie. Verhuis je en pas je alleen het
adres aan, dan blijft Google je feitelijk op het oude adres behandelen en rank je nooit in het nieuwe
gebied. Het adres wijzigen kan bovendien een schorsing uitlokken.

**Juiste volgorde:** nieuwe vermelding op het nieuwe adres aanmaken en verifiëren → daarna Google
support vragen de oude te sluiten en de recensies over te zetten.

### 2. Een lokale algoritme-update

- **Openness update** — Google weegt realtime mee of je open bent. Verklaart het patroon van 1 → 10 →
  1 binnen een dag.
- **Vicinity update** — nabijheid werd veel zwaarder. Vóór deze update konden bedrijven met veel
  zoekwoorden in hun naam een groot gebied domineren; daarna werden de resultaten veel lokaler.
- **Possum** — het lokale filter (zie [diagnose 2](#diagnose-2-het-lokale-filter-possum)).
- **Diversity update** — raakt vooral je organische posities (zie
  [diagnose 5](#diagnose-5-organisch-zakt-terwijl-het-lokale-pakket-goed-staat)).

### 3. Google of iemand anders heeft iets op je profiel gewijzigd

Naam, categorie of diensten. Zelfs kleine wijzigingen kunnen je rankings onderuithalen. Edits komen
uit vier bronnen:

1. **Je eigen website en sociale profielen.** Google crawlt je site en kan je profiel overschrijven —
   conflicteren je openingstijden op de site met die op je profiel, dan kan Google de laatste
   aanpassen.
2. **Externe apps** waaraan je koppelingsrechten hebt gegeven. Diensten als Yext en Semrush kunnen
   foute data doorduwen. Eén klant kreeg zijn telefoonnummer overschreven met een trackingnummer dat
   niet van hem was; de app verwijderen loste het direct op.
3. **Andere eigenaren en beheerders** van de vermelding.
4. **Voorstellen van gebruikers.** Gebruikers met een hoge vertrouwensscore kunnen wijzigingen
   voorstellen die Google automatisch goedkeurt.

De klassieke case: een klimaatbedrijf zag zijn primaire categorie wijzigen van
*airconditioningreparatieservice* naar *airconditioninginstallateur* en zakte **van 1 naar 31**.
Snel gesignaleerd en teruggezet stond het binnen twee weken weer op één.

**Controleer periodiek drie dingen:** wie heeft toegang tot je profiel, welke externe apps zijn
geautoriseerd, en komen je openingstijden op het profiel overeen met die op je site.

### 4. De landingspagina van je profiel is gewijzigd

De URL die aan je vermelding hangt weegt zwaar. Wordt die van je *busongevallen*-pagina naar je
homepage gezet, dan stort je relevantie voor busongeval-termen in.

### 5. Je kaartpin ligt buiten de gemeentegrens

**Google rankt op de plaatsing van de pin, niet op je postadres.** Ligt de pin net buiten de grens
die Google voor die plaats hanteert, dan word je aan een andere plaats toegewezen: je scoort dan op
díe plaatsnaam en nauwelijks op je eigen.

### 6. Iemand heeft je pin verplaatst — en de logische reactie is een valstrik

⚠️ **Dit is de gevaarlijkste fout in deze hele skill.**

Sterling Sky zag een klant wiens pin uren rijden van zijn locatie werd verplaatst. Soms is het een
concurrent die het opzettelijk doet — ze zagen pins die naar een woestijn werden gezet, wat weinig
ruimte laat voor goede bedoelingen — soms iemand die je locatie oprecht denkt te corrigeren.

**Herstel het niet in je eigen dashboard.** Dat is precies wat iedereen doet, en ze zagen er een
enorm aantal schorsingen door ontstaan — meestal harde schorsingen, waarbij je volledig van de kaart
verdwijnt. Zo wordt een kwaadaardige actie van een concurrent jouw schorsing.

**Wel doen:** laat iemand **met een ander Google-account**, dat geen toegang heeft tot je profiel,
via Google Maps een wijziging voorstellen om de pin te corrigeren. Dat triggert geen schorsing.
Lukt dat na een paar pogingen niet, vraag dan Google support het aan de achterkant te doen — leg uit
dat je geen schorsing wilt riskeren, en stuur een schermafbeelding van waar de pin hoort. Helpt dat
ook niet, dan het Google Bedrijfsprofiel-forum.

### Plus: de Kansas-bug

Soms is er niets veranderd — geen edits, geen verhuizing, geen update — en raakt Google de
locatiedata van je vermelding kwijt. Het bedrijf rankt dan in Kansas in plaats van in de eigen
staat, vandaar de naam. Je kunt weken auditen zonder iets te vinden, omdat het probleem niet aan jouw
kant zit.

---

## Diagnose 2: het lokale filter (possum)

Google **verwijdert** je vermelding niet, het **filtert** hem. Het doel is te voorkomen dat
vergelijkbare vermeldingen samen in de resultaten verschijnen. Het kijkt naar overeenkomst in naam,
websiteadres en telefoonnummer — en vooral naar **hoe dicht je bij je concurrent zit**.

Filtering treedt vaak op binnen **200 voet (ongeveer 60 meter)** van een andere vermelding die op
dezelfde zoekwoorden concurreert.

**Het filter werkt op zoekwoordniveau.** Je kunt prima ranken op de ene term en volledig gefilterd
zijn op de andere. Zelfde vermelding, zelfde locatie, totaal andere uitkomst.

### Vaststellen dat je gefilterd wordt

Kijk naar **patronen**, niet naar posities.

| Signaal | Zekerheid |
|---|---|
| BrightLocal toont een doorhaling (geen enkele ranking) | Aanwijzing, geen bewijs |
| Places Scout: groen raster over de hele markt, maar **rood precies op je eigen pin** | ~90% zeker |
| Local Falcon trendanalyse: je posities **wisselen** steeds met één andere vermelding | Sterke aanwijzing |
| Je posities naast die van een specifieke concurrent plotten en een **omgekeerd verband** zien | 100%; dit wijst de dader aan |

### Het filter werkt als een gewicht, niet als een schakelaar

Dit corrigeert een wijdverbreid misverstand. Mensen denken dat het filter één vermelding wegstopt.
Sterling Sky's orthodontist-case laat iets anders zien: een extra vermelding werkt als een **gewicht
dat je hoofdvermelding omlaag trekt**.

De praktijkvermelding stond op 6, de behandelaarsvermelding op 10 — ze concurreerden met elkaar en
sleepten elkaar naar beneden. Toen ze de behandelaarsvermelding verwijderden, sprong de praktijk
omhoog en schoot het verkeer omhoog.

Dit speelt bij **behandelaarsvermeldingen** (arts, tandarts, advocaat, makelaar),
**afdelingsvermeldingen**, en bij bedrijven die tegen de richtlijnen in extra vermeldingen aanmaken
in de veronderstelling dat meer beter is.

> Levert een extra vermelding je geen leads of verkeer op, dan is de kans groot dat hij je schaadt.
> Weg ermee.

### Oplossingen, in volgorde van ingrijpendheid

1. **Duplicaat of nutteloze extra vermelding verwijderen.** Bij een tapijtreiniger filterde een
   duplicaat mét slechtere recensies de goede weg; laten verwijderen en de goede nam de plek over.
2. **Kaartpin verplaatsen** buiten de straal van 200 voet. Omstreden, maar bij één klant stegen de
   telefoontjes vanuit het bedrijfsprofiel met **400%**.
3. **Rebranden**, zodat het zoekwoord waarop je gefilterd wordt in je bedrijfsnaam komt (zie
   [Bedrijfsnaam](#bedrijfsnaam-de-legale-route)).
4. **Fysiek verhuizen** binnen dezelfde stad. Een strafrechtkantoor herwon zo al zijn posities.
5. **Wachten.** Bij een letselschadekantoor met een tweede vestiging duurde het ongeveer **acht
   maanden** voor de nieuwe locatie genoeg autoriteit had.

**Wat níét werkte in hun test:** de vermelding "gevestigd binnen een ander bedrijf" weghalen. Deed
niets.

**Let op bij een tweede vestiging.** Een advocaat in Houston opende een kantoor in Katy, Texas. Het
Houston-kantoor had zoveel prominentie dat Google in Katy het kantoor op **26 mijl** afstand bleef
tonen en de nieuwe vestiging wegfilterde.

---

## Diagnose 3: goede posities, maar de telefoon gaat niet

Rankings staan als een huis, leads lopen terug. De oorzaak ligt niet in SEO.

Sterling Sky liet Jeepto data trekken uit **179 bedrijfsprofielen van 34 advocatenkantoren** in de
VS. Klikken-om-te-bellen daalt structureel over twee jaar — óók bij bedrijven die onverminderd goed
ranken.

**1. Advertenties in het lokale pakket.** Begin 2025 in 1% van hun mobiele rankingrapporten, in
november 2025 **14%**. Google haalde tegelijk de belknop weg bij de gewone vermeldingen en verving
die door afbeeldingen, terwijl de belknop in de betaalde plaatsing fors werd vergroot.

> Consumenten stopten niet met bellen. Google verplaatste de knop.

**2. AI-lokale pakketten.** Die komen niet naast het lokale pakket, ze **vervangen** het.

- Doorgaans **twee** bedrijven in plaats van drie
- **Geen belknoppen**
- Vaak **andere** bedrijven dan het traditionele pakket
- De meeste rankingtrackers meten ze nog niet — je rapport oogt gezond terwijl je zichtbaarheid
  verdampt

In hun meting: **5.943** unieke bedrijven in AI-pakketten tegenover **18.330** in traditionele
pakketten, ongeveer **32%**. In 322 markten hadden er **88%** minder unieke bedrijven in het
AI-pakket.

**Wat Sterling Sky adviseert:** meer locaties openen, en Google Ads draaien in alle formats. Hun
klanten haalden eind 2025 een betere ROI uit Ads — niet omdat advertenties goedkoper werden, maar
omdat de plaatsing beter werd en organische vermeldingen functionaliteit verloren. Daarnaast
autoriteit opbouwen op YouTube en Reddit als een van de weinige verdedigbare strategieën.

⚠️ Dit advies loopt richting "koop advertenties", en komt van een bureau dat ook Ads beheert. De
onderliggende data is controleerbaar; de conclusie is hun afweging.

---

## Diagnose 4: recensies verschijnen niet

Er zijn **drie verschillende oorzaken** die op elkaar lijken. Ze door elkaar halen leidt tot het
verkeerde advies.

| | Wat er gebeurt | Herkenbaar aan |
|---|---|---|
| **Recensiefilter** | Individuele recensies worden tegengehouden | *Sommige* recensies verschijnen wel, andere niet |
| **Recensieblokkade ("review jail")** | De vermelding mag helemaal geen nieuwe recensies ontvangen | **Geen enkele** recensie verschijnt nog |
| **Categorieblokkade** | Google staat voor deze categorie geen recensies meer toe | Geldt voor de hele branche |

### Het recensiefilter

Zie [Recensies krijgen en behouden](#recensies-krijgen-en-behouden) voor de oorzaken en de
oplossingen.

### Recensieblokkade (review jail)

Google kan een vermelding blokkeren zodat er **geen nieuwe recensies meer bij kunnen**. De term is
van Joy Hawkins, niet van Google.

- **Je krijgt geen melding.** In Noord-Amerika ziet een consument niets bijzonders: de knop staat er,
  je kunt een recensie schrijven, hij verschijnt alleen nooit. In het VK plaatst Google inmiddels wél
  een waarschuwingslabel op de vermelding dat er recensies zijn verwijderd — vermoedelijk vanwege
  andere wetgeving.
- **Enige manier om het te bevestigen:** Google support vragen.
- **Duur: zes tot acht maanden** in de gevallen die ze volgden, en langer als het gedrag doorgaat.
- **Je kunt er niets aan doen.** Er is geen bezwaarprocedure, geen versnelling. Google zegt de
  vermelding te monitoren en heft de blokkade op wanneer hij dat gepast vindt.
- **Het effect is dubbel.** Omdat recensiefrequentie een rankingfactor is, verlies je niet alleen de
  recensies maar ook je posities.
- **En daarna wordt het niet meteen beter.** Heeft Google veel valse recensies bij je verwijderd, dan
  wordt het filter op jouw vermelding **strenger**. Na afloop van de blokkade krijg je ook echte
  recensies moeilijk gepubliceerd — als hardlopen met gewichten aan je benen.

De case die dit illustreert: een noodloodgieter met stralende vijfsterrenrecensies, een F bij de
Better Business Bureau, één ster op Yelp en een plek op de Canadese consumentenwaarschuwingslijst.
Google verwijderde herhaaldelijk honderden tot duizenden valse recensies; een maand later stond het
aantal weer op peil omdat ze gewoon nieuwe kochten. Sinds de blokkades staan hun vermeldingen op
één tot drie sterren.

⚠️ Eerlijkheidshalve: Joy ziet **veel meer bedrijven die recensies kopen zonder deze straf** dan
bedrijven die hem krijgen. Het is een reëel maar niet vanzelfsprekend risico.

### Categorieblokkades en incidenten

- Vanaf **april 2025** staat Google wereldwijd geen recensies meer toe op vermeldingen voor algemeen
  onderwijs. Er is geen gepubliceerde lijst van getroffen categorieën, dus bedrijven denken vaak dat
  er iets mis is met hun profiel.
- Google kan recensies tijdelijk blokkeren bij een **incident**. Een advocaat met een negatief virale
  video kon tijdelijk geen nieuwe recensies ontvangen — bescherming tegen een recensieaanval.

---

## Diagnose 5: organisch zakt terwijl het lokale pakket goed staat

De **diversity update**, die Sterling Sky vanaf augustus 2024 zag en die daarna breder toesloeg.

**Wat er gebeurt:** staat je bedrijf al in het lokale pakket, dan **degradeert Google je organische
positie**. De redenering lijkt: we hebben dit bedrijf al één keer laten zien. Jarenlang was het doel
juist om beide te domineren.

Het werkt als een negatieve score bovenop je totaal, en het is **niet** de enige factor — sta je
sterk genoeg, dan kun je de klap opvangen en nog steeds beide plekken pakken. Dat verklaart waarom
sommige bedrijven nog altijd overal staan.

Wie het hardst geraakt wordt: merken die vóór de update lokaal én organisch domineerden. Eén
thuisdienstenbedrijf verloor **242 klikken** in een paar maanden. Wie het juist wint: bedrijven die
sterk leunen op servicegebiedpagina's in plaatsen waar ze géén bedrijfsprofiel hebben.

**De degradatie is op paginaniveau.** Dat maakt de oplossing concreet:

> Controleer naar welke pagina je bedrijfsprofiel linkt. Is dat precies de pagina waarvan de
> organische positie inzakt, koppel je profiel dan aan een **andere, nog steeds relevante** pagina.

⚠️ **Dit botst met hun eigen eerdere advies, en ze zeggen dat zelf.** Jarenlang luidde de regel: link
je bedrijfsprofiel aan de pagina die organisch het best presteert. Die regel geldt niet meer. Toen ze
bij testklanten het profiel aan de best presterende organische pagina koppelden, stortte de
organische positie in; terugzetten herstelde hem.

**De werkbare synthese** — en zeg erbij dat dit een afweging is, geen bevinding uit één test: koppel
je profiel aan de pagina die **het meest relevant is voor de termen die je in het lokale pakket wilt
winnen**, en vermijd daarbij je sterkste organische pagina. Specifiek blijft beter dan je homepage
(zie [De landingspagina](#de-landingspagina-van-je-profiel)); alleen mag "specifiek" niet samenvallen
met "mijn beste organische pagina".

---

## Rankingfactoren in het lokale pakket

Uit een onderzoek van Sterling Sky met Places Scout: **ruim 8.000 bedrijven, 200 steden**, van grote
steden tot plaatsen met 50.000 inwoners, gericht op "near me"-zoekopdrachten. Het gaat om
**correlaties**; geen enkele factor koopt je de eerste plek.

### Een zichtbaar adres (tegen Google's eigen advies in)

Servicegebiedbedrijven zonder zichtbaar adres ranken **slechter**. Google adviseert zelf je adres te
verbergen als je geen bezoeklocatie hebt.

Getest bij een klant in de thuisdiensten: adres verborgen → rankings stortten in; een maand later
teruggezet → volledig herstel. Herhaald op een tweede vermelding van hetzelfde bedrijf, zelfde
uitkomst.

**Een kantoor met zichtbare pin is dus een rankingfactor**, en kan de investering waard zijn.

### Primaire categorie

Volgens het lokale-rankingfactorenonderzoek de **belangrijkste** factor. Zie de klimaatcase hierboven:
van 1 naar 31 door één categoriewijziging.

Kies niet op gevoel: kijk welke categorieën de best presterende bedrijven in jouw markt gebruiken. De
Plepper-extensie toont in één oogopslag alle categorieën van concurrenten op Maps; een
leadgeneratierapport in Places Scout geeft hetzelfde datagedreven.

### Secundaire categorieën: méér is beter

⚠️ Hier wijkt Sterling Sky bewust af van Google's richtlijn, die zegt zo weinig mogelijk categorieën
te gebruiken. Je mag er **tot tien** kiezen, en meer categorieën betekent meer kansen om te ranken —
"categorieverdunning" bestaat volgens hen niet.

Voorbeeld: een hovenier had alleen *hovenier*. Ze voegden *tuinontwerper*, *tuinarchitect* en
*leverancier van keermuren* toe, waarna hij ging verschijnen voor termen als keermuren en
graszodenlevering. Tandartsen hebben meer dan tien categorieën beschikbaar; wie alleen de generieke
kiest, mist bijvoorbeeld *tandbleking*.

Blijf wel binnen de bedoeling van het veld: een categorie beschrijft wat je **bent**, niet wat je
verkoopt (zie [De richtlijnen](#de-richtlijnen-in-het-kort)).

### Seizoensgebonden categorie wisselen

Wissel je primaire categorie mee met de vraag. Een klimaatbedrijf zet in de winter *cv-reparatie* als
primaire categorie en in de zomer *airconditioningreparatie*. Niemand belt in juli over een cv-ketel.

⚠️ Weeg dit tegen de waarschuwing bij [schorsingen](#preventie): herhaald wisselen van naam en
categorie is precies het patroon dat detectie triggert. Eén keer per seizoen is iets anders dan om de
twee weken testen, maar houd het beperkt en voorspelbaar.

### Bedrijfsnaam: de legale route

Zoekwoorden in de bedrijfsnaam zijn volgens hetzelfde onderzoek de **op één na belangrijkste** factor.
Een makelaar die strategisch rebrandde kwam in de top drie voor zijn belangrijkste zoekwoord — in een
straal van **80 kilometer**.

Ze testten het ook direct: bij een restaurant *saladebar* aan de profielnaam toegevoegd → posities
omhoog; weggehaald → omlaag; teruggezet → weer omhoog.

Zomaar zoekwoorden in je naam proppen is in strijd met de richtlijnen. De legale route:
**registreer een handelsnaam** (in de VS een DBA). Zolang die authentiek is, consistent wordt
doorgevoerd in je hele online aanwezigheid en ook echt in je marketing wordt gebruikt, accepteert
Google hem — en is hij ook je verdediging als je wordt aangesproken.

> ⚠️ **Voor Nederland en België:** DBA is een Amerikaanse constructie. Het principe — een echt
> geregistreerde handelsnaam die je consequent voert — vertaalt naar een handelsnaam bij de KvK of de
> KBO. De transcripties gaan hier niet over; controleer dit lokaal.

### Openingstijden

Realtime rankingfactor: **ben je dicht, dan zak je**. Een advocaat en een psychiater zakten weg zodra
ze gesloten waren; in het weekend stortten hun posities in. Local Falcon laat de verschuiving per uur
zien. 24-uursbedrijven hebben 's nachts een enorm voordeel omdat hun concurrenten verdwijnen.

Wie zich als 24/7 vermeldt hoeft niet 24/7 open te zijn — maar moet de telefoon wél kunnen opnemen.
Een antwoordservice buiten kantooruren maakt dit mogelijk. Resultaten:

- Hovenier naar 24/7: telefoontjes buiten kantooruren **+142%**, totaal **+58%**
- Ander bedrijf: van **57 naar 119** nieuwe bellers in één maand
- Een audit waarin alleen de foute openingstijden werden gecorrigeerd: telefoontjes **verdubbeld in
  30 dagen**

Drie praktische details:

- **Alleen je hoofdopeningstijden tellen voor rankings.** Extra tijdvakken en online-openingstijden
  doen niets voor je positie.
- **Je kunt meerdere tijdvakken per dag instellen** (bijvoorbeeld een lunchpauze) via de plusknop, en
  **speciale openingstijden** voor feestdagen.
- **Sluit je definitief, markeer dan "permanent gesloten"** in plaats van je profiel te verwijderen.
- Controleer of er *"openingstijden bevestigd door bedrijf"* staat. Zo niet, dan kan een
  gebruikersvoorstel je tijden hebben gewijzigd.

### Recensies

Meerdere afzonderlijke factoren, die je los moet sturen:

- **Gemiddelde score** — duidelijk verband met posities op "near me"-termen.
- **Frequentie verslaat volume.** Een tandarts haalde 60 recensies in één maand en domineerde; daarna
  kwam er 18 dagen niets binnen en zakten ze weg, terwijl concurrenten 13 tot 45 per maand bleven
  binnenhalen. Het aantal recensies in de **afgelopen maand** correleert met betere posities.
- **De grens van 10.** Ontdekt door Joel Headley, opnieuw getest op acht elektricien-vermeldingen —
  vier met 9 en vier met 10 recensies, gemengd servicegebied en fysieke vestiging. Bij het passeren
  van de **tiende** schoten de rankings omhoog. Van 10 naar 11: niets.
- **Recensies mét tekst wegen zwaarder** dan losse sterren. Een ster zonder tekst toont Google niet
  eens in de Maps-app.

Benchmark op drie dingen tegelijk: hoeveel recensies krijgen concurrenten per maand, hoe verhoudt je
gemiddelde zich, en hoe verhoudt je totaal zich.

### Foto's

Hoe langer je geen nieuwe foto toevoegt, hoe slechter je posities op "near me"-termen. Ouder
onderzoek (BrightLocal, 2019) koppelt meer foto's aan meer kliks, telefoontjes en routeaanvragen.

Maar dit is **niet universeel**: in sommige branches kritiek, in andere zagen ze geen enkel effect.
Een garagedeurenbedrijf hoeft niet dagelijks een nieuwe garagedeur te uploaden.

### Betekenisvolle woorden op de landingspagina

Een hogere woordtelling **exclusief stopwoorden** correleert met betere posities. Dit gaat niet over
lengte maar over inhoudelijke substantie. Places Scout signaleerde dit al in 2016.

### De landingspagina van je profiel

Link naar de **meest relevante** pagina, niet standaard naar je homepage.

Een advocatenkantoor in New York had losse profielen per advocaat, allemaal op hetzelfde adres met
dezelfde categorie — en werd weggefilterd. Ze koppelden één profiel aan de *busongevallen*-pagina in
plaats van de homepage: rankings omhoog. Bij een volgend profiel de *fietsongevallen*-pagina: opnieuw
omhoog.

⚠️ Combineer dit met de [diversity update](#diagnose-5-organisch-zakt-terwijl-het-lokale-pakket-goed-staat):
specifiek en relevant, maar **niet** je sterkste organische pagina.

### Diensten in het profiel

Getest in 2019 met weinig effect, opnieuw in 2022 met een **significant** effect — ook op zeer
specifieke diensten. De omvang verschilt per regio en concurrentiedruk. Kost een paar minuten.

---

## Hoe het Google-systeem vanbinnen werkt

Dit deel komt van twee ex-Googlers die elk ruim elf jaar aan het product werkten. Het verklaart
gedrag dat van buitenaf willekeurig lijkt.

### Twee databases: de sleutel tot "uitgeschakeld" versus "geschorst"

Er zijn **twee gescheiden databases**:

1. De **GBP-database** — waar je in inlogt op business.google.com en je wijzigingen maakt. Hier leven
   ook je reacties op recensies en je lokale posts.
2. De **Maps-database** — die het openbare kaart- en lokale-pakketresultaat voedt.

Je vermelding bestaat in beide. Wat je in GBP wijzigt wordt bij publicatie naar de Maps-kant
doorgezet — vandaar het verschijnsel "wijziging in behandeling".

| | Wat er gebeurt | Symptoom |
|---|---|---|
| **Uitgeschakeld (disabled)** | De verbinding tussen beide databases is doorgesneden | De vermelding staat **nog gewoon op Maps**, maar je kunt niets meer wijzigen |
| **Geschorst (suspended)** | De vermelding is van de Maps-kant **afgehaald** en in GBP als geschorst gemarkeerd | Je bent weg van de kaart; herstel vraagt oplossen van de onderliggende oorzaak |

Verwarrend randgeval: is een vermelding eerst uitgeschakeld en daarna ook *ongeverifieerd*, dan
verdwijnt hij alsnog van de kaart terwijl het dashboard "uitgeschakeld" blijft zeggen.

### Google is geen "Google"

Het team dat het beleid schrijft, het team dat de QR-code bouwde en het team dat recensies verwijdert
zijn **verschillende teams**. Daarom kan Google je iets aanraden dat een ander onderdeel bestraft.

> Dat is niet omdat Google je wil pakken. Het is een groot bedrijf met veel mensen die verschillende
> dingen doen.

De richtlijnen zijn **bewust vaag**, zodat Google ruimte houdt in de handhaving. Wat de richtlijn
zegt en wat er gehandhaafd wordt zijn twee vragen. Intern viel regelmatig het antwoord "dit is een
business decision": geen schending van Google-breed beleid, maar de productmanager beslist.

### Er is geen algoritme, er zijn scripts

Voor spam- en recensiedetectie schrijft het trust-and-safety-team scripts die kenmerken van bekende
spamvoorbeelden targeten, en meten die af op een steekproef: *"ik haal 80% van mijn doelwit neer, en
20% dat er niet bij hoort — win ik hier?"* Bij 80/20 vinden ze dat prima; in de praktijk sturen ze
richting 90/10.

**Bij 100 miljoen bedrijven is 10% nevenschade nog altijd 10 miljoen bedrijven.** Verdwijnen jouw
legitieme recensies, dan ben je meestal geen doelwit maar nevenschade.

### De cyclus van recensieverwijderingen

**Seizoensgebonden.** Rond maart–april wordt het detectiealgoritme aangescherpt en volgt een golf
verwijderde legitieme recensies; na klachten wordt het teruggedraaid en komt een deel terug. In het
vierde kwartaal gebeurt dit niet: Google gaat rond de feestdagen in code freeze.

**Verwacht niet dat alles terugkomt.** Verlies je er tien, dan is zes tot acht terugkrijgen
realistisch.

### Google verwijdert content niet echt

Alleen de **maker** kan content echt verwijderen. Verwijdert Google een recensie, dan wordt die
verborgen voor het publiek maar blijft bestaan — de spammer ziet zijn eigen recensie gewoon staan,
wat hem geen signaal geeft dat hij gepakt is. De recensie hoort technisch bij het **account van de
schrijver**, niet bij het bedrijfsprofiel; bij verwijdering wordt alleen de koppeling verbroken.

Gevolgen:

- Herstel gebeurt door **herverwerking**, niet door terugzetten. Daarom komen recensies soms vanzelf
  terug bij een volgende ronde.
- Een supportmedewerker die zegt *"ik kan ze niet vinden"* heeft half gelijk (de koppeling is weg) en
  is half lui. **Kom met bewijs**: een export of back-up van de verdwenen recensies haalt dat antwoord
  van tafel. Sommige GBP-beheersoftware maakt daar back-ups van.
- ⚠️ Sinds ongeveer 2020 is Google kostenbewuster en ruimt hij wél op — onder meer vermeldingen waar
  jarenlang niets mee gebeurde. Het oude "Google gooit nooit iets weg" geldt minder onvoorwaardelijk.

### Vertrouwensscore

Zowel gebruikers als bedrijven hebben er een. Elke geaccepteerde bijdrage aan de kaart telt positief;
een voorstel dat wordt afgewezen of later teruggedraaid telt negatief. Als kaarten tellen: plus één,
min één.

- Een **vers Gmail-account** dat één recensie meldt is een lege stem. Een account met historie weegt
  zwaar; een google.com-adres liet een recensie binnen een uur of twee verdwijnen.
- **Meldingen met meerdere mensen werken**, maar niet omdat Google stemmen telt. Twintig melders maken
  **twintig aparte tickets**, dus twintig kansen dat een beoordelaar hem weghaalt. Je benut de
  foutmarge van een handmatig team.
- Het snijdt aan twee kanten: wordt de recensie later teruggezet, dan kan dat je eigen score schaden.
- Profielen met veel verwijderde recensies krijgen een **lagere vertrouwensscore**, waarna ook echte
  recensies moeilijker blijven plakken.
- Er is geen magisch Local Guide-niveau. Niveau 7 is "het nieuwe niveau 5"; meer positieve bijdragen
  is het enige recept, en het loont: actieve accounts krijgen hun wijzigingen vaker gepubliceerd en
  triggeren minder herverificaties.

### Support: niveaus, talen en wat nog handmatig is

- **Niveau 1 en 2** zitten samen op één locatie en overleggen via realtime chat. Om niveau 2 vragen is
  zinnig: dat zijn de doorgegroeide medewerkers. Het antwoord verandert er niet per se door, maar de
  beoordelaar is beter.
- **Niveau 3** is uitsluitend voor **bugs**, en zit in de VS. Een ontbrekende recensie, een schorsing
  of foute data is géén bug maar een datakwestie — daarmee kom je er niet.
- Zaken worden **per taal naar callcenters gerouteerd**, met flinke kwaliteitsverschillen. De
  Engelstalige ondersteuning vanuit India scoorde het slechtst; wie in het Spaans belde kwam bij
  Buenos Aires uit, met aanzienlijk hogere kwaliteitsscores.
- **Bij achterstanden zijn er aparte wachtrijen per taal.** Minder gangbare talen hebben kortere
  wachtrijen. Toen de Engelse wachtrij vastliep moesten ze de Athene-locatie omscholen naar Engels,
  waardoor de Europese talen juist sneller werden afgehandeld.
- **Wat nog handmatig is:** on-demand videoverificatie en handmatige verificatie. Die laatste is een
  bewust verstopte noodklep — zie [Verificatie](#de-verstopte-noodklep-handmatige-verificatie).
- Het **forum voor productexperts** is voor herstelzaken veel minder effectief geworden, om dezelfde
  reden: de handmatige beoordelingen erachter zijn grotendeels weg.
- Historisch werden supportmedewerkers beloond op klanttevredenheid, wat betekende dat ze overal ja
  op zeiden — spammers maakten daar gretig gebruik van. Dat is omgezet naar belonen op de **juiste**
  beslissing, wat soms nee betekent.

### Handmatige maatregelen zijn zeldzaam

Bijna alles is algoritmisch. In jaren zag Sterling Sky er één bij een klein bedrijf: het had een
linkbureau ingehuurd dat van nul naar honderd links ging in een paar maanden, dezelfde tekst vijftig
keer herschreven op vijftig sites, geplaatst vanaf accounts die ook over cryptocurrency schreven.

> Zie je iets dat je een straf noemt, ga er dan van uit dat het algoritmisch is. Er komt geen melding
> in Search Console.

---

## Verificatie

### De basis goed zetten

- **Gebruik geen Gmail maar een merkgebonden e-mailadres** (`hallo@jouwbedrijf.nl`). Een Gmail toont
  geen enkele band met je bedrijf; dat is een rode vlag.
- **Bouw historie op met het account.** Een account met een staat van dienst in het beheren van
  profielen krijgt aantoonbaar betere verificatieopties.
- **Zet eerst je aanwezigheid elders neer.** Eén klant bouwde eerst profielen op gezaghebbende sites
  als Facebook en Yelp en kreeg daarna directe verificatie en telefoonverificatie aangeboden in plaats
  van video.
- **Koppel Search Console en Analytics aan hetzelfde account.** Volgens Danny Owens kan dat directe
  verificatie triggeren, omdat Google dat account al aan je eigendommen gekoppeld ziet.

### Videoverificatie voor een servicegebiedbedrijf

Je hoeft geen fysieke vestiging te hebben. Je moet laten zien dat je **in je servicegebied opereert**:

- Heb je een bedrijfswagen met belettering, parkeer die dan in je servicegebied, bij een
  bedrijvenpand of een kruispunt met duidelijke straatnaamborden.
- Geen belettering? Een herkenbare plek volstaat — je eigen oprit, of bij een straatnaambord.
- **Voor makelaars**, van een ex-Googler: verifieer bij een huis dat je in de verkoop hebt. Open de
  deur om te laten zien dat je toegang hebt, en toon het bord in de voortuin.
- Werk je vanuit huis, laat dan je woning en huisnummer zien. **Je hoeft geen bedrijfsbord te hebben** —
  Google eist dat niet, ook al zeggen supportmedewerkers dat soms wel.

### Als verificatie vastloopt

- **Je kunt geen andere methode kiezen.** Biedt Google videoverificatie aan, dan moet je die
  gebruiken. In zeldzame gevallen helpt support, maar meestal sturen ze je terug naar video.
- **"Geen manieren meer om te verifiëren"** — dan is contact met support de enige weg.
- **Video uploadt niet** — herstart je apparaat; helpt dat niet, vraag support om handmatige
  verificatie.
- **Post videoverificatieproblemen niet op het forum.** Daar kunnen ze er niets mee.
- **Gebruik Google's verificatietool** om te zien wat er speelt. Klik door alle stappen tot het einde;
  daar staat een *contact opnemen*-link naar support.
- **Onderscheid vertraging van storing:** zegt de verificatietool dat het nog verwerkt wordt, dan is
  het wachten. Zegt de tool dat je geverifieerd bent terwijl je profiel dat ontkent, dan is het een
  technisch probleem en moet je support hebben.
- **"Gaat live over vijf minuten"** klopt vaak niet — reken op dagen.
- **Een tweede verificatieronde is normaal.** Ging het de eerste keer heel makkelijk (telefoon of
  direct), dan dwingt Google soms een herverificatie af, en ze kunnen je zelfs schorsen. Beleid staat
  toe dat er meer dan één methode nodig is als de eerste manipuleerbaar lijkt.

### De verstopte noodklep: handmatige verificatie

Google wil dat je de geautomatiseerde route neemt — bij vertrek verwerkten ze drie miljoen contacten
per jaar. Handmatige verificatie is de uitzondering, en bewust lastig te vinden:

1. **Probeer eerst videoverificatie en laat die mislukken.** Daarmee wordt in de database een vlag
   gezet.
2. Doorloop daarna opnieuw de supportflow (zoek op verificatie, klik door tot de vervolgflow).
3. Waar eerder *"feedback verzenden"* stond, staat nu **"neem contact op"** — een klein blauw
   tekstlinkje, geen knop.
4. Dat leidt naar een formulier waarin je **bewijs kunt uploaden**. Dat gaat naar een mens.

### Wie beheert deze vermelding eigenlijk?

Ga naar `business.google.com/add/info`, typ je bedrijfsnaam, selecteer je bedrijf en klik door. Je
krijgt een **hint van het e-mailadres** dat de vermelding nu beheert. Dat scheelt vaak de hele
eigendomsoverdracht.

### Eigendom opvragen als je de inloggegevens kwijt bent

1. Ga naar `business.google.com` en zoek je bedrijf.
2. Krijg je "geclaimd door iemand anders" met een hint die je herkent — log daar in, klaar.
3. Zo niet: **vraag toegang aan**. De huidige eigenaar krijgt een mail en heeft **zeven dagen** om te
   reageren.
4. Reageert hij niet binnen zeven dagen, dan kun je de vermelding zelf verifiëren. **Bewaar de mail
   met de verificatielink** die je bij je aanvraag kreeg — die heb je dan nodig.
5. Wordt je verzoek geweigerd, dan kun je in bezwaar en alsnog verifiëren dat jij bevoegd bent.

**Voor servicegebiedbedrijven met verborgen adres** verloopt het anders: je vindt de vermelding niet
in het zoekresultaat. Doorloop de stappen alsof je de vermelding opnieuw aanmaakt; zodra je verifieert
wordt hij als **duplicaat** gemarkeerd en verschijnt in je dashboard de knop *toegang aanvragen*.

Alternatieve route om zo'n verborgen vermelding tóch te vinden: zoek de **place ID** op (bijvoorbeeld
met de Plepper-extensie) en plak die in de daarvoor bedoelde URL — dan komt de vermelding
tevoorschijn.

### Bulkverificatie

Voor ketens, franchises en bedrijven met meerdere vestigingen: tien of meer vermeldingen in één keer.

**Wie mag het:**

- Minstens **tien fysieke vestigingen**. Servicegebiedbedrijven komen niet in aanmerking.
- Geen geschorste of te herverifiëren vermeldingen in de groep.
- Het aantal locaties op je website moet **exact** overeenkomen met de bedrijfsgroep.
- **Foto's van je gevelreclame** per vestiging, geüpload naar de vermeldingen. Naam op het bord,
  website en vermelding moeten overeenkomen.
- Meerdere merken of handelsnamen mogen, mits je aantoont dat dezelfde moederonderneming ze bezit.

**Hoe:**

1. Groepeer alle locaties onder één bedrijfsgroep.
2. Zet een **merkgebonden domeinmail als hoofdeigenaar** van de groep én van elke losse vermelding.
3. Ga naar het tabblad verificaties → wijzigen → vul het bulkverificatieformulier in.
   Zie je dat tabblad niet (bureau-account), vraag er dan via het normale supportformulier om.
4. Zorg dat elke vermelding een **winkelcode** heeft; anders vraagt Google daar alsnog om.
5. Reageer snel op vervolgvragen.

**Twee valkuilen:**

- Google denkt vaak dat je één locatie wilt verifiëren. Leg expliciet uit dat het om de hele
  bedrijfsgroep gaat en geef het **bedrijfsgroep-ID** en het **domeinmailadres van de hoofdeigenaar**.
- **Wijzig of verwijder dat e-mailadres daarna niet** — dan kun je je bulkgeverifieerde status
  kwijtraken.

**Zonder bulkverificatie** zit er een limiet van ongeveer **tien vermeldingen per week** per account.
Er circuleert een omweg via een ander IP-adres; Google houdt IP-adressen bij, dus dat is riskant.

**Na bulkverificatie** kun je de bulkupload gebruiken: sjabloon downloaden, alles invullen,
terugzetten. Ook dan geldt: **doe grote wijzigingen één voor één** — telefoonnummer, naam, adres of
website-URL — met een paar dagen ertussen.

### Herverificatie voorkomen

Grote wijzigingen (naam, telefoonnummer, adres) kunnen herverificatie triggeren, zeker vanaf een
nieuw of niet-vertrouwd account. Dat is bedoeld als bescherming tegen kapers. Gebruik dus een account
met historie en stapel geen grote wijzigingen.

---

## Eigendom, beheerders en toegang

### Hoe je het inricht

- **Zet het bedrijfsdomein als hoofdeigenaar, geen Gmail.** Een domeinaccount erft de autoriteit van
  het domein en biedt herstelmogelijkheden; raakt een Gmail geschorst, dan is herstel zwaar.
  Nuance: een Gmail met vijftien jaar historie verslaat een gisteren aangemaakt domeinaccount. Bouw
  de autoriteit op het domein op — die haalt de Gmail uiteindelijk in.
- **Drie personen op een profiel**: één hoofdeigenaar, nog een eigenaar en een beheerder. Met één
  account ben je kwetsbaar als dat account iets overkomt; met vijftien beheerders kan elk van die
  vijftien je schade berokkenen.
- **Ieder zijn eigen toegang** — geen gedeelde inloggegevens.

### De mechaniek

- **Alleen eigenaren** kunnen gebruikers toevoegen of verwijderen. Beheerders kunnen alleen zichzelf
  verwijderen.
- **De hoofdeigenaar kun je niet verwijderen** zonder eerst het hoofdeigenaarschap over te dragen.
- **Nieuwe eigenaren en beheerders moeten zeven dagen wachten** voor ze alles kunnen. In die periode
  krijg je een foutmelding bij: een profiel verwijderen, andere eigenaren of beheerders verwijderen,
  en hoofdeigenaarschap overdragen.
- Verwijder je je Google-account, dan word je automatisch van het profiel gehaald. Later opnieuw
  toevoegen kan.

### Het bureau-dashboard

Voor wie tientallen tot honderden profielen beheert.

**Opzetten:**

1. Registreer met een **domeinmail van je eigen bureau**, en dat adres mag **nog geen andere Google-
   vermeldingen beheren**.
2. Teamleden hebben elk ook een schoon domeinmailadres nodig, eveneens zonder bestaande profielen.
3. Importeer daarna de vermeldingen.

**Toegang tot klantprofielen, twee routes:**

- **Vraag beheerderstoegang aan**, niet eigenaarstoegang. Vraag je eigenaarschap aan, dan degradeer
  je het account van je klant — een snelle manier om vertrouwen te verliezen.
- **Laat de klant je handmatig toevoegen.** Bij servicegebiedbedrijven met verborgen adres is dit de
  enige weg, omdat je de vermelding niet kunt vinden. Dat gaat via het **locatiegroep-ID** (één
  vermelding) of het **organisatie-ID** (bedrijfsgroepen).

**De grote nadelen, en dit is de reden om te twijfelen:**

- **Je verliest e-mailmeldingen.** Boven de honderd vermeldingen stuurt Google geen meldingen meer
  over recensies, vragen of profielwijzigingen — en ook met minder dan honderd raak je ze bij
  overstap waarschijnlijk kwijt. Je hebt dan externe tools nodig of je controleert handmatig.

**Waarom Sterling Sky het toch gebruikt:** de interface is veel sneller, en je kunt teams rond
groepen bedrijven organiseren, wat opschalen makkelijker maakt.

**Praktische gewoontes:** geef locatiegroepen duidelijke namen (klanten zien die), leer klanten het
locatiegroep-ID of organisatie-ID **zonder spaties** te plakken, en houd een schone-accountchecklist
aan voor nieuwe medewerkers.

---

## Schorsingen

### Risicogroepen

Google let extra scherp op de **dwangsectoren** — branches waarin de klant onder druk beslist:
slotenmakers, garagedeuren, loodgieters, sleepdiensten. Daar zit de meeste fraude.

Restaurants worden vrijwel nooit geschorst, om een leerzame reden: **het is makkelijk te bewijzen dat
ze echt zijn.** Echte locatie, echte gevelreclame, alles klopt. Bij een servicegebiedbedrijf zonder
zichtbare vestiging is dat veel lastiger — en een virtueel kantoor huren kan iedereen.

**Truc om te achterhalen of jouw categorie als risicogroep geldt:** probeer een wijziging voor te
stellen op een vermelding met die primaire categorie. Bij dwangcategorieën wordt dat **automatisch
geweigerd** — het lukt niet bij slotenmakers, garagedeurherstel of sleepdiensten.

### Preventie

De rode draad van beide ex-Googlers: **denk als een spammer en doe dat niet.**

> Herken wat gebruikers willen en lever dat, in plaats van te proberen iets te forceren.

- Verander je adres niet om je pin gunstiger te laten vallen
- Wijzig je categorie niet naar iets dat hiërarchisch nergens op slaat
- Verander je naam niet vijf keer in een maand
- Herhaald "testen" met naam en categorie is precies het patroon dat gedetecteerd wordt
- Geen virtueel adres, geen zoekwoorden stapelen, geen doorverwijzingen, geen overlappende
  servicegebieden met je eigen andere vermeldingen
- **Hergebruik nooit hetzelfde telefoonnummer op meerdere vermeldingen.** Dat leidt tot samenvoegingen
  die je nauwelijks kunt terugdraaien, en geschorste vermeldingen komen er vaak niet meer doorheen als
  het nummer op te veel andere plekken online staat.

**Wees proactief met bewijs.** In een risicosector wil je uit het grijze gebied blijven vóór er een
golf komt: draag foto's van je locatie bij, blijf actief op je profiel, zorg dat je gevelreclame
overeenkomt met je profielnaam. Een keten met 4.000 vestigingen gebruikte overal dezelfde beelden —
**lokaliseer je beeldmateriaal**, laat zien dat je in Tampa zit en niet in New York.

### De nieuwe bezwaarprocedure en de klok van 60 minuten

Uitgerold in de EU in 2023, daarna in de VS. Zeven stappen:

1. Je krijgt een e-mail dat de vermelding is geschorst of uitgeschakeld.
2. Klik op de blauwe **bezwaar**-knop.
3. Ga naar de bezwaartool en bevestig welke vermeldingen je beheert.
4. Bevestigen → je komt bij het profiel.
5. Selecteer de vermelding die je hersteld wilt hebben.
6. De tool toont drie dingen: het beperkte profiel, **de reden voor de maatregel**, en een link naar
   het geschonden beleid.
7. Dien het bezwaar in.

⚠️ **Daarna verschijnt een link "bewijs toevoegen". Zodra je daarop klikt loopt er een klok van 60
minuten.** Wat je binnen dat uur niet hebt geüpload, wordt niet meegenomen in je bezwaar.

**Zorg dus dat alles klaarstaat vóór je het bezwaar indient:**

- officiële inschrijving van het bedrijf
- vergunning of licentie
- belastingdocumenten
- energierekeningen op het bedrijf
- foto's en video's van de locatie

**Zorg dat naam, adres en telefoonnummer op elk document exact overeenkomen** met de vermelding
waarvoor je bezwaar maakt.

Statussen die je daarna kunt zien: ingediend, goedgekeurd, niet goedgekeurd, kan geen bezwaar tegen,
in aanmerking voor bezwaar.

**Bonus:** klik in de oorspronkelijke schorsingsmail op de link naar het beleid. Die brengt je naar
de **specifieke sectie van de richtlijnen die je zou hebben geschonden** — historisch gaf Google die
informatie helemaal niet.

### De zeven stappen bij herstel

1. **Bepaal het type.** Zacht = profiel nog zichtbaar, alleen niet beheerbaar. Hard = van de kaart.
   Zoek je bedrijfsnaam op Maps. Bij hard is haast geboden. (Zie ook
   [uitgeschakeld versus geschorst](#twee-databases-de-sleutel-tot-uitgeschakeld-versus-geschorst).)
2. **Audit je profiel op rode vlaggen.** Klopt je adres exact met je inschrijving? Virtuele kantoren
   en veel wijzigingen in korte tijd zijn triggers. Ruim duplicaten op.
3. **Controleer eigenaren en beheerders.** Is het Google-account van een van hen geschorst, dan trekt
   dat jouw vermelding mee. Verwijder die accounts vóór je bezwaar maakt.
4. **Verzamel bewijs** (zie hierboven). Ontbreekt gevelreclame, dan is die soms echt nodig — ziet
   Google op Street View alleen een woonhuis, dan moet het vertrouwenssignaal omhoog.
5. **Maak het profiel schoon.**
6. **Dien het bezwaar in met al het bewijs tegelijk.**
7. **Voorkom herhaling.** Wijzig langzaam, geen virtueel adres, beperk het aantal gebruikers.

**Maak geen nieuw profiel aan** en raak niet in paniek.

---

## Recensies krijgen en behouden

### Waarom recensies niet gepubliceerd worden

Volgens Claudia Tomina is de belangrijkste oorzaak dat er **geen echte interactie was tussen de
recensent en het bedrijfsprofiel** voordat de recensie geschreven werd. Iemand die via een
doorverwijzing komt, jouw recensielink krijgt en direct schrijft, heeft nooit met je profiel
geïnterageerd — en dat is een vlag.

**Wat wel werkt:**

- Laat mensen het bedrijf **opzoeken op Google of Maps** (een merkzoekopdracht) en daarvandaan de
  recensie plaatsen. Merkzoekopdrachten blijven veel beter plakken.
- Deel **niet** de recensielink of QR-code die Google zelf in het dashboard aanbiedt — juist die
  vergroot de kans op filtering. Stuur naar een zoekresultatenpagina met de merknaam erin.
- Laat iemand die al iets op het profiel heeft aangeklikt (bellen, route, boeken) de recensie
  achterlaten.

Waarom dit werkt volgens de ex-Googlers: het gaat niet om de omweg zelf, maar om **gedrag dat op een
mens lijkt**. Vergelijk het met reCAPTCHA, dat muisbewegingen en kliks meet in plaats van je antwoord.
Minder klikken vóór het tekstveld betekent minder signalen en dus minder vertrouwen.

**Gefilterde recensie terugkrijgen:** laat de schrijver hem **licht bewerken**, een paar woorden
veranderen. Twee verklaringen die elkaar aanvullen: spammers komen nooit terug om hun werk bij te
schaven, dus bewerken is menselijk gedrag; en een bewerking triggert **herverwerking** door een
inmiddels mogelijk minder agressief algoritme.

Een bijvangst: recensiecampagnes leveren zichtbare rankingpieken op door de merkzoekopdrachten en
kliks die ze veroorzaken — maar die zakken weer weg.

### Snelheidslimieten

Recensies die veel te snel binnenkomen voor je branche worden gemarkeerd. Een dakdekker met **drie à
vier per dag** is onrealistisch. Patroon dat ze vaker zien: maandenlang groei, dan ineens alles
verwijderd plus een label "recensiemanipulatie".

De nuance: is dit oprecht je nieuwe normaal, houd het dan vol zodat het je normaal wórdt. Is het een
campagne of manipulatie, dan werkt het tegen je. Wat je een jaar geleden nog kon maken, kan nu niet
meer.

Ook geclusterd gedrag valt op: mensen uit **hetzelfde huishouden** of met dezelfde achternaam die
tegelijk plaatsen komen er vaak niet door, en een groep die binnen enkele minuten allemaal negatief
plaatst kan als recensieaanval worden gelezen. Druppelen dezelfde reviews over dagen binnen vanaf
verschillende accounts, dan blijven ze staan.

**Recensiefeestjes** (iedereen laten schrijven terwijl ze fysiek in de zaak zijn) waren ooit een
sterk echtheidssignaal, maar keren zich nu tegen bedrijven: tijdstip én locatie zijn onderdeel van
het detectiepatroon. Dat betekent níét dat ter plekke om recensies vragen slecht is — in een gestaag
tempo blijft het waardevol. Denk niet in absoluten; het algoritme doet dat ook niet.

**Gekochte recensies** hebben een risico dat verder gaat dan verlies van die recensies: een
[recensieblokkade](#recensieblokkade-review-jail), en daarna een strenger filter waardoor ook echte
klanten er niet meer doorheen komen.

### Uitgelichte recensies in het kennispaneel

Zoek je een bedrijf op naam, dan licht Google in het kennispaneel **drie recensies** uit. Joy Hawkins
noemt dit een van de slechtste functies die er voor kleine bedrijven bestaan.

Wat ze vond na drie jaar meten:

- **Ze verversen ongeveer eens per één tot twee jaar.** Bij een bedrijf dat ze drie jaar volgde
  gebeurde dat één keer.
- **Ze zijn stokoud.** Een uitgelichte negatieve recensie van **zeven jaar** oud. De CN Tower in
  Toronto heeft ruim 75.000 recensies en toch is de bovenste uitgelichte vijf jaar oud.
- **Het meest voorkomende patroon is twee positieve en één negatieve.** Soms lichten ze zelfs een
  positief beoordeelde recensie met negatieve strekking uit.
- **Bij een verversing vervangen ze de oudste door de nieuwste.**
- Het is geen gelijktijdige cyclus voor alle bedrijven; het lijkt een timer die per bedrijf verschilt.

**De enige manier om het te beïnvloeden:** de uitgelichte recensie helemaal van Google laten
verwijderen — dan ververst het geheel. Dat lukt zelden. In één geval lukte het door het **profiel van
de recensent** te laten verwijderen omdat dat een spamprofiel was: open het profiel van de recensent,
klik op de drie puntjes en meld het profiel. De slagingskans is laag.

### Recensie-afpersing

Een netwerk van nepprofielen overspoelt één bedrijf met eensterrenrecensies, vaak met uitgeschreven
verhalen. In de profielfoto of bio staat een WhatsApp-nummer; neem je contact op, dan vragen ze geld
om ze weg te halen, of ze willen ingehuurd worden om positieve recensies te plaatsen. Herkenbaar aan
terugkerende schrijfstijlen en **hetzelfde WhatsApp-nummer** in de bio's.

Drie stappen, en snel:

1. **Meld elke recensie afzonderlijk** (drie puntjes → recensie melden → spam of niet ter zake). Laat
   zoveel mogelijk mensen dit doen — elke melding is een apart ticket.
2. **Meld elk profiel afzonderlijk.** Alleen mogelijk in de Maps-app: tik op de naam van de recensent,
   open het profiel, drie puntjes, profiel melden.
3. **Meld het via het speciale formulier** dat Google hiervoor heeft gemaakt.

Bij elk bedrijf dat alle drie de stappen doorliep, verdwenen de recensies.

### De DMCA-verwijderingszwendel

⚠️ **Dit staat hier zodat je het herkent, niet zodat je het gebruikt.** Joy Hawkins noemt het niet
alleen schimmig maar simpelweg fout, in dezelfde categorie als recensies kopen.

Bedrijven betalen duizenden euro's aan diensten die negatieve **externe** vermeldingen laten
verdwijnen — een Reddit-thread of forumdiscussie die op je merknaam rankt. De methode: een
**DMCA-verzoek** indienen, de procedure die bedoeld is voor auteursrechtschendingen.

Sterling Sky's eigen forum werd hier slachtoffer van. De verwijderde pagina was een negatieve thread
over een bedrijf dat juist recensieverwijdering aanbiedt. In het DMCA-verzoek stond als
"gekopieerde bron" een **nieuwsartikel over een aardbeving in Haïti** — volstrekt ongerelateerd. Het
verzoek werd toch goedgekeurd en de pagina verdween; het verkeer viel terug naar nul.

De conclusie: er komt vrijwel zeker **geen mens** aan te pas. Dezelfde partij kreeg ook de
Reddit-thread verwijderd door genoeg gebruikers te laten melden, al kunnen moderators dat terugdraaien.

**Wat je hiermee doet:** wees ervan op de hoogte voordat je zo'n dienst inhuurt, en gebruik DMCA
alleen waarvoor het bedoeld is. Sterling Sky diende er zelf wel een legitieme in, toen een concurrent
letterlijk de content van hun klant had gekopieerd — inclusief de naam van die klant.

### Nepbelletjes namens Google

Scammers bellen bedrijven namens "Google". Vaste kenmerken:

- **Google werkt niet met externe partners** die je rechtstreeks bellen — wie dat zegt, liegt.
- **Een bedrijfsprofiel is gratis.** Google zal je nooit laten betalen om je profiel toe te voegen,
  bij te werken of te verwijderen.
- **Google vraagt nooit om gevoelige of persoonlijke gegevens.** Hang op.
- **"Er is een spoedprobleem met je vermelding"** is een drukmiddel, geen echt bericht van Google.

Google *belt* wel geautomatiseerd om openingstijden of de bedrijfsstatus te controleren — maar vraagt
daarbij nooit om gegevens.

### Reageren op negatieve recensies

Zeven principes, van Tommy Mello (A1 Garage Door) en Mike Blumenthal:

1. **Bel ze.** Laat de klant ook een leidinggevende spreken; zet daar mensen op die goed zijn in
   de-escaleren.
2. **Laat ze uitrazen.** Onderbreek niet. Ze willen gehoord worden.
3. **Verdedig jezelf niet.** Erken het deel dat klopt en ga door naar een oplossing.
4. **Schrijf de reactie niet zelf.** Je bent te betrokken. De reactie is voor je toekomstige klanten,
   niet voor de recensent.
5. **Neem verantwoordelijkheid** voor het deel dat terecht is.
6. **Beschrijf hoe je voorkomt dat het opnieuw gebeurt.**
7. **Bied aan het op te lossen.** Een kleine terugbetaling kost minder dan de omzet die je verliest.

Waarschuwend voorbeeld: een ondernemer reageerde met *"we betreuren het dat u een beeld schetst dat
niet met de werkelijkheid overeenkomt"* en kreeg er acht eensterrenrecensies bij. Google verwijderde
ze niet.

**Praktisch:**

- **Reageer binnen 24 tot 72 uur.** 53% van de klanten verwacht een reactie binnen een week, één op
  de drie sneller.
- **Iedereen met toegang mag reageren**; de reactie wordt altijd namens de eigenaar getoond. Noemt de
  recensie een specifieke medewerker, laat die dan reageren en zijn naam of initialen eronder zetten.
- **Reageer ook op positieve recensies**, en gebruik het moment om iets nieuws te noemen.
- **Een paar negatieve recensies helpen je geloofwaardigheid.** Een perfecte vijf sterren oogt vals.

**Reageren op recensies is een betrokkenheidssignaal, geen rankingfactor.** De ex-Googlers zien geen
reden waarom Google eigenaarsreacties als rankingsignaal zou gebruiken.

### Namen van medewerkers

Google nam in de richtlijnen op dat recensenten geen specifieke medewerkers bij naam moeten noemen.
De ex-Googlers vermoeden bescherming van persoonsgegevens, zeker bij minderjarige medewerkers.

Hun advies is **branche-afhankelijk**: bij restaurants met jonge bediening beter niet; bij
servicebedrijven waar de kwaliteit van de monteur er echt toe doet — loodgieter, slotenmaker,
klimaattechniek — wel.

> Dit is een verandering in beleid, niet in handhaving.

---

## Wat derden bijdragen weegt zwaarder dan wat jij zegt

Het structurele principe achter het bedrijfsprofiel.

> Je bedrijfsomschrijving doet niets voor SEO. Wat de eigenaar aanlevert is minder waardevol, want
> het is wat de eigenaar wil dat je weet.

Diensten, productkenmerken en omschrijvingen zijn **steigerwerk**. Een menukaart is nuttig omdat
gasten er foto's van maken en het in recensies noemen — niet omdat de menukaart zelf het resultaat
aanjaagt.

**Rangorde van waarde volgens de ex-Googlers:** recensies eerst, daarna foto's, video's en lokale
posts.

**Foto's van klanten wegen zwaarder dan die van jezelf.** Beide zijn nuttig — eigen foto's zijn een
betrokkenheidssignaal, en betrokkenheid werkt als proxy voor datanauwkeurigheid — maar
gebruikersfoto's zijn validatie door een derde, en dat weegt in de AI-laag naar verwachting zwaarder.

**Q&A is dood.** Daar zou je geen tijd meer aan besteden; Google leidt die antwoorden inmiddels uit
recensies af.

**Lokale posts juist wél**, en dat is een omslag. Google investeert er weer in: inplannen, plaatsen
over meerdere vermeldingen, uitbreiding via de API. De redenering: Google heeft geen middelen over
voor dingen die er niet toe doen, dus die investering verraadt een plan — vermoedelijk om die data als
AI-signaal te gebruiken.

> Let op de release notes van de API. Functionaliteit landt daar eerder dan in de interface — het is
> een voorproefje van wat eraan komt.

---

## Citaties

⚠️ **Dit hoofdstuk corrigeert waarschijnlijk wat je elders leest, inclusief oudere lokale-SEO-adviezen.**

### Ze werken nauwelijks voor het lokale pakket

Sterling Sky bestelde **50 citaties in één keer** voor een tandarts en voor een klusbedrijf, in
gebieden waar ze verder niets deden zodat er niets anders meespeelde. Beide keren hetzelfde patroon:

- **Merkbare stijging in organische posities**
- **Geen enkel effect op de lokale-pakketposities**

Dat is opmerkelijk, want de term "citatie" is ooit juist bedacht voor het lokale algoritme. De waarde
zit niet in de vermelding van naam, adres en telefoonnummer — die informatie heeft Google allang —
maar in **de link**.

### Het echte probleem is indexering

Staat de pagina met jouw vermelding niet in Google's index, dan levert hij **niets** op.

| Test | Uitkomst |
|---|---|
| Tandarts, 50 citaties | Na een maand nog **2** in de index (eerst 26) |
| Klusbedrijf, 50 citaties | Na zes maanden nog **2** in de index |
| 15 tier-2-citaties | 4 geïndexeerd (26%); geforceerd indexeren bracht er 5 bij; **zes maanden later was er nog één over** |
| Meerlocatie-letselschadekantoor met een dure jaarabonnement, **516 citaties** | **16 in de index — 3%** |

Bij het geforceerde experiment kwamen de rankingwinsten terug én verdwenen ze weer, precies in de pas
met de indexering.

> Betaal je maandelijks voor citaties, dan betaal je mogelijk voor SEO die zichzelf ongedaan maakt.

### Hoe je bepaalt welke citaties er wél toe doen

1. **Doe een merkzoekopdracht** op Google en kijk wat er rankt. Voor een loodgieter zijn dat totaal
   andere sites dan voor een advocaat.
2. **Doe hetzelfde voor de best rankende concurrenten** in jouw branche, om te zien wat je mist.
3. Kijk naar de **top 10 tot 20 resultaten**.

Dat zijn je citaties. Alles wat daar niet in voorkomt is een tier-2-citatie: Brownbook, Merchant
Circle, Hotfrog, Manta, Cityfinder en dergelijke. Buiten SEO-kringen praat niemand over die sites, en
dat is precies het punt.

**Er zijn wél branchespecifieke uitzonderingen.** Ben je weddingplanner, dan wil je op The Knot staan;
advocaten hebben hun eigen gezaghebbende juridische sites. Die zitten meestal **niet** in de goedkope
citatiepakketten, want daar moet je voor betalen.

**KPI:** verwacht bij generieke citaties dat je moeite hebt er meer dan **10 tot 20 in de index** te
houden. Controleer bij een verlenging welk percentage geïndexeerd is, en **controleer opnieuw na drie
tot zes maanden** — dat is de echte toets.

### Waarom Google die pagina's laat vallen

Vergelijk Citysearch met Yelp. Op Citysearch staan vermeldingen zonder activiteit, met recensies uit
2010. Op Yelp voegen gebruikers foto's toe, staan openingstijden ingevuld en komen er recente,
gedetailleerde recensies bij. Bij gelijke informatie houdt Google de versie met **verse,
gebruikersgegenereerde content** en laat de rest vallen — indexeren kost tijd, geld en middelen.

Google beloont daarnaast sites waar mensen **actief naar zoeken**. Dat verklaart mede waarom Reddit
het zo goed doet: mensen zoeken er expliciet naar en klikken erop.

### Een verhuizing en achterstallige citaties

Vroeger was een verhuizing dodelijk vanwege de mismatch met al je citaties. Nu geldt: **werk bij wat
rankt op je merknaam**, en negeer de rest.

De praktijkcase: een klant nam een bedrijf over waarvan het telefoonnummer niet meeverhuisde, zodat
klanten via Google op een dood nummer uitkwamen. Dat is precies wanneer het de moeite waard is.

**Kom je niet in een vermelding omdat de inloggegevens weg zijn** — tip van Darren Shaw (Whitespark):

1. Maak eerst een **e-mailadres op het domein van dat bedrijf** aan. Dit is de kern: het bewijst dat
   je bij het bedrijf hoort en niet iemand bent die een vermelding probeert te kapen.
2. Mail de site vanaf dat adres, leg uit dat de aanmaker er niet meer werkt en vraag toegang.

Zonder domeinmail kun je het beter niet proberen — er is geen enkele manier waarop zij je band met het
bedrijf kunnen vaststellen.

### De spanning met wat de ex-Googlers zeggen

⚠️ Joel Headley verwacht dat citaties en externe recensiesites **belangrijker** worden in de AI-wereld,
omdat modellen die bronnen gebruiken om echte klantdata van ruis te onderscheiden — iets wat hij vijf
jaar geleden belachelijk zou hebben genoemd.

Dat botst niet frontaal met Joy's tests, maar wijst wel een andere kant op. Een verdedigbare lezing:
haar tests gaan over **generieke citatiepakketten die niet geïndexeerd blijven**, terwijl hij het
heeft over **sites die daadwerkelijk in AI-antwoorden opduiken**. Dat is dezelfde selectieregel: kijk
wat er rankt en wat geciteerd wordt, en negeer de rest. Zeg erbij dat dit een afweging is.

---

## Links

Sterling Sky's driejarige linkonderzoek. Joy Hawkins begon het omdat ze SEO's bleef vragen hoe ze de
impact van een link meten en nooit een concreet antwoord kreeg — niemand kon zeggen *"ik bouwde deze
link en deze pagina steeg"*. De testopzet: een verlaten site zonder enige SEO-historie, zodat er
niets anders meespeelde.

Ze heeft in dit onderzoek meerdere keren haar eigen standpunt omgedraaid. Die omkeringen staan hier
expliciet in, want ze zijn leerzamer dan de conclusies.

### Organisch veel, lokaal weinig

In de scherpste opzet: **één link** vanaf hun eigen site (domain rating 71, thematisch verwant) naar
die testsite.

- **Organisch: enorme sprong** — van vrijwel nergens naar de top drie.
- **Lokaal pakket: van 4 naar 3.** Eén positie.

Meerdere keren herhaald met hetzelfde beeld.

Eén positie in het lokale pakket kan wel degelijk het verschil maken — net binnen of net buiten de
drie. Maar het eerlijke voorbehoud dat Joy zelf maakt: **linkbuilding is duur en arbeidsintensief**,
en voor veel kleine bedrijven is er geen rendement als het doel alleen het lokale pakket is. Je moet
te veel volume maken voor te weinig beweging.

**Verdeel je budget naar waar je leads vandaan komen.** Een advocaat haalt veel leads uit organische
posities en moet links bouwen. Een verzekeringsagent haalt het leeuwendeel uit zijn bedrijfsprofiel —
daar is linkbuilding een inefficiënte manier om de kaartposities te bewegen.

### Vergeet domain authority

De metriek waar bijna iedereen op stuurt — en waarvoor mensen letterlijk meer betalen — deugt niet als
enige maat. DA en DR zijn grotendeels gebaseerd op **linkvolume**: 2.000 links leveren een hoge score
op, ongeacht of die links iets waard zijn.

Het patroon dat ze steeds ziet: een site met een hoge domain authority die na een algoritme-update
nergens meer rankt. Zo'n link levert niets op, hoe mooi de score ook is.

### De vier dingen die je wél controleert

Na drie jaar onderzoek, in deze volgorde:

1. **Staat de pagina waarop je link komt in Google's index?** Zo niet, dan is de link waardeloos.
2. **Is de link gevolgd of nofollow?** Gevolgde links doen meer — met een belangrijke uitzondering,
   zie [Nofollow-links](#nofollow-links-doen-wél-iets).
3. **Kun je de ankertekst bepalen?** Dat blijkt zwaarder te wegen dan verwacht.
4. **Hoe staat de site er als geheel voor?** De *organic pages*-metriek in Ahrefs: hoeveel pagina's
   van dat domein staan in de index. Eén pagina die al het verkeer trekt is veel slechter dan
   duizenden die het goed doen, want jouw link komt op zo'n gewone pagina te staan.

**Aanvullende rode vlag:** een site die volgestouwd is met advertenties, waar je de content nauwelijks
kunt lezen zonder pop-ups weg te klikken. Dat is precies het type site waar Google achteraan gaat.

### Indexering is de kern

Joy ziet linkbuildingrapporten van klanten waarin de gelinkte pagina's simpelweg niet geïndexeerd
zijn. Ze sprak een fulltime linkbuilder voor wie indexering **geen onderdeel van het proces** was:
link binnen is klaar.

**Waarom die pagina's uit de index vallen:** contentsites zetten nieuwe stukken vooraan; naarmate er
meer bijkomt, zakt jouw gastartikel steeds verder naar achteren. Dat is voor Google een signaal dat
het niet belangrijk is. Linkt niemand ernaar en praat niemand erover, dan komt daar nog een signaal
bij. Google indexeert niet alles — dat kost tijd, geld en middelen, en hij houdt liever wat hij nog
niet heeft.

**Controleer de trend in *organic pages*** voor je een link najaagt. Een vlakke lijn is prima, een
dalende niet. Let ook op de **duur van het patroon**: private blog networks zien er een tijd goed uit
tot een update toeslaat en hun organic pages instorten.

### Ankertekst weegt zwaarder dan de link zelf

De meest verrassende uitkomst van het hele onderzoek, en Joy noemt het zelf schokkend.

Ze bouwde een link met een ankertekst gericht op een specifiek zoekwoord: **positie omhoog**.
Vervolgens veranderde ze **alleen de ankertekst** naar een ander zoekwoord in hetzelfde vakgebied. De
link bleef bestaan.

> Ik verwachtte een kleine daling. Het ging van een klif af. Alle winst van die link verdween.

Ze kreeg wel winst op de nieuwe ankertekst, maar de oude ging volledig verloren.

**Dat maakt ankertekst mogelijk belangrijker dan de link zelf** — de link stond er nog, alleen het
zoekwoord was weg. En anders dan bij linkecho's is er **geen ankertekstecho**: Google onthoudt de
oude ankertekst niet.

Deze omkering was ook zichtbaar in het **lokale pakket**: link erbij → in de drie; ankertekst
gewijzigd → terug naar af.

⚠️ Dit is precies de tactiek waar Google achteraan gaat, juist omdat hij werkt. Doe het **niet op
schaal**.

### Nofollow-links doen wél iets

Nog een omkering. Het gangbare beeld is dat nofollow-links niets doen. Het concept komt van Kyle
Roof, en Sterling Sky heeft het meerdere keren gerepliceerd:

> Een nofollow-link geeft wél rankingwaarde door, mits hij staat op een pagina die op Google rankt en
> daar verkeer van krijgt.

Waarom SEO's dit misten: de meeste links die ze analyseren staan op pagina's die **helemaal geen
verkeer** krijgen. Een gastartikel op een willekeurige site is misschien geïndexeerd, maar trekt niets.
Dan geeft hij ook niets door — en de conclusie "nofollow doet niets" is dan een verkeerde generalisatie.

De onderbouwing sluit aan bij wat er over het algoritmelek is besproken: Google volgt waar mensen
klikken. Een pagina waar mensen op klikken en naartoe gaan krijgt autoriteit, en geeft die door aan
wat hij linkt — gevolgd of niet.

**Haar test:** een nofollow-link in een reactie op een oude, veel bezochte forumpagina, naar een
artikel op de site van Sterling Sky. De dag erna verscheen er in de zoekresultaten voor die ankertekst
een **YouTube-sectie die er niet was** — met de video van die pagina erin.

**Praktisch gevolg:** schrijf digitale PR niet af omdat grote publicaties hun links nofollow zetten.
Forbes rankt overal; zo'n link geeft je waarschijnlijk veel waarde.

### Gastartikelen: ze had ongelijk, en toen weer gelijk

Joy dacht dat gastartikelen spam waren en niet zouden werken. Ze huurde een bureau in dat "white hat"
gastartikelen beloofde en bestelde er zes, twee per maand.

**Ze werkten.** Vanaf de tweede maand zag ze stijgingen — op een testsite waar verder niets speelde.

**En daarna niet meer.** De winst hield geen stand naarmate die pagina's uit de index verdwenen. Van
de zes links stond er een paar jaar later nog **één** in de index.

> Stel je een rij voor bij een nachtclub. Een deel komt binnen met een vals identiteitsbewijs. Het is
> een kwestie van tijd voor de uitsmijter doorheeft dat je er niet hoort en je weer op straat zet.

**De grote case:** een thuisdienstenbedrijf dat twee jaar lang door een ander bureau
gastartikelen liet bouwen — **425 links** in totaal. In Analytics was het patroon glashelder: het team
optimaliseerde een pagina, verkeer omhoog; het linkbureau bouwde één of twee links naar die pagina,
verkeer nog verder omhoog. Dat bevestigde opnieuw dat je de impact van een **enkele** link kunt meten.

Tot een core update. Daarna zakte het maandenlang door — al het betaalde werk maakte zichzelf ongedaan.
Van de onderzochte links stond **36%** niet meer in de index.

**Hoe je een gastartikelfabriek herkent:**

- Een **"artikel indienen"-knop** prominent op de homepage
- Bij "wie mag indienen": **iedereen**. Geen enkele echte uitgever laat willekeurige vreemden
  publiceren zonder redactie
- Opvallend veel bijdragen van **letselschadeadvocaten** — een branche die berucht is om deze tactiek,
  simpelweg omdat één zaak een heel SEO-budget terugverdient

### Wat te doen na een algoritme-update

Word je geraakt, controleer dan twee dingen aan je backlinkprofiel:

1. **Hoeveel van je links staan nog in de index?** (Er zijn bulk-indexcheckers voor.)
2. **Hoe doen de sites die naar je linken het zelf?** Zakken die weg, dan zakt jouw waarde mee. Je zit
   aan ze vast.

### Wanneer links giftig worden

Het patroon bij sites die na een core update instorten:

- Alle wegzakkende pagina's hadden **veel backlinks met zoekwoordrijke ankerteksten**
- De links waren **niet nieuw** — vaak vijf jaar oud
- De **verwijzende domeinen zakten zelf ook weg**
- Rode vlag: **verwijzende domeinen omhoog terwijl organisch verkeer omlaag gaat**

Google draait dan niet alleen de eerdere winst terug maar lijkt het als **negatief signaal** te
behandelen: nieuwe pagina's zónder links presteerden beter dan de pagina's mét.

Het meest verontrustende geval: een thuisdienstenbedrijf met tientallen zulke links van andere kleine
bedrijven in dezelfde branche — deels directe concurrenten. Ze wisten er niets van en hadden nooit
een SEO-bureau ingehuurd.

### De ene handmatige maatregel die ze in jaren zag

Handmatige maatregelen voor links zijn zeldzaam. Joy vroeg publiekelijk of iemand er recent een had
gezien en kreeg vrijwel geen reacties. Daarna deelde Google er in korte tijd een reeks uit, rond de
core update van maart.

Het geval dat zij analyseerde: een klein thuisdienstenbedrijf dat een **bekend, veelgebruikt
linkbureau** had ingehuurd.

**Wat ze deden:**

- Van **0 naar ongeveer 87 tot 100 verwijzende domeinen** in zeer korte tijd — voor een lokaal
  thuisdienstenbedrijf een volstrekt onnatuurlijk patroon
- Gastartikelen waarin **hetzelfde stuk telkens licht herschreven** werd, vermoedelijk via AI, en in
  sommige gevallen **letterlijk woord voor woord** op tientallen sites geplaatst
- Sites vol advertenties, waar de content nauwelijks leesbaar was
- Auteurs die op dezelfde sites ook over **gokken en cryptocurrency** publiceerden
- Verwijzende domeinen omhoog terwijl het organische verkeer van die sites omlaag ging

**En het werkte** — hun posities en verkeer stegen aantoonbaar. Daarom deden ze het.

**Drie dingen die tegen de intuïtie ingaan:**

1. **De maatregel had niet meteen effect.** Ze kregen hem in maart; posities en verkeer bleven
   gewoon staan. De klap kwam pas twee maanden later met de spamupdate van juni. Dat is anders dan de
   Penguin-tijd, toen het onmiddellijk was.
2. **Ze herstelden weer**, bij de update van augustus. Een handmatige maatregel is niet de doodsteek
   die mensen ervan maken.
3. **De reputatie van je linkbureau zegt niets.** Dit was een bekende partij die iedereen gebruikt.
   Controleer wat ze feitelijk doen.

**Actiepunt bij een handmatige maatregel:** stop met wat je deed, evalueer je strategie, en dien een
disavow in.

### Wat "links kopen" eigenlijk betekent

Joy's standpunt hierover is de afgelopen jaren verschoven, en het is een nuttige nuance tegen
morele paniek.

> Betaal je een bureau om links te bouwen, dan koop je links. Sponsor je een jeugdteam dat je een
> link geeft, dan koop je een link. Betaal je voor gastartikelen of citaties, dan koop je links.

Ze vindt het niet verkeerd om **een publicatie een vergoeding te betalen** die de werkelijke kosten
dekt van het plaatsen van een artikel. Waar de grens ligt is een grijs gebied waarover mensen van
mening verschillen.

Belangrijker is haar observatie over wat Google aanpakt:

> Google gaat achter precies die dingen aan die werken — gevolgde links meer dan nofollow,
> zoekwoordrijke ankertekst meer dan een link naar je homepage. Juist omdat ze werken.

En Google's eigen richtlijn zegt dat je geen links mag bouwen om posities te beïnvloeden, wat
feitelijk alle SEO uitsluit. Dat is niet werkbaar; wat je wél doet is kiezen voor wat het minste
risico oplevert.

### Scale is de scheidslijn

Dit is het terugkerende thema in het hele linkonderzoek, en het geldt evengoed voor ankertekst,
gastartikelen, servicegebiedpagina's en AI-content.

Twee mogelijke aanpakken:

| | Op schaal | Methodisch |
|---|---|---|
| Methode | Veel links, goedkoop ingekocht, kijken wat blijft plakken | Zeer kleine lijst sites die aan alle criteria voldoen, één tot twee links per site |
| Werkt het? | Ja, aantoonbaar | Ja, meetbaar per link |
| Houdbaarheid | Maakt zichzelf ongedaan bij de volgende core update | Blijft staan |
| Detecteerbaarheid | Patronen zijn triviaal voor Google te herkennen | Nauwelijks een patroon |

> Ik wil geen strategieën voor klanten die zichzelf over een paar maanden ongedaan maken bij de
> volgende core update.

### Linkecho's

Rand Fishkin beschreef in 2014 "link echoes" of "link ghosts": links weghalen deed de gewonnen
posities niet verdwijnen. Er was daarna niets recents over te vinden, dus Sterling Sky toetste het.

Een site waar klanten gastartikelen op hadden staan werd door een update geraakt, waarna die artikelen
uit de index vielen — functioneel hetzelfde als verwijderd. De rankingwinst **bleef staan**:

| Klant | Effect van één link | Na deïndexering |
|---|---|---|
| Orthodontist | 5 → 3, verkeer op dat zoekwoord **verdubbeld** over drie maanden | Behouden |
| Tandarts | 4 → 2 | Behouden |
| Echtscheidingsadvocaat | 3 → 1 | Behouden |

⚠️ **Maar dit geldt niet overal.** Bij **citaties** ziet ze juist wél een daling zodra ze
gedeïndexeerd raken; bij **gastartikelen** blijft de winst staan. Dezelfde regel geldt dus niet voor
elk type link.

**Joy's theorie waarom sommigen het houden en anderen niet:** verdien je de positie en heb je een
gezonde doorklikratio, dan houd je hem. Ben je met een link boven een partij gekomen waar je
eigenlijk niet boven hoort — haar voorbeeld is Reddit — dan houd je hem niet.

Hetzelfde echo-effect lijkt te spelen bij het **lokale algoritme**: een descriptor of categorie
toevoegen en later weghalen liet de gewonnen posities soms staan. Vermoedelijk moet iets een zekere
tijd bestaan voor Google het vasthoudt.

### Elke link heeft een houdbaarheidsdatum

Het onderbelichte deel van het echo-verhaal. De testlink vanaf Sterling Sky's eigen site hield de
site bijna een jaar hoog — en na **ongeveer acht maanden** begon hij te zakken.

> Verwacht niet dat je positie eeuwig blijft. Daarom moet je links blijven bouwen en aan je SEO
> blijven werken.

Praktisch: controleer dit soort dingen **herhaald over tijd**. Dat er in drie tot zes maanden niets
gebeurde, betekent niet dat er over acht maanden niets gebeurt.

### Classifiers

Sinds de helpful content update (2023) kan Google een **domeinbreed** label toepassen waardoor geen
enkele pagina nog rankt. Dit is **algoritmisch**: geen melding in Search Console.

Zolang die classifier er zit, verbetert **niets** wat je op de site doet je positie. Verwijdering
vraagt doorgaans een volgende core update én substantiële verbeteringen. Sites die in juni 2025
geraakt werden herstelden pas bij de december-update; van de in december geraakte sites herstelde er
bij de maart-update nog geen enkele. Reken op **meer dan één core update**.

De helpful content update raakte lokale SEO nauwelijks, en deze classifiers werken **alleen
organisch** door.

### De lawinetechniek

Herstelaanpak via Kyle Roof. Jaag niet meteen op de verloren zware termen. Ga eerst achter de
kleinere onderwerpen aan die je snel kunt domineren, en bouw laag voor laag autoriteit op.

Vruchtbaarste grond: zoekwoorden die al op **positie 2 tot 10** staan.

### Persberichten (herzien standpunt)

Jaren geleden getest, geen effect, afgeschreven. Opnieuw getest mét echte data en nieuwswaardige
cijfers:

- **Makelaar: +83% verkeer binnen 28 dagen**, plus stijging in het lokale pakket
- **Advocaat:** bescheiden maar gestage winst; eerst lokaal, weken later organisch
- **Hoveniersbedrijf:** lokaal omhoog, organisch nog meer — en het **AI-overzicht** voor hun
  belangrijkste zoekwoord ging **rechtstreeks uit het persbericht citeren**

Dat laatste is het interessantst: het gaat niet meer alleen om backlinks, maar om **de bron zijn die
Google's AI vertrouwt**.

⚠️ Bij een site die al door de augustus-spamupdate geraakt was (gekochte links van Fiverr) zakte juist
het zoekwoord uit de ankertekst van het persbericht weg bij de volgende core update. Op een belaste
site is dit geen veilige tactiek.

### Lokale sponsorlinks

Voor een winkelketen zochten ze lokale organisaties die op hun site naar sponsors linken, en regelden
links per vestiging. De locaties die zo'n backlink kregen gingen beter ranken.

Dit is ook het type link waar het echo-effect logisch voelt: je sponsort niet elk jaar opnieuw, en de
link blijft toch iets waard.


## Mythes, getest

| Mythe | Verdict |
|---|---|
| Title tags moeten onder de 60 tekens blijven | **Onwaar.** Titels boven de 200 tekens verbeterden posities. De waarschuwing komt van een tool, niet van Google of van data. |
| Een descriptor in je GBP-naam levert een schorsing op | **Zeer zeldzaam.** Het kán, maar in de praktijk is dit meer angst dan handhaving. Gebeurt het, laat dan een handelsnaam zien die met de naamsopmaak overeenkomt en je wordt hersteld. |
| Servicegebieden toevoegen beïnvloedt je lokale positie | **Onwaar.** Jarenlang gevolgd, nooit effect gezien. Het effect is vooral **visueel**: je krijgt een omtrek op de kaart. Het kan zelfs schaden — overlappende servicegebieden bij meerdere vestigingen leiden tot schorsingen. |
| Op "meer" klikken bij recensies verandert de volgorde | **Onwaar.** 135 mensen op dezelfde recensie: één positie, ongeveer een maand, daarna weg. |
| Backlinks naar je Google Bedrijfsprofiel verbeteren je positie | **Niet duurzaam.** In drie testopzetten aanvankelijk tijdelijke stijgingen, langetermijneffect nul — en kwalitatieve links naar een profiel zijn nauwelijks op te schalen. Steek je energie in links naar je **website**. |

### CTR-manipulatie

Rand Fishkin liet honderden mensen op een Vietnamees restaurant in Seattle klikken. Het schoot van
pagina twee naar positie twee. Sterling Sky volgde de posities daarna maandenlang: **de winst zakte
volledig weg**.

Twee redenen om het niet te doen:

1. **Je moet blijven betalen.** Zolang de manipulatie loopt blijven de posities; stopt de campagne,
   dan val je terug. Een bureau dat je zo laat ranken, laat je bij opzegging met lege handen achter.
2. **Het kan zich tegen je keren.** Volgens een bureau dat het wél doet, duwt Google een bedrijf naar
   pagina twee of drie zodra hij nepklikken vermoedt — en blijven die klikken dan komen, dan zakt de
   positie verder. Sterling Sky zag exact dat patroon bij hun testbedrijf: een scherpe duik die niet
   optrad bij andere bedrijven in dezelfde markt.

---

## Wat werkt op de website

### Servicegebiedpagina's

Werken, soms uitstekend — een advocaat die op Staten Island wilde ranken had baat bij een pagina
specifiek daarvoor. Een KNO-arts zag duidelijke winst in het gerichte gebied.

**Wat het verschil maakt is eigen data:** uitgevoerde klussen in die plaats, recensies van klanten
daar, prijzen, foto's, je team, en vermeldingen van herkenbare buurten en oriëntatiepunten. Dat
vertelt Google dat je die omgeving echt kent.

Een servicegebiedpagina is iets anders dan een locatiepagina: je hebt er geen adres en geen
bedrijfsprofiel, dus je moet op een andere manier laten zien dat je die plaats bedient.

⚠️ **Niet op schaal uitrollen.** Zie [AI-content op schaal](#ai-content-op-schaal-de-harde-uitkomst).

### Aparte pagina per intentie

Iemand van wie de cv-ketel om één uur 's nachts uitvalt zit in een andere modus dan iemand die
jaarlijks onderhoud zoekt.

### Woordenaantal loslaten

Een makelaar had twee pagina's over hetzelfde onderwerp; de langere verloor. Content weggehaald,
posities bleven. Er ranken pagina's op "alimentatiecalculator" met vrijwel geen tekst omdat er een
**werkende rekenmodule** staat.

> Google beloont geen lengte, Google beloont relevantie.

### Lange title tags

Sterling Sky negeert de 60-tekensregel bewust. Ze testten ook het omgekeerde — korter maken — en zagen
de posities dalen; teruggezet gingen ze weer omhoog.

Joel Headley testte dit rond 2020 op duizenden zorgsites door **buurtnamen** aan de titels toe te
voegen: **15% meer zichtbaarheid**, doordat de sites op meer zoekopdrachten gingen ranken.

Voorbeelden van Sterling Sky: een titel van **229 tekens** die het verkeer omhoog stuwde, en een
letselschadeadvocaat die met **232 tekens** van positie 6 naar 4 ging.

> Wees niet bang voor het beletselteken.

### Hoofdletters in de title tag

Opgemerkt bij Yelp en TripAdvisor, die woorden als "BEST" in hoofdletters zetten. Getest op een
kapperszaak: de positie bleef lager dan die van concurrenten, maar de **doorklikratio steeg**. Bij een
andere klant leverde de wissel van "top rated" naar "BEST" op vijf pagina's al 159 extra klikken op —
en die klant had duizenden van zulke pagina's.

Ondersteunend extern onderzoek: Semrush vond 7% betere prestaties met "BEST" in hoofdletters,
SearchPilot 14% meer mobiel verkeer.

### "Near me"-optimalisatie

Binnen het vak omstreden — een zaal op een vakevent was 50/50 verdeeld — maar hun data is consistent:
het werkt, en **uitsluitend organisch**. In het lokale pakket zitten de nabijheidssignalen al in het
algoritme; daar helpt dit niet.

Zet zinsdelen als "bij mij in de buurt", "bij jou in de buurt" en "in de omgeving" in je titels,
URL's, koppen en tekst. "Bij jou in de buurt" klinkt natuurlijker en Google leest het hetzelfde.

De BBB heeft een pagina die letterlijk op "loodgieters bij jou in de buurt" is gebouwd en die in
allerlei steden goed rankt; hun zichtbaarheid op dit type zoekopdracht loopt sinds ongeveer 2020
gestaag op.

Voorbeeld: een gloednieuwe pagina over botox voor een klant zonder eerdere content daarover rankte
binnen enkele maanden op "botox bij mij in de buurt". Bij een tandarts ging het verkeer op
near me-termen van niets naar substantieel.

Ze zien geen negatieve effecten op gebruikers: geen hogere bouncepercentages, geen lagere conversie.

### Interne links

Een van de snelste manieren om je lokale SEO te bewegen. Bij een advocatenwebsite leverde **één
enkele interne link** een directe stijging op.

De methode: link vanaf je **autoriteitspagina's** — de pagina's met veel organisch verkeer en veel
externe links — naar je **converterende pagina's**. Zo geef je door wat Google al belangrijk vindt, en
maak je duidelijk hoe je site in elkaar zit.

### Het navigatiemenu uitdunnen

Een volgepropt menu verwart Google en de klant. Je menu vertelt Google welke pagina's het belangrijkst
zijn; staat alles erin, dan zegt het niets. Zet er alleen de pagina's in die leads opleveren.

Resultaten: **+40%** verkeer naar de overgebleven pagina's bij één bedrijf, **+89%** bij een ander, en
na focus op de juiste pagina's **+25%** conversie.

### Bestaande content bijwerken

Behandel content als een levend document. **De publicatiedatum is een rankingfactor** — werk die mee
bij als je de inhoud vernieuwt. Een bijgewerkte blogpost voor een schilder ging van 4 naar 1.

Prioriteer: eerst de pagina's die leads genereren, daarna de pagina's die backlinks ontvangen.

### Vastgezet mobiel menu

Cijfers van Ross Hudgens: een sticky navigatiemenu geeft **+39% conversie**, **+12% paginabezoeken**
en **+11% gemiddelde sessieduur**.

### Contentideeën uit "Mensen vragen ook"

Scrape die sectie voor je branche en beantwoord precies die vragen.

Maar: **de gebruikelijke content gap-analyse is stuk.** De vraag is niet "wat ontbreekt bij mij", maar
**"waar zoeken mensen naar waar Google nog geen vijf miljoen kopieën van heeft"**.

---

## Afbeeldingen

Het onderwerp waar Sterling Sky zijn eigen aannames het vaakst heeft moeten bijstellen.

### Het beeldfilter

Google wil **geen 500 kopieën van dezelfde afbeelding**, net zomin als dezelfde tekst op vijf sites.
Dat werkt als een filter, vergelijkbaar met wat je elders in de zoekresultaten ziet.

De case: een tandarts kreeg veel afbeeldingsverkeer op een Invisalign-pagina, tot dat volledig
wegviel. Oorzaak: de gebruikte stockfoto was identiek aan die van concurrenten, en een van die
concurrenten nam de plek over.

Illustratief voorbeeld: zoek je op Joy Hawkins' naam, dan krijg je niet twintig keer dezelfde headshot
die ze overal gebruikt, maar één exemplaar plus andere foto's van haar door de jaren heen.

> Ben je de bron en heb je de meeste links, dan win je misschien. Ben je dat niet, dan sta je
> waarschijnlijk nergens.

### Relevantie verslaat "uniek"

De stinkdiercase: op een pagina over dieren die gaten in je gazon graven verving Joy een kleine,
korrelige foto door een **stockfoto van een stinkdier**. De positie zakte van 2 naar 3. Ze vroeg
alsnog een echte, grote foto bij de eigenaar op die het probleem zelf toonde — en de pagina pakte
positie **1**, die hij jaren later nog vasthoudt.

De les: haar aanname dat de kleine foto slecht was klopte, maar wat ze nodig had was een foto die
toonde **waar Google naar zocht**.

En het werkt beide kanten op. Bij een garagedeurenbedrijf verving ze een stockfoto door een echte
foto die niet precies het onderwerp toonde — waarna een concurrent met diezelfde stockfoto haar plek
innam. Stockfoto teruggezet, positie terug.

### De directe test: stock versus uniek

Vijf pagina's met stockfoto's, vervangen door unieke foto's, vier weken gevolgd, met bestandsnaam en
alt-tekst identiek gehouden.

**Uitkomst: vrijwel geen verschil.** Een paar pagina's zakten zelfs licht.

De conclusie die ze eruit trekken: het is niet stock-versus-uniek dat telt, maar of de afbeelding
**relevant en waarheidsgetrouw** is. Een plastisch chirurg gebruikt uiteraard nooit stockfoto's voor
voor-en-na-beelden. Hun eigen voorkeur gaat naar unieke foto's omdat die het merk versterken.

**De praktische regel:** kijk naar de afbeeldingen die nu voor jouw zoekterm ranken en lever iets dat
**daarop lijkt maar er geen kopie van is**.

### Welke afbeeldingen presteren

Uit een analyse van **383 pagina's** met afbeeldingsverkeer:

- **Infographics** krijgen de meeste klikken, en zijn het op één na meest gebruikte beeldtype op goed
  converterende pagina's
- **Afbeeldingen met mensen erop** converteren het best
- AI-afbeeldingen werkten aanvankelijk goed en stortten daarna in

Voorbeelden van infographics die werkten: een advocaat die per staat het aantal vuurwapendoden tegen
de wapenvriendelijkheid afzette, een elektricien over veiligheid op bouwplaatsen, een tandarts die
soorten tandbreuken met symptomen en behandelingen indeelde.

### Wanneer afbeeldingen er niet toe doen

Niet elke zoekopdracht weegt afbeeldingen mee. Kijk op de resultatenpagina of er een
**afbeeldingencarrousel**, een **lokaal pakket met afbeeldingen** of een **uitgelicht fragment met
afbeelding** staat. Zo niet, besteed er dan geen tijd aan.

### Logo's en de uitgelichte afbeelding

Uit hun tests: **een logo op je afbeeldingen maakt niets uit** voor posities of verkeer. Wat wél
telt is de **uitgelichte afbeelding** instellen — dat veld gebruikt Google vaak om te bepalen welke
foto naast je resultaat komt.

Vier regels daarvoor: maak hem **vierkant** (anders snijdt Google bij), gebruik **weinig tekst** en
houd die leesbaar, gebruik **geen stockfoto** (uit hun onderzoek naar Google-posts leveren die minder
klikken op), en overweeg **prijzen of kortingen** te tonen. In WordPress zetten Yoast en Rank Math de
benodigde schema-opmaak.

---

## Waar deze skill botst met `/seo`

**Dit is een echte tegenspraak. Kies bewust en zeg welke lijn je volgt.**

`/seo` (Nathan Gotch) leunt zwaar op AI-eerste versies: AI is goed in onderzoek, data-analyse en
eerste versies, en "de magie zit in het redigeren".

### Sterling Sky's parallelle test

Bij een **letselschadeadvocaat** draaiden ze AI-content en verhaal-gedreven content **tegelijk,
naast elkaar**:

- De AI-content deed **vrijwel niets**
- De verhaal-gedreven content gaf een forse stijging

| Klant | Wat ze toevoegden | Resultaat |
|---|---|---|
| Strafrechtadvocaat, DUI-termen | Een echte zaak — bewijs onjuist verzameld, zaak geseponeerd — in plaats van uitleg over de wetgeving | Sprong in het lokale pakket |
| Tandarts | Een echt verhaal van een behandeling | **+50% conversie** |
| Schilder | Foto's, de werkelijke kosten, de doorlooptijd | **+350% verkeer** |

### AI-content op schaal: de harde uitkomst

Een bedrijf wilde per se **200 tot 300 AI-servicegebiedpagina's** in één keer publiceren voor alle
plaatsen in hun staat.

**Er gebeurde niets.** Geen piek in Search Console. De reden: **de meeste pagina's kwamen niet eens in
de index**. De enige metriek die steeg was het aantal niet-geïndexeerde pagina's.

> Google strafte deze pagina's niet. Google indexeerde ze niet. "Deze content is niet uniek, hier
> hebben we al 5.000 kopieën van — waarom zouden we er middelen aan besteden?"

Dat is een belangrijke nuance: het gaat niet om een straf op AI-content, maar om de **indexeringsdrempel**.
Om geïndexeerd te worden moet iets voldoende anders zijn.

En het kan erger. Een bedrijf dat dit met **3.000 pagina's** deed kreeg wél een handmatige maatregel.

⚠️ Joy zegt er eerlijk bij dat ze AI **wel** nuttig vindt voor servicegebiedpagina's — de content
daarop lijkt nu eenmaal op elkaar. Haar bezwaar richt zich op **schaal**, niet op AI als zodanig.

### Forums stijgen — het spiegelbeeld

In dezelfde periode zag Sterling Sky forums de zoekresultaten overnemen in branches waar hun klanten
concurreren: advocaten, tandartsen, thuisdiensten. Hun eigen Local Search Forum zag het verkeer met
**144%** stijgen. Forums ranken ook hoog op merknamen — soms met een negatieve thread die je merk
schaadt.

Hun duiding: forums zijn zowat de meest **door mensen gemodereerde** content op internet, met
moderators die geen spam en promotie tolereren.

> In een wereld vol gefabriceerde reacties en valse recensies zijn forums een van de weinige plekken
> met eerlijk, verkoopvrij advies.

Ross Simmonds, in gesprek bij Sterling Sky, komt strategisch op hetzelfde uit:

> Ik vind het goed dat marketeers weer marketing moeten doen. Laten we teruggaan naar de basis. Begrijp
> je publiek. Maak goede verhalen. Maak content die niet bedoeld is om te ranken, maar om te beïnvloeden.

### Hoe je hiermee omgaat

Beide standpunten zijn onderbouwd, en ze sluiten elkaar niet volledig uit:

- Gotch test op **brede, informatieve SEO en AI-zichtbaarheid**, waar volume en dekking meetellen.
- Sterling Sky test op **lokale dienstverleners**, waar het onderscheidende juist zit in wat alleen
  dit bedrijf kan vertellen: deze zaak, deze klus, deze prijs, dit team.

Werkbare synthese, maar noem het als jouw afweging: gebruik AI voor onderzoek, structuur en dekking,
en laat het onderscheidende deel uit echte ervaring komen. Voor een lokaal dienstverlenend bedrijf is
dat laatste geen versiering maar de kern. En schaal is het echte gevaar — niet de tool.

Het bewijs is aan beide kanten deels anekdotisch. **Presenteer geen van beide als vaststaand.**

---

## Meten en gereedschap

### Meet het zoekresultaat, niet je rapport

De meest onderschatte tactiek volgens Sterling Sky. Andy Crestodina liet zien hoe Google eruitzag voor
het zoekwoord "buckets" in 2014 tegenover 2025: het best gerankte organische resultaat staat inmiddels
**8.500 pixels** van de bovenkant van de pagina. Die site verloor enorm veel verkeer terwijl de
rankingtracker meldde dat er niets veranderd was.

Gebruik een tracker die **schermafbeeldingen bewaart**, en kijk er ook echt naar.

### Search Console goed uitlezen

Wil je een daling helder zien, filter dan twee dingen weg:

1. **Al je merkgebonden verkeer**
2. **De URL die aan je Google Bedrijfsprofiel hangt**

Doe je dat niet, dan zie je de daling mogelijk helemaal niet.

Voor afbeeldingsverkeer: zet het zoektypefilter op **afbeelding**. Dat gedraagt zich als een aparte
zoekmachine met eigen data.

### Waarschuwingssignalen bij core updates

Vrijwel elke site die volledig onderuitging bij een update was **al eerder geraakt** door een
voorgaande update. Die eerdere klap is de waarschuwing.

### Gereedschap en waar het voor dient

| Gereedschap | Waarvoor |
|---|---|
| **Places Scout** | Rasterweergave van posities per stad; zien of er AI-lokale pakketten in je markt draaien en welke concurrenten daarin zitten, inclusief schermafbeeldingen; leadgeneratierapporten met de categorieën van best presterende bedrijven |
| **Local Falcon** | Trendanalyse; positieverschuiving per uur (openingstijden, filtering) |
| **BrightLocal** | Positiecontrole; doorhalingen als eerste indicatie van filtering |
| **Ahrefs** | *Organic pages*-trend van een domein vóór je een link najaagt of een citatie koopt |
| **Plepper** (Chrome) | Alle GBP-categorieën van concurrenten op Maps in één oogopslag; place ID opzoeken |
| **Wappalyzer** (Chrome) | De techniekstack achter een concurrentensite |
| **GS Location Changer** (Chrome) | Zoeken emuleren vanaf een andere locatie |
| **Advanced GSC Visualizer** (Chrome) | Search Console-data ontleden |
| **Google's verificatietool** | Verificatiestatus controleren en het verschil zien tussen vertraging en storing |
| **`business.google.com/add/info`** | Achterhalen welk e-mailadres een vermelding beheert |

---

## De richtlijnen in het kort

Google's *Guidelines for representing your business on Google* is het meest geraadpleegde artikel in
hun helpcentrum. **Lees het minstens één keer per jaar** — Google werkt het voortdurend bij.

- **Naam.** Moet je werkelijke naam weerspiegelen zoals je die consistent voert op je gevel, website,
  briefpapier en zoals klanten je kennen.
- **Adres.** Geen postbussen, geen adressen op afstand, geen virtuele kantoren. Toon je een adres, dan
  moet er **permanente gevelreclame** met je bedrijfsnaam zijn.
- **Servicegebiedbedrijven.** Eén profiel voor de centrale locatie, met een servicegebied ingesteld.
  Geen virtueel of postadres bij verificatie: het adres moet tijdens openingstijden bemand zijn. Heb
  je meerdere locaties met **eigen personeel en eigen servicegebieden**, dan mag je meerdere profielen
  hebben. Je servicegebied mag niet verder reiken dan ongeveer **twee uur reizen**.
- **Telefoon en website.** Liever een lokaal nummer dan een callcenter, en geen URL's of nummers die
  ergens anders heen doorschakelen.
- **Categorieën.** Vul de zin in: *"dit bedrijf **is** een ___"*, niet *"dit bedrijf **heeft** een
  ___"*. Een ijzerwarenwinkel kiest niet de categorie "hamer". Beschrijf je bedrijf als geheel, geen
  opsomming van diensten, producten of voorzieningen.
- **Ketens.** Houd naam en categorie consistent over alle vestigingen; binnen één land zouden ze
  dezelfde naam moeten hebben en één gedeelde categorie die het bedrijf het best beschrijft.
- **Afdelingen.** Publieksgerichte afdelingen (universiteiten, overheidsdiensten) mogen een eigen
  profiel als ze zelfstandig opereren, met een eigen ingang, telefoonnummer, categorie en
  openingstijden. Autodealers en zorgverleners hebben eigen richtlijnen.
- **Behandelaars.** Een individuele, publieksgerichte persoon met een eigen klantenkring — arts,
  tandarts, advocaat, makelaar. Hier mag je professionele titels in de naam zetten. Vraag jezelf af:
  moeten klanten mij rechtstreeks benaderen, en heb ik een publieksgerichte rol?
  ⚠️ Weeg dit tegen het [gewicht-effect](#het-filter-werkt-als-een-gewicht-niet-als-een-schakelaar):
  een behandelaarsvermelding die niets oplevert, schaadt.

> Dit zijn richtlijnen, geen wetten. Let vooral op wat Google **doet**, niet alleen op wat hij zegt.

### Kiosken op Google Maps

Een kiosk kan een eigen vermelding krijgen — Redbox was het eerste bekende voorbeeld, inmiddels doen
slotenmakers en verhuisbedrijven het ook. Voorwaarden:

1. **Een eigen telefoonnummer**, anders dan dat van de winkel waar de kiosk in staat.
2. **Openingstijden die kloppen** met wanneer de kiosk echt toegankelijk is. Zit hij binnen en gaan de
   deuren op slot, zet hem dan niet op 24 uur.
3. **Permanent**, niet tijdelijk of eenmalig.

Zonder personeel gelden er nog twee, die volgens Joy nergens gepubliceerd staan en uit hun ervaring
komen:

4. Een **winkelzoeker-pagina** op je site die elke kiosk met adres en telefoonnummer benoemt.
5. Een manier om **contact op te nemen bij storingen** — bijvoorbeeld een nummer op de machine zelf,
   niet op het scherm, want dat kan uit staan.

En: **één vermelding per locatie.** Twee vermeldingen op hetzelfde adres kunnen niet.

---

## Kleine ingrepen met verrassend effect

- **Een kapotte boekingslink repareren.** Bij een tandartspraktijk in de categorie *spoedeisende
  tandheelkunde* was het veld voor de afspraaklink niet bewerkbaar. Oplossing: primaire categorie
  tijdelijk omzetten naar *tandartspraktijk*, link aanpassen, categorie terugzetten — de nieuwe link
  bleef staan. Google support beval hetzelfde aan.
- **Telefoonnummeropmaak in AI-overzichten.** Een klant zag het nummer van een concurrent in het
  AI-overzicht staan. Het verschil: de concurrent zette het netnummer tussen haakjes en de klant niet.
  Haakjes toegevoegd, probleem verholpen.
- **Het woord "eerlijk"** toevoegen aan recensiepagina's gaf op elke pagina waar ze het deden meer
  klikken én een hogere doorklikratio. (Idee van Steve Toth.)
- **Reddit voor reputatie.** Een AMA-thread is het makkelijkst te laten ranken en je stuurt het
  verhaal. Optimaliseer daarnaast je testimonialpagina op "[merk] reviews".

---

## Werkwijze

1. **Bepaal welk scorebord stuk is.** Lokaal pakket, organisch, of allebei. Aparte algoritmes, aparte
   oorzaken — en een maatregel die het ene helpt kan het andere schaden.
2. **Zijn de kaartrankings weg? Loop eerst diagnose 1 na.** Meestal is het er één van, en dan is
   optimaliseren zonde van de tijd.
3. **Is je pin verplaatst, herstel dat dan nooit in je eigen dashboard.** Dit is de duurste fout uit
   deze skill.
4. **Sluit filtering uit** voor je iets anders doet — per zoekwoord, want het filter werkt op
   zoekwoordniveau. Tel daarbij je eigen extra vermeldingen mee als mogelijke oorzaak.
5. **Rankings goed maar leads omlaag? Kijk naar het zoekresultaat zelf**, niet naar je rapport.
6. **Zakt organisch terwijl lokaal goed staat?** Controleer eerst de landingspagina van je profiel —
   diversity update.
7. **Verschijnen recensies niet? Bepaal eerst welk van de drie mechanismen speelt** — filter,
   blokkade of categorie. Ze vragen totaal verschillende antwoorden, en bij een blokkade is het
   antwoord "wachten".
8. **Controleer de basis op het profiel** in deze volgorde: primaire categorie, secundaire
   categorieën, landingspagina-URL, openingstijden, zichtbaar adres, naam. Wijzigingen van minuten met
   effecten van tientallen posities.
9. **Zet recensies op frequentie, niet op volume.** Benchmark tegen de maandelijkse instroom van
   concurrenten, haal eerst de tien, stuur op recensies mét tekst — en repareer de **route** voor je
   er meer gaat vragen.
10. **Controleer bij elke citatie- of linkinvestering de indexering.** Dat is de enige maat die
    telt, en opnieuw na drie tot zes maanden.
11. **Breng je backlinkprofiel in kaart** voor je nieuwe links bouwt — ook links die je nooit zelf hebt
    aangevraagd.
12. **Laat het onderscheidende uit echte ervaring komen**: deze zaak, deze klus, deze prijs, dit team.
13. **Hertest wat je hebt afgeschreven.** SEO evolueert niet alleen, het cycleert. Persberichten en
    diensten in het profiel werkten niet, en werken nu wel.

---

## Wat snel veroudert

- **AI-lokale pakketten.** Bij opname alleen mobiel, alleen waargenomen in de VS, bij ongeveer **8%**
  van de gevolgde zoekwoorden — en groeiend.
- **Advertenties in het lokale pakket.** Van 1% naar 14% in één jaar. Ook de vormgeving kan Google
  terugdraaien.
- **De supportinrichting.** Callcenterlocaties, kwaliteitsverschillen per taal en de verstopte route
  naar handmatige verificatie komen van iemand die twee jaar geleden vertrok. De richting is duidelijk:
  steeds minder menselijke processen.
- **De bezwaarprocedure en de klok van 60 minuten.** Nieuw ten tijde van opname, en een procedure die
  Google eerder heeft gewijzigd.
- **Het seizoenspatroon van recensieverwijderingen** is een observatie uit hun tijd bij Google, geen
  gepubliceerd beleid.
- **Recensieblokkades.** Nieuw verschijnsel, waarvan de duur (zes tot acht maanden) op een beperkt
  aantal gevolgde gevallen berust. Het waarschuwingslabel bestond alleen in het VK; Google zou
  meldingen gaan sturen, maar die zagen ze nauwelijks.
- **Richtlijnen over namen van medewerkers in recensies.** Nieuw, met onbekende handhaving.
- **Herstelduur na een classifier.** Gebaseerd op drie core updates.
- **De grens van tien recensies** en **de bulkverificatielimiet van tien per week** zijn drempels in
  systemen die kunnen verschuiven.
- **Categorieblokkades op recensies.** Begonnen bij onderwijs in april 2025, zonder gepubliceerde lijst.
- **Indexeringspercentages van citatiesites.** Die dalen al jaren; de cijfers hier worden waarschijnlijk
  eerder slechter dan beter.

---

## Let op

- **De bewijskracht verschilt sterk per uitspraak.** Het "near me"-onderzoek (8.000 bedrijven, 200
  steden), de belknopdata (179 profielen) en de citatietests (516 citaties) staan op heel andere grond
  dan een enkele klantcase. Deze skill benoemt de steekproef waar die bekend is; neem dat onderscheid
  mee.
- **Correlatie is geen oorzaak.** Ze zeggen dat zelf bij het "near me"-onderzoek: lichte verbanden,
  geen garanties.
- **Denk niet in absoluten.** Het terugkerende advies van de ex-Googlers. Het systeem weegt signalen;
  er is geen drempel waarboven je gestraft wordt en waaronder je veilig bent. Advies in de vorm van
  "doe X nooit meer" is bijna altijd een verkeerde lezing van een gewogen signaal.
- **Sterling Sky spreekt zichzelf soms tegen, en dat is een kenmerk van testen.** Deze skill markeert
  waar dat gebeurt — de landingspagina vóór en ná de diversity update, citaties versus de verwachting
  van de ex-Googlers, linkecho's die bij gastartikelen wel en bij citaties niet optreden, stockfoto's
  die soms schaden en soms helpen. Presenteer die spanningen als spanningen, niet als één regel.
- **Sommige tactieken zitten in een grijs gebied.** Twee voorbeelden waarover ze het intern oneens
  waren:
  - Een letselschadeadvocaat deelde op een festival gratis fietshelmen uit en vroeg om recensies:
    **431 → 503 recensies** in een maand, daarna vijf maanden op nummer één in de hele stad. Die mensen
    namen de dienst nooit af, dus de recensies zijn vermoedelijk "niet ter zake". Google zei
    desgevraagd dat je dit niet moet doen. Ze presenteren dit expliciet als open vraag.
  - De kaartpin verplaatsen om aan het filter te ontkomen wordt binnen het vak betwist.
- **Sterling Sky is een bureau dat ook Google Ads beheert.** Relevant bij het advies om Ads te gaan
  draaien.
- **Bijna alles is Amerikaans.** Gemeentegrenzen, handelsnaamregistratie, callcenterrouting,
  brancheverdeling, de bezwaarprocedure. De mechanismen gelden breder, de uitvoering niet automatisch.
  Controleer voor Nederland en België.
- **Sponsorblokken en productplugs zijn weggelaten.** Waar een onderliggend principe los daarvan
  terugkwam, is het principe zonder het product opgenomen — zo staat de antwoordservice erin als middel
  om 24/7-openingstijden waar te maken, zonder de aanbieder die ze aanraden.
- **Wat hier niet in staat, stond niet in de bronnen.** Deze skill is gebouwd op 34 gelezen video's uit
  een corpus van 98. De ongelezen 64 zijn beoordeeld op titel en lengte; het gaat vooral om herhaling
  van geteste tactieken, brede SEO-gastinterviews en verkoop- en branchevideo's. Onderbelicht blijven:
  lokale SEO buiten de VS, e-commerce met lokale voorraad, meerlocatie-strategie voorbij
  bulkverificatie, en parasite SEO — dat laatste noemt Joy expliciet werkend, maar de onderbouwing zit
  in een video die hier niet gelezen is. Is een gebied hier te dun onderbouwd, zeg dat dan in plaats
  van het aan te vullen met aannames.
