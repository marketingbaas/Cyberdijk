# -*- coding: utf-8 -*-
"""SEO-uitbreiding oktober 2026: artikels die in Search Console vertoningen halen, verder uitgediept,
plus een nieuw artikel over cybersecurity voor kmo's en mkb. Wordt ingeladen door pages_kennis.py."""

UITBREIDING = {
"/kennisbank/nis2-meldplicht-incident/": dict(
    updated="2026-10-09",
    title="NIS2-meldplicht: wanneer meld je een incident? | Cyberdijk",
    desc="Wanneer is een incident significant onder NIS2, wat meld je binnen 24 uur, 72 uur en een maand, en hoe meld je in België en Nederland? Met voorbeelden.",
    body="""
<h2>Wanneer is een incident significant?</h2>
<p>De richtlijn noemt een incident significant als het minstens één van deze twee gevolgen heeft of kan hebben:</p>
<ul>
<li><strong>Een ernstige operationele verstoring</strong> van je diensten, of een aanzienlijk financieel verlies voor je organisatie.</li>
<li><strong>Aanzienlijke materiële of immateriële schade</strong> voor andere personen of organisaties, bijvoorbeeld klanten die hun dienst niet meer krijgen.</li>
</ul>
<p>Het woord <em>kan</em> is belangrijk: je hoeft niet te wachten tot de schade er is. Een ransomware-aanval die je net op tijd tegenhoudt, maar die je hele productie had kunnen stilleggen, kan al significant zijn.</p>
<p>Voor een aantal digitale dienstverleners, zoals cloud- en datacenterdiensten, beheerde IT-diensten (MSP's en MSSP's), online marktplaatsen en zoekmachines, legt de Europese uitvoeringsverordening (EU) 2024/2690 concrete drempels vast. Een voorbeeld: een rechtstreeks financieel verlies van meer dan 500.000 euro of 5% van de jaaromzet, het laagste van de twee, maakt een incident significant. Voor de andere sectoren beoordeel je zelf, op basis van de impact, de duur, het aantal getroffen gebruikers en de gevolgen voor anderen.</p>
<h2>Voorbeelden: melden of niet?</h2>
<ul>
<li><strong>Ransomware legt je ERP-systeem twee dagen plat</strong> en klanten krijgen geen leveringen: significant, melden.</li>
<li><strong>Een phishingmail waarop niemand klikte:</strong> niet significant. Wel registreren in je logboek.</li>
<li><strong>Een medewerker gaf zijn wachtwoord af, de aanvaller las een week mee in de mailbox van de boekhouding:</strong> vaak significant, en meestal ook een datalek onder de AVG.</li>
<li><strong>Een storing bij je hostingpartij legt je webshop een uur plat:</strong> meestal niet significant, tenzij je dienstverlening aan klanten ernstig verstoord raakt.</li>
<li><strong>Een DDoS-aanval maakt je klantenportaal een halve dag onbereikbaar:</strong> afhankelijk van het aantal getroffen klanten en de duur vaak wel.</li>
</ul>
<p>Twijfel je, meld dan. Een vroegtijdige waarschuwing die achteraf niet nodig bleek, wordt je niet kwalijk genomen. Een melding die te laat komt wel.</p>
<h2>Hoe meld je concreet?</h2>
<p><strong>In België</strong> meld je bij het Centrum voor Cybersecurity België (CCB) via het meldplatform op Safeonweb@Work. Je registreert je organisatie vooraf, zodat je bij een incident meteen kunt melden. Het CCB stuurt de melding door naar je sectorale overheid.</p>
<p><strong>In Nederland</strong> meld je bij het CSIRT dat voor je sector is aangewezen, en bij je toezichthouder. Voor de meeste sectoren is het NCSC het CSIRT. Leg vooraf vast via welk kanaal je meldt.</p>
<p>Wat er minstens in je meldingen staat:</p>
<ul>
<li><strong>24 uur:</strong> dat er een incident is, of je een kwaadwillige oorzaak vermoedt, en of er gevolgen in andere landen kunnen zijn.</li>
<li><strong>72 uur:</strong> een eerste inschatting van de ernst en de impact, en technische indicatoren die je al kent, zoals verdachte IP-adressen of bestandsnamen.</li>
<li><strong>Eén maand:</strong> een beschrijving van het incident, de oorzaak of het type dreiging, de maatregelen die je nam en de gevolgen over de grens.</li>
</ul>
<h2>Uitbesteed aan een IT-partner of MDR-dienst?</h2>
<p>Veel bedrijven laten hun beveiliging bewaken door een externe partner, bijvoorbeeld een MDR-dienst (managed detection and response) of hun vaste IT-leverancier. De meldplicht blijft dan bij jou: de partner detecteert, maar jij moet melden. Leg daarom in het contract vast dat de partner je binnen enkele uren verwittigt bij een vermoedelijk significant incident, ook 's nachts en in het weekend, en dat hij de technische informatie aanlevert die je voor de melding nodig hebt.</p>
""",
    faq=[
        ("Wat is een significant incident onder NIS2?", "Een incident dat een ernstige verstoring van je diensten of een aanzienlijk financieel verlies veroorzaakt of kan veroorzaken, of dat anderen aanzienlijke schade berokkent of kan berokkenen. Voor sommige digitale dienstverleners gelden concrete drempels in uitvoeringsverordening (EU) 2024/2690."),
        ("Moet ik ook een poging tot aanval melden?", "Een geslaagde inbraak of een verstoring die ernstige gevolgen kan hebben, meld je. Een afgeslagen poging zonder gevolgen meestal niet. Je kunt zulke voorvallen wel vrijwillig melden en registreer ze altijd in je logboek."),
        ("Wie meldt: mijn IT-leverancier of ik?", "Jij, als organisatie die onder NIS2 valt. Je IT-partner of MDR-dienst helpt met de informatie, maar de verantwoordelijkheid blijft bij jou. Leg de afspraken vast in het contract."),
    ],
),
"/kennisbank/nis2-boetes/": dict(
    updated="2026-10-09",
    title="NIS2-boetes: bedragen en voorbeelden | Cyberdijk",
    desc="Hoe hoog zijn de NIS2-boetes in België en Nederland? Maximumbedragen, rekenvoorbeelden, gevolgen voor bestuurders en hoe je een boete voorkomt.",
    body="""
<h2>Rekenvoorbeelden</h2>
<p>De maximumboete is het hoogste van twee bedragen: een vast bedrag of een percentage van de wereldwijde jaaromzet van de groep.</p>
<ul>
<li><strong>Essentiële entiteit met 300 miljoen euro omzet:</strong> 2% is 6 miljoen, dus geldt het vaste maximum van 10 miljoen euro.</li>
<li><strong>Essentiële entiteit met 800 miljoen euro omzet:</strong> 2% is 16 miljoen euro, en dat wordt het maximum.</li>
<li><strong>Belangrijke entiteit met 50 miljoen euro omzet:</strong> 1,4% is 700.000 euro, dus geldt het vaste maximum van 7 miljoen euro.</li>
</ul>
<p>Dat zijn plafonds, geen tarieven. Een kmo die te laat registreert maar meteen meewerkt, krijgt in de praktijk eerst een waarschuwing of een termijn om de tekortkoming weg te werken.</p>
<h2>Wat bepaalt de hoogte van een boete?</h2>
<ul>
<li>De ernst en de duur van de inbreuk, en of het om een eerste keer gaat.</li>
<li>De werkelijke schade, voor de organisatie en voor anderen.</li>
<li>Of de inbreuk opzettelijk of door nalatigheid gebeurde.</li>
<li>De maatregelen die je al nam om schade te voorkomen of te beperken.</li>
<li>De mate waarin je meewerkt met de toezichthouder en eerlijk communiceert.</li>
</ul>
<h2>Persoonlijke gevolgen voor bestuurders</h2>
<p>NIS2 legt de verantwoordelijkheid uitdrukkelijk bij het bestuur. Bestuurders moeten de maatregelen goedkeuren, het toezicht houden en een opleiding volgen, en ze kunnen aansprakelijk gesteld worden als ze dat niet doen. Bij essentiële entiteiten kan de toezichthouder in het uiterste geval vragen dat een bestuurder tijdelijk zijn functie niet meer mag uitoefenen. Lees meer in ons artikel over <a href="/kennisbank/nis2-bestuur-aansprakelijkheid/">NIS2 en de aansprakelijkheid van het bestuur</a>.</p>
<h2>Vijf stappen om een boete te voorkomen</h2>
<ol>
<li><a href="/kennisbank/valt-mijn-bedrijf-onder-nis2/">Bepaal of je onder NIS2 valt</a> en registreer je tijdig.</li>
<li>Maak een risicoanalyse en leg je maatregelen vast, op basis van <a href="/kennisbank/nis2-maatregelen/">de tien maatregelen</a>.</li>
<li>Laat het bestuur het beleid formeel goedkeuren en een opleiding volgen. Leg dat vast in de notulen.</li>
<li>Zorg voor een incidentprocedure en ken de <a href="/kennisbank/nis2-meldplicht-incident/">meldtermijnen</a>.</li>
<li>Bewaar bewijs: beleid, verslagen, logboeken, opleidingsattesten. Bij controle telt wat je kunt tonen.</li>
</ol>
""",
    faq=[
        ("Hoe hoog is de NIS2-boete voor een kmo?", "Het maximum voor een belangrijke entiteit is 7 miljoen euro of 1,4% van de wereldwijde omzet, het hoogste van de twee. In de praktijk begint de toezichthouder bij een kmo meestal met een waarschuwing of een bindende instructie met een termijn."),
        ("Kan een bestuurder persoonlijk een boete krijgen?", "NIS2 voorziet dat bestuurders aansprakelijk gesteld kunnen worden als ze hun plichten niet nakomen, en bij essentiële entiteiten kan een tijdelijk functieverbod gevraagd worden. Hoe dat precies uitwerkt, hangt af van de nationale wet en het vennootschapsrecht."),
    ],
),
"/kennisbank/nis2-bestuur-aansprakelijkheid/": dict(
    updated="2026-10-09",
    title="NIS2-bestuurdersaansprakelijkheid uitgelegd | Cyberdijk",
    desc="NIS2 maakt bestuurders persoonlijk verantwoordelijk voor cybersecurity. Wat moet het bestuur goedkeuren, opvolgen en leren, en hoe toon je dat aan?",
    body="""
<h2>Wat je als bestuur concreet moet kunnen tonen</h2>
<ul>
<li><strong>Een goedgekeurd beleid.</strong> Het informatiebeveiligingsbeleid en de risicoanalyse zijn door het bestuur besproken en formeel goedgekeurd, met datum in de notulen.</li>
<li><strong>Toezicht op de uitvoering.</strong> Het bestuur krijgt minstens jaarlijks, en bij belangrijke incidenten meteen, een verslag over de stand van de maatregelen, de incidenten en de grootste risico's.</li>
<li><strong>Een gevolgde opleiding.</strong> Elke bestuurder heeft een opleiding gevolgd die genoeg kennis geeft om risico's te herkennen en de maatregelen te beoordelen. Bewaar de attesten.</li>
<li><strong>Middelen.</strong> Uit de begroting blijkt dat er budget en mensen zijn voor de maatregelen die het bestuur goedkeurde.</li>
</ul>
<h2>Acht vragen die een bestuurder aan IT moet stellen</h2>
<ol>
<li>Wat zijn onze vijf belangrijkste systemen en hoe lang kunnen we zonder?</li>
<li>Wanneer hebben we voor het laatst een back-up volledig teruggezet, en hoe lang duurde dat?</li>
<li>Gebruikt iedereen tweestapsverificatie voor e-mail en toegang op afstand?</li>
<li>Welke leveranciers hebben toegang tot onze systemen, en wat staat daarover in het contract?</li>
<li>Wie beslist bij een incident, en wie meldt binnen 24 uur?</li>
<li>Welke incidenten hadden we het afgelopen jaar, en wat hebben we geleerd?</li>
<li>Welke maatregelen uit de risicoanalyse zijn nog niet uitgevoerd, en waarom?</li>
<li>Wanneer laten we onze maatregelen extern toetsen?</li>
</ol>
<h2>Bestuurdersaansprakelijkheid en verzekering</h2>
<p>Veel bestuurders rekenen op hun bestuurdersaansprakelijkheidsverzekering (D&amp;O). Kijk na wat die dekt: administratieve boetes zelf zijn vaak niet verzekerbaar, verdedigingskosten en schadeclaims van derden soms wel. Bespreek met je makelaar of cyberrisico's en NIS2-inbreuken uitgesloten zijn. De beste bescherming blijft aantoonbaar doen wat de wet vraagt.</p>
<h2>Kmo-zaakvoerders</h2>
<p>In een kleine vennootschap ben jij als zaakvoerder het bestuur. De plichten gelden dus voor jou persoonlijk: beleid goedkeuren, opvolgen en een opleiding volgen. Het hoeft niet groot: een beleid van enkele pagina's, een jaarlijks overleg met je IT-partner dat je noteert, en een opleiding van een dag volstaan vaak om aan te tonen dat je je verantwoordelijkheid neemt.</p>
""",
    faq=[
        ("Kan een bestuurder persoonlijk aansprakelijk gesteld worden onder NIS2?", "Ja. De richtlijn bepaalt dat bestuursleden aansprakelijk gesteld kunnen worden als ze hun plichten niet nakomen: maatregelen goedkeuren, toezicht houden en een opleiding volgen. België en Nederland hebben dat overgenomen."),
        ("Dekt mijn D&O-verzekering een NIS2-boete?", "Administratieve boetes zijn meestal niet verzekerbaar. Verdedigingskosten en schadeclaims van derden kunnen wel gedekt zijn. Laat je polis nakijken door je makelaar."),
    ],
),
}

