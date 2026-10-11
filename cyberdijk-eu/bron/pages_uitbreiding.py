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
    for n in NIEUW:
        if not any(p["path"] == n["path"] for p in pages):
            n = dict(n)
            n["sources"] = n.get("sources") or bronnen_kmo
            pages.append(n)
    return pages
