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
            n["sources"] = bronnen_kmo
            pages.append(n)
    return pages
