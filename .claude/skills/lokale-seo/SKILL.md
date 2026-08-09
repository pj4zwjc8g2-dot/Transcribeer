---
name: lokale-seo
description: Lokale SEO, Google Bedrijfsprofiel en Google Maps volgens de werkwijze van Sterling Sky (Joy Hawkins). Gebruik deze skill bij vragen over het lokale pakket of de kaartresultaten, Google Bedrijfsprofiel of Google Business Profile, GBP, Google Maps-rankings, recensies die verdwijnen of niet gepubliceerd worden, geschorste of gefilterde vermeldingen, het lokale filter of possum-filter, servicegebiedbedrijven, "near me"-zoekopdrachten, vestigingen en meerdere locaties, lokale citaties, AI-lokale pakketten, of wanneer iemand zegt "mijn rankings op Maps zijn ineens weg", "mijn recensies verdwijnen", "mijn profiel is geschorst", "ik sta wel in de top 3 maar de telefoon gaat niet", of "/lokale-seo" typt.
---

# Lokale SEO: het lokale pakket en Google Bedrijfsprofiel

De werkwijze van **Sterling Sky** — het bureau van Joy Hawkins, gespecialiseerd in lokale SEO, met
eigen tests, klantcases en onderzoek op schaal. Gedistilleerd uit 24 recente video's (2025–2026),
inclusief gesprekken met twee ex-Googlers die elk ruim elf jaar aan Google Bedrijfsprofiel werkten
(Brad Weatherall, Joel Headley) en met recensie-specialist Claudia Tomina.

Zelfdragend: alles staat hier, er is geen externe kennismap nodig.

