# -*- coding: utf-8 -*-
"""Praktische AVG/GDPR-artikels voor kmo's en mkb (oktober 2026). Zelfde formaat als pages_kennis.PAGES."""
from pages_be import GBA
from pages_nl import AP

AVG = ("Verordening (EU) 2016/679 (GDPR/AVG) op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2016/679/oj")
EDPB = ("European Data Protection Board: richtsnoeren", "https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_nl")
CAMERA_BE = ("FOD Binnenlandse Zaken: aangifte van bewakingscamera's", "https://www.aangifte-camera.be")
KB = [("Kennisbank", "/kennisbank/")]

PAGES = [
dict(
    path="/kennisbank/avg-checklist-kmo/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "privacy", "checklist"],
    title="AVG-checklist voor kmo's en mkb: 10 stappen | Cyberdijk",
    desc="Wat moet een kleine onderneming voor de GDPR/AVG minimaal geregeld hebben? Tien concrete stappen, van verwerkingsregister tot datalekprocedure.",
    h1="AVG-checklist voor kmo's en mkb: tien stappen die je moet regelen",
    lede="De GDPR, in Nederland de AVG, geldt voor elke onderneming die persoonsgegevens verwerkt. Dat is dus ook de kapper met een klantenbestand en de aannemer met offertes. Deze tien stappen vormen de basis die een toezichthouder of een grote klant verwacht.",
    kort=[
        "De AVG geldt voor elk bedrijf dat gegevens van klanten, medewerkers of leveranciers bijhoudt, ongeacht de grootte.",
        "De kern: weten welke gegevens je hebt, waarom, hoe lang, wie erbij kan en wat je doet bij een lek.",
        "Bijna alles kan je zelf regelen; schriftelijke documentatie is het bewijs dat je het gedaan hebt.",
    ],
    body="""
<h2>De tien stappen</h2>
<ol>
<li><strong>Breng in kaart welke persoonsgegevens je hebt.</strong> Klanten, prospecten, medewerkers, sollicitanten, leveranciers. Noteer per groep welke gegevens en waar ze staan: boekhoudpakket, mailbox, cloud, papier.</li>
<li><strong>Leg een <a href="/kennisbank/verwerkingsregister/">verwerkingsregister</a> aan.</strong> Per verwerking het doel, de categorieën gegevens, de ontvangers en de bewaartermijn.</li>
<li><strong>Bepaal per doel de grondslag.</strong> Een overeenkomst, een wettelijke plicht, een gerechtvaardigd belang of toestemming. Toestemming is zelden de juiste keuze voor gewone klantgegevens.</li>
<li><strong>Zet een <a href="/kennisbank/privacyverklaring-website/">privacyverklaring</a> op je website.</strong> In begrijpelijke taal, met je contactgegevens en de rechten van mensen.</li>
<li><strong>Sluit <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomsten</a></strong> met leveranciers die gegevens voor je verwerken: sociaal secretariaat of salarisadministratie, cloud, IT-partner, nieuwsbriefdienst.</li>
<li><strong>Beveilig de basis.</strong> Tweestapsverificatie op mail en cloud, updates, back-ups, versleutelde laptops en een wachtwoordbeheerder.</li>
<li><strong>Beperk toegang.</strong> Medewerkers zien alleen de gegevens die ze nodig hebben. Haal accounts weg als iemand vertrekt.</li>
<li><strong>Spreek bewaartermijnen af en wis wat te oud is.</strong> Gegevens van een prospect die nooit klant werd, horen niet jaren in je mailbox.</li>
<li><strong>Weet wat je doet bij een datalek.</strong> Een korte <a href="/kennisbank/datalek-melden-72-uur/">datalekprocedure</a> en een logboek van incidenten, ook van incidenten die je niet moest melden.</li>
<li><strong>Weet hoe je een <a href="/kennisbank/inzageverzoek-avg/">inzageverzoek</a> beantwoordt.</strong> Je hebt een maand. Wie de procedure vooraf kent, haalt dat zonder stress.</li>
</ol>
<h2>Waar loopt het meestal mis?</h2>
<p>Bij kleine ondernemingen zien we steeds dezelfde punten: een privacyverklaring die van een andere site is gekopieerd, een <a href="/kennisbank/cookiebanner-toestemming/">cookiebanner</a> die toch al cookies plaatst voor er geklikt is, camera's zonder aangifte of pictogram, en oude Excel-lijsten met klantgegevens op een gedeelde schijf. Geen van die punten is moeilijk op te lossen, maar ze vallen meteen op bij een klacht.</p>
<h2>Heb je een DPO of FG nodig?</h2>
<p>Voor de meeste kmo's niet. Een functionaris voor gegevensbescherming is verplicht voor overheidsinstanties en voor organisaties die op grote schaal gevoelige gegevens verwerken of mensen stelselmatig volgen. Lees meer voor <a href="/be/gdpr-dpo/">België</a> of <a href="/nl/avg-fg/">Nederland</a>.</p>
""",
    faq=[
        ("Geldt de AVG ook voor eenmanszaken?", "Ja. Zodra je gegevens van klanten of andere personen bijhoudt, geldt de AVG. Alleen puur privégebruik valt erbuiten."),
        ("Moet ik dit allemaal op papier zetten?", "Ja. De AVG vraagt dat je kan aantonen dat je de regels naleeft. Een verwerkingsregister, je privacyverklaring en je verwerkersovereenkomsten zijn daarvoor het bewijs."),
        ("Hoeveel tijd kost dit?", "Voor een kleine onderneming lukt de basis vaak in één tot twee dagen werk. Daarna volstaat een jaarlijkse controle en een update als je een nieuwe leverancier of software neemt."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/privacyverklaring-website/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "privacy", "website"],
    title="Privacyverklaring op je website: wat moet erin? | Cyberdijk",
    desc="Elke website die persoonsgegevens verzamelt heeft een privacyverklaring nodig. Wat artikel 13 AVG verplicht vermeldt en de fouten die je best vermijdt.",
    h1="Privacyverklaring op je website: wat moet erin staan?",
    lede="Heeft je website een contactformulier, een offerteaanvraag, een nieuwsbrief of statistieken, dan verzamel je persoonsgegevens. De AVG verplicht je om mensen daarover te informeren. Dat doe je met een privacyverklaring.",
    kort=[
        "Artikel 13 van de AVG bepaalt wat je moet vertellen als je gegevens rechtstreeks bij iemand verzamelt.",
        "De verklaring moet kloppen met wat je echt doet; een gekopieerde tekst is een veelgemaakte fout.",
        "Zet een link in de voettekst van elke pagina en bij elk formulier.",
    ],
    body="""
<h2>Verplichte onderdelen</h2>
<ul>
<li>Wie je bent: bedrijfsnaam, adres, ondernemingsnummer of KVK-nummer en een contactadres voor privacyvragen.</li>
<li>De contactgegevens van je DPO of FG, als je er een hebt.</li>
<li>Welke gegevens je verzamelt en voor welke doelen, met per doel de rechtsgrond.</li>
<li>Het gerechtvaardigd belang, als je je daarop baseert.</li>
<li>Wie de gegevens ontvangt: hostingpartij, mailprovider, boekhouder, CRM.</li>
<li>Of gegevens buiten de Europese Economische Ruimte gaan, en op welke basis.</li>
<li>Hoe lang je de gegevens bewaart, of hoe je die termijn bepaalt.</li>
<li>De rechten van mensen: inzage, correctie, wissing, beperking, bezwaar en overdraagbaarheid.</li>
<li>Het recht om toestemming in te trekken, als je op toestemming steunt.</li>
<li>Het recht om klacht in te dienen bij de Gegevensbeschermingsautoriteit of de Autoriteit Persoonsgegevens.</li>
<li>Of iemand verplicht is de gegevens te geven, en wat er gebeurt als hij dat niet doet.</li>
<li>Of je geautomatiseerde besluitvorming of profilering gebruikt.</li>
</ul>
<h2>Fouten die vaak voorkomen</h2>
<p>De meest voorkomende fout is een tekst die van een generator of van een andere website komt en niet beschrijft wat jouw bedrijf echt doet. Andere klassiekers: geen bewaartermijnen, geen vermelding van de nieuwsbriefdienst of het statistiekenpakket, en een verklaring die jaren niet is bijgewerkt terwijl je ondertussen van software veranderde.</p>
<h2>Privacyverklaring en cookies</h2>
<p>Cookies en trackers vallen onder een aparte regel: voor niet-noodzakelijke cookies heb je vooraf toestemming nodig. Je kan dat in een aparte cookieverklaring uitleggen. Lees meer in <a href="/kennisbank/cookiebanner-toestemming/">cookiebanner en toestemming</a>.</p>
<h2>Waar zet je ze?</h2>
<p>Zet een link in de voettekst van elke pagina en vlak bij elk formulier waar mensen gegevens invullen. Gebruik eenvoudige taal en vermijd juridisch jargon: de AVG vraagt uitdrukkelijk een beknopte, transparante en begrijpelijke tekst.</p>
""",
    faq=[
        ("Is een privacyverklaring verplicht zonder contactformulier?", "Verzamel je via je website echt geen persoonsgegevens, ook geen statistieken met IP-adressen, dan niet. In de praktijk verzamelt bijna elke site wel iets, al is het maar via de hosting of een statistiekenpakket."),
        ("Mag ik een gratis generator gebruiken?", "Als vertrekpunt wel, maar pas de tekst aan zodat ze klopt met jouw leveranciers, doelen en bewaartermijnen. Een verklaring die niet overeenkomt met de werkelijkheid voldoet niet."),
        ("Hoe vaak moet ik ze bijwerken?", "Telkens als er iets verandert: nieuwe software, een nieuwsbrief, een ander statistiekenpakket. Controleer ze minstens één keer per jaar."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/cookiebanner-toestemming/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["cookies", "privacy", "website", "avg"],
    title="Cookiebanner: wanneer is toestemming nodig? | Cyberdijk",
    desc="Welke cookies mag je zonder toestemming plaatsen en hoe ziet een correcte cookiebanner eruit? De regels in België en Nederland.",
    h1="Cookiebanner: wanneer heb je toestemming nodig?",
    lede="Voor cookies en vergelijkbare technieken geldt een aparte Europese regel, de ePrivacy-richtlijn, naast de AVG. Kort gezegd: strikt noodzakelijke cookies mogen altijd, voor de rest vraag je eerst toestemming.",
    kort=[
        "Strikt noodzakelijke cookies (inloggen, winkelmandje, je cookiekeuze onthouden) vragen geen toestemming.",
        "Marketing- en trackingcookies plaats je pas nadat iemand actief ja heeft gezegd.",
        "Weigeren moet even makkelijk zijn als accepteren, en vooraf aangevinkte vakjes tellen niet als toestemming.",
    ],
    body="""
<h2>Welke cookies mogen zonder toestemming?</h2>
<p>Cookies die strikt noodzakelijk zijn om de dienst te leveren waar de bezoeker om vraagt: een sessie bij het inloggen, een winkelmandje, beveiliging tegen misbruik en het onthouden van de cookiekeuze zelf. Voor statistieken is het verschillend per land. In Nederland mogen analytische cookies met weinig impact op de privacy zonder toestemming, onder voorwaarden. De Belgische Gegevensbeschermingsautoriteit is strenger en vraagt in principe ook voor statistiekcookies toestemming. Wie in beide landen actief is, kiest het veiligst voor toestemming of voor een statistiekenpakket zonder cookies.</p>
<h2>Wat is een geldige toestemming?</h2>
<ul>
<li>Vrij gegeven: de site blijft bruikbaar als iemand weigert.</li>
<li>Actief: een klik op een knop. Vooraf aangevinkte vakjes of verder scrollen tellen niet, zo besliste het Europees Hof van Justitie in de zaak Planet49 (2019).</li>
<li>Geïnformeerd: de bezoeker weet welke cookies, van wie en waarvoor.</li>
<li>Even makkelijk in te trekken als te geven, bijvoorbeeld via een link in de voettekst.</li>
</ul>
<h2>Zo ziet een correcte banner eruit</h2>
<p>Een knop "Alles accepteren" en een knop "Weigeren" op hetzelfde niveau en even opvallend, plus een optie om per categorie te kiezen. Geen cookies van marketing of advertenties voordat er geklikt is. Test dat zelf: open je site in een privévenster en kijk in de ontwikkelaarstools of er al cookies van advertentieplatformen staan voor je iets hebt aangeklikt.</p>
<h2>Veelgemaakte fouten</h2>
<p>Alleen een knop "OK" zonder weigeroptie. Een weigerknop die verstopt zit in een tweede scherm. Een banner die er staat, maar waarbij de trackingcode toch al bij het laden van de pagina start. Dat laatste is de fout die het vaakst voorkomt en ook het makkelijkst te controleren is.</p>
""",
    faq=[
        ("Heb ik een cookiebanner nodig als ik alleen Google Analytics gebruik?", "In België in principe wel. In Nederland mag het zonder toestemming alleen als de statistiekcookies weinig impact op de privacy hebben en je aan de voorwaarden van de Autoriteit Persoonsgegevens voldoet; lees daarvoor de actuele uitleg van de AP. Een statistiekenpakket zonder cookies maakt de banner overbodig voor statistieken."),
        ("Geldt dit ook voor een kleine website?", "Ja. De regels hangen af van welke cookies je plaatst, niet van de grootte van je bedrijf of je site."),
        ("Hoe lang mag ik een cookiekeuze onthouden?", "Toezichthouders aanvaarden doorgaans een termijn van enkele maanden tot een jaar. Vraag daarna opnieuw."),
    ],
    sources=[AVG, GBA, AP, EDPB],
),
dict(
    path="/kennisbank/camerabewaking-avg/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["camera", "privacy", "avg", "beveiliging"],
    title="Camerabewaking in je bedrijf: regels in BE en NL | Cyberdijk",
    desc="Camera's in je winkel, magazijn of op je parking? De Belgische camerawet en de AVG in Nederland: aangifte, pictogram, bewaartermijn en personeel.",
    h1="Camerabewaking in je bedrijf: wat moet je regelen in België en Nederland?",
    lede="Camerabeelden waarop mensen herkenbaar zijn, zijn persoonsgegevens. In België komt daar nog een aparte camerawet bij. Dit zijn de regels voor een winkel, kantoor, werkplaats of bedrijfsterrein.",
    kort=[
        "In België moet je bewakingscamera's aangeven via aangifte-camera.be en een pictogram ophangen.",
        "In Nederland is er geen aangifte, maar de AVG geldt volledig: doel, noodzaak, bewaartermijn en informatie.",
        "Camera's mogen niet gericht zijn op de openbare weg of op plekken waar medewerkers zich omkleden of rusten.",
    ],
    body="""
<h2>België: de camerawet</h2>
<p>Voor bewakingscamera's geldt de camerawet van 21 maart 2007. De belangrijkste plichten voor een onderneming:</p>
<ul>
<li>Aangifte bij de politie via <a href="https://www.aangifte-camera.be" rel="noopener">aangifte-camera.be</a>, vóór de camera in gebruik gaat. De aangifte is gratis en moet elk jaar bevestigd worden.</li>
<li>Een officieel pictogram aan de ingang dat aangeeft dat er gefilmd wordt, met je contactgegevens.</li>
<li>Beelden bewaar je niet langer dan één maand, tenzij ze nodig zijn als bewijs van een misdrijf, schade of overlast.</li>
<li>Een register van de beeldverwerkingsactiviteiten, dat je op vraag aan de politie en de toezichthouder toont.</li>
<li>Richt de camera niet op de openbare weg. Komt een stukje straat voor je ingang in beeld, beperk dat dan zoveel mogelijk.</li>
</ul>
<h2>Nederland: de AVG</h2>
<p>In Nederland is er geen aparte aangifteplicht, maar de AVG geldt volledig. Je hebt een gerechtvaardigd belang nodig, zoals de bescherming tegen diefstal, en je moet kunnen uitleggen waarom minder ingrijpende maatregelen niet volstaan. Bezoekers moeten zien dat er camera's hangen. De Autoriteit Persoonsgegevens noemt vier weken als richtlijn voor de bewaartermijn, tenzij er een incident is.</p>
<h2>Camera's en personeel</h2>
<p>Camera's die ook medewerkers filmen, vragen extra zorg. Informeer medewerkers vooraf. In België gelden daarnaast de regels van cao nr. 68 over camerabewaking op de werkvloer. In Nederland heeft de ondernemingsraad instemmingsrecht als je er een hebt. Verborgen camera's zijn alleen in uitzonderlijke situaties toegestaan, en camera's in kleedruimtes, toiletten of pauzeruimtes nooit.</p>
<h2>Een camera die beelden in de cloud zet</h2>
<p>Bewaart je camera de beelden bij een leverancier, dan is die leverancier een verwerker. Je hebt dan een <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomst</a> nodig en je controleert waar de beelden staan.</p>
""",
    faq=[
        ("Geldt dit ook voor één camera aan de kassa?", "Ja. Het aantal camera's maakt niet uit: ook één bewakingscamera in een winkel of werkplaats moet in België aangegeven worden en een pictogram krijgen."),
        ("Mag ik camerabeelden aan de politie geven?", "Ja, bij een misdrijf of op vraag van de politie mag je de relevante beelden overhandigen. Bewaar die beelden dan zolang het onderzoek ze nodig heeft."),
        ("Wat als iemand zijn beelden wil zien?", "Iemand die gefilmd werd, heeft een recht op inzage. Je mag andere herkenbare personen op de beelden onherkenbaar maken."),
    ],
    sources=[CAMERA_BE, GBA, AP, AVG],
),
dict(
    path="/kennisbank/inzageverzoek-avg/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "rechten", "privacy"],
    title="Inzageverzoek AVG beantwoorden: stappenplan | Cyberdijk",
    desc="Een klant, ex-medewerker of sollicitant vraagt welke gegevens je over hem hebt? Je hebt een maand. Stappenplan voor een inzageverzoek volgens de AVG.",
    h1="Een inzageverzoek volgens de AVG beantwoorden: stappenplan",
    lede="Iedereen mag vragen welke persoonsgegevens jouw bedrijf over hem heeft. Dat recht staat in artikel 15 van de AVG. Je moet binnen een maand antwoorden, en meestal gratis.",
    kort=[
        "Je antwoordt binnen een maand; bij complexe of talrijke verzoeken mag je dat met twee maanden verlengen, als je dat binnen de eerste maand meldt.",
        "Een eerste kopie is gratis. Een redelijke vergoeding mag alleen voor bijkomende kopieën.",
        "Controleer de identiteit, maar vraag niet meer gegevens dan nodig.",
    ],
    body="""
<h2>Stap voor stap</h2>
<ol>
<li><strong>Registreer het verzoek.</strong> Noteer de datum van ontvangst: de termijn van een maand loopt vanaf dan. Een verzoek hoeft geen vaste vorm te hebben; een mail of een bericht via sociale media telt ook.</li>
<li><strong>Controleer wie het vraagt.</strong> Twijfel je aan de identiteit, vraag dan bijkomende informatie. Vraag geen kopie van een identiteitskaart als je de persoon op een andere manier kan herkennen, bijvoorbeeld via zijn gekende e-mailadres.</li>
<li><strong>Zoek alle gegevens op.</strong> Klantenbestand, boekhouding, mailbox, CRM, back-ups, papieren dossiers en de systemen van je verwerkers.</li>
<li><strong>Geef een kopie en de uitleg.</strong> Naast de gegevens zelf vertel je ook de doelen, de ontvangers, de bewaartermijn, de herkomst van de gegevens en de rechten van de persoon.</li>
<li><strong>Bescherm anderen.</strong> Staan er gegevens van andere mensen in, zoals collega's in een mailwisseling, maak die dan onleesbaar.</li>
<li><strong>Documenteer.</strong> Bewaar wat je gestuurd hebt en wanneer. Dat is je bewijs bij een klacht.</li>
</ol>
<h2>Mag je weigeren?</h2>
<p>Alleen als het verzoek kennelijk ongegrond of buitensporig is, bijvoorbeeld bij steeds herhaalde verzoeken over dezelfde gegevens. Je moet dat zelf kunnen aantonen en de persoon wijzen op zijn recht om klacht in te dienen. Een inzageverzoek in het kader van een arbeidsconflict is niet automatisch misbruik.</p>
<h2>Andere rechten</h2>
<p>Naast inzage kunnen mensen ook vragen om correctie, wissing, beperking, overdraagbaarheid of bezwaar. Voor al die verzoeken geldt dezelfde termijn van een maand. Een korte interne procedure helpt, zodat iedereen in je bedrijf weet bij wie zo'n vraag terechtkomt.</p>
""",
    faq=[
        ("Moet ik ook interne mails geven?", "Je geeft de persoonsgegevens over de persoon, niet noodzakelijk elk document. Mails waarin de persoon voorkomt, kunnen wel persoonsgegevens bevatten. Geef die gegevens, desnoods als uittreksel, en maak gegevens van anderen onleesbaar."),
        ("Wat als ik niets over de persoon heb?", "Laat dat dan binnen de maand weten. Ook een negatief antwoord is een antwoord."),
        ("Wat als ik de termijn mis?", "Dan kan de persoon klacht indienen bij de Gegevensbeschermingsautoriteit of de Autoriteit Persoonsgegevens. Antwoord alsnog zo snel mogelijk en leg uit waarom het later was."),
    ],
    sources=[AVG, GBA, AP, EDPB],
),
]