NIEUW = [
dict(
    path="/kennisbank/cybersecurity-kmo-mkb/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["kmo", "maatregelen", "nis2", "iso", "cyfun"], updated="2026-10-09",
    title="Cybersecurity voor kmo's en mkb: 12 maatregelen | Cyberdijk",
    desc="Cybersecurity voor kleine bedrijven: 12 maatregelen die de meeste aanvallen tegenhouden, wat ze kosten en waar je begint. Voor kmo's en mkb.",
    h1="Cybersecurity voor kmo's en mkb: 12 maatregelen die het verschil maken",
    lede="De meeste aanvallen op kleine bedrijven zijn geen gerichte hacks maar gewone oplichting en geautomatiseerde aanvallen die zwakke plekken zoeken. Met een handvol basismaatregelen hou je het grootste deel daarvan tegen, ook zonder eigen IT-afdeling.",
    kort=[
        "Tweestapsverificatie, updates en back-ups die je terugzet, houden de meeste aanvallen tegen.",
        "Je medewerkers zijn je eerste verdedigingslijn: oefen phishing en factuurfraude.",
        "Ook als je niet onder NIS2 valt, vragen grote klanten steeds vaker naar deze maatregelen.",
    ],
    body="""
<h2>Waarom kmo's een doelwit zijn</h2>
<p>Criminelen kiezen geen bedrijven uit op grootte, maar op gemak. Een boekhouder met een zwak wachtwoord, een webshop met een verouderde plugin of een bouwbedrijf dat facturen per mail goedkeurt: ze worden automatisch gevonden. Kleine bedrijven hebben bovendien vaak geen back-up die ze echt kunnen terugzetten, waardoor ransomware harder aankomt. Het goede nieuws: de basis is betaalbaar en haalbaar.</p>
<h2>De 12 maatregelen</h2>
<ol>
<li><strong>Tweestapsverificatie overal.</strong> Voor e-mail, boekhouding, bankieren, cloudopslag en toegang op afstand. Dit alleen al houdt het overgrote deel van de accountovernames tegen.</li>
<li><strong>Updates automatisch.</strong> Besturingssystemen, browsers, firewall, router en websites. Vervang apparaten die geen updates meer krijgen.</li>
<li><strong>Back-ups die je terugzet.</strong> Volgens de 3-2-1-regel: drie kopieën, op twee soorten media, één buiten het bedrijf of offline. Test minstens één keer per jaar een volledige terugzetting.</li>
<li><strong>Een wachtwoordmanager.</strong> Unieke, lange wachtwoorden voor elke dienst, zonder dat iemand ze moet onthouden.</li>
<li><strong>Beheerdersrechten beperken.</strong> Medewerkers werken met een gewoon account; alleen wie het nodig heeft, krijgt beheerdersrechten, en dan op een apart account.</li>
<li><strong>Beveiliging op elk toestel.</strong> Een moderne antivirus of EDR op laptops en pc's, schijfversleuteling op laptops, en een schermvergrendeling.</li>
<li><strong>E-mail beschermen.</strong> SPF, DKIM en DMARC op je domein, zodat niemand in jouw naam kan mailen. <a href="/kennisbank/spf-dkim-dmarc/">Zo stel je dat in.</a></li>
<li><strong>Factuurfraude voorkomen.</strong> Een gewijzigd rekeningnummer altijd telefonisch bevestigen via een nummer dat je al kende, nooit via het nummer in de mail.</li>
<li><strong>Medewerkers trainen.</strong> Korte, regelmatige oefeningen rond phishing en oplichting, en een cultuur waarin je een fout meteen durft te melden.</li>
<li><strong>Leveranciers en toegang op afstand.</strong> Weet welke partijen toegang hebben tot je systemen, beperk die toegang en leg afspraken vast.</li>
<li><strong>Een incidentplan op één pagina.</strong> Wie bel je, wie beslist, waar staan de back-ups, en wanneer moet je <a href="/kennisbank/datalek-melden-72-uur/">een datalek melden</a>.</li>
<li><strong>Weet wat je hebt.</strong> Een eenvoudige lijst van apparaten, software, clouddiensten en gegevens. Je kunt niet beveiligen wat je niet kent.</li>
</ol>
<h2>Wat kost het?</h2>
<p>De meeste maatregelen kosten vooral tijd: tweestapsverificatie, updates, beheerdersrechten en een incidentplan zijn gratis. Een wachtwoordmanager en een goede back-up kosten enkele euro's per gebruiker per maand. Een externe IT-partner die beveiliging beheert, kost meer, maar minder dan een dag stilstand. Begin met de maatregelen 1 tot 3: die geven de grootste winst voor de kleinste inspanning.</p>
<h2>Kaders die je helpen</h2>
<p>In België biedt het CyberFundamentals-kader van het CCB een stapsgewijze aanpak op niveaus, en voor kleine bedrijven is er de gratis Safeonweb-quickscan. In Nederland helpt het Digital Trust Center met de basismaatregelen en een gratis check. Wil je verder gaan of vragen klanten erom, dan is <a href="/kennisbank/iso-27001-maatregelen/">ISO 27001</a> de internationale norm.</p>
<h2>Val je onder NIS2?</h2>
<p>Middelgrote en grote bedrijven in een groot aantal sectoren vallen onder de NIS2-regels en moeten deze maatregelen aantoonbaar nemen. <a href="/kennisbank/valt-mijn-bedrijf-onder-nis2/">Check of jouw bedrijf eronder valt.</a> Ook als dat niet zo is, krijg je de vragen vaak via je klanten, die hun leveranciers moeten beoordelen.</p>
""",
    faq=[
        ("Waar begin ik als klein bedrijf met cybersecurity?", "Met drie dingen: tweestapsverificatie op e-mail en belangrijke diensten, automatische updates, en een back-up die je ook echt kunt terugzetten. Die drie houden het grootste deel van de aanvallen tegen."),
        ("Heb ik als kmo een IT-specialist nodig?", "Niet per se. De basis kun je zelf of met je vaste IT-partner regelen. Een specialist is nuttig voor een risicoanalyse, bij NIS2-verplichtingen of als klanten om een certificaat vragen."),
        ("Is cybersecurity verplicht voor kmo's?", "Onder de AVG moet elk bedrijf persoonsgegevens passend beveiligen. Middelgrote en grote bedrijven in bepaalde sectoren vallen daarnaast onder NIS2. Kleine bedrijven buiten NIS2 krijgen de eisen vaak via hun klanten."),
        ("Wat is de grootste dreiging voor een kmo?", "Phishing en factuurfraude, gevolgd door ransomware via gestolen wachtwoorden of onbeveiligde toegang op afstand. Daarom zijn tweestapsverificatie en training van medewerkers zo belangrijk."),
    ],
    sources=[],
),
dict(
    path="/kennisbank/toegankelijkheidswet-website/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["toegankelijkheid", "eaa", "webshop", "wcag"], updated="2026-10-11",
    title="Toegankelijkheidswet (EAA) voor websites | Cyberdijk",
    desc="De European Accessibility Act geldt sinds 28 juni 2025. Welke websites en webshops vallen eronder, wat eist de norm en wie controleert in BE en NL?",
    h1="De Europese toegankelijkheidswet: wat betekent ze voor je website of webshop?",
    lede="Sinds 28 juni 2025 moeten webshops en andere online diensten voor consumenten toegankelijk zijn voor mensen met een beperking. De regels komen uit de European Accessibility Act (EAA). Hier lees je wie eronder valt, wat de norm vraagt en hoe je begint.",
    kort=[
        "De EAA geldt onder meer voor e-commerce: sites en apps waar consumenten kopen, bestellen, reserveren of een contract sluiten.",
        "Micro-ondernemingen (minder dan 10 werknemers en maximaal 2 miljoen euro omzet of balanstotaal) zijn voor diensten grotendeels vrijgesteld.",
        "De norm is EN 301 549, die verwijst naar WCAG 2.1 niveau AA. Toezicht: FOD Economie in België, ACM in Nederland.",
    ],
    body="""
<h2>Wat is de European Accessibility Act?</h2>
<p>De EAA is een Europese richtlijn (2019/882) die een reeks producten en diensten toegankelijk moet maken voor mensen met een visuele, auditieve, motorische of cognitieve beperking. De lidstaten moesten de regels omzetten, en ze gelden sinds 28 juni 2025. Voor websites gaat het vooral om <strong>e-handelsdiensten</strong>: alles waarmee een consument online iets koopt, bestelt, reserveert of afsluit. Ook bankdiensten, e-books, ticketing en elektronische communicatie vallen eronder.</p>
<h2>Wie valt eronder?</h2>
<p>Bedrijven die zulke diensten aan consumenten aanbieden in de EU. Een uitzondering geldt voor <strong>micro-ondernemingen</strong> die diensten leveren: bedrijven met minder dan 10 werknemers en een jaaromzet of balanstotaal van maximaal 2 miljoen euro. Een louter informatieve bedrijfssite zonder verkoop of boeking valt doorgaans niet onder de EAA. Een webshop, een online boekingsmodule of een klantenportaal waar contracten worden afgesloten, wel.</p>
<h2>België en Nederland</h2>
<p>In <strong>België</strong> zijn de regels voor bank- en e-handelsdiensten opgenomen in het Wetboek van Economisch Recht. De FOD Economie houdt toezicht; de Economische Inspectie behandelt meldingen. Voor overheden gelden al langer aparte regels rond digitale toegankelijkheid. In <strong>Nederland</strong> houdt de ACM toezicht op webshops en communicatiediensten, en consumenten kunnen problemen melden via ACM ConsuWijzer. Uit onderzoek van de ACM bleek in 2026 dat een groot deel van de webshops nog niet in orde is.</p>
<h2>Wat vraagt de norm?</h2>
<p>De geharmoniseerde norm EN 301 549 verwijst voor websites naar <strong>WCAG 2.1 niveau AA</strong>. Concreet betekent dat onder meer:</p>
<ul>
<li>voldoende contrast tussen tekst en achtergrond;</li>
<li>een tekstalternatief voor afbeeldingen die iets betekenen;</li>
<li>een logische structuur met koppen, lijsten en labels;</li>
<li>alles bedienbaar met het toetsenbord, met een zichtbare focus;</li>
<li>formulieren met duidelijke labels en begrijpelijke foutmeldingen;</li>
<li>werkt bij inzoomen tot 200% en op kleine schermen;</li>
<li>geen tijdslimieten of bewegende inhoud die je niet kunt pauzeren.</li>
</ul>
<p>Daarnaast moet je informatie geven over hoe je dienst aan de toegankelijkheidseisen voldoet, bijvoorbeeld in een toegankelijkheidsverklaring of in je algemene voorwaarden.</p>
<h2>Hoe begin je?</h2>
<ol>
<li>Bepaal of je onder de wet valt: verkoop of boeking aan consumenten, en groter dan een micro-onderneming.</li>
<li>Laat je belangrijkste pagina's en je volledige bestel- of boekingsproces testen, automatisch én handmatig.</li>
<li>Los eerst de blokkerende problemen op: alles wat iemand verhindert om een aankoop af te ronden.</li>
<li>Leg vast wie verantwoordelijk is en neem toegankelijkheid op in elke nieuwe aanpassing van je site.</li>
<li>Publiceer de informatie over toegankelijkheid en een manier om problemen te melden.</li>
</ol>
<p>Een check van je website en de aanpassingen kun je laten doen bij onze partner <a href="https://www.marketingbaas.com/website-toegankelijk-maken/">Marketingbaas</a>.</p>
""",
    faq=[
        ("Geldt de toegankelijkheidswet voor elke website?", "Nee. Ze geldt vooral voor diensten waarmee consumenten online iets kopen, bestellen, reserveren of afsluiten, en voor bepaalde sectoren zoals bankdiensten. Micro-ondernemingen die diensten leveren, zijn grotendeels vrijgesteld."),
        ("Sinds wanneer geldt de EAA?", "Sinds 28 juni 2025 in de hele EU."),
        ("Welke norm moet mijn website halen?", "EN 301 549, die voor websites verwijst naar WCAG 2.1 niveau AA."),
        ("Wie controleert de toegankelijkheidswet?", "In België de FOD Economie, in Nederland de ACM. Beide kunnen optreden na meldingen van consumenten."),
        ("Is toegankelijkheid ook nuttig als ik niet verplicht ben?", "Ja. Een toegankelijke site is bruikbaar voor meer klanten, ook ouderen en mensen op een klein scherm, en de structuur die toegankelijkheid vraagt helpt ook je vindbaarheid in zoekmachines."),
    ],
    sources=[("Richtlijn (EU) 2019/882 (European Accessibility Act) op EUR-Lex", "https://eur-lex.europa.eu/eli/dir/2019/882/oj"),
             ("Vlaanderen: EU-richtlijn 2019/882 voor B2C (EAA)", "https://www.vlaanderen.be/inter/overheden-en-professionelen/werken-aan-digitale-toegankelijkheid/eu-richtlijn-2019-882-voor-b2c-eaa"),
             ("ACM: bereid je voor op regels toegankelijkheid websites en apps", "https://www.acm.nl/nl/publicaties/acm-roept-bedrijven-op-zich-voor-te-bereiden-op-regels-toegankelijkheid-websites-en-apps")],
),
dict(
    path="/kennisbank/website-gehackt-datalek-melden/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["datalek", "avg", "hack", "website"], updated="2026-10-11",
    title="Website gehackt: is het een datalek? | Cyberdijk",
    desc="Je website is gehackt. Wanneer is dat een datalek dat je binnen 72 uur moet melden bij de GBA of de AP? Zo beoordeel je het, met stappenplan.",
    h1="Website gehackt: moet je dat melden als datalek?",
    lede="Niet elke hack is een datalek, maar veel hacks zijn het wel. Zodra persoonsgegevens mogelijk in verkeerde handen zijn gekomen, gelden de regels van de AVG: beoordelen, documenteren en bij risico binnen 72 uur melden.",
    kort=[
        "Een hack is een datalek als persoonsgegevens mogelijk bekeken, gekopieerd, gewijzigd of gewist zijn.",
        "Bij risico voor de betrokkenen meld je binnen 72 uur aan de GBA (België) of de AP (Nederland).",
        "Documenteer elk incident, ook als je niet hoeft te melden.",
    ],
    body="""
<h2>Wanneer is een hack een datalek?</h2>
<p>Een datalek is volgens de AVG een inbreuk op de beveiliging waardoor persoonsgegevens per ongeluk of onrechtmatig worden vernietigd, verloren, gewijzigd, openbaar gemaakt of ingezien. Bij een gehackte website is dat het geval als de aanvaller toegang had tot gegevens van mensen. Denk aan:</p>
<ul>
<li>berichten uit het <strong>contactformulier</strong> die in de database of mailbox bewaard worden;</li>
<li><strong>klantaccounts</strong> en bestellingen in een webshop;</li>
<li><strong>inschrijvingen</strong>, nieuwsbrieflijsten of afspraken;</li>
<li>de <strong>gebruikersaccounts</strong> van medewerkers in het beheer van de site.</li>
</ul>
<p>Ging het om een hack die alleen spam toonde of bezoekers doorstuurde, en stonden er geen persoonsgegevens op de server, dan is het meestal geen datalek. Je kunt dat pas zeggen na onderzoek van hoe de aanvaller binnenkwam en wat hij kon zien.</p>
<h2>Melden of niet?</h2>
<p>Je meldt een datalek aan de toezichthouder als het waarschijnlijk een risico inhoudt voor de rechten en vrijheden van de betrokkenen. Dat doe je zonder onnodige vertraging en <a href="/kennisbank/datalek-melden-72-uur/">uiterlijk binnen 72 uur</a> nadat je ervan op de hoogte bent. In België is dat de Gegevensbeschermingsautoriteit (GBA), in Nederland de Autoriteit Persoonsgegevens (AP). Is het risico hoog, bijvoorbeeld bij wachtwoorden, betaalgegevens of gevoelige informatie, dan informeer je ook de betrokkenen zelf.</p>
<h2>Stappenplan na een hack</h2>
<ol>
<li><strong>Beperk de schade:</strong> haal de site offline of zet een onderhoudspagina, en vervang alle wachtwoorden.</li>
<li><strong>Zoek uit wat er gebeurde:</strong> hoe kwam de aanvaller binnen, sinds wanneer, en welke gegevens kon hij bereiken?</li>
<li><strong>Beoordeel het risico</strong> voor de mensen van wie gegevens betrokken zijn.</li>
<li><strong>Meld binnen 72 uur</strong> als er risico is. Ontbreekt nog informatie, meld dan wat je weet en vul later aan.</li>
<li><strong>Documenteer</strong> het incident in je register, ook als je niet meldt.</li>
<li><strong>Laat de site schoonmaken en het lek dichten</strong>, en neem maatregelen zodat het niet opnieuw gebeurt.</li>
</ol>
<p>Twijfel je of je site gehackt is? Doe de gratis <a href="https://www.marketingbaas.com/tools/website-gehackt-check/">hack-check van Marketingbaas</a>. Moet de site schoongemaakt worden, dan kan dat bij <a href="https://www.marketingbaas.com/website-gehackt-herstellen/">Marketingbaas voor een vaste prijs</a>.</p>
<h2>Voorkomen</h2>
<p>De meeste websitehacks komen binnen via verouderde plugins of zwakke wachtwoorden. Houd je site bij, beperk het aantal plugins, zet tweestapsverificatie aan voor het beheer en bewaar niet meer persoonsgegevens dan nodig: berichten uit een contactformulier hoeven niet jarenlang in de database te staan.</p>
""",
    faq=[
        ("Is elke websitehack een datalek?", "Nee. Alleen als persoonsgegevens mogelijk bekeken, gekopieerd, gewijzigd of gewist zijn. Een hack die alleen spam toont, zonder toegang tot gegevens, is meestal geen datalek."),
        ("Binnen hoeveel tijd moet ik een datalek melden?", "Zonder onnodige vertraging en uiterlijk binnen 72 uur nadat je ervan op de hoogte bent, als het lek een risico inhoudt voor de betrokkenen."),
        ("Bij wie meld ik een datalek?", "In België bij de Gegevensbeschermingsautoriteit (GBA), in Nederland bij de Autoriteit Persoonsgegevens (AP)."),
        ("Moet ik ook mijn klanten verwittigen?", "Als het lek waarschijnlijk een hoog risico inhoudt, bijvoorbeeld bij wachtwoorden, betaalgegevens of gevoelige gegevens, moet je ook de betrokkenen zelf informeren."),
    ],
    sources=[("AVG (Verordening (EU) 2016/679), artikels 33 en 34, op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2016/679/oj"),
             ("Gegevensbeschermingsautoriteit (België)", "https://www.gegevensbeschermingsautoriteit.be"),
             ("Autoriteit Persoonsgegevens (Nederland)", "https://www.autoriteitpersoonsgegevens.nl")],
),
dict(
    path="/kennisbank/nis2/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["nis2", "maatregelen", "meldplicht", "registratie", "boetes", "cyfun", "iso"], updated="2026-10-11",
    title="NIS2 uitgelegd: complete gids voor België en Nederland",
    desc="Alles over NIS2 op één plek: wie valt eronder, de plichten, deadlines, boetes en het verschil tussen de Belgische NIS2-wet en de Cyberbeveiligingswet.",
    h1="NIS2 uitgelegd: de complete gids voor België en Nederland",
    lede="NIS2 is de Europese richtlijn die duizenden organisaties verplicht om hun digitale beveiliging aantoonbaar op orde te hebben. België en Nederland hebben ze elk op hun eigen manier omgezet. Deze gids zet alles op een rij en verwijst je door naar de uitleg per onderwerp.",
    kort=[
        "België: NIS2-wet sinds 18 oktober 2024, toezicht door het CCB, beoordeling voor essentiële entiteiten tegen 18 april 2027.",
        "Nederland: Cyberbeveiligingswet sinds 15 augustus 2026, zonder overgangsperiode, registratie bij het NCSC.",
        "In de regel vanaf 50 medewerkers of meer dan 10 miljoen euro omzet en balanstotaal, in aangewezen sectoren.",
    ],
    body="""
<h2>Wat is NIS2?</h2>
<p>NIS2 is Richtlijn (EU) 2022/2555 over maatregelen voor een hoog gezamenlijk niveau van cyberbeveiliging in de Unie. Ze vervangt de eerste NIS-richtlijn uit 2016 en breidt het aantal sectoren en organisaties fors uit. Het doel: organisaties die belangrijk zijn voor economie en samenleving moeten hun risico's beheersen, ernstige incidenten snel melden en hun bestuur verantwoordelijk maken voor cyberbeveiliging. Elke lidstaat moest de richtlijn omzetten in eigen wetgeving.</p>
<h2>België en Nederland naast elkaar</h2>
<div style="overflow-x:auto"><table style="min-width:520px">
<thead><tr><th></th><th>België</th><th>Nederland</th></tr></thead>
<tbody>
<tr><td>Wet</td><td>NIS2-wet</td><td>Cyberbeveiligingswet (Cbw)</td></tr>
<tr><td>Van kracht</td><td>18 oktober 2024</td><td>15 augustus 2026, zonder overgangsperiode</td></tr>
<tr><td>Registratie</td><td>Bij het CCB via Safeonweb@Work</td><td>In het entiteitenregister van het NCSC</td></tr>
<tr><td>Maatregelen aantonen</td><td>Met CyFun of ISO 27001</td><td>Zorgplicht op basis van een risicoanalyse</td></tr>
<tr><td>Belangrijke deadline</td><td>Conformiteitsbeoordeling essentiële entiteiten tegen 18 april 2027</td><td>Plichten gelden meteen</td></tr>
<tr><td>Incidenten melden</td><td>Bij het CCB</td><td>Bij het CSIRT en de sectortoezichthouder</td></tr>
</tbody></table></div>
<h2>Valt mijn organisatie onder NIS2?</h2>
<p>Twee dingen bepalen het: je sector en je grootte. De richtlijn noemt sectoren als energie, transport, bankwezen, gezondheidszorg, drinkwater, digitale infrastructuur, ICT-dienstverlening, overheid, post, afvalbeheer, chemie, levensmiddelen en maakindustrie. In de regel val je eronder vanaf 50 medewerkers, of met een jaaromzet en balanstotaal boven 10 miljoen euro. Voor enkele digitale diensten geldt de wet ongeacht de grootte. Grote organisaties in de meest kritieke sectoren zijn <strong>essentiële entiteiten</strong>, de andere <strong>belangrijke entiteiten</strong>. <a href="/kennisbank/valt-mijn-bedrijf-onder-nis2/">Lees hoe je het nagaat</a>, of doe de check voor <a href="/be/nis2-check/">België</a> of <a href="/nl/nis2-check/">Nederland</a>.</p>
<h2>De plichten in het kort</h2>
<ul>
<li><strong>Registreren</strong> bij de nationale autoriteit. <a href="/kennisbank/nis2-registratie-ccb/">Zo registreer je in België.</a></li>
<li><strong>Maatregelen nemen</strong> op basis van een risicoanalyse: van tweestapsverificatie en back-ups tot leveranciersbeheer en incidentrespons. <a href="/kennisbank/nis2-maatregelen/">De tien maatregelen uitgelegd.</a></li>
<li><strong>Incidenten melden</strong> in drie stappen: 24 uur, 72 uur en een maand. <a href="/kennisbank/nis2-meldplicht-incident/">Zo werkt de meldplicht.</a></li>
<li><strong>Het bestuur</strong> keurt de maatregelen goed, volgt een opleiding en is aansprakelijk. <a href="/kennisbank/nis2-bestuur-aansprakelijkheid/">Wat dat betekent voor bestuurders.</a></li>
</ul>
<h2>Boetes en toezicht</h2>
<p>Essentiële entiteiten riskeren boetes tot 10 miljoen euro of 2% van de wereldwijde jaaromzet, belangrijke tot 7 miljoen euro of 1,4%. Meestal beginnen toezichthouders met waarschuwingen en bindende instructies. <a href="/kennisbank/nis2-boetes/">Alle sancties op een rij.</a></p>
<h2>Ook als je er zelf niet onder valt</h2>
<p>Organisaties onder NIS2 moeten ook de beveiliging van hun leveranciers beoordelen. Daardoor krijgen veel kleinere bedrijven vragenlijsten en contractclausules van hun klanten. <a href="/kennisbank/nis2-vragenlijst-leverancier/">Zo beantwoord je een NIS2-vragenlijst.</a> De basismaatregelen voor elke kmo vind je in <a href="/kennisbank/cybersecurity-kmo-mkb/">cybersecurity voor kmo's en mkb</a>.</p>
<h2>Waar begin je?</h2>
<ol>
<li>Ga na of je eronder valt, en als wat: essentieel of belangrijk.</li>
<li>Registreer je, als dat nog niet gebeurd is.</li>
<li>Maak een risicoanalyse en een plan met de maatregelen die ontbreken.</li>
<li>Leg de meldprocedure vast: wie meldt wat, bij wie, binnen welke termijn.</li>
<li>Laat het bestuur goedkeuren en zorg voor opleiding.</li>
<li>Kies hoe je het aantoont: in België <a href="/be/nis2-cyfun/">CyFun</a> of <a href="/kennisbank/iso-27001/">ISO 27001</a>, in Nederland met je eigen documentatie of ISO 27001.</li>
</ol>
""",
    faq=[
        ("Wat is NIS2 in het kort?", "Een Europese richtlijn die organisaties in belangrijke sectoren verplicht om hun cyberbeveiliging op orde te hebben, ernstige incidenten te melden en hun bestuur verantwoordelijk te maken."),
        ("Sinds wanneer geldt NIS2?", "In België sinds 18 oktober 2024 via de NIS2-wet. In Nederland sinds 15 augustus 2026 via de Cyberbeveiligingswet."),
        ("Voor wie geldt NIS2?", "Voor organisaties in aangewezen sectoren, in de regel vanaf 50 medewerkers of meer dan 10 miljoen euro omzet en balanstotaal. Enkele digitale diensten vallen eronder ongeacht hun grootte."),
        ("Wat is het verschil tussen essentiële en belangrijke entiteiten?", "Essentiële entiteiten zijn grote organisaties in de meest kritieke sectoren en krijgen vooraf en regelmatig toezicht. Belangrijke entiteiten worden vooral achteraf gecontroleerd, bijvoorbeeld na een incident."),
        ("Is ISO 27001 verplicht onder NIS2?", "Nee. In België is ISO 27001 wel een erkende manier om je maatregelen aan te tonen, naast CyFun. In Nederland kun je ISO 27001 gebruiken als bewijs van je zorgplicht."),
        ("Wat als ik niet onder NIS2 val?", "Dan heb je geen wettelijke plichten, maar je klanten die er wel onder vallen, zullen vaak vragen hoe je je beveiliging regelt. De basismaatregelen zijn voor elke organisatie verstandig."),
    ],
    sources=[("Richtlijn (EU) 2022/2555 (NIS2) op EUR-Lex", "https://eur-lex.europa.eu/eli/dir/2022/2555/oj"),
             ("Centrum voor Cybersecurity België (CCB)", "https://ccb.belgium.be"),
             ("Nationaal Cyber Security Centrum (NCSC)", "https://www.ncsc.nl")],
),
dict(
    path="/kennisbank/iso-27001/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["iso", "maatregelen", "nis2", "certificering"], updated="2026-10-11",
    title="ISO 27001: wat is het, kosten en certificering | Cyberdijk",
    desc="ISO 27001 uitgelegd voor kmo's en mkb: wat de norm vraagt, het stappenplan naar certificering, de kosten, de doorlooptijd en de link met NIS2.",
    h1="ISO 27001: wat is het, wat kost het en hoe word je gecertificeerd?",
    lede="ISO/IEC 27001 is de internationale norm voor informatiebeveiliging. Steeds meer klanten, aanbestedingen en wetten vragen erom. Deze gids legt uit wat de norm inhoudt, hoe je naar een certificaat gaat en wat dat kost.",
    kort=[
        "De norm vraagt een managementsysteem voor informatiebeveiliging (ISMS), gebaseerd op risico's, en kent 93 beheersmaatregelen.",
        "Reken voor een kmo op 15.000 tot 50.000 euro in totaal en zes tot twaalf maanden.",
        "Het certificaat geldt drie jaar, met elk jaar een controle-audit.",
    ],
    body="""
<h2>Wat is ISO 27001?</h2>
<p>ISO/IEC 27001 beschrijft hoe een organisatie haar informatiebeveiliging beheerst: door risico's systematisch in kaart te brengen, passende maatregelen te nemen en die voortdurend te verbeteren. Het hart is het <strong>ISMS</strong>, het managementsysteem voor informatiebeveiliging. De huidige versie is ISO/IEC 27001:2022. Een onafhankelijke certificatie-instelling controleert of je aan de norm voldoet en reikt dan het certificaat uit.</p>
<h2>Uit welke delen bestaat de norm?</h2>
<p>De hoofdstukken 4 tot 10 bevatten de eisen aan het managementsysteem: context en scope, leiderschap, risicobeoordeling, ondersteuning, uitvoering, evaluatie en verbetering. Bijlage A bevat 93 beheersmaatregelen in vier groepen: organisatorisch, mensgericht, fysiek en technologisch. Je kiest welke maatregelen voor jou gelden en legt dat vast in een verklaring van toepasselijkheid. <a href="/kennisbank/iso-27001-maatregelen/">De 93 maatregelen uitgelegd.</a></p>
<h2>Het stappenplan naar certificering</h2>
<ol>
<li><strong>Scope bepalen:</strong> welke activiteiten, locaties en systemen vallen onder het certificaat.</li>
<li><strong>Risicobeoordeling:</strong> welke informatie is belangrijk, wat kan er misgaan, hoe groot is het risico.</li>
<li><strong>Maatregelen kiezen</strong> en de verklaring van toepasselijkheid opstellen.</li>
<li><strong>Invoeren:</strong> beleid, procedures, technische maatregelen en bewustwording van medewerkers.</li>
<li><strong>Interne audit en directiebeoordeling:</strong> werkt het systeem zoals bedoeld?</li>
<li><strong>Certificatie-audit</strong> in twee fasen: eerst de documentatie, dan de werking in de praktijk.</li>
<li><strong>Onderhouden:</strong> elk jaar een controle-audit, na drie jaar een hercertificering.</li>
</ol>
<h2>Wat kost ISO 27001?</h2>
<p>Voor een kmo of mkb-bedrijf ligt het totaal doorgaans tussen 15.000 en 50.000 euro, afhankelijk van de grootte, de scope en het vertrekpunt. Daarin zitten externe begeleiding, de eigen tijd van medewerkers, eventuele technische aanpassingen en de audits zelf. Daarna volgen jaarlijkse kosten voor de controle-audits en het onderhoud van het systeem. In België kan advies rond cybersecurity in aanmerking komen voor de kmo-portefeuille.</p>
<h2>Hoe lang duurt het?</h2>
<p>De meeste kmo's rekenen op zes tot twaalf maanden. Het systeem moet enkele maanden aantoonbaar werken voordat de certificatie-audit kan slagen: de auditor wil bewijs zien van risicobeoordelingen, interne audits en verbeteracties.</p>
<h2>ISO 27001 en NIS2</h2>
<p>ISO 27001 is niet wettelijk verplicht, maar sluit goed aan bij <a href="/kennisbank/nis2/">NIS2</a>. In België is het een erkend alternatief voor <a href="/be/nis2-cyfun/">CyFun</a> om je maatregelen aan te tonen. In Nederland kun je het gebruiken als bewijs voor de zorgplicht van de Cyberbeveiligingswet. Voor de praktische uitwerking per land: <a href="/be/iso-27001/">ISO 27001 in België</a> en <a href="/nl/iso-27001/">ISO 27001 in Nederland</a>.</p>
<h2>Voor wie is ISO 27001 de moeite waard?</h2>
<ul>
<li>Organisaties die onder NIS2 vallen en een internationaal erkend bewijs willen.</li>
<li>IT- en softwarebedrijven, en dienstverleners die gevoelige gegevens van klanten beheren.</li>
<li>Bedrijven die meedoen aan aanbestedingen of werken voor grote klanten die erom vragen.</li>
<li>Organisaties die in meerdere landen werken: ISO 27001 wordt overal herkend.</li>
</ul>
""",
    faq=[
        ("Is ISO 27001 verplicht?", "Nee, het is een vrijwillige norm. Klanten, aanbestedingen of NIS2 kunnen er wel om vragen als bewijs dat je beveiliging op orde is."),
        ("Wat kost een ISO 27001-certificering?", "Voor een kmo doorgaans 15.000 tot 50.000 euro in totaal, inclusief begeleiding, eigen tijd en audits. Daarna volgen jaarlijkse kosten voor de controle-audits."),
        ("Hoe lang duurt ISO 27001?", "Meestal zes tot twaalf maanden. Het systeem moet enkele maanden werken voordat de certificatie-audit kan slagen."),
        ("Hoe lang is een ISO 27001-certificaat geldig?", "Drie jaar, met elk jaar een controle-audit. Daarna volgt een hercertificering."),
        ("Wat is het verschil tussen ISO 27001 en ISO 27002?", "ISO 27001 bevat de eisen waarop je gecertificeerd wordt. ISO 27002 is een richtlijn die de maatregelen uit bijlage A uitgebreider toelicht. Je kunt alleen voor ISO 27001 gecertificeerd worden."),
        ("Kan een klein bedrijf ISO 27001 halen?", "Ja. De norm schaalt mee met de grootte. Een kleine organisatie met een duidelijke scope kan het halen, vaak met begeleiding voor de risicoanalyse en de documentatie."),
    ],
    sources=[("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001"),
             ("Centrum voor Cybersecurity België (CCB)", "https://ccb.belgium.be"),
             ("Nationaal Cyber Security Centrum (NCSC)", "https://www.ncsc.nl")],
),
dict(
    path="/kennisbank/nen-7510/", lang="nl-NL", kind="artikel", land="nl", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["nen7510", "zorg", "iso", "nis2", "certificering"], updated="2026-10-11",
    title="NEN 7510 uitgelegd: zorg, plicht en certificaat | Cyberdijk",
    desc="NEN 7510 voor zorgaanbieders: wat de norm vraagt, voor wie verplicht, de versie 2024, certificering, kosten en een checklist om te starten.",
    h1="NEN 7510: informatiebeveiliging in de zorg, van verplichting tot certificaat",
    lede="NEN 7510 is de Nederlandse norm voor informatiebeveiliging in de zorg. Ze bouwt op ISO 27001 en 27002, met extra eisen voor patiëntgegevens. Voor zorgaanbieders is werken volgens NEN 7510 geen keuze maar een wettelijke verplichting. Dit is wat de norm vraagt en hoe je begint.",
    kort=[
        "Verplicht voor zorgaanbieders via de Wabvpz en het Besluit elektronische gegevensverwerking door zorgaanbieders; toezicht door IGJ en de Autoriteit Persoonsgegevens.",
        "Nieuwe versie NEN 7510-1:2024 sinds december 2024; gecertificeerde organisaties stappen over vóór 20 februari 2027.",
        "Werken volgens de norm is verplicht, een certificaat niet. Veel zorgverzekeraars, ketenpartners en aanbestedingen vragen er wel om.",
    ],
    body="""
<h2>Wat is NEN 7510?</h2>
<p>NEN 7510 beschrijft hoe een zorgorganisatie haar informatiebeveiliging organiseert: een managementsysteem (ISMS) op basis van risico's, met beheersmaatregelen die zijn toegesneden op de zorg. De norm bestaat uit twee delen. <strong>NEN 7510-1</strong> bevat de eisen aan het managementsysteem en de maatregelen, <strong>NEN 7510-2</strong> geeft de toelichting en praktische richtlijnen. Daarnaast horen <strong>NEN 7512</strong> (veilige uitwisseling van gegevens) en <strong>NEN 7513</strong> (logging van toegang tot patiëntdossiers) bij dezelfde familie.</p>
<h2>Voor wie is NEN 7510 verplicht?</h2>
<p>De Wet aanvullende bepalingen verwerking persoonsgegevens in de zorg (Wabvpz) en het bijbehorende Besluit elektronische gegevensverwerking door zorgaanbieders verwijzen naar NEN 7510, 7512 en 7513. Daardoor moet elke zorgaanbieder die patiëntgegevens elektronisch verwerkt, volgens deze normen werken: ziekenhuizen, ggz-instellingen, huisartsen, apotheken, fysiotherapeuten, tandartsen, verpleeghuizen en ook kleine praktijken. De Inspectie Gezondheidszorg en Jeugd (IGJ) en de Autoriteit Persoonsgegevens houden toezicht. Ook leveranciers van zorgsoftware en hostingpartijen krijgen de norm via hun klanten opgelegd.</p>
<h2>De nieuwe versie: NEN 7510-1:2024</h2>
<p>In december 2024 verscheen NEN 7510-1:2024, de opvolger van de versie uit 2017. De norm is afgestemd op ISO/IEC 27001:2022 en 27002:2022: dezelfde structuur en dezelfde 93 maatregelen, waarvan er 14 zijn aangepast voor de zorg, plus 8 extra zorgspecifieke maatregelen. Er is aandacht voor nieuwe wetgeving zoals de Wegiz en NIS2 (in Nederland de Cyberbeveiligingswet). Gecertificeerde organisaties krijgen twee jaar om over te stappen: tot 20 februari 2027.</p>
<h2>Wat vraagt de norm concreet?</h2>
<ul>
<li>Een <strong>risicoanalyse</strong> van de informatie die je verwerkt en de systemen die je gebruikt.</li>
<li><strong>Beleid en verantwoordelijkheden</strong>: wie is verantwoordelijk voor informatiebeveiliging, en wat verwacht je van medewerkers.</li>
<li><strong>Toegangsbeheer</strong>: alleen wie het nodig heeft, ziet patiëntgegevens; met logging volgens NEN 7513.</li>
<li><strong>Veilige uitwisseling</strong> met andere zorgverleners, volgens NEN 7512.</li>
<li><strong>Leveranciersbeheer</strong>: afspraken met softwareleveranciers, hosting en verwerkers.</li>
<li><strong>Incidentbeheer</strong>: melden, afhandelen en leren van beveiligingsincidenten en datalekken.</li>
<li><strong>Continuïteit</strong>: back-ups, herstel en doorwerken bij uitval.</li>
<li><strong>Bewustwording</strong>: training van medewerkers, want de meeste incidenten beginnen bij een klik.</li>
</ul>
<h2>Moet ik me laten certificeren?</h2>
<p>De wet verplicht het werken volgens de norm, niet het certificaat. Een certificaat van een geaccrediteerde instelling bewijst wel dat je het aantoonbaar op orde hebt. Grote zorginstellingen en ICT-leveranciers in de zorg laten zich vrijwel allemaal certificeren; zorgverzekeraars, ketenpartners en aanbestedingen vragen er steeds vaker om. Een kleine praktijk kan ook kiezen voor een zelfverklaring of een toetsing door een externe adviseur.</p>
<h2>Wat kost NEN 7510?</h2>
<p>Voor een kleine praktijk gaat het vooral om tijd: beleid vastleggen, afspraken met leveranciers controleren en medewerkers trainen. Reken met begeleiding op enkele duizenden euro's. Voor een instelling die zich laat certificeren, ligt het totaal doorgaans tussen 15.000 en 60.000 euro, afhankelijk van de omvang en het vertrekpunt, plus jaarlijkse controle-audits. Heb je al ISO 27001, dan is de stap naar NEN 7510 klein: de structuur is dezelfde.</p>
<h2>Checklist: zo begin je</h2>
<ol>
<li>Ga na welke norm op je van toepassing is: NEN 7510 voor elke zorgaanbieder, NEN 7512 en 7513 zodra je gegevens uitwisselt of dossiers bijhoudt.</li>
<li>Maak een inventaris van systemen, gegevens en leveranciers.</li>
<li>Voer een risicoanalyse uit en leg de maatregelen vast die je neemt.</li>
<li>Controleer verwerkersovereenkomsten en de certificaten van je leveranciers.</li>
<li>Zet logging en toegangsbeheer op orde.</li>
<li>Train medewerkers en leg een procedure vast voor incidenten en datalekken.</li>
<li>Plan een interne audit, en beslis daarna of je certificering wilt.</li>
</ol>
<p>Meer over de basis vind je in onze gids over <a href="/kennisbank/iso-27001/">ISO 27001</a>. Valt je organisatie ook onder de Cyberbeveiligingswet, lees dan <a href="/nl/cyberbeveiligingswet-nis2/">wat die voor de zorg betekent</a>.</p>
""",
    faq=[
        ("Is NEN 7510 verplicht?", "Ja. Via de Wabvpz en het Besluit elektronische gegevensverwerking door zorgaanbieders moet elke zorgaanbieder die patiëntgegevens elektronisch verwerkt volgens NEN 7510, 7512 en 7513 werken. Een certificaat is niet verplicht, werken volgens de norm wel."),
        ("Wat is het verschil tussen NEN 7510 en ISO 27001?", "NEN 7510 is de Nederlandse zorgversie van ISO 27001 en 27002: dezelfde structuur en maatregelen, aangevuld met eisen voor patiëntgegevens. Wie ISO 27001 heeft, kan NEN 7510 er relatief eenvoudig bij halen."),
        ("Wat is er nieuw in NEN 7510:2024?", "De norm is afgestemd op ISO 27001:2022 en 27002:2022, met 14 aangepaste en 8 extra maatregelen voor de zorg, en aandacht voor de Wegiz en NIS2. Overstappen moet vóór 20 februari 2027."),
        ("Geldt NEN 7510 ook voor een kleine praktijk?", "Ja. Ook een huisarts, tandarts of fysiotherapeut moet volgens de norm werken. De maatregelen schalen mee met de grootte; certificering is voor kleine praktijken meestal niet nodig."),
        ("Wie controleert NEN 7510?", "De Inspectie Gezondheidszorg en Jeugd (IGJ) houdt toezicht op zorgaanbieders; de Autoriteit Persoonsgegevens op de verwerking van persoonsgegevens."),
    ],
    sources=[("NEN: NEN 7510 informatiebeveiliging in de zorg", "https://www.nen.nl/zorg-welzijn/informatiebeveiliging-in-de-zorg"),
             ("Kiwa: NEN 7510 voor informatiebeveiliging zorg vernieuwd", "https://www.kiwa.com/nl/nl/over-kiwa/nieuws/nen-7510-voor-informatiebeveiliging-zorg-vernieuwd/"),
             ("Inspectie Gezondheidszorg en Jeugd", "https://www.igj.nl")],
),
dict(
    path="/kennisbank/iso-27002/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["iso", "maatregelen"], updated="2026-10-11",
    title="ISO 27002: maatregelen en verschil met 27001 | Cyberdijk",
    desc="ISO 27002 uitgelegd: wat de norm is, de 93 maatregelen in vier thema's, het verschil met ISO 27001 en waarom je er niet voor gecertificeerd kunt worden.",
    h1="ISO 27002: wat is het en wat is het verschil met ISO 27001?",
    lede="ISO/IEC 27002 is de handleiding bij ISO 27001. Waar 27001 zegt wát je moet regelen, legt 27002 per maatregel uit hóe je dat doet. Je kunt er niet voor gecertificeerd worden, maar zonder 27002 bouw je geen goed ISMS.",
    kort=[
        "ISO 27001 bevat de eisen en is certificeerbaar; ISO 27002 is de toelichting bij de maatregelen en is dat niet.",
        "De versie 2022 telt 93 maatregelen in vier thema's: organisatorisch, mensgericht, fysiek en technologisch.",
        "Elke maatregel heeft attributen (zoals preventief of detectief) waarmee je ze kunt sorteren en koppelen aan risico's.",
    ],
    body="""
<h2>ISO 27001 en 27002 naast elkaar</h2>
<div style="overflow-x:auto"><table style="min-width:520px">
<thead><tr><th></th><th>ISO/IEC 27001</th><th>ISO/IEC 27002</th></tr></thead>
<tbody>
<tr><td>Wat</td><td>Eisen aan een managementsysteem voor informatiebeveiliging (ISMS)</td><td>Richtlijnen bij de beheersmaatregelen</td></tr>
<tr><td>Certificeerbaar</td><td>Ja</td><td>Nee</td></tr>
<tr><td>Maatregelen</td><td>Bijlage A: lijst van 93 maatregelen, één regel per maatregel</td><td>Dezelfde 93 maatregelen, elk met doel, uitleg en implementatietips</td></tr>
<tr><td>Gebruik</td><td>Wat je moet aantonen bij de audit</td><td>Hoe je de maatregelen in de praktijk invult</td></tr>
</tbody></table></div>
<h2>De vier thema's van ISO 27002:2022</h2>
<ul>
<li><strong>Organisatorisch (37 maatregelen):</strong> beleid, rollen, leveranciersbeheer, incidentbeheer, continuïteit, naleving van wetgeving.</li>
<li><strong>Mensgericht (8):</strong> screening, arbeidsvoorwaarden, bewustwording en training, disciplinaire procedure, thuiswerken.</li>
<li><strong>Fysiek (14):</strong> toegang tot gebouwen en ruimtes, apparatuur, bekabeling, veilig afvoeren van media.</li>
<li><strong>Technologisch (34):</strong> toegangsbeheer, versleuteling, logging, back-ups, netwerkbeveiliging, veilige ontwikkeling, beheer van kwetsbaarheden.</li>
</ul>
<p>Nieuw in de versie 2022 zijn onder meer dreigingsinformatie, beveiliging van clouddiensten, gereedheid voor continuïteit, fysieke monitoring, configuratiebeheer, wissen van informatie, maskeren van gegevens, voorkomen van gegevenslekken, monitoring van activiteiten, webfiltering en veilig programmeren.</p>
<h2>Attributen: maatregelen slim sorteren</h2>
<p>Elke maatregel in 27002:2022 heeft vijf attributen: het type (preventief, detectief, correctief), de eigenschap van informatie (vertrouwelijkheid, integriteit, beschikbaarheid), het cyberbeveiligingsconcept (identificeren, beschermen, detecteren, reageren, herstellen), het operationele domein en het beveiligingsdomein. Daarmee kun je bijvoorbeeld snel alle detectieve maatregelen voor beschikbaarheid selecteren, of de koppeling met het NIST-raamwerk of CyFun maken.</p>
<h2>Hoe gebruik je ISO 27002 in de praktijk?</h2>
<ol>
<li>Voer eerst een risicoanalyse uit volgens ISO 27001.</li>
<li>Kies per risico de maatregelen uit bijlage A die het risico verkleinen.</li>
<li>Lees in ISO 27002 hoe je elke gekozen maatregel invult en wat de auditor verwacht.</li>
<li>Leg in de verklaring van toepasselijkheid vast welke maatregelen je toepast en waarom je andere weglaat.</li>
</ol>
<p>De volledige lijst van de 93 maatregelen vind je in <a href="/kennisbank/iso-27001-maatregelen/">ISO 27001: de 93 maatregelen uitgelegd</a>. Het hele traject naar certificering staat in <a href="/kennisbank/iso-27001/">de gids over ISO 27001</a>.</p>
""",
    faq=[
        ("Kan ik een ISO 27002-certificaat halen?", "Nee. ISO 27002 is een richtlijn, geen eisennorm. Je certificeert je voor ISO 27001; daarin verwijst bijlage A naar de maatregelen die 27002 toelicht."),
        ("Hoeveel maatregelen telt ISO 27002:2022?", "93, verdeeld over vier thema's: 37 organisatorische, 8 mensgerichte, 14 fysieke en 34 technologische maatregelen. De vorige versie had er 114 in 14 hoofdstukken."),
        ("Moet ik alle 93 maatregelen toepassen?", "Nee. Je kiest op basis van je risicoanalyse welke maatregelen van toepassing zijn, en je onderbouwt in de verklaring van toepasselijkheid waarom je andere weglaat."),
        ("Is ISO 27002 nuttig zonder certificering?", "Ja. Het is een praktische handleiding voor elke organisatie die haar beveiliging gestructureerd wil opzetten, ook zonder audit."),
    ],
    sources=[("ISO: de norm ISO/IEC 27002", "https://www.iso.org/standard/75652.html"), ("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001")],
),
dict(
    path="/kennisbank/iso-27000-familie/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["iso", "privacy", "cloud"], updated="2026-10-11",
    title="ISO 27000-familie: welke norm heb je nodig? | Cyberdijk",
    desc="De ISO 27000-reeks uitgelegd: 27001, 27002, 27005, 27017, 27018, 27701 en 27799. Wat elke norm doet, welke certificeerbaar is en welke jij nodig hebt.",
    h1="De ISO 27000-familie: welke norm heb je wanneer nodig?",
    lede="ISO 27001 is de bekendste, maar de reeks 27000 telt tientallen normen voor informatiebeveiliging, privacy en cloud. De meeste zijn richtlijnen. Dit overzicht zegt wat elke norm doet en wanneer je ze nodig hebt.",
    kort=[
        "Alleen ISO 27001 en ISO 27701 zijn certificeerbaar; de andere normen zijn richtlijnen die je daarbij helpen.",
        "ISO 27017 en 27018 zijn voor cloudaanbieders, ISO 27799 en NEN 7510 voor de zorg.",
        "Begin altijd met 27001 en 27002; de rest komt erbij als je sector of klanten erom vragen.",
    ],
    body="""
<h2>Overzicht van de belangrijkste normen</h2>
<div style="overflow-x:auto"><table style="min-width:560px">
<thead><tr><th>Norm</th><th>Wat</th><th>Certificeerbaar</th><th>Voor wie</th></tr></thead>
<tbody>
<tr><td><strong>ISO 27000</strong></td><td>Overzicht en begrippen van de hele reeks</td><td>Nee</td><td>Iedereen die start</td></tr>
<tr><td><strong>ISO 27001</strong></td><td>Eisen aan een managementsysteem voor informatiebeveiliging (ISMS)</td><td>Ja</td><td>Elke organisatie</td></tr>
<tr><td><strong>ISO 27002</strong></td><td>Toelichting bij de 93 beheersmaatregelen</td><td>Nee</td><td>Wie 27001 invoert</td></tr>
<tr><td><strong>ISO 27005</strong></td><td>Richtlijnen voor risicobeheer</td><td>Nee</td><td>Wie de risicoanalyse opzet</td></tr>
<tr><td><strong>ISO 27017</strong></td><td>Extra maatregelen voor clouddiensten</td><td>Als aanvulling op 27001</td><td>Cloudaanbieders en grote cloudgebruikers</td></tr>
<tr><td><strong>ISO 27018</strong></td><td>Bescherming van persoonsgegevens in de publieke cloud</td><td>Als aanvulling op 27001</td><td>Cloudaanbieders die persoonsgegevens verwerken</td></tr>
<tr><td><strong>ISO 27701</strong></td><td>Managementsysteem voor privacy (PIMS)</td><td>Ja, sinds de versie 2025 ook zelfstandig</td><td>Wie de AVG aantoonbaar wil naleven</td></tr>
<tr><td><strong>ISO 27799</strong></td><td>Informatiebeveiliging in de zorg (internationaal)</td><td>Nee</td><td>Zorgorganisaties; in Nederland geldt NEN 7510</td></tr>
<tr><td><strong>ISO 27035</strong></td><td>Beheer van beveiligingsincidenten</td><td>Nee</td><td>Wie een incidentproces opzet</td></tr>
<tr><td><strong>ISO 27036</strong></td><td>Beveiliging in leveranciersrelaties</td><td>Nee</td><td>Wie leveranciers moet beoordelen, bijvoorbeeld onder NIS2</td></tr>
</tbody></table></div>
<h2>Welke norm heb jij nodig?</h2>
<ul>
<li><strong>Je wilt aantonen dat je beveiliging op orde is:</strong> <a href="/kennisbank/iso-27001/">ISO 27001</a>, met <a href="/kennisbank/iso-27002/">27002</a> als handleiding.</li>
<li><strong>Je levert clouddiensten:</strong> 27001 plus 27017, en 27018 als je persoonsgegevens verwerkt.</li>
<li><strong>Je wilt de AVG aantoonbaar naleven:</strong> <a href="/kennisbank/iso-27701/">ISO 27701</a>.</li>
<li><strong>Je werkt in de zorg in Nederland:</strong> <a href="/kennisbank/nen-7510/">NEN 7510</a>, de Nederlandse uitwerking van 27001 en 27799.</li>
<li><strong>Je valt onder NIS2:</strong> 27001 als bewijs van je maatregelen, 27036 voor je leveranciers. In België is <a href="/be/nis2-cyfun/">CyFun</a> het alternatief.</li>
</ul>
<h2>Veelgemaakte fouten</h2>
<p>Organisaties zeggen soms "ISO 27002-gecertificeerd" te zijn; dat bestaat niet. Ook "ISO 27000" op een website is meestal een losse verwijzing naar de reeks. Vraag bij een leverancier altijd naar het certificaat zelf: welke norm, welke scope, welke certificerende instelling en tot wanneer geldig.</p>
""",
    faq=[
        ("Wat is het verschil tussen ISO 27000 en ISO 27001?", "ISO 27000 is het overzicht met begrippen van de hele reeks. ISO 27001 bevat de eisen aan een managementsysteem en is de norm waarvoor je gecertificeerd wordt."),
        ("Welke ISO 27000-normen zijn certificeerbaar?", "ISO 27001 en ISO 27701. ISO 27017 en 27018 kun je laten toetsen als aanvulling op een 27001-certificaat. De andere normen zijn richtlijnen."),
        ("Heb ik ISO 27017 of 27018 nodig?", "Alleen als je zelf clouddiensten levert of op grote schaal persoonsgegevens in de cloud verwerkt voor klanten. Voor de meeste kmo's volstaat 27001."),
        ("Welke norm geldt voor de zorg?", "Internationaal ISO 27799, in Nederland NEN 7510, die wettelijk verplicht is voor zorgaanbieders."),
    ],
    sources=[("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001"), ("ISO: ISO/IEC 27000-familie", "https://www.iso.org/standard/iso-iec-27000-family")],
),
dict(
    path="/kennisbank/iso-27701/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["iso", "privacy", "avg", "gdpr"], updated="2026-10-11",
    title="ISO 27701: privacy aantoonbaar op orde (PIMS) | Cyberdijk",
    desc="ISO 27701 uitgelegd: de norm voor een privacymanagementsysteem, wat er nieuw is in 2025, de link met de AVG en wanneer certificering loont.",
    h1="ISO 27701: de norm om je privacybeleid aantoonbaar te maken",
    lede="De AVG vraagt dat je kunt aantonen dat je persoonsgegevens goed beschermt. ISO/IEC 27701 geeft daar een structuur voor: een managementsysteem voor privacy, kortweg PIMS. Sinds de versie 2025 kun je er ook zonder ISO 27001 voor gecertificeerd worden.",
    kort=[
        "ISO 27701 beschrijft een Privacy Information Management System (PIMS) met aparte eisen voor verwerkingsverantwoordelijken en verwerkers.",
        "De versie 2025 is een zelfstandige norm; een ISO 27001-certificaat is niet langer een voorwaarde.",
        "Het certificaat is geen officiële AVG-certificering, maar wel een sterk bewijs van verantwoordingsplicht.",
    ],
    body="""
<h2>Wat is ISO 27701?</h2>
<p>ISO/IEC 27701 beschrijft hoe een organisatie de bescherming van persoonsgegevens structureel beheert: beleid, rollen, risicoanalyse op privacy, maatregelen, en continue verbetering. De norm maakt onderscheid tussen de verplichtingen van een <strong>verwerkingsverantwoordelijke</strong> (wie bepaalt waarom en hoe gegevens verwerkt worden) en een <strong>verwerker</strong> (wie dat in opdracht doet). Dat sluit rechtstreeks aan op de rolverdeling in de AVG.</p>
<h2>Wat is er nieuw in de versie 2025?</h2>
<p>De eerste versie uit 2019 was een uitbreiding op ISO 27001: zonder 27001-certificaat geen 27701. De versie 2025 is een zelfstandige managementsysteemnorm met dezelfde structuur als de andere ISO-normen. Een organisatie kan zich nu rechtstreeks voor 27701 laten certificeren, al blijft de combinatie met 27001 logisch voor wie beide wil aantonen. Er ligt meer nadruk op governance, verantwoording en transparantie, en op moderne technologie en internationale doorgifte. Voor bestaande certificaten geldt een overgangsperiode.</p>
<h2>Wat vraagt de norm?</h2>
<ul>
<li>Een <strong>register</strong> van verwerkingen en een duidelijke grondslag per verwerking.</li>
<li><strong>Privacyrisicoanalyses</strong>, en waar nodig een DPIA.</li>
<li>Procedures voor <strong>rechten van betrokkenen</strong>: inzage, correctie, verwijdering, bezwaar.</li>
<li><strong>Afspraken met verwerkers</strong> en controle op hun naleving.</li>
<li>Maatregelen voor <strong>dataminimalisatie</strong>, bewaartermijnen en versleuteling.</li>
<li>Een proces voor <strong>datalekken</strong>, inclusief de melding binnen 72 uur.</li>
<li>Regels voor <strong>doorgifte</strong> buiten de EU.</li>
</ul>
<h2>Is ISO 27701 een AVG-certificaat?</h2>
<p>Nee. De AVG voorziet in eigen certificeringsmechanismen die door toezichthouders moeten worden goedgekeurd, en ISO 27701 is daar geen van. Het certificaat toont wel aan dat je privacybeheer systematisch is opgezet en extern getoetst. In de praktijk weegt dat zwaar bij klanten, aanbestedingen en toezichthouders, zeker voor verwerkers zoals softwarebedrijven, hostingpartijen en dienstverleners met veel klantgegevens.</p>
<h2>Voor wie is het de moeite waard?</h2>
<ul>
<li>Verwerkers die voor veel klanten persoonsgegevens verwerken: SaaS, hosting, marketingbureaus, callcenters, salarisverwerkers.</li>
<li>Organisaties met gevoelige gegevens: zorg, hr-dienstverleners, financiële dienstverleners.</li>
<li>Bedrijven die al ISO 27001 hebben en hun privacybeheer op hetzelfde niveau willen brengen.</li>
</ul>
<p>Wie nog geen managementsysteem heeft, begint beter met de <a href="/kennisbank/avg-checklist-kmo/">AVG-checklist voor kmo's en mkb</a> en het <a href="/kennisbank/verwerkingsregister/">verwerkingsregister</a>. Het overzicht van alle normen staat in <a href="/kennisbank/iso-27000-familie/">de ISO 27000-familie</a>.</p>
""",
    faq=[
        ("Heb ik ISO 27001 nodig voor ISO 27701?", "Niet meer. Sinds de versie 2025 is ISO 27701 een zelfstandige norm. De combinatie blijft wel gebruikelijk, omdat privacy en informatiebeveiliging sterk overlappen."),
        ("Is ISO 27701 verplicht onder de AVG?", "Nee. De AVG verplicht geen enkele norm. ISO 27701 is een vrijwillige manier om je verantwoordingsplicht aantoonbaar in te vullen."),
        ("Wat kost ISO 27701?", "Vergelijkbaar met ISO 27001: voor een kmo doorgaans 10.000 tot 40.000 euro voor begeleiding, eigen tijd en audit, lager als je al een 27001-systeem hebt."),
        ("Wat is een PIMS?", "Een Privacy Information Management System: het geheel van beleid, processen en maatregelen waarmee je de bescherming van persoonsgegevens beheert en verbetert."),
    ],
    sources=[("ISO: de norm ISO/IEC 27701", "https://www.iso.org/standard/27701"),
             ("Kiwa: ISO/IEC 27701:2025 gepubliceerd", "https://www.kiwa.com/nl/nl/over-kiwa/nieuws/isoiec-277012025-gepubliceerd-vernieuwde-privacy-standaard-biedt-organisaties-meer-houvast/"),
             ("AVG (Verordening (EU) 2016/679) op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2016/679/oj")],
),
dict(
    path="/kennisbank/iso-27001-kosten/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["iso", "kosten", "certificering"], updated="2026-10-11",
    title="ISO 27001 kosten: wat betaal je echt? | Cyberdijk",
    desc="Wat kost ISO 27001 voor een kmo of mkb-bedrijf? Begeleiding, eigen uren, tools, audit en jaarlijkse kosten, met rekenvoorbeelden en bespaartips.",
    h1="ISO 27001 kosten: wat betaal je echt voor certificering?",
    lede="De prijs van ISO 27001 bestaat uit vier delen: begeleiding, eigen tijd, technische aanpassingen en de audit. Voor een kmo komt dat samen meestal uit tussen 15.000 en 50.000 euro, en daarna enkele duizenden euro's per jaar. Hier zie je waar het geld naartoe gaat en hoe je bespaart.",
    kort=[
        "Certificatie-audit: 5.000 tot 15.000 euro voor de eerste cyclus, afhankelijk van grootte en scope.",
        "Begeleiding: 5.000 tot 25.000 euro; eigen uren vaak het grootste, onzichtbare deel.",
        "Jaarlijks daarna: 2.000 tot 6.000 euro voor controle-audits plus het onderhoud van het systeem.",
    ],
    body="""
<h2>De vier kostenposten</h2>
<div style="overflow-x:auto"><table style="min-width:560px">
<thead><tr><th>Kostenpost</th><th>Klein bedrijf (10-25 mensen)</th><th>Middelgroot (50-150 mensen)</th></tr></thead>
<tbody>
<tr><td>Externe begeleiding</td><td>€5.000 – €12.000</td><td>€12.000 – €25.000</td></tr>
<tr><td>Eigen uren (schatting)</td><td>150 – 300 uur</td><td>400 – 800 uur</td></tr>
<tr><td>Tools en technische aanpassingen</td><td>€1.000 – €5.000</td><td>€5.000 – €15.000</td></tr>
<tr><td>Certificatie-audit (fase 1 + 2)</td><td>€5.000 – €8.000</td><td>€8.000 – €15.000</td></tr>
<tr><td><strong>Totaal eerste jaar</strong></td><td><strong>€15.000 – €25.000</strong></td><td><strong>€30.000 – €50.000+</strong></td></tr>
<tr><td>Jaarlijkse controle-audit</td><td>€2.000 – €3.500</td><td>€3.500 – €6.000</td></tr>
</tbody></table></div>
<p>Bedragen excl. btw, gebaseerd op gangbare tarieven in België en Nederland in 2026. De audit wordt berekend op het aantal medewerkers binnen de scope en het aantal locaties; certificerende instellingen rekenen een vast aantal auditdagen per grootteklasse.</p>
<h2>Waar het geld naartoe gaat</h2>
<ul>
<li><strong>Begeleiding:</strong> een consultant die de risicoanalyse, het beleid en de documentatie mee opzet. Hoe meer je zelf doet, hoe lager deze post.</li>
<li><strong>Eigen tijd:</strong> de grootste verborgen kost. Iemand moet het systeem trekken, en elke afdeling levert input. Reken dat uur in.</li>
<li><strong>Tools:</strong> een wachtwoordmanager, MFA, logging, back-upoplossing, eventueel software voor het ISMS zelf. Veel kmo's hebben het meeste al.</li>
<li><strong>Audit:</strong> fase 1 toetst de documentatie, fase 2 de werking. Vraag offertes bij minstens drie geaccrediteerde instellingen; de verschillen zijn groot.</li>
</ul>
<h2>Zo houd je de kosten laag</h2>
<ol>
<li><strong>Kies een smalle scope.</strong> Begin met de afdeling of dienst waar klanten om vragen, breid later uit.</li>
<li><strong>Doe de basis zelf.</strong> Inventaris, risicoanalyse en beleid kun je met een goed sjabloon grotendeels zelf. Laat een adviseur het nakijken in plaats van alles schrijven.</li>
<li><strong>Gebruik wat je al hebt.</strong> Bestaande procedures, IT-beleid en leverancierscontracten tellen mee.</li>
<li><strong>Vraag subsidie aan.</strong> In Vlaanderen komt advies rond cybersecurity in aanmerking voor de kmo-portefeuille. In Nederland bestaan regionale regelingen en de cyberweerbaarheidssubsidies via het Digital Trust Center en de regionale ontwikkelingsmaatschappijen.</li>
<li><strong>Combineer normen.</strong> Wie ook NEN 7510 of ISO 27701 wil, laat ze in één audit meenemen.</li>
</ol>
<h2>Wat levert het op?</h2>
<p>De kosten staan tegenover wat je zonder certificaat verliest: aanbestedingen waar het een eis is, klanten die een alternatief zoeken, en de schade van een incident dat je had kunnen voorkomen. Voor een IT- of softwarebedrijf is één behouden klant vaak genoeg om de investering terug te verdienen. Onder <a href="/kennisbank/nis2/">NIS2</a> is het certificaat bovendien een erkend bewijs van je maatregelen.</p>
<p>Het hele traject staat in <a href="/kennisbank/iso-27001/">de gids over ISO 27001</a>; de stappen per land in <a href="/be/iso-27001/">ISO 27001 in België</a> en <a href="/nl/iso-27001/">ISO 27001 in Nederland</a>.</p>
""",
    faq=[
        ("Wat kost een ISO 27001-audit?", "De certificatie-audit kost voor een klein bedrijf doorgaans 5.000 tot 8.000 euro, voor een middelgroot bedrijf 8.000 tot 15.000 euro. Daarna volgen jaarlijkse controle-audits van 2.000 tot 6.000 euro."),
        ("Kan ik ISO 27001 halen zonder consultant?", "Ja, als iemand intern de tijd en de kennis heeft. De meeste kmo's laten de risicoanalyse en de documentatie wel nakijken; dat is goedkoper dan alles uitbesteden."),
        ("Hoe lang blijft een certificaat geldig?", "Drie jaar, met elk jaar een controle-audit. Na drie jaar volgt een hercertificering, die iets goedkoper is dan de eerste audit."),
        ("Zijn er subsidies voor ISO 27001?", "In Vlaanderen via de kmo-portefeuille voor advies rond cybersecurity. In Nederland via regionale regelingen; informeer bij het Digital Trust Center of je regionale ontwikkelingsmaatschappij."),
    ],
    sources=[("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001"), ("VLAIO: kmo-portefeuille", "https://www.vlaio.be/nl/subsidies-financiering/kmo-portefeuille"), ("Digital Trust Center", "https://www.digitaltrustcenter.nl")],
),
dict(
    path="/kennisbank/nis2-checklist/", lang="nl", kind="artikel", land="eu", crumbs=[("Kennisbank", "/kennisbank/")],
    tags=["nis2", "checklist", "maatregelen", "registratie", "meldplicht"], updated="2026-10-11",
    title="NIS2-checklist: 20 punten voor BE en NL | Cyberdijk",
    desc="NIS2-checklist in 20 punten: toepasselijkheid, registratie, de tien maatregelen, meldplicht en bestuur. Voor België (CCB) en Nederland (Cbw).",
    h1="NIS2-checklist: 20 punten om na te lopen",
    lede="Val je onder NIS2, dan moet je een reeks zaken aantoonbaar geregeld hebben. Deze checklist loopt ze in volgorde af, met per punt wat de toezichthouder wil zien. Print hem, vink af, en je weet waar je staat.",
    kort=[
        "Vijf blokken: toepasselijkheid, registratie, maatregelen, meldplicht en bestuur.",
        "In België toon je de maatregelen aan met CyFun of ISO 27001; in Nederland met je eigen documentatie of ISO 27001.",
        "Elke stap moet aantoonbaar zijn: een beleid dat niemand kent, telt niet.",
    ],
    body="""
<h2>1. Toepasselijkheid</h2>
<ol>
<li>Wij hebben vastgesteld of we in een NIS2-sector actief zijn. <a href="/kennisbank/valt-mijn-bedrijf-onder-nis2/">Zo check je dat.</a></li>
<li>Wij weten of we een essentiële of een belangrijke entiteit zijn (grootte en sector).</li>
<li>Wij weten welke wet geldt: de Belgische NIS2-wet (CCB) of de Nederlandse Cyberbeveiligingswet (NCSC).</li>
</ol>
<h2>2. Registratie</h2>
<ol start="4">
<li>Wij zijn geregistreerd: in België via Safeonweb@Work bij het CCB, in Nederland in het entiteitenregister van het NCSC.</li>
<li>Onze contactgegevens voor incidenten zijn actueel en worden bewaakt, ook buiten de kantooruren.</li>
</ol>
<h2>3. De maatregelen (zorgplicht)</h2>
<ol start="6">
<li>Er is een actuele risicoanalyse en een beleid voor informatiebeveiliging, goedgekeurd door het bestuur.</li>
<li>Er is een procedure voor incidentbeheer: detecteren, afhandelen, documenteren.</li>
<li>Back-ups en continuïteit zijn geregeld en getest: we kunnen terug na een ransomware-aanval.</li>
<li>Leveranciers en dienstverleners zijn beoordeeld; beveiligingseisen staan in de contracten.</li>
<li>Beveiliging is onderdeel van aankoop, ontwikkeling en onderhoud van systemen, inclusief kwetsbaarhedenbeheer.</li>
<li>We meten of de maatregelen werken: interne audits, tests, rapportage.</li>
<li>Medewerkers krijgen training in cyberhygiëne; het bestuur volgt een opleiding.</li>
<li>Versleuteling is geregeld waar nodig: gegevens in opslag en onderweg.</li>
<li>Toegangsbeheer en personeelsbeveiliging zijn op orde: wie heeft toegang tot wat, en wat gebeurt er bij vertrek.</li>
<li>Multifactorauthenticatie staat aan voor e-mail, beheer en toegang op afstand; communicatie is beveiligd.</li>
</ol>
<p>De volledige uitleg per maatregel staat in <a href="/kennisbank/nis2-maatregelen/">NIS2: de tien maatregelen</a>. In België kies je een <a href="/kennisbank/cyfun-niveaus/">CyFun-niveau</a> of ISO 27001 om dit aan te tonen.</p>
<h2>4. Meldplicht</h2>
<ol start="16">
<li>We weten wat een significant incident is en wie beslist of we melden.</li>
<li>De drie termijnen staan in de procedure: waarschuwing binnen 24 uur, melding binnen 72 uur, eindverslag binnen een maand. <a href="/kennisbank/nis2-meldplicht-incident/">Zo werkt het.</a></li>
<li>Een datalek met persoonsgegevens melden we daarnaast apart aan de GBA of de AP.</li>
</ol>
<h2>5. Bestuur en bewijs</h2>
<ol start="19">
<li>Het bestuur heeft de maatregelen goedgekeurd, volgt ze op en kent zijn <a href="/kennisbank/nis2-bestuur-aansprakelijkheid/">aansprakelijkheid</a>.</li>
<li>Alles is gedocumenteerd en terug te vinden: beleid, risicoanalyse, registraties, audits, trainingen, meldingen. Essentiële entiteiten in België plannen hun conformiteitsbeoordeling vóór 18 april 2027.</li>
</ol>
<h2>Niet onder NIS2, wel een vragenlijst gekregen?</h2>
<p>Dan gebruik je dezelfde checklist, zonder de registratie en de meldplicht. Je klant wil vooral de punten 6 tot 15 zien. <a href="/kennisbank/nis2-vragenlijst-leverancier/">Zo beantwoord je een NIS2-vragenlijst als leverancier.</a> Het volledige overzicht staat in <a href="/kennisbank/nis2/">de NIS2-gids voor België en Nederland</a>.</p>
""",
    faq=[
        ("Is er een officiële NIS2-checklist?", "Nee. De richtlijn noemt tien categorieën maatregelen; België werkt ze uit in CyFun, Nederland in de Cyberbeveiligingswet en de toelichting van het NCSC. Deze checklist volgt die structuur."),
        ("Waar begin ik als ik nog niets heb?", "Bij punt 1 tot 5: weet of je eronder valt en registreer je. Daarna de risicoanalyse en de maatregelen met de grootste winst: multifactorauthenticatie, back-ups en updates."),
        ("Moet ik alles tegelijk klaar hebben?", "In Nederland gelden de plichten sinds 15 augustus 2026. In België geldt de wet sinds oktober 2024, met 18 april 2027 als deadline voor de beoordeling van essentiële entiteiten. Toezichthouders kijken naar aantoonbare voortgang."),
        ("Telt ISO 27001 als bewijs voor NIS2?", "In België is het een erkend alternatief voor CyFun. In Nederland kun je het gebruiken om je zorgplicht aan te tonen."),
    ],
    sources=[("Richtlijn (EU) 2022/2555 (NIS2) op EUR-Lex", "https://eur-lex.europa.eu/eli/dir/2022/2555/oj"), ("Centrum voor Cybersecurity België (CCB)", "https://ccb.belgium.be"), ("Nationaal Cyber Security Centrum (NCSC)", "https://www.ncsc.nl")],
),
]