**Verhouding tot `/seo`:** die skill is strategisch en AI-eerst (Nathan Gotch). Deze is operationeel
en testgedreven. Ze spreken elkaar op één punt hard tegen — zie [Waar deze skill botst met
`/seo`](#waar-deze-skill-botst-met-seo). Strijk dat niet glad.

---

## Kernstelling: lokaal is een apart algoritme

Het lokale pakket draait op een **eigen algoritme**, los van het organische. Dat heeft twee gevolgen
die bijna alles in deze skill sturen:

- **Core updates raken de kaartresultaten meestal niet.** Lokaal heeft zijn eigen updates (openness,
  vicinity, possum, diversity).
- **Algoritmische straffen op links werken alleen organisch door.** Sterling Sky zag sites die ruim
  **90% van hun organische verkeer** verloren en wier lokale-pakketposities volledig ongemoeid bleven
  — bij één site schoten die zelfs omhoog terwijl het organische verkeer vlak sloeg.

Diagnose begint dus altijd met: **welk scorebord is stuk?** Organisch, lokaal pakket, of allebei.
Een probleem in het ene zegt weinig over het andere.

---

## Diagnose 1: de rankings op Maps zijn ineens weg

Loop deze vijf oorzaken in volgorde na vóór je iets optimaliseert. Meestal is het er één van.

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
- **Possum** — het lokale filter (zie diagnose 2).
- **Diversity update** — raakt ook organisch; hangt samen met de landingspagina van je profiel.

### 3. Google heeft zelf iets op je profiel gewijzigd

Naam, categorie of diensten. Zelfs kleine wijzigingen kunnen je rankings onderuithalen. Edits komen
uit vier bronnen:

1. Je eigen website en sociale profielen
2. Externe apps waaraan je koppelingsrechten hebt gegeven
3. Andere eigenaren en beheerders van de vermelding
4. **Voorstellen van willekeurige gebruikers** — iedereen op Maps kan een wijziging voorstellen, en
   Google publiceert foute informatie soms automatisch

Daarom: controleer je profiel structureel, niet alleen als er iets misgaat.

### 4. De landingspagina van je profiel is gewijzigd

De URL die aan je vermelding hangt weegt zwaar. Wordt die van je *busongevallen*-pagina naar je
homepage gezet, dan stort je relevantie voor busongeval-termen in. Dit kan ook de diversity update
triggeren, die organisch doorwerkt.

### 5. Je kaartpin ligt buiten de gemeentegrens

**Google rankt op de plaatsing van de pin, niet op je postadres.** Ligt de pin net buiten de grens
die Google voor die plaats hanteert, dan word je aan een andere plaats toegewezen: je scoort dan op
díe plaatsnaam en nauwelijks op je eigen.

### Plus: de Kansas-bug

Soms is er niets veranderd — geen edits, geen verhuizing, geen update — en raakt Google de
locatiedata van je vermelding gewoon kwijt. Het bedrijf rankt dan in Kansas in plaats van in de eigen
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
zijn op de andere. Zelfde vermelding, zelfde locatie, totaal andere uitkomst. Dit is het detail dat
de meeste mensen missen.

### Vaststellen dat je gefilterd wordt

Kijk naar **patronen**, niet naar posities. Sterling Sky gebruikt Places Scout, Local Falcon en
BrightLocal.

| Signaal | Zekerheid |
|---|---|
| BrightLocal toont een doorhaling (geen enkele ranking) | Aanwijzing, geen bewijs |
| Places Scout: groen raster over de hele markt, maar **rood precies op je eigen pin** | ~90% zeker |
| Local Falcon trendanalyse: je posities **wisselen** steeds met één andere vermelding | Sterke aanwijzing |
| Je posities naast die van een specifieke concurrent plotten en een **omgekeerd verband** zien — jij rankt waar zij niet ranken en andersom | 100%; dit wijst de dader aan |

### Oplossingen, in volgorde van ingrijpendheid

1. **Duplicaat laten verwijderen.** Bij een tapijtreiniger filterde een duplicaat mét slechtere
   recensies de goede vermelding weg. Google het duplicaat laten verwijderen; de goede nam meteen de
   plek in het lokale pakket over.
2. **Kaartpin verplaatsen** buiten de straal van 200 voet. Omstreden — hier wordt binnen het vak over
   gediscussieerd — maar bij één klant stegen de telefoontjes vanuit het bedrijfsprofiel met **400%**.
3. **Rebranden**, zodat het zoekwoord waarop je gefilterd wordt in je bedrijfsnaam komt (zie
   [Bedrijfsnaam](#bedrijfsnaam-de-legale-route) voor de legale route).
4. **Fysiek verhuizen** binnen dezelfde stad. Een strafrechtkantoor deed dit en herwon al zijn
   concurrerende posities.
5. **Wachten.** Bij een letselschadekantoor met een tweede vestiging duurde het ongeveer **acht
   maanden** voor de nieuwe locatie genoeg autoriteit had om niet meer gefilterd te worden.

**Wat níét werkte in hun test:** de vermelding "gevestigd binnen een ander bedrijf" weghalen. Ze
vermoedden dat dit het filter triggerde; verwijderen deed helemaal niets.

**Let op bij een tweede vestiging.** Een advocaat in Houston opende een kantoor in Katy, Texas. Het
Houston-kantoor had zoveel prominentie en relevantie dat Google in Katy het kantoor op **26 mijl**
afstand bleef tonen in plaats van dat om de hoek — en de nieuwe vestiging wegfilterde.

---

## Diagnose 3: goede posities, maar de telefoon gaat niet

Dit is sinds 2025 een apart en veelvoorkomend probleem: de rankings staan als een huis, maar de leads
lopen terug. De oorzaak ligt niet in SEO.

Sterling Sky liet Jeepto data trekken uit **179 bedrijfsprofielen van 34 advocatenkantoren** in de
VS. Klikken-om-te-bellen daalt structureel over twee jaar — óók bij bedrijven die onverminderd goed
ranken in het lokale pakket.

Twee ontwikkelingen verklaren dat:

**1. Advertenties in het lokale pakket.** Begin 2025 verscheen dit advertentietype in 1% van hun
mobiele rankingrapporten. In november 2025 was dat **14%**. Google haalde tegelijk de belknop weg bij
de gewone vermeldingen in het lokale pakket en verving die door afbeeldingen, terwijl de belknop in
de betaalde plaatsing juist fors werd vergroot. De belangrijkste actie zit daarmee achter een
advertentie.

> Consumenten stopten niet met bellen. Google verplaatste de knop.

**2. AI-lokale pakketten.** Deze komen niet naast het lokale pakket, ze **vervangen** het.

- Ze tonen doorgaans **twee** bedrijven in plaats van drie
- Er zijn **geen belknoppen**
- Ze tonen vaak **andere** bedrijven dan het traditionele pakket
- De meeste rankingtrackers meten ze nog niet — je rapport ziet er gezond uit terwijl je zichtbaarheid
  verdampt

In hun meting brachten AI-lokale pakketten **5.943** unieke bedrijven naar boven tegenover **18.330**
in traditionele pakketten: ongeveer **32%**. In 322 onderzochte markten hadden er **88%** minder unieke
bedrijven in het AI-pakket.

**Wat Sterling Sky adviseert:** meer locaties openen (één profiel is te kwetsbaar), en Google Ads
draaien in alle formats. Hun eigen klanten haalden eind 2025 een betere ROI uit Google Ads dan
daarvoor — niet omdat de advertenties goedkoper werden, maar omdat de plaatsing beter werd en de
organische vermeldingen functionaliteit verloren. Daarnaast: autoriteit opbouwen op platforms als
YouTube en Reddit, als een van de weinige verdedigbare strategieën.

> Dit is niet het einde van SEO, maar wel het einde van doen alsof organische zichtbaarheid alleen
> genoeg is.

⚠️ Dit advies loopt richting "koop advertenties". Het komt van een SEO-bureau dat ook Ads beheert.
De onderliggende data (belknop verplaatst, AI-pakketten tonen minder bedrijven) is controleerbaar en
staat los van dat belang; de conclusie is hun afweging, niet een natuurwet. Zie ook
[Wat snel veroudert](#wat-snel-veroudert) — dit is het meest tijdgebonden onderdeel van deze skill.

---

## Rankingfactoren in het lokale pakket

Uit een onderzoek van Sterling Sky met Places Scout: **ruim 8.000 bedrijven, 200 steden**, van grote
steden tot plaatsen met 50.000 inwoners, gericht op "near me"-zoekopdrachten. Het gaat om
**correlaties**, niet om gegarandeerde oorzaken; geen enkele factor koopt je de eerste plek.

### Een zichtbaar adres (tegen Google's eigen advies in)

Servicegebiedbedrijven zonder zichtbaar adres ranken **slechter** — een negatief verband. Google
adviseert zelf je adres te verbergen als je geen fysieke bezoeklocatie hebt.

Ze testten het bij een klant in de thuisdiensten: adres verborgen → rankings stortten in; een maand
later het adres teruggezet → rankings volledig hersteld. Herhaald op een tweede vermelding van
hetzelfde bedrijf, met dezelfde uitkomst.

Praktisch gevolg: **een kantoor met zichtbare pin is een rankingfactor**, en kan de investering waard
zijn.

### Primaire categorie

Volgens het lokale-rankingfactorenonderzoek de **belangrijkste** factor. Eén klant in de
klimaattechniek zag zijn primaire categorie veranderen van *airconditioningreparatieservice* naar
*airconditioninginstallateur* en zakte **van positie 1 naar 31**.

Kies niet op gevoel: kijk welke categorieën de best presterende bedrijven in jouw markt gebruiken en
sluit daarop aan. De Plepper-extensie voor Chrome toont in één oogopslag alle categorieën van je
concurrenten op Maps.

### Bedrijfsnaam: de legale route

Zoekwoorden in de bedrijfsnaam zijn volgens hetzelfde onderzoek de **op één na belangrijkste** factor
in het lokale pakket. Een makelaar die strategisch rebrandde kwam in de top drie voor zijn
belangrijkste zoekwoord — in een straal van **80 kilometer**.

Zomaar zoekwoorden in je naam proppen is in strijd met de richtlijnen en kan averechts werken. De
legale route: **registreer een handelsnaam** (in de VS een DBA) bij je gemeente of provincie. Zolang
die authentiek is, consistent wordt doorgevoerd in je hele online aanwezigheid en ook echt in je
marketing wordt gebruikt, accepteert Google hem.

> ⚠️ **Voor Nederland en België:** DBA is een Amerikaanse constructie. Het onderliggende principe —
> een echt geregistreerde handelsnaam die je consequent voert — vertaalt naar een handelsnaam bij de
> KvK of de KBO. De transcripties gaan hier niet over; controleer dit lokaal voor je het adviseert.

### Openingstijden

Realtime rankingfactor: **ben je dicht, dan zak je**. Een advocaat en een psychiater zakten
consistent weg zodra ze gesloten waren; in het weekend stortten hun posities in. Local Falcon laat de
verschuiving per uur zien. 24-uursbedrijven hebben 's nachts een enorm voordeel omdat hun
concurrenten letterlijk verdwijnen.

Wie zich als 24/7 vermeldt hoeft niet 24/7 open te zijn — maar moet de telefoon wél kunnen opnemen.
Een antwoordservice buiten kantooruren maakt dit mogelijk. Resultaten uit hun tests:

- Hovenier naar 24/7: telefoontjes buiten kantooruren **+142%**, totaal aantal telefoontjes **+58%**
- Ander bedrijf: van **57 naar 119** nieuwe bellers in één maand
- Een audit waarin alleen de verkeerde openingstijden werden gecorrigeerd: aantal telefoontjes
  **verdubbeld in 30 dagen**

### Recensies

Meerdere afzonderlijke factoren, die je los moet sturen:

- **Gemiddelde score** — duidelijk verband met posities op "near me"-termen.
- **Frequentie verslaat volume.** Dit is de belangrijkste nuance. Een tandarts haalde 60 recensies in
  één maand en domineerde; daarna kwam er 18 dagen niets binnen en zakten ze hard weg, terwijl
  concurrenten 13 tot 45 per maand bleven binnenhalen. Het aantal recensies in de **afgelopen maand**
  correleert met betere posities.
- **De grens van 10.** Ontdekt door Joel Headley (oud-Google), opnieuw getest door Sterling Sky op
  acht elektricien-vermeldingen, half met 9 en half met 10 recensies, gemengd servicegebied en
  fysieke vestiging. Bij het passeren van de **tiende** recensie schoten de rankings omhoog. Van 10
  naar 11: geen merkbaar effect.
- **Recensies mét tekst wegen zwaarder** dan losse sterren. Een ster zonder tekst toont Google niet
  eens in de Maps-app, dus die eenzame 1-ster doet minder pijn dan je denkt. Tekst helpt Google
  begrijpen waar je bedrijf over gaat.

Benchmark op drie dingen tegelijk: hoeveel recensies krijgen concurrenten per maand, hoe verhoudt je
gemiddelde zich, en hoe verhoudt je totaal zich.

### Foto's

Hoe langer je geen nieuwe foto toevoegt, hoe slechter je posities op "near me"-termen. Ouder
onderzoek (BrightLocal, 2019) laat zien dat meer foto's leiden tot meer kliks, telefoontjes en
routeaanvragen.

Maar dit is **niet universeel**: in sommige branches zijn foto's kritiek voor rankings, in andere
zagen ze geen enkel effect. Een garagedeurenbedrijf hoeft niet dagelijks een nieuwe garagedeur te
uploaden.

### Betekenisvolle woorden op de landingspagina

Een hogere woordtelling **exclusief stopwoorden** correleert met betere posities in het lokale pakket.
Dit gaat niet over lengte of over zoekwoorden stapelen, maar over inhoudelijke substantie die Google
kan begrijpen. Places Scout signaleerde ditzelfde al in 2016.

### De landingspagina zelf

Link je bedrijfsprofiel naar de **meest relevante** pagina, niet standaard naar je homepage.

Een advocatenkantoor in New York had losse profielen per advocaat, allemaal op hetzelfde adres met
dezelfde categorie — en werd daarom weggefilterd. Ze koppelden één profiel aan de
*busongevallen*-pagina in plaats van de homepage: rankings omhoog. Bij een volgend profiel de
*fietsongevallen*-pagina: opnieuw omhoog.

Een klimaatbedrijf linkt naar de pagina over cv-reparatie, niet naar de homepage. De aanpassing kost
seconden.

### Diensten in het profiel

Getest in 2019 met weinig effect, opnieuw getest in 2022 met een **significant** effect — ook op zeer
specifieke diensten. De omvang verschilt per regio en per concurrentiedruk. Kost een paar minuten.

---

## Google Bedrijfsprofiel: hoe het systeem vanbinnen werkt

Dit deel komt van twee ex-Googlers die elk ruim elf jaar aan het product werkten. Het verklaart
gedrag dat van buitenaf willekeurig lijkt.

### Google is geen "Google"

Het team dat het beleid schrijft, het team dat de QR-code bouwde en het team dat recensies verwijdert
zijn **verschillende teams**. Ze werken langs elkaar heen. Daarom kan Google je iets aanraden dat een
ander onderdeel van Google bestraft.

> Dat is niet omdat Google je wil pakken. Het is een groot bedrijf met veel mensen die verschillende
> dingen doen.

De richtlijnen zijn bovendien **bewust vaag gehouden**, zodat Google de ruimte houdt zelf te bepalen
hoe hij ze toepast. Wat de richtlijn zegt en wat er gehandhaafd wordt zijn twee vragen. Intern viel
regelmatig het antwoord "dit is een business decision": geen schending van het Google-brede beleid,
maar de productmanager beslist.

### Er is geen algoritme, er zijn scripts

Voor spam- en recensiedetectie schrijft het trust-and-safety-team scripts die kenmerken van bekende
spamvoorbeelden targeten. Ze meten die af op een steekproef: *"ik haal 80% van mijn doelwit neer, en
20% dat er niet bij hoort — win ik hier?"* Bij 80/20 vinden ze dat prima. In de praktijk sturen ze
richting 90/10.

**Bij 100 miljoen bedrijven is 10% nevenschade nog altijd 10 miljoen bedrijven.** Als jouw legitieme
recensies verdwijnen, ben je meestal geen doelwit maar nevenschade.

### De cyclus van recensieverwijderingen

Het is **seizoensgebonden**. Rond maart–april wordt het detectiealgoritme aangescherpt en volgt een
golf verwijderde legitieme recensies; na klachten wordt het weer wat teruggedraaid en komt een deel
terug. In het vierde kwartaal gebeurt dit niet: Google gaat rond de feestdagen in code freeze, zowel
om bedrijven niet te raken als omdat de engineers vrij zijn.

**Verwacht niet dat alles terugkomt.** Verlies je er tien, dan is zes tot acht terugkrijgen een
realistische verwachting.

### Google verwijdert content niet echt

Alleen de **maker** kan content echt verwijderen. Verwijdert Google een recensie, dan wordt die
verborgen voor het publiek maar blijft hij bestaan — de spammer ziet zijn eigen recensie gewoon
staan, wat hem geen signaal geeft dat hij gepakt is. De recensie hoort bovendien technisch bij het
**account van de schrijver**, niet bij het bedrijfsprofiel; bij verwijdering wordt alleen de koppeling
verbroken.

Twee praktische gevolgen:

- Herstel gebeurt door **herverwerking**, niet door terugzetten. Daarom komen recensies soms vanzelf
  terug bij een volgende algoritmeronde.
- Een supportmedewerker die zegt *"ik kan ze niet vinden"* heeft half gelijk (de koppeling is weg) en
  is half lui (hij kán ze vinden). **Kom met bewijs**: een export of back-up van de verdwenen
  recensies haalt dat antwoord van tafel. Sommige GBP-beheersoftware maakt daar back-ups van.
- ⚠️ Sinds ongeveer 2020 is Google veel kostenbewuster geworden en is hij wél gaan opschonen — onder
  meer vermeldingen waar jarenlang niets mee gebeurde. Het oude "Google gooit nooit iets weg" gaat
  daarmee minder onvoorwaardelijk op.

### Vertrouwensscore

Zowel gebruikers als bedrijven hebben een vertrouwensscore. Elke geaccepteerde bijdrage aan de kaart
telt positief; een voorstel dat wordt afgewezen of later teruggedraaid telt negatief. Denk aan
kaarten tellen: plus één, min één.

Gevolgen:

- Een **vers Gmail-account** dat één recensie meldt is een lege stem. Een account met historie en
  positieve bijdragen weegt zwaar. Een google.com-adres liet een recensie binnen een uur of twee
  verdwijnen.
- **Meldingen met meerdere mensen werken**, maar niet omdat Google stemmen telt. Twintig mensen die
  melden maken **twintig aparte tickets**, en daarmee twintig kansen dat een beoordelaar hem
  weghaalt. Je benut de foutmarge van een handmatig team — niet een democratisch signaal.
- Het snijdt aan twee kanten: wordt de recensie later teruggezet, dan kan dat je eigen
  vertrouwensscore schaden. Gebruik het niet kwaadwillend.
- Profielen die veel verwijderde recensies hebben gehad, krijgen een **lagere vertrouwensscore** —
  waarna ook echte recensies moeilijker blijven plakken. Dat is een vicieuze cirkel die lastig te
  doorbreken is.

### Support: niveaus en talen

- **Niveau 1 en 2** zitten samen op dezelfde locatie en overleggen via realtime chat. Om niveau 2
  vragen is zinnig: dat zijn de doorgegroeide, ervaren medewerkers. Het antwoord verandert er niet
  per se door, maar de beoordelaar is beter.
- **Niveau 3** is uitsluitend voor **bugs**, en zit in de VS. Een ontbrekende recensie, een schorsing
  of foute data is géén bug maar een datakwestie — daarmee kom je er niet.
- Zaken worden **per taal naar callcenters gerouteerd**. De kwaliteitsscores verschilden sterk: de
  Engelstalige, in India gevestigde ondersteuning scoorde het slechtst; wie in het Spaans belde kwam
  bij Buenos Aires uit, met aanzienlijk hogere kwaliteitsscores. Bij schorsingsachterstanden gelden
  bovendien **aparte wachtrijen per taal**, en minder gangbare talen hebben kortere wachtrijen.
- Er wordt vrijwel niets meer handmatig beoordeeld. Uitzonderingen zijn **on-demand
  videoverificatie** en **handmatige verificatie**. Die laatste is een bewust verstopte noodklep: je
  moet **eerst videoverificatie proberen en laten mislukken**, waarna in de database een vlag wordt
  gezet. Doorloop daarna opnieuw de supportflow; waar eerst *"feedback verzenden"* stond, staat nu
  *"neem contact op"* — een klein blauw tekstlinkje dat leidt naar een formulier waarin je bewijs kunt
  uploaden. Dat gaat naar een mens.
- Het forum voor productexperts is voor dít doel veel minder effectief geworden, om dezelfde reden:
  de handmatige beoordelingen erachter zijn grotendeels weg.

### Eigendom en beheer

- **Zet het bedrijfsdomein als hoofdeigenaar, geen Gmail.** Een domeinaccount erft de autoriteit van
  het domein en biedt herstelmogelijkheden; raakt een Gmail-account geschorst, dan is herstel zwaar.
  Nuance: een Gmail met vijftien jaar historie verslaat een gisteren aangemaakt domeinaccount. Bouw
  de autoriteit op het domein op, die haalt de Gmail uiteindelijk in.
- **Drie personen op een profiel**: één hoofdeigenaar, nog een eigenaar en een beheerder. Met één
  account ben je kwetsbaar als dat account iets overkomt; met vijftien beheerders kan elk van die
  vijftien je schade berokkenen.

---

## Schorsingen

### Risicogroepen

Google let extra scherp op de **dwangsectoren** — branches waarin de klant onder druk beslist:
slotenmakers, garagedeuren, loodgieters, sleepdiensten. Daar zit de meeste fraude, dus daar wordt het
strengst gehandhaafd.

Restaurants worden vrijwel nooit geschorst, om een leerzame reden: **het is makkelijk te bewijzen dat
ze echt zijn.** Echte locatie, echte gevelreclame, alles klopt. Bij een servicegebiedbedrijf zonder
zichtbare vestiging is dat veel lastiger — en een virtueel kantoor huren kan iedereen.

**Truc om te achterhalen of jouw categorie als risicogroep geldt:** probeer een wijziging voor te
stellen op een vermelding met die primaire categorie. Bij dwangcategorieën wordt dat automatisch
geweigerd — het lukt niet bij slotenmakers, garagedeurherstel of sleepdiensten.

### Preventie

De rode draad van beide ex-Googlers: **denk als een spammer en doe dat niet.**

> Herken wat gebruikers willen en lever dat, in plaats van te proberen iets te forceren.

- Verander je adres niet om je pin gunstiger te laten vallen
- Wijzig je categorie niet naar iets dat hiërarchisch nergens op slaat
- Verander je naam niet vijf keer in een maand — dat is een sneltrein naar een schorsing
- Herhaald "testen" met naam en categorie is precies het patroon dat gedetecteerd wordt
- Geen virtueel adres, geen zoekwoorden stapelen, geen doorverwijzingen, geen overlappende
  servicegebieden met je eigen andere vermeldingen

**Wees proactief met bewijs.** Draai je in een risicosector, zorg dan dat je uit het grijze gebied
blijft vóór er een golf komt: draag foto's van je locatie bij, blijf actief op je profiel, zorg dat
je gevelreclame overeenkomt met je profielnaam. Een keten met 4.000 vestigingen die overal dezelfde
beelden gebruikte: **lokaliseer je beeldmateriaal**, laat zien dat je in Tampa zit en niet in New
York.

### Herstel in zeven stappen

1. **Bepaal het type.** Zacht = je profiel is nog zichtbaar, je kunt het alleen niet beheren. Hard =
   het is volledig van de kaart. Zoek je bedrijfsnaam op Maps om te zien welke je hebt. Bij een harde
   schorsing is haast geboden.
2. **Audit je profiel op rode vlaggen.** Klopt je adres exact met je inschrijving? Virtuele kantoren
   en veel wijzigingen in korte tijd zijn triggers. Ruim duplicaten op.
3. **Controleer de eigenaren en beheerders.** Is het Google-account van een van hen geschorst, dan
   trekt dat jouw vermelding mee. Verwijder die accounts vóór je bezwaar maakt.
4. **Verzamel bewijs dat je een echt bedrijf bent**: energierekeningen, belastingstukken, vergunningen,
   foto's en video's van je locatie. Ontbreekt gevelreclame, dan is die soms echt nodig — als Google
   op Street View alleen een woonhuis ziet, moet het vertrouwenssignaal omhoog.
5. **Maak het profiel schoon**: geen zoekwoorden stapelen, geen doorverwijzingen, geen overlappende
   servicegebieden.
6. **Dien het bezwaar in met al het bewijs tegelijk.** Het bezwaarformulier is de enige route naar
   herstel; een half ingevuld bezwaar vertraagt alleen.
7. **Voorkom herhaling.** Wijzig je profiel langzaam, gebruik nooit een virtueel adres, en houd het
   aantal gebruikers beperkt.

**Maak geen nieuw profiel aan** en raak niet in paniek.

---

## Recensies: krijgen en behouden

### Waarom recensies niet gepubliceerd worden

Volgens Claudia Tomina is de belangrijkste oorzaak dat er **geen echte interactie was tussen de
recensent en het bedrijfsprofiel** voordat de recensie geschreven werd. Iemand die via een
doorverwijzing komt, jouw recensielink krijgt en direct schrijft, heeft nooit met je profiel
geïnterageerd — en dat is een vlag.

**Wat wel werkt:**

- Laat mensen het bedrijf **opzoeken op Google of Maps** (een merkzoekopdracht) en daarvandaan de
  recensie plaatsen. Merkzoekopdrachten blijven veel beter plakken.
- Deel **niet** de recensielink of QR-code die Google zelf in het dashboard aanbiedt — juist die
  vergroot de kans dat de recensie eruit gefilterd wordt. Stuur in plaats daarvan naar een
  zoekresultatenpagina met de merknaam erin.
- Laat iemand die al iets op het profiel heeft aangeklikt (bellen, route, boeken) de recensie
  achterlaten.

Waarom dit werkt volgens de ex-Googlers: het gaat niet om de omweg zelf, maar om **gedrag dat op een
mens lijkt**. Vergelijk het met reCAPTCHA, dat muisbewegingen en kliks meet in plaats van je antwoord.
Minder klikken en minder beweging vóór het tekstveld betekent minder signalen en dus minder
vertrouwen. Hoe meer echte interactie en historie, hoe waarschijnlijker Google de recensie vertrouwt.

**Gefilterde recensie terugkrijgen:** laat de schrijver hem **licht bewerken**, een paar woorden
veranderen. Dan blijft hij vaak wel staan. Twee verklaringen, die elkaar aanvullen: spammers komen
nooit terug om hun werk bij te schaven, dus bewerken is menselijk gedrag; en een bewerking triggert
**herverwerking** door een inmiddels mogelijk minder agressief algoritme.

Een bijvangst: recensiecampagnes leveren zichtbare rankingpieken op door de merkzoekopdrachten en
kliks die ze veroorzaken — maar die pieken zakken weer weg. Dat effect is niet blijvend.

### Snelheidslimieten

Recensies die veel te snel binnenkomen voor je branche worden gemarkeerd. Een dakdekker met **drie à
vier recensies per dag** is onrealistisch, en dan gaat er iets mis. Patroon dat ze vaker zien:
maandenlang groei, dan ineens alles verwijderd plus een label "recensiemanipulatie".

De nuance: is dit oprecht je nieuwe normaal, houd het dan vol zodat het je normaal wórdt. Is het een
campagne of manipulatie, dan werkt het tegen je. Wat je een jaar geleden nog kon maken, kan nu niet
meer.

Ook geclusterd gedrag valt op: mensen uit **hetzelfde huishouden** of met dezelfde achternaam die
tegelijk plaatsen komen er vaak niet door, en een groep die binnen enkele minuten allemaal negatief
plaatst kan als recensieaanval worden gelezen. Druppelen die dezelfde reviews over dagen binnen vanaf
verschillende accounts, dan blijven ze staan.

**Recensiefeestjes** (iedereen laten schrijven terwijl ze fysiek in de zaak zijn) waren ooit een
sterk echtheidssignaal, maar keren zich nu tegen bedrijven: de combinatie van tijdstip én locatie is
onderdeel van het detectiepatroon. Dat betekent níét dat ter plekke om recensies vragen slecht is —
in een gestaag tempo blijft het waardevol. Denk niet in absoluten; het algoritme doet dat ook niet.

**Gekochte recensies** hebben een risico dat verder gaat dan verlies van die recensies: het
vertrouwen van het profiel daalt, waarna ook echte klanten hun recensie niet meer gepubliceerd
krijgen.

### Namen van medewerkers

Google nam in de richtlijnen op dat recensenten geen specifieke medewerkers bij naam moeten noemen.
Dat raakt bedrijven die hun monteurs op die manier belonen. De ex-Googlers vermoeden dat het om
bescherming van persoonsgegevens gaat, zeker bij minderjarige medewerkers.

Hun advies is **branche-afhankelijk**: bij restaurants met jonge bediening beter niet; bij
servicebedrijven waar de kwaliteit van de monteur er echt toe doet — loodgieter, slotenmaker,
klimaattechniek — wel.

> Dit is een verandering in beleid, niet in handhaving. Wat de richtlijn zegt en wat er gehandhaafd
> wordt zijn twee verschillende vragen.

### Recensie-afpersing

Een netwerk van nepprofielen overspoelt één bedrijf met eensterrenrecensies, vaak met uitgeschreven
verhalen. In de profielfoto of bio staat een WhatsApp-nummer; neem je contact op, dan vragen ze geld
om ze weg te halen, of ze willen ingehuurd worden om positieve recensies te plaatsen. Herkenbaar aan
terugkerende schrijfstijlen en **hetzelfde WhatsApp-nummer** in de bio's.

Drie stappen, en snel:

1. **Meld elke recensie afzonderlijk** (drie puntjes → recensie melden → spam of niet ter zake). Laat
   zoveel mogelijk mensen dit doen — elke melding is een apart ticket.
2. **Meld elk profiel afzonderlijk.** Dit kan alleen in de Maps-app: tik op de naam van de recensent,
   open het profiel, drie puntjes, profiel melden.
3. **Meld het via het speciale formulier** dat Google hiervoor heeft gemaakt.

Bij elk bedrijf dat ze hiermee hielpen en alle drie de stappen doorliep, verdwenen de recensies.

### Reageren op negatieve recensies

Zeven principes, van Tommy Mello (A1 Garage Door) en Mike Blumenthal:

1. **Bel ze.** Laat de klant ook een leidinggevende spreken; zet daar mensen op die goed zijn in
   de-escaleren.
2. **Laat ze uitrazen.** Onderbreek niet. Ze willen gehoord worden.
3. **Verdedig jezelf niet.** Erken het deel dat klopt en ga door naar een oplossing.
4. **Schrijf de reactie niet zelf.** Je bent te betrokken; laat iemand neutraals het doen. De reactie
   is voor je toekomstige klanten, niet voor de recensent.
5. **Neem verantwoordelijkheid** voor het deel dat terecht is, ook als het verhaal onvolledig is.
6. **Beschrijf hoe je voorkomt dat het opnieuw gebeurt.** Een publieke excuses mét actie erachter.
7. **Bied aan het op te lossen.** Een kleine terugbetaling of korting kost minder dan de omzet die je
   verliest door de klacht te laten staan.

Waarschuwend voorbeeld: een ondernemer reageerde met *"we betreuren het dat u een beeld schetst dat
niet met de werkelijkheid overeenkomt"* en kreeg er acht eensterrenrecensies bij, waarschijnlijk van
vrienden en familie. Google verwijderde ze niet.

**Reageren op recensies is een betrokkenheidssignaal, geen rankingfactor.** De ex-Googlers zien geen
reden waarom Google eigenaarsreacties als rankingsignaal zou gebruiken.

---

## Wat derden bijdragen weegt zwaarder dan wat jij zegt

Dit is het structurele principe achter het bedrijfsprofiel, en het loopt door alles heen.

> Je bedrijfsomschrijving doet niets voor SEO. Wat de eigenaar aanlevert is minder waardevol, want
> het is wat de eigenaar wil dat je weet.

Diensten, productkenmerken en omschrijvingen zijn **steigerwerk**. Een menukaart is nuttig omdat
gasten er foto's van maken en het in recensies noemen — niet omdat de menukaart zelf het resultaat
aanjaagt. Investeer niet zwaar in het steigerwerk in de veronderstelling dat dáár het resultaat
vandaan komt.

**Rangorde van waarde volgens de ex-Googlers:** recensies eerst, daarna foto's, video's en lokale
posts.

**Foto's van klanten wegen zwaarder dan die van jezelf.** Beide zijn nuttig — eigen foto's zijn een
goed betrokkenheidssignaal en betrokkenheid werkt als proxy voor datanauwkeurigheid — maar
gebruikersfoto's zijn validatie door een derde partij, en dat weegt in de AI-laag naar verwachting
nog zwaarder.

**Lokale posts en Q&A.** Q&A is dood: daar zou je geen tijd meer aan besteden; Google leidt die
antwoorden inmiddels uit recensies af. Lokale posts juist wél, en dat is een omslag — Google
investeert er weer in (inplannen, plaatsen over meerdere vermeldingen, uitbreiding via de API). De
redenering: Google heeft geen middelen over voor dingen die er niet toe doen, dus die investering
verraadt een plan, vermoedelijk om die data als AI-signaal te gebruiken.

> Let op de release notes van de API. Functionaliteit landt daar eerder dan in de interface — het is
> een voorproefje van wat eraan komt.

**Citaties zijn terug.** Vermeldingen op externe sites en recensiesites werden vijf jaar lang als
achterhaald beschouwd. In de AI-wereld worden ze weer belangrijk, omdat modellen die bronnen
gebruiken om echte klantdata van ruis te onderscheiden. Kijk welke sites in AI-overzichten opduiken
voor jouw branche en plaats, en zorg dat je daar staat — het liefst met inhoud die niet van jezelf
komt.

---

## Wat werkt op de website

### Servicegebiedpagina's

Werken, soms uitstekend — een advocaat die op Staten Island wilde ranken had baat bij een pagina
specifiek daarvoor. Maar **niet op schaal uitrollen** voor elke plaatsnaam; dat faalt volledig.

Wat het verschil maakt is **eigen data**: echte resultaten, prijzen, foto's van uitgevoerde klussen,
je eigen team, echte casestudy's. Dat scheidt het van generieke pagina's.

### Aparte pagina per intentie

Iemand van wie de cv-ketel om één uur 's nachts uitvalt zit in een compleet andere modus dan iemand
die jaarlijks onderhoud zoekt. Dat scheelt voor zowel ranking als conversie.

### Woordenaantal loslaten

Een makelaar had twee pagina's over hetzelfde onderwerp; de langere verloor. Ze haalden content weg
uit de langere en verwachtten een daling — die kwam niet. Er ranken pagina's op "alimentatiecalculator"
met vrijwel geen tekst, omdat er een **werkende rekenmodule** staat.

> Google beloont geen lengte, Google beloont relevantie.

### Lange title tags

Sterling Sky negeert de 60-tekensregel bewust. Langere titels presteren consistent beter, tot **229
tekens** aan toe. Google kort in wat hij toont, maar leest de volledige tag.

Joel Headley (oud-Google) testte dit op duizenden mkb-sites door buurtnamen toe te voegen aan de
titels: **15% meer zichtbaarheid**, omdat de sites op meer zoekopdrachten gingen ranken.

> Wees niet bang voor het beletselteken.

### "Near me"-optimalisatie

Binnen het vak omstreden — bij een navraag op een vakevent was de zaal 50/50 verdeeld — maar hun data
is consistent: het werkt nog steeds, vooral **organisch**, minder in het lokale pakket. Zet zinsdelen
als "bij mij in de buurt", "bij jou in de buurt" en "in de omgeving" in je titels, koppen en tekst.
"Bij jou in de buurt" klinkt natuurlijker en Google leest het hetzelfde.

Voorbeeld: een gloednieuwe pagina over botox voor een klant zonder eerdere content daarover rankte
binnen enkele maanden op "botox bij mij in de buurt" en levert nu patiënten op.

### Het navigatiemenu uitdunnen

Een volgepropt menu verwart zowel Google als de klant. Je menu vertelt Google welke pagina's het
belangrijkst zijn; staat alles erin, dan zegt het niets. Zet er alleen de pagina's in die
daadwerkelijk leads opleveren.

Resultaten: bij één bedrijf **+40%** verkeer naar de overgebleven pagina's, bij een ander **+89%**, en
na focus op de juiste pagina's **+25%** conversie.

### Bestaande content bijwerken

Behandel content als een levend document. **De publicatiedatum is een rankingfactor** — werk die dus
mee bij als je de inhoud vernieuwt. Een bijgewerkte blogpost voor een schilder ging van positie 4
naar 1.

Prioriteer: eerst de pagina's die leads genereren, daarna de pagina's die backlinks ontvangen.

### Vastgezet mobiel menu

Cijfers van Ross Hudgens: een sticky navigatiemenu geeft **+39% conversie**, **+12% paginabezoeken**
en **+11% gemiddelde sessieduur**. Op mobiel moet je contactgegevens altijd binnen bereik zijn.

### Contentideeën uit "Mensen vragen ook"

Scrape de "Mensen vragen ook"-sectie van Google voor je branche en maak content die precies die
vragen beantwoordt. Dat is een spiekbriefje voor je hele contentstrategie.

Maar: **de gebruikelijke content gap-analyse is stuk.** Kopiëren wat je concurrent heeft is niet
genoeg meer. De vraag is niet "wat ontbreekt bij mij", maar **"waar zoeken mensen naar waar Google
nog geen vijf miljoen kopieën van heeft"**.

---

## Linkbuilding: eerst niet schaden

### Oude links die giftig worden

Sterling Sky ziet dit consistent bij sites die na een core update instorten. Het patroon:

- Alle wegzakkende pagina's hadden **veel backlinks met zoekwoordrijke ankerteksten** ("beste
  loodgieter Dallas", "Dallas loodgieter expert")
- De links waren **niet nieuw** — vaak vijf jaar oud, gebouwd door een ingehuurd bureau
- De **verwijzende domeinen zakten zelf ook weg** — het netwerk erachter was door Google afgeschreven
- Rode vlag: **verwijzende domeinen omhoog terwijl organisch verkeer omlaag gaat**

Google draait dan niet alleen de eerdere winst terug, maar lijkt het als **negatief signaal** te
behandelen: nieuwe pagina's zónder links presteerden bij zo'n site beter dan de pagina's mét.

Het meest verontrustende geval: een thuisdienstenbedrijf met tientallen zulke links, afkomstig van
andere kleine bedrijven in dezelfde branche — deels directe concurrenten. Ze wisten er niets van en
hadden nooit een SEO-bureau ingehuurd.

**Praktisch:** breng in kaart waar je links vandaan komen. Er kunnen links tussen zitten die je niet
kent en die je bij de volgende core update de kop kosten. Dat links vandaag werken zegt niets; Google
wordt hier sneller in.

### Classifiers

Sinds de helpful content update (2023) kan Google een **domeinbreed** label toepassen waardoor geen
enkele pagina nog ergens rankt. Dit is een **algoritmische** straf: je krijgt géén melding in Search
Console, anders dan bij een handmatige maatregel (die ze al jaren nauwelijks meer zien).

Zolang die classifier er zit, verbetert **niets** wat je op de site doet je positie. Verwijdering
vraagt doorgaans een volgende core update én substantiële verbeteringen. Sites die in juni 2025
geraakt werden herstelden pas bij de december-update; van de in december geraakte sites herstelde er
bij de maart-update nog geen enkele. Reken op **meer dan één core update**.

Belangrijk: de helpful content update raakte lokale SEO nauwelijks, en deze classifiers werken
**alleen organisch** door — het lokale pakket blijft ongemoeid.

### De lawinetechniek

Herstelaanpak van Sterling Sky, via Kyle Roof. Jaag niet meteen op de verloren zware termen. Ga eerst
achter de kleinere, makkelijke onderwerpen aan die je snel kunt domineren omdat concurrenten er nog
niet over geschreven hebben, en bouw daarmee laag voor laag autoriteit op tot je de zware termen
weer aankunt.

Vruchtbaarste grond: zoekwoorden die al op **positie 2 tot 10** staan. Eén of twee plekken stijgen
maakt daar een enorm verschil.

### Persberichten (herzien standpunt)

Ze hadden persberichten jaren geleden getest, geen effect gezien en volledig afgeschreven. Opnieuw
getest — mét echte data en nieuwswaardige cijfers van klanten — met heel andere uitkomsten:

- **Makelaar: +83% verkeer binnen 28 dagen**, plus stijging in het lokale pakket
- **Advocaat:** bescheiden maar gestage winst; eerst het lokale pakket, weken later organisch
- **Hoveniersbedrijf:** lokaal pakket omhoog, organisch nog meer — en het **AI-overzicht** voor hun
  belangrijkste zoekwoord ging **rechtstreeks uit het persbericht citeren**

Dat laatste is het interessantste: het gaat niet meer alleen om backlinks, maar om **de bron zijn die
Google's AI vertrouwt**.

⚠️ Eén waarschuwing uit hun eigen data: bij een site die al door de augustus-spamupdate geraakt was
(gekochte links van Fiverr) zakte juist het zoekwoord uit de ankertekst van het persbericht weg bij
de volgende core update. Op een belaste site is dit dus geen veilige tactiek.

### Lokale sponsorlinks

Voor een winkelketen met meerdere vestigingen zochten ze lokale organisaties die op hun site naar
sponsors linken, en regelden links per vestiging. De locaties die zo'n backlink kregen gingen beter
ranken.

---

## Waar deze skill botst met `/seo`

**Dit is een echte tegenspraak. Kies bewust en zeg welke lijn je volgt.**

`/seo` (Nathan Gotch) leunt zwaar op AI-eerste versies: AI is goed in onderzoek, data-analyse en
eerste versies, en "de magie zit in het redigeren".

Sterling Sky's test wijst de andere kant op. Bij een **letselschadeadvocaat** draaiden ze
AI-content en verhaal-gedreven content **tegelijk, naast elkaar**:

- De AI-content deed **vrijwel niets**
- De verhaal-gedreven content gaf een forse stijging

Andere resultaten in dezelfde lijn:

| Klant | Wat ze toevoegden | Resultaat |
|---|---|---|
| Strafrechtadvocaat, DUI-termen | Een echte zaak — bewijs onjuist verzameld, zaak geseponeerd — in plaats van uitleg over de wetgeving | Sprong in het lokale pakket |
| Tandarts | Een echt verhaal van een behandeling | **+50% conversie** |
| Schilder | Foto's, de werkelijke kosten, de doorlooptijd | **+350% verkeer** |

Hun verklaring: Reddit is het model. Het is niet geoptimaliseerd voor SEO maar voor mensen, en Google
wordt daar steeds beter in herkennen.

Ze zagen hetzelfde bij **AI-afbeeldingen**: die werkten aanvankelijk goed en stortten daarna in. Na
analyse van honderden afbeeldingen op klantsites: infographics krijgen de meeste kliks, en
**afbeeldingen met mensen erop** converteren het best.

Ross Simmonds, in gesprek bij Sterling Sky, komt strategisch op hetzelfde uit:

> Ik vind het goed dat marketeers weer marketing moeten doen. Laten we teruggaan naar de basis. Begrijp
> je publiek. Maak goede verhalen. Maak content die niet bedoeld is om te ranken, maar om te beïnvloeden.

### Hoe je hiermee omgaat

Beide standpunten zijn onderbouwd, en ze sluiten elkaar niet volledig uit:

- Gotch test op **brede, informatieve SEO en AI-zichtbaarheid**, waar volume en dekking meetellen.
- Sterling Sky test op **lokale dienstverleners**, waar het onderscheidende juist zit in wat alleen
  dit bedrijf kan vertellen: deze zaak, deze klus, deze prijs, dit team.

Werkbare synthese, maar noem het als jouw afweging en niet als bevinding uit een van beide bronnen:
gebruik AI voor onderzoek, structuur en dekking, en laat het onderscheidende deel — de zaak, de
klus, de prijs, de foto's — uit echte ervaring komen. Voor een lokaal dienstverlenend bedrijf is dat
laatste geen versiering maar de kern.

Het bewijs is aan beide kanten anekdotisch: één parallelle test bij één advocaat, tegenover Gotch's
eigen praktijk. **Presenteer geen van beide als vaststaand.**

---

## Meten en gereedschap

### Meet het zoekresultaat, niet je rapport

De meest onderschatte tactiek volgens Sterling Sky. Zie je in je rankingrapport dat je op één staat
en denk je dat alles goed is, dan mis je de helft.

Andy Crestodina liet zien hoe Google eruitzag voor het zoekwoord "buckets" in 2014, tegenover 2025:
het best gerankte organische resultaat staat inmiddels **8.500 pixels** van de bovenkant van de
pagina. Die site verloor enorm veel verkeer terwijl de rankingtracker meldde dat er niets veranderd
was.

Gebruik een tracker die **schermafbeeldingen van het werkelijke zoekresultaat bewaart**, en kijk er
ook echt naar.

### Search Console goed uitlezen

Wil je een daling helder zien, filter dan twee dingen weg:

1. **Al je merkgebonden verkeer**
2. **De URL die aan je Google Bedrijfsprofiel hangt**

Doe je dat niet, dan zie je de daling mogelijk helemaal niet. Zij gebruiken de Chrome-extensie
Advanced GSC Visualizer om de data te bekijken.

### Waarschuwingssignalen bij core updates

Vrijwel elke site die volledig onderuitging bij een update was **al eerder geraakt** door een
voorgaande update. Die eerdere klap is de waarschuwing.

### Gereedschap en waar het voor dient

| Gereedschap | Waarvoor |
|---|---|
| **Places Scout** | Rasterweergave van posities per stad; zien of er AI-lokale pakketten in je markt draaien en welke concurrenten daarin zitten, inclusief schermafbeeldingen; categorierapporten van best presterende bedrijven |
| **Local Falcon** | Trendanalyse; positieverschuiving per uur zichtbaar maken (openingstijden, filtering) |
| **BrightLocal** | Positiecontrole; doorhalingen als eerste indicatie van filtering |
| **Ahrefs** | Vóór je een link najaagt: check de trend in *organic pages*. Manta was ooit een sterke directory en verliest nu duizenden pagina's uit de index — daar wil je geen link van |
| **Plepper** (Chrome) | In één keer alle GBP-categorieën van concurrenten op Maps zien |
| **Wappalyzer** (Chrome) | De volledige techniekstack achter een concurrentensite |
| **GS Location Changer** (Chrome) | Zoeken emuleren vanaf een andere locatie — voor audits en om resultaten aan klanten te laten zien |
| **Advanced GSC Visualizer** (Chrome) | Search Console-data ontleden |

---

## Werkwijze

1. **Bepaal welk scorebord stuk is.** Lokaal pakket, organisch, of allebei. Ze hebben aparte
   algoritmes en aparte oorzaken; een organische straf raakt het lokale pakket niet.
2. **Zijn de kaartrankings weg? Loop eerst de vijf oorzaken uit diagnose 1 na.** Meestal is het er
   één van, en dan is optimaliseren zonde van de tijd.
3. **Sluit filtering uit** voor je aan iets anders begint — en toets per zoekwoord, want het filter
   werkt op zoekwoordniveau.
4. **Rankings goed maar leads omlaag? Kijk naar het zoekresultaat zelf**, niet naar je rapport.
   Advertenties in het lokale pakket en AI-lokale pakketten verklaren dit vaker dan SEO.
5. **Controleer de basis op het profiel** in deze volgorde: primaire categorie, landingspagina-URL,
   openingstijden, zichtbaar adres, naam. Dit zijn wijzigingen van minuten met effecten van
   tientallen posities.
6. **Zet recensies op frequentie, niet op volume.** Benchmark tegen de maandelijkse instroom van
   concurrenten, haal eerst de tien, en stuur op recensies mét tekst.
7. **Repareer de recensieroute** voor je meer recensies gaat vragen: merkzoekopdracht in plaats van
   de directe link of QR-code.
8. **Breng je backlinkprofiel in kaart** voor je nieuwe links bouwt — ook links die je nooit zelf
   hebt aangevraagd.
9. **Laat het onderscheidende uit echte ervaring komen**: deze zaak, deze klus, deze prijs, dit team.
10. **Hertest wat je hebt afgeschreven.** Dit is hun expliciete meta-les: SEO evolueert niet alleen,
    het cycleert. Persberichten en diensten in het profiel werkten niet, en werken nu wel.

---

## Wat snel veroudert

Deze onderwerpen bewegen hard. Controleer ze voor je ze als vaststaand presenteert.

- **AI-lokale pakketten.** Ten tijde van de opname alleen op mobiel, alleen waargenomen in de VS, bij
  ongeveer **8%** van de gevolgde zoekwoorden — en groeiend. Aandeel, land en verschijningsvorm zijn
  allemaal aan verandering onderhevig.
- **Advertenties in het lokale pakket.** Van 1% (begin 2025) naar 14% (november 2025) in hun mobiele
  rapporten. Ook de vormgeving — belknop weg bij organisch, groot bij betaald — kan Google morgen
  terugdraaien.
- **De supportinrichting.** Callcenterlocaties, kwaliteitsverschillen per taal en de verstopte route
  naar handmatige verificatie komen van iemand die twee jaar geleden bij Google vertrok. Hij zegt er
  zelf bij dat het veranderd kan zijn, en de richting is duidelijk: steeds minder menselijke
  processen.
- **Het seizoenspatroon van recensieverwijderingen** (maart–april streng, Q4 code freeze) is een
  observatie uit hun tijd bij Google, geen gepubliceerd beleid.
- **Richtlijnen over namen van medewerkers in recensies.** Nieuw op het moment van opname, met
  onbekende handhaving.
- **Herstelduur na een classifier.** Gebaseerd op de core updates van juni, december en maart. Het
  aantal updates dat nodig is verandert mee met Google's tempo.
- **De grens van tien recensies.** Oorspronkelijk ontdekt door een oud-Googler, opnieuw bevestigd —
  maar dat is een drempel in een algoritme dat kan verschuiven.

---

## Let op

- **De bewijskracht verschilt per uitspraak.** Het "near me"-onderzoek (8.000 bedrijven, 200 steden)
  en de belknopdata (179 profielen) staan op heel andere grond dan een enkele klantcase. Neem het
  onderscheid mee als je iemand adviseert; deze skill benoemt de steekproef waar die bekend is.
- **Correlatie is geen oorzaak.** Ze zeggen dat zelf expliciet bij het "near me"-onderzoek: het zijn
  lichte verbanden, geen enkele factor garandeert de eerste positie.
- **Denk niet in absoluten.** Dat is het terugkerende advies van de ex-Googlers. Het detectiesysteem
  weegt signalen; er is geen drempel waarboven je gestraft wordt en waaronder je veilig bent. Advies
  in de vorm van "doe X nooit meer" is bijna altijd een verkeerde lezing van een gewogen signaal.
- **Sommige tactieken zitten in een grijs gebied.** Twee voorbeelden waarover ze het intern oneens
  waren:
  - Een letselschadeadvocaat deelde op een lokaal festival gratis fietshelmen uit en vroeg om
    recensies: **431 → 503 recensies** in een maand, daarna vijf maanden op nummer één in de hele
    stad. Maar die mensen namen de dienst nooit af, dus de recensies zijn vermoedelijk "niet ter
    zake". Google zei desgevraagd dat je dit niet moet doen. Ze presenteren dit expliciet als open
    vraag, niet als aanbeveling.
  - De kaartpin verplaatsen om aan het filter te ontkomen wordt binnen het vak betwist.
  Presenteer zulke tactieken met het risico erbij, nooit als standaardadvies.
- **Sterling Sky is een bureau dat ook Google Ads beheert.** Dat is relevant bij het advies om Ads te
  gaan draaien. De onderliggende data staat er los van, de conclusie niet.
- **Bijna alles is Amerikaans.** Gemeentegrenzen, DBA-registratie, callcenterrouting,
  brancheverdeling. De mechanismen gelden breder, de uitvoering niet automatisch. Controleer voor
  Nederland en België.
- **Sponsorblokken en productplugs zijn hier weggelaten.** Waar een onderliggend principe los
  daarvan steeds terugkwam, is het principe zonder het product opgenomen — zo staat de
  antwoordservice erin als middel om 24/7-openingstijden waar te maken, zonder de aanbieder die ze
  in de video aanraden.
- **Wat hier niet in staat, stond niet in de bronnen.** Deze skill is gebouwd op 24 video's. Wil je
  een gebied uitbreiden — bijvoorbeeld meerdere vestigingen, lokale linkbuilding of lokale SEO buiten
  de VS — dan is dat hier te dun onderbouwd om op te vullen. Zeg dat liever dan het aan te vullen met
  aannames.
