# -*- coding: utf-8 -*-
"""AI Act, artikel 50: watermerken, labels en chatbots (oktober 2026). Zelfde formaat als pages_kennis.PAGES."""
from pages_be import GBA
from pages_nl import AP

AIACT = ("Verordening (EU) 2024/1689 (AI Act) op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj")
COP = ("Europese Commissie: Code of Practice voor het markeren en labelen van AI-inhoud", "https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content")
A50 = ("AI Act Explorer: praktische gids bij artikel 50", "https://artificialintelligenceact.eu/transparency-rules-article-50/")
KB = [("Kennisbank", "/kennisbank/")]

PAGES = [
dict(
    path="/kennisbank/ai-tekst-labelen-watermerk/", lang="nl", kind="artikel", land="eu", crumbs=KB,
    tags=["ai", "ai-act", "transparantie", "website", "marketing"],
    title="AI-tekst labelen: watermerk en AI Act uitgelegd | Cyberdijk",
    desc="ChatGPT en Claude krijgen een onzichtbaar watermerk. Moet je AI-teksten op je website nu labelen? Wat artikel 50 van de AI Act echt vraagt van je bedrijf.",
    h1="AI-teksten en het onzichtbare watermerk: wat moet je bedrijf labelen?",
    lede="OpenAI en Anthropic stoppen een onzichtbaar watermerk in teksten die ChatGPT en Claude schrijven. Tegelijk gelden sinds 2 augustus 2026 de transparantieregels van de Europese AI Act. Veel ondernemers vragen zich nu af of ze hun blogs, productteksten en nieuwsbrieven moeten labelen, of dat ze een probleem hebben als Google het watermerk ziet. Dit artikel zet alles op een rij: wat het watermerk is, wat de wet precies vraagt, voor wie, en wat je als kmo of mkb-bedrijf vandaag concreet regelt.",
    kort=[
        "Het watermerk is een statistisch patroon in de woordkeuze. Het is onzichtbaar, zegt niets over wie de tekst maakte en is voorlopig alleen voor onderzoekers te controleren.",
        "De plicht om AI-inhoud machineleesbaar te markeren ligt bij de aanbieders van AI-tools, zoals OpenAI, Anthropic en Google, niet bij jou als gebruiker.",
        "Als bedrijf moet je AI-tekst alleen zichtbaar labelen als hij het publiek informeert over zaken van algemeen belang en er geen echte menselijke redactie en eindverantwoordelijkheid is.",
        "Deepfakes, dus echt lijkende beelden, video of audio, moet je altijd als AI-inhoud aanduiden. Een chatbot op je website moet zich als AI voorstellen.",
        "Boetes kunnen oplopen tot 15 miljoen euro of 3% van de wereldwijde jaaromzet, met lagere bedragen voor kmo's. Een eenvoudig intern beleid volstaat meestal om in orde te zijn.",
    ],
    body="""
<h2>Wat is er aan de hand?</h2>
<p>In de zomer van 2026 kondigden de grote makers van taalmodellen aan dat ze een onzichtbaar watermerk toevoegen aan teksten die hun modellen schrijven. OpenAI doet dat voor ChatGPT en Codex, eerst voor gebruikers in de Europese Unie. Anthropic doet het voor Claude en gebruikt daarvoor SynthID, een techniek van Google DeepMind. Beide bedrijven gaven aan dat ze het watermerk wereldwijd willen toepassen.</p>
<p>De aanleiding is Europees. Artikel 50 van de AI Act verplicht aanbieders van AI-systemen die tekst, beelden, audio of video maken om die inhoud in een machineleesbaar formaat te markeren, zodat ze als AI-inhoud herkenbaar is. Die regel geldt sinds 2 augustus 2026. Voor generatieve AI-systemen die al vóór die datum op de markt waren, geldt een overgangstermijn tot 2 december 2026. De Europese Commissie publiceerde in juni 2026 een gedragscode, de Code of Practice voor het markeren en labelen van AI-inhoud, en in juli 2026 definitieve richtsnoeren bij artikel 50. Wie de code ondertekent, heeft een praktisch referentiekader om aan te tonen dat hij de regels volgt.</p>

<h2>Hoe werkt zo'n tekstwatermerk?</h2>
<p>Een watermerk in een tekst is geen logo, geen verborgen teken en geen metadata die je kan wegknippen. Het zit in de woordkeuze zelf. Een taalmodel kiest bij elk woord uit een reeks mogelijke vervolgwoorden. Bij een watermerk stuurt het model die keuze heel lichtjes, volgens een geheim patroon. Voor een lezer is dat niet te merken: de tekst leest even vlot en betekent hetzelfde. Een detector die het patroon kent, kan over een langere tekst wel berekenen of die keuzes vaker dan toevallig in dat patroon passen.</p>
<p>Daaruit volgen een paar belangrijke eigenschappen:</p>
<ul>
<li><strong>Korte teksten zijn moeilijk te herkennen.</strong> Een detector heeft genoeg woorden nodig om een statistisch patroon te zien. Een titel, een slogan of een korte productomschrijving levert te weinig signaal.</li>
<li><strong>Bewerken verzwakt het watermerk.</strong> Volgens cijfers die OpenAI zelf bekendmaakte, daalde de herkenningskans van ongeveer 92% naar 66% wanneer 10% van de woorden door synoniemen werd vervangen, en naar 17% bij een kwart van de woorden. Anthropic meldt ook dat zwaar herschrijven, inkorten of mengen met andere tekst het signaal verzwakt.</li>
<li><strong>De detector kan zich vergissen.</strong> Hij kan onterecht een watermerk melden of een bestaand watermerk missen. Een gevonden watermerk is dus een aanwijzing, geen bewijs.</li>
<li><strong>Een watermerk zegt niets over jou.</strong> Het onthult niet wie de gebruiker is, geeft geen toegang tot je gesprekken en zegt niet hoeveel je zelf geschreven of aangepast hebt. Het ontbreken van een watermerk bewijst ook niet dat een mens de tekst schreef.</li>
<li><strong>Bijna niemand heeft de detector.</strong> Docenten, werkgevers en klanten krijgen voorlopig geen toegang. OpenAI geeft alleen goedgekeurde onderzoekers en deskundige organisaties toegang, omdat de technologie nog niet betrouwbaar genoeg is voor breed gebruik.</li>
</ul>
<p>Geen watermerk is van toepassing op broncode waar elk teken exact moet kloppen, zoals een script of een configuratiebestand. De richtsnoeren van de Commissie sluiten ook vertalingen, heel korte antwoorden en tussenresultaten in een werkproces uit van de markeringsplicht.</p>

<h2>Wat vraagt artikel 50 van de AI Act precies?</h2>
<p>Artikel 50 maakt een duidelijk onderscheid tussen <strong>aanbieders</strong>, de bedrijven die een AI-systeem ontwikkelen en op de markt brengen, en <strong>gebruiksverantwoordelijken</strong>, in het Engels deployers: de bedrijven en organisaties die het systeem in hun eigen activiteiten inzetten. Als kmo of mkb-bedrijf dat ChatGPT, Claude, Gemini of Copilot gebruikt, ben je een gebruiksverantwoordelijke.</p>
<div style="overflow-x:auto"><table style="min-width:520px">
<thead><tr><th>Wie</th><th>Plicht</th><th>Artikel</th></tr></thead>
<tbody>
<tr><td>Aanbieder van een chatbot of AI-assistent</td><td>Het systeem zo ontwerpen dat mensen weten dat ze met AI praten, tenzij dat voor een redelijk geïnformeerd persoon vanzelf duidelijk is</td><td>50, lid 1</td></tr>
<tr><td>Aanbieder van generatieve AI</td><td>Tekst, beeld, audio en video machineleesbaar markeren en detecteerbaar maken als AI-inhoud: dit is het watermerk</td><td>50, lid 2</td></tr>
<tr><td>Gebruiker van emotieherkenning of biometrische categorisering</td><td>De betrokken personen informeren</td><td>50, lid 3</td></tr>
<tr><td>Gebruiker die deepfakes publiceert</td><td>Bekendmaken dat het beeld, de video of de audio kunstmatig gemaakt of bewerkt is</td><td>50, lid 4</td></tr>
<tr><td>Gebruiker die AI-tekst publiceert om het publiek te informeren over zaken van algemeen belang</td><td>Bekendmaken dat de tekst met AI gemaakt of bewerkt is, tenzij er menselijke redactie is en iemand de redactionele verantwoordelijkheid draagt</td><td>50, lid 4</td></tr>
</tbody>
</table></div>
<p>De informatie moet duidelijk en herkenbaar gegeven worden, uiterlijk op het moment dat iemand de inhoud voor het eerst ziet of de eerste keer met het systeem in contact komt. Ze moet ook toegankelijk zijn voor mensen met een beperking.</p>

<h3>Het watermerk is de taak van de aanbieder</h3>
<p>Dit is het belangrijkste punt voor ondernemers: de technische markering, dus het watermerk, is een verplichting van OpenAI, Anthropic, Google en andere aanbieders. Jij hoeft geen watermerk toe te voegen, te bewaren of te controleren. Je bent ook niet in overtreding als het watermerk door jouw bewerkingen verzwakt.</p>

<h3>Wanneer moet jij AI-tekst zichtbaar labelen?</h3>
<p>Voor tekst geldt de labelplicht alleen voor tekst die gepubliceerd wordt <em>met als doel het publiek te informeren over aangelegenheden van algemeen belang</em>. Denk aan nieuwsberichten, politieke of maatschappelijke analyses, informatie over gezondheid, veiligheid, economie of overheidsbeleid. Een gewone productbeschrijving, een offerte, een interne mail of een tekst over de diensten van je schilderbedrijf valt daar normaal niet onder.</p>
<p>En zelfs voor tekst over zaken van algemeen belang vervalt de plicht als aan twee voorwaarden samen voldaan is:</p>
<ol>
<li>De tekst heeft een <strong>menselijke beoordeling of redactionele controle</strong> doorlopen.</li>
<li>Een natuurlijke persoon of een rechtspersoon draagt de <strong>redactionele verantwoordelijkheid</strong> voor de publicatie.</li>
</ol>
<p>De richtsnoeren van de Commissie zijn daarbij streng op de kwaliteit van die controle. Een spellingcontrole of een snelle blik volstaat niet. Er moet een inhoudelijke beoordeling zijn door iemand met voldoende kennis van het onderwerp, die feiten controleert, de tekst aanpast waar nodig en bereid is er zijn naam aan te verbinden. Leg vast hoe dat gebeurt: wie leest na, wat wordt gecontroleerd en wie keurt goed.</p>

<h3>Deepfakes: altijd melden</h3>
<p>Voor beelden, video en audio die echte personen, plaatsen, voorwerpen of gebeurtenissen nabootsen en daardoor echt lijken, geldt geen uitzondering voor menselijke controle. Gebruik je een AI-gegenereerde foto van een werf, een team of een klant die echt lijkt, of een stem die op een bestaande persoon lijkt, dan meld je dat. Voor duidelijk artistiek, creatief, satirisch of fictief werk volstaat een lichtere melding die het werk niet stoort. De richtsnoeren maken duidelijk dat reclame zelden onder die lichtere regeling valt.</p>

<h2>Wat betekent dit voor jouw website, blog en sociale media?</h2>
<p>Voor de meeste kleine ondernemingen is het goede nieuws dat er weinig verandert, zolang je AI gebruikt als hulpmiddel en zelf de eindredactie doet. Een paar situaties uit de praktijk:</p>
<ul>
<li><strong>Dienstenpagina's en productteksten.</strong> Je laat een eerste versie schrijven, past ze aan je bedrijf aan en publiceert ze. Dit is geen informatie over een zaak van algemeen belang. Een label is niet verplicht.</li>
<li><strong>Een blog met tips voor klanten.</strong> Bijvoorbeeld "zo onderhoud je je dakgoot" of "wat kost een badkamerrenovatie". Ook dit is doorgaans geen aangelegenheid van algemeen belang in de zin van de wet. Lees de tekst inhoudelijk na en neem er verantwoordelijkheid voor.</li>
<li><strong>Uitleg over wetgeving, subsidies of veiligheid.</strong> Hier wordt het grijzer: informatie over premies, regels of risico's kan wel het publiek informeren over zaken van algemeen belang. Laat zo'n tekst nakijken door iemand die het onderwerp kent, vermeld wie de eindverantwoordelijke is en bewaar wie wat gecontroleerd heeft. Dan geldt de uitzondering.</li>
<li><strong>AI-beelden in advertenties of op sociale media.</strong> Lijkt het beeld echt en toont het mensen, plaatsen of situaties die niet bestaan, dan label je het. Gebruik je liever echte foto's van je eigen werk: dat is eerlijker en het werkt ook beter.</li>
<li><strong>Een chatbot op je website.</strong> De chatbot moet zich bij het begin van het gesprek als AI voorstellen. Lees meer in ons artikel over <a href="/kennisbank/ai-chatbot-website-ai-act/">AI-chatbots op je website</a>.</li>
</ul>

<h2>Straft Google AI-teksten af?</h2>
<p>Google heeft herhaaldelijk gezegd dat het niet kijkt naar hoe een tekst gemaakt is, maar naar of hij nuttig, betrouwbaar en origineel is. Massaal geproduceerde teksten zonder meerwaarde, met als enige doel hoger te scoren, beschouwt Google wel als spam, ongeacht of een mens of een AI ze schreef. Of en hoe zoekmachines watermerken gebruiken, is niet bekendgemaakt; Google zegt in zijn richtlijnen alleen dat de manier van maken niet bepalend is.</p>
<p>Wat wel telt, is wat Google ervaring, expertise, gezag en betrouwbaarheid noemt. Een tekst scoort beter als hij dingen bevat die een taalmodel niet kan verzinnen: eigen foto's, echte klantcases, je eigen prijzen en werkwijze, een naam en gezicht achter de tekst en ervaring uit je eigen praktijk. Dat is ook de beste reden om AI-teksten grondig te herwerken: niet om een watermerk weg te werken, maar omdat een tekst met jouw eigen kennis meer klanten oplevert.</p>

<h2>Moet je het watermerk uit je teksten halen?</h2>
<p>Nee. Er is voor een gewone onderneming geen reden om dat te doen, en het lost niets op. Het watermerk is niet zichtbaar voor je klanten, Google beoordeelt teksten volgens zijn eigen richtlijnen op kwaliteit en niet op hun maakwijze, en het watermerk zegt niets over jou. Voor jouw wettelijke plichten maakt het niet uit of het watermerk er nog in zit: wat telt, is of je deepfakes meldt, of je chatbot zich voorstelt als AI en of je teksten over zaken van algemeen belang inhoudelijk nakijkt of labelt.</p>
<p>Opzettelijk watermerken verwijderen om AI-inhoud als menselijk werk voor te stellen, bijvoorbeeld in een schoolopdracht, een sollicitatie of een gepubliceerd nieuwsbericht, kan wel tot problemen leiden: met je school of werkgever, met je klanten, en in het geval van publicaties over zaken van algemeen belang ook met de AI Act. Eerlijk zijn over je werkwijze is in de praktijk de veiligste keuze.</p>

<h2>Boetes en toezicht</h2>
<p>Inbreuken op artikel 50 kunnen bestraft worden met een administratieve boete tot 15 miljoen euro of tot 3% van de wereldwijde jaaromzet, als dat hoger is. Voor kmo's en start-ups geldt telkens het laagste van die twee bedragen, en toezichthouders moeten rekening houden met de grootte van de onderneming, de ernst van de inbreuk en de maatregelen die genomen zijn. Elke lidstaat duidt zijn eigen toezichthouders aan. In Nederland spelen de Autoriteit Persoonsgegevens en de Rijksinspectie Digitale Infrastructuur een centrale rol. Wie de Code of Practice volgt, kan dat volgens de Commissie laten meewegen bij de beoordeling.</p>

<h2>Stappenplan voor kmo's en mkb</h2>
<ol>
<li><strong>Maak een lijst van je AI-gebruik.</strong> Welke tools gebruik je, voor welke teksten, beelden, video's en gesprekken? Een eenvoudige tabel volstaat.</li>
<li><strong>Bepaal per gebruik of het onder artikel 50 valt.</strong> Gaat het om een chatbot, een deepfake of tekst over een zaak van algemeen belang? Zo nee, dan is er geen labelplicht.</li>
<li><strong>Leg je redactieproces vast.</strong> Wie leest AI-teksten na, wat wordt gecontroleerd, wie keurt goed? Een halve pagina in je interne afspraken is genoeg.</li>
<li><strong>Kies een vaste vermelding voor wanneer het wel moet.</strong> Bijvoorbeeld onder een artikel: "Deze tekst werd met behulp van AI opgesteld en door [naam] inhoudelijk nagekeken." Voor beelden: een duidelijke vermelding "AI-gegenereerd beeld" bij of op het beeld.</li>
<li><strong>Controleer je chatbot.</strong> Stelt hij zich bij het begin van elk gesprek voor als AI?</li>
<li><strong>Zorg voor AI-geletterdheid.</strong> Sinds 2 februari 2025 moet wie AI inzet ervoor zorgen dat medewerkers voldoende kennis hebben om er verantwoord mee te werken. Een korte interne uitleg over wat mag, wat niet mag en welke gegevens nooit in een AI-tool horen, is een goed begin. Lees meer in <a href="/kennisbank/ai-act-kmo-mkb/">de AI Act voor kmo's en mkb</a>.</li>
<li><strong>Vergeet de AVG niet.</strong> Voer je persoonsgegevens van klanten of medewerkers in een AI-tool in, dan gelden de gewone privacyregels: een rechtsgrond, een <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomst</a> met de aanbieder en een vermelding in je <a href="/kennisbank/privacyverklaring-website/">privacyverklaring</a>.</li>
</ol>

<h2>Een voorbeeld van een korte interne AI-richtlijn</h2>
<p>Voor een kleine onderneming kan een interne richtlijn er zo uitzien:</p>
<ul>
<li>We gebruiken AI om eerste versies van teksten te schrijven. Elke tekst wordt voor publicatie inhoudelijk nagelezen door de zaakvoerder of een aangeduide medewerker.</li>
<li>Teksten over wetgeving, premies, gezondheid of veiligheid worden extra gecontroleerd op feiten en bronnen.</li>
<li>We publiceren geen AI-beelden van mensen, werven of situaties die echt lijken zonder de vermelding "AI-gegenereerd beeld".</li>
<li>Onze chatbot stelt zich bij elk gesprek voor als AI-assistent en verwijst voor persoonlijk advies naar een medewerker.</li>
<li>We voeren geen namen, adressen, telefoonnummers of andere persoonsgegevens van klanten in een AI-tool in, tenzij de tool daarvoor contractueel goedgekeurd is.</li>
</ul>
""",
    faq=[
        ("Moet ik onder elke blog vermelden dat ik AI gebruikte?", "Niet als de blog geen informatie over een zaak van algemeen belang is, of als iemand de tekst inhoudelijk heeft nagekeken en er de redactionele verantwoordelijkheid voor draagt. Vrijwillig vermelden mag altijd."),
        ("Kan Google zien dat mijn tekst met ChatGPT of Claude geschreven is?", "Google zegt dat het een tekst beoordeelt op nut, betrouwbaarheid en originaliteit, niet op de manier waarop hij gemaakt is. Massaal geproduceerde teksten zonder meerwaarde worden wel als spam gezien, of ze nu door een mens of door AI geschreven zijn."),
        ("Kan mijn klant of concurrent het watermerk controleren?", "Voorlopig niet. De detectoren zijn alleen beschikbaar voor goedgekeurde onderzoekers en deskundige organisaties. De makers willen de toegang later uitbreiden."),
        ("Zit er ook een watermerk in vertalingen of code?", "Code die exact moet kloppen krijgt geen watermerk. De richtsnoeren van de Commissie sluiten ook vertalingen, heel korte antwoorden en tussenresultaten uit van de markeringsplicht."),
        ("Geldt dit ook voor teksten van vóór augustus 2026?", "Er is geen verplichting om oudere inhoud met terugwerkende kracht te labelen. Voor nieuwe publicaties gelden de regels sinds 2 augustus 2026."),
        ("Is een gevonden watermerk een bewijs dat een tekst met AI geschreven is?", "Nee. Een detector kan zich vergissen, en het watermerk zegt niets over hoeveel iemand zelf schreef of aanpaste. Omgekeerd bewijst het ontbreken van een watermerk ook niet dat een mens de tekst schreef."),
    ],
    sources=[AIACT, COP, A50],
),
dict(
    path="/kennisbank/ai-chatbot-website-ai-act/", lang="nl", kind="artikel", land="eu", crumbs=KB,
    tags=["ai", "ai-act", "chatbot", "website", "avg"],
    title="AI-chatbot op je website: regels van de AI Act | Cyberdijk",
    desc="Een AI-chatbot op je website moet zich als AI voorstellen. Wat de AI Act en de AVG vragen, met een voorbeeldtekst en een checklist voor kmo's en mkb.",
    h1="Een AI-chatbot op je website: wat zeggen de AI Act en de AVG?",
    lede="Steeds meer kleine ondernemingen zetten een AI-chatbot op hun website die vragen beantwoordt, afspraken plant of offertes voorbereidt. Sinds 2 augustus 2026 gelden daarvoor de transparantieregels van de AI Act, bovenop de AVG. Dit zijn de regels en zo zet je je chatbot in orde.",
    kort=[
        "Een chatbot moet duidelijk maken dat de bezoeker met AI praat, uiterlijk bij het eerste contact.",
        "Die plicht ligt bij de aanbieder van het systeem, maar als bedrijf dat de chatbot inzet zorg je best dat de melding er staat.",
        "Verwerkt de chatbot namen, e-mailadressen of andere persoonsgegevens, dan gelden ook de AVG-regels: privacyverklaring, verwerkersovereenkomst en bewaartermijnen.",
    ],
    body="""
<h2>De regel: zeg dat het AI is</h2>
<p>Artikel 50, lid 1 van de AI Act bepaalt dat AI-systemen die rechtstreeks met mensen communiceren, zo ontworpen moeten worden dat die mensen weten dat ze met een AI-systeem te maken hebben. Er is één uitzondering: als dat voor een redelijk geïnformeerde, oplettende persoon uit de context al duidelijk is. Vertrouw daar niet op. Een chatbot met een menselijke naam en een foto kan bezoekers makkelijk doen denken dat ze met een medewerker praten.</p>
<p>De informatie moet duidelijk zijn en uiterlijk op het moment van de eerste interactie gegeven worden. De verplichting rust formeel op de aanbieder van het systeem, maar in de praktijk is de onderneming die de chatbot op haar website zet het aanspreekpunt voor de bezoeker. Zorg dus dat het in orde is.</p>

<h2>Een goede openingszin</h2>
<p>Een voorbeeld dat aan de regel voldoet: <em>"Hallo, ik ben Max, de AI-assistent van [bedrijfsnaam]. Ik beantwoord je vragen over onze diensten. Wil je liever iemand spreken? Laat je gegevens achter, dan nemen we contact op."</em></p>
<p>Zet daarnaast een korte vermelding in het chatvenster zelf, bijvoorbeeld "AI-assistent" naast de naam, zodat de melding ook zichtbaar blijft als iemand de eerste zin niet leest.</p>

<h2>De AVG gaat ook mee</h2>
<p>Vraagt de chatbot naar een naam, telefoonnummer of e-mailadres, of kunnen bezoekers vrij tekst typen waarin persoonsgegevens staan, dan verwerk je persoonsgegevens. Dan geldt het volgende:</p>
<ul>
<li>Vermeld de chatbot in je <a href="/kennisbank/privacyverklaring-website/">privacyverklaring</a>: welke gegevens, waarvoor, hoe lang en wie de leverancier is.</li>
<li>Sluit een <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomst</a> met de leverancier van de chatbot en, als die een taalmodel van een derde gebruikt, controleer waar de gegevens verwerkt worden.</li>
<li>Bewaar gesprekken niet langer dan nodig. Spreek een termijn af, bijvoorbeeld drie maanden, en wis daarna.</li>
<li>Laat de chatbot geen gevoelige gegevens vragen, zoals gezondheidsinformatie, en geef geen medisch, juridisch of financieel advies zonder menselijke controle.</li>
<li>Gebruik je cookies voor de chatbot die niet strikt noodzakelijk zijn, dan vraag je eerst toestemming. Lees meer over de <a href="/kennisbank/cookiebanner-toestemming/">cookiebanner</a>.</li>
</ul>

<h2>Wat als de chatbot iets fout zegt?</h2>
<p>Een taalmodel kan overtuigend klinken en toch fouten maken. Als onderneming blijf je verantwoordelijk voor wat je website aan klanten belooft. Beperk de chatbot tot je eigen informatie, zoals diensten, openingsuren en prijzen, en laat hem bij twijfel doorverwijzen naar een medewerker. Controleer regelmatig een reeks gesprekken om fouten op te sporen.</p>

<h2>Checklist</h2>
<ol>
<li>De chatbot stelt zich bij het begin van elk gesprek voor als AI.</li>
<li>In het chatvenster staat zichtbaar "AI-assistent" of een vergelijkbare vermelding.</li>
<li>Bezoekers kunnen altijd kiezen voor contact met een mens.</li>
<li>De chatbot staat in je privacyverklaring en je hebt een verwerkersovereenkomst.</li>
<li>Er is een bewaartermijn voor gesprekken.</li>
<li>De chatbot beantwoordt alleen vragen over je eigen diensten en verwijst bij twijfel door.</li>
<li>Je controleert maandelijks een steekproef van gesprekken.</li>
</ol>
""",
    faq=[
        ("Mag mijn chatbot een menselijke naam hebben?", "Ja, zolang meteen duidelijk is dat het om een AI-assistent gaat. Zet 'AI-assistent' naast de naam en vermeld het in de eerste zin."),
        ("Geldt dit ook voor een eenvoudige keuzemenu-bot zonder AI?", "Artikel 50 gaat over AI-systemen. Een bot die alleen vaste knoppen en vooraf geschreven antwoorden toont, is meestal geen AI-systeem. Duidelijk zijn naar je bezoekers blijft wel verstandig."),
        ("Wat riskeer ik als de melding ontbreekt?", "Inbreuken op artikel 50 kunnen een boete tot 15 miljoen euro of 3% van de wereldwijde jaaromzet opleveren, met lagere bedragen voor kmo's. Belangrijker in de praktijk: een klant die zich misleid voelt, verlies je."),
    ],
    sources=[AIACT, A50, GBA, AP],
),
]