def toepassen(pages, bronnen_kmo):
    """Past de uitbreidingen toe op de bestaande artikels en voegt de nieuwe toe."""
    for p in pages:
        u = UITBREIDING.get(p["path"])
        if not u:
            continue
        p["body"] = p["body"] + u["body"]
        p["faq"] = list(p["faq"]) + u["faq"]
        for k in ("title", "desc", "updated"):
            if u.get(k):
                p[k] = u[k]
    for p in pages:
        if p["path"].startswith("/kennisbank/") and p["path"] not in ("/kennisbank/nis2/", "/kennisbank/iso-27001/"):
            tags = p.get("tags") or []
            extra = []
            if "nis2" in tags:
                extra.append('<a href="/kennisbank/nis2/">de complete NIS2-gids voor België en Nederland</a>')
            if "iso" in tags:
                extra.append('<a href="/kennisbank/iso-27001/">de complete gids over ISO 27001</a>')
            if extra:
                p["body"] = p["body"] + "<p><strong>Overzicht nodig?</strong> Lees " + " en ".join(extra) + ".</p>"
    # Kruislinks naar artikels die anders maar één interne link hebben (SEO-doorlichting 15 okt)
    KRUIS = {
        "/kennisbank/datalek-melden-72-uur/": [("/kennisbank/website-gehackt-datalek-melden/", "wat je doet als je website gehackt is en of dat een datalek is")],
        "/kennisbank/website-gehackt-datalek-melden/": [("/kennisbank/datalek-melden-72-uur/", "het stappenplan om een datalek binnen 72 uur te melden")],
        "/kennisbank/verwerkingsregister/": [("/kennisbank/camerabewaking-avg/", "de regels voor camerabewaking onder de AVG"), ("/kennisbank/inzageverzoek-avg/", "hoe je een inzageverzoek afhandelt")],
        "/kennisbank/inzageverzoek-avg/": [("/kennisbank/camerabewaking-avg/", "camerabeelden en de AVG")],
        "/kennisbank/camerabewaking-avg/": [("/kennisbank/inzageverzoek-avg/", "wat je doet als iemand zijn camerabeelden opvraagt")],
        "/kennisbank/cybersecurity-kmo-mkb/": [("/kennisbank/toegankelijkheidswet-website/", "de toegankelijkheidswet voor websites"), ("/kennisbank/website-gehackt-datalek-melden/", "website gehackt: datalek of niet")],
        "/kennisbank/ai-act-kmo-mkb/": [("/kennisbank/ai-tekst-labelen-watermerk/", "wanneer je AI-tekst en -beelden moet labelen")],
        "/kennisbank/toegankelijkheidswet-website/": [("/kennisbank/cybersecurity-kmo-mkb/", "cybersecurity voor kmo en mkb in gewone taal")],
    }
    for p in pages:
        k = KRUIS.get(p["path"])
        if k:
            p["body"] = p["body"] + "<p><strong>Lees ook:</strong> " + ", ".join(f'<a href="{u}">{t}</a>' for u, t in k) + ".</p>"
    for n in NIEUW:
        if not any(p["path"] == n["path"] for p in pages):
            n = dict(n)
            n["sources"] = n.get("sources") or bronnen_kmo
            pages.append(n)
    for p in pages:
        k = KRUIS.get(p["path"])
        if k and "<strong>Lees ook:</strong>" not in p["body"]:
            p["body"] = p["body"] + "<p><strong>Lees ook:</strong> " + ", ".join(f'<a href="{u}">{t}</a>' for u, t in k) + ".</p>"
    return pages
