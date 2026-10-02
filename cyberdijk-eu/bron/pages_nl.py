NCSC = ("Nationaal Cyber Security Centrum (NCSC)", "https://www.ncsc.nl")
RIJK = ("Rijksoverheid", "https://www.rijksoverheid.nl")
DTC = ("Digital Trust Center", "https://www.digitaltrustcenter.nl")
AP = ("Autoriteit Persoonsgegevens", "https://www.autoriteitpersoonsgegevens.nl")
ISO = ("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001")
FM = ("Forvis Mazars: Cyberbeveiligingswet in werking op 15 augustus 2026", "https://www.forvismazars.com/nl/nl/wie-zijn-wij/nieuws-events-en-publicaties/nieuws/cyberbeveiligingswet-vanaf-15-augustus-2026")
MAAS = ("MaasISO: prijsindicatie ISO 27001 voor mkb", "https://www.maasiso.nl/")

NL = [("Nederland", "/nl/")]

PAGES = [
dict(
    path="/nl/", lang="nl-NL", kind="hub", land="nl", alt="/be/", crumbs=[],
    title="NIS2, ISO 27001 en AVG voor mkb in West-Brabant | Cyberdijk",
    desc="De Cyberbeveiligingswet geldt sinds 15 augustus 2026. Wat betekent dat voor je bedrijf in Roosendaal, Bergen op Zoom of Breda? Doe de gratis check.",
    h1="Cyberbeveiligingswet, ISO 27001 en AVG voor mkb in West-Brabant",
    lede="Sinds 15 augustus 2026 geldt de Cyberbeveiligingswet, de Nederlandse invulling van NIS2. Ruim 8.000 organisaties vallen er rechtstreeks onder, zonder overgangsperiode. Hun leveranciers merken het ook: grote klanten vragen bewijs van informatiebeveiliging.",
    vragen=[
        ("Val ik onder de Cyberbeveiligingswet?", "Drie vragen over je sector, je omvang en je klanten. Je ziet meteen de uitkomst.", "/nl/nis2-check/"),
        ("Wat moet ik regelen?", "Zorgplicht, meldplicht en registratie, en wat je doet als een klant om bewijs vraagt.", "/nl/cyberbeveiligingswet-nis2/"),
        ("Heb ik ISO 27001 nodig?", "De stappen naar een certificaat, de doorlooptijd en wat begeleiding kost.", "/nl/iso-27001/"),
        ("Heb ik een FG nodig?", "Wanneer een FG verplicht is en wat elk mkb-bedrijf voor de AVG moet regelen.", "/nl/avg-fg/"),
    ],
    regios=[
        ("Roosendaal", "Logistiek knooppunt tussen Rotterdam en Antwerpen, met klanten in twee landen.", "/nl/regio/roosendaal/"),
        ("Bergen op Zoom", "Procesindustrie en voeding, met technische toeleveranciers eromheen.", "/nl/regio/bergen-op-zoom/"),
        ("Breda", "Zakelijke dienstverleners, hoofdkantoren en aanbestedingen die ISO 27001 vragen.", "/nl/regio/breda/"),
        ("Moerdijk", "Haven- en industrieterrein: chemie, afvalverwerking en logistiek.", "/nl/regio/moerdijk/"),
    ],
    body="",
    sources=[NCSC, FM],
),
dict(
    path="/nl/cyberbeveiligingswet-nis2/", lang="nl-NL", kind="uitleg", land="nl", alt="/be/nis2-cyfun/", crumbs=NL, tags=["nis2", "maatregelen", "meldplicht", "registratie", "bestuur"],
    title="Cyberbeveiligingswet: wat moet je mkb regelen? | Cyberdijk",
    desc="De Cyberbeveiligingswet (NIS2) geldt sinds 15 augustus 2026. Wie valt eronder, wat zijn de plichten en wat als je klant om bewijs vraagt?",
    h1="Cyberbeveiligingswet: wat moet je mkb-bedrijf regelen?",
    lede="De Cyberbeveiligingswet is de Nederlandse invulling van de Europese NIS2-richtlijn. Ze verplicht organisaties in aangewezen sectoren om hun digitale beveiliging aantoonbaar op orde te hebben.",
    kort=[
        "De wet geldt sinds 15 augustus 2026, zonder overgangsperiode.",
        "Ze geldt voor ruim 8.000 organisaties, in de regel vanaf 50 medewerkers of meer dan 10 miljoen euro omzet en balanstotaal.",
        "Drie plichten: zorgplicht, meldplicht en registratieplicht.",
    ],
    body="""
<h2>Val je eronder?</h2>
<p>De wet geldt voor organisaties in sectoren als energie, transport, zorg, drinkwater, digitale infrastructuur, ICT-dienstverlening, chemie, levensmiddelen, afvalbeheer en maakindustrie. Daarnaast telt de omvang: vanaf 50 medewerkers, of met een jaaromzet en balanstotaal boven 10 miljoen euro. Grote organisaties in de meest kritieke sectoren zijn essentiële entiteiten, de andere belangrijke entiteiten. <a href="/nl/nis2-check/">Doe de check</a> om te zien waar je staat.</p>
<h2>De drie plichten</h2>
<ul>
<li>Zorgplicht: je neemt passende maatregelen op basis van een risicoanalyse, en je kunt dat aantonen.</li>
<li>Meldplicht: bij een ernstig incident geef je binnen 24 uur een eerste waarschuwing, binnen 72 uur volgt de melding en binnen een maand het eindverslag.</li>
<li>Registratieplicht: je registreert je organisatie in het entiteitenregister van het NCSC.</li>
</ul>
<p>Bestuurders moeten genoeg kennis hebben om de risico's te beoordelen en volgen daarvoor opleiding. Wie dat nalaat, kan zelf een boete krijgen.</p>
<h2>Leverancier van een NIS2-bedrijf</h2>
<p>Ook als je er zelf niet onder valt, krijg je ermee te maken. Organisaties onder de wet moeten de risico's in hun keten beheersen. Ze sturen leveranciers een vragenlijst, nemen eisen op in contracten of vragen om een ISO 27001-certificaat.</p>
<h2>ISO 27001 als route</h2>
<p>De zorgplicht sluit nauw aan op ISO 27001: risicobeheer, incidentafhandeling, toegangsbeheer, leveranciersbeheer en continuïteit. Wie al gecertificeerd is, heeft het grootste deel van het werk gedaan. Voor de overheid geldt de BIO2 als uitwerking. Lees meer op <a href="/nl/iso-27001/">ISO 27001 voor mkb</a>.</p>
""",
    faq=[
        ("Is er een overgangsperiode?", "Nee. De verplichtingen gelden sinds 15 augustus 2026 voor organisaties die onder de wet vallen."),
        ("Hoe hoog zijn de boetes?", "Tot 10 miljoen euro of 2% van de wereldwijde jaaromzet voor essentiële entiteiten, en tot 7 miljoen euro of 1,4% voor belangrijke entiteiten."),
        ("Moet ik ISO 27001 halen?", "Dat is niet verplicht. Het is wel een erkende manier om te laten zien dat je de zorgplicht invult, en klanten vragen er vaak om."),
    ],
    sources=[NCSC, RIJK, DTC, FM],
),
dict(
    path="/nl/iso-27001/", lang="nl-NL", kind="uitleg", land="nl", alt="/be/iso-27001/", crumbs=NL, tags=["iso", "maatregelen"],
    title="ISO 27001 voor mkb: stappen, kosten en duur | Cyberdijk",
    desc="Is ISO 27001 verplicht, welke stappen doorloop je en wat kost begeleiding voor een mkb-bedrijf? Heldere uitleg met prijsindicatie.",
    h1="ISO 27001 voor mkb: stappen, kosten en doorlooptijd",
    lede="ISO 27001 is de internationale norm voor informatiebeveiliging. Een geaccrediteerde instelling controleert je organisatie en geeft het certificaat af.",
    kort=[
        "ISO 27001 is niet wettelijk verplicht, maar klanten en aanbestedingen vragen er steeds vaker om.",
        "De norm sluit nauw aan op de zorgplicht uit de Cyberbeveiligingswet.",
        "Mkb-consultants noemen 10.000 tot 18.000 euro voor de begeleiding.",
    ],
    body="""
<h2>Verplicht of niet?</h2>
<p>Geen wet verplicht ISO 27001. In de praktijk wordt het certificaat wel een voorwaarde: in aanbestedingen van overheden en zorginstellingen, in inkoopvoorwaarden van grote bedrijven en als bewijs dat je de zorgplicht uit de <a href="/nl/cyberbeveiligingswet-nis2/">Cyberbeveiligingswet</a> invult.</p>
<h2>De stappen</h2>
<ol>
<li>Bepaal de scope: welke activiteiten, locaties en systemen vallen onder het certificaat.</li>
<li>Breng de risico's in kaart en kies de maatregelen. De norm telt 93 beheersmaatregelen. In een verklaring van toepasselijkheid leg je vast welke je toepast.</li>
<li>Voer de maatregelen in en leg beleid en procedures vast.</li>
<li>Doe een interne audit en een directiebeoordeling.</li>
<li>Laat de certificatie-audit uitvoeren, in twee fasen. Het certificaat geldt drie jaar, met elk jaar een controle-audit.</li>
</ol>
<h2>Wat kost het?</h2>
<p>Mkb-consultants noemen 10.000 tot 18.000 euro voor de begeleiding naar ISO 27001. Daar komen de kosten van de certificerende instelling en je eigen uren bij.</p>
<h2>Hoe lang duurt het?</h2>
<p>De meeste mkb-bedrijven rekenen op zes tot twaalf maanden. Het systeem moet enkele maanden aantoonbaar werken voor de audit kan slagen.</p>
""",
    faq=[
        ("Wie geeft het certificaat af?", "Een geaccrediteerde certificerende instelling. De consultant die je begeleidt, mag niet zelf certificeren."),
        ("Dekt ISO 27001 de Cyberbeveiligingswet?", "Voor een groot deel van de zorgplicht wel. De meldplicht en de registratie bij het NCSC regel je apart."),
        ("Is NEN 7510 hetzelfde?", "NEN 7510 is de variant voor de zorg en bouwt voort op ISO 27001."),
    ],
    sources=[ISO, NCSC, MAAS],
),
dict(
    path="/nl/avg-fg/", lang="nl-NL", kind="uitleg", land="nl", alt="/be/gdpr-dpo/", crumbs=NL, tags=["avg", "gdpr", "privacy", "dpo", "datalek", "register"],
    title="AVG en FG voor mkb: wat is verplicht? | Cyberdijk",
    desc="Wanneer is een FG verplicht, wat hoort in je verwerkingsregister en hoe snel meld je een datalek bij de AP? De AVG-basis voor mkb.",
    h1="AVG en FG voor mkb: wat is verplicht?",
    lede="Elk bedrijf dat persoonsgegevens verwerkt, valt onder de AVG. Een FG is alleen in drie situaties verplicht, maar een verwerkingsregister en een procedure voor datalekken heeft bijna elk mkb-bedrijf nodig.",
    kort=[
        "Een FG is verplicht voor overheden, en voor bedrijven die op grote schaal personen volgen of gevoelige gegevens verwerken.",
        "Een verwerkingsregister heeft in de praktijk elk mkb-bedrijf nodig.",
        "Een datalek met risico meld je binnen 72 uur bij de Autoriteit Persoonsgegevens.",
    ],
    body="""
<h2>Wanneer is een FG verplicht?</h2>
<p>Een functionaris gegevensbescherming, de FG, is verplicht in drie gevallen: je bent een overheidsinstantie, je kernactiviteit bestaat uit het op grote schaal en stelselmatig volgen van personen, of je verwerkt op grote schaal gevoelige gegevens zoals gezondheidsgegevens. De meeste mkb-bedrijven vallen daar niet onder. Een vast aanspreekpunt voor privacy blijft wel verstandig.</p>
<h2>Wat elk mkb-bedrijf moet hebben</h2>
<ul>
<li>Een verwerkingsregister: welke gegevens, waarvoor, hoe lang en met wie gedeeld.</li>
<li>Een privacyverklaring die klopt met wat je doet.</li>
<li>Verwerkersovereenkomsten met leveranciers die gegevens voor je verwerken, zoals je salarisadministratie of je cloudleverancier.</li>
<li>Een DPIA, een risicoanalyse vooraf, bij verwerkingen met een hoog risico.</li>
<li>Een procedure voor verzoeken van betrokkenen en voor datalekken.</li>
</ul>
<h2>Een datalek melden</h2>
<p>Een datalek met een risico voor de betrokkenen meld je binnen 72 uur bij de Autoriteit Persoonsgegevens. Is het risico hoog, dan informeer je ook de betrokkenen zelf. Houd elk incident bij in een intern register, ook als je het niet hoeft te melden.</p>
<h2>AVG en Cyberbeveiligingswet samen</h2>
<p>De twee wetten overlappen. De Cyberbeveiligingswet gaat over de beveiliging van je systemen, de AVG over persoonsgegevens. Een goede risicoanalyse en een incidentprocedure dienen voor allebei. Lees ook <a href="/nl/cyberbeveiligingswet-nis2/">wat de Cyberbeveiligingswet vraagt</a>.</p>
""",
    faq=[
        ("Mag een medewerker de FG zijn?", "Ja, als die persoon genoeg kennis heeft en er geen belangenconflict is. Een directeur of IT-manager die zelf over de verwerkingen beslist, komt daarom niet in aanmerking."),
        ("Hoe hoog zijn de boetes?", "Tot 20 miljoen euro of 4% van de wereldwijde jaaromzet."),
        ("Moet ik een register hebben met minder dan 250 medewerkers?", "In de praktijk wel. De uitzondering voor kleinere organisaties vervalt zodra de verwerking niet incidenteel is, en loon- en klantenadministratie zijn dat nooit."),
    ],
    sources=[AP],
),
dict(
    path="/nl/nis2-check/", lang="nl-NL", kind="check", land="nl", alt="/be/nis2-check/", crumbs=NL, tags=["nis2"],
    title="Cyberbeveiligingswet-check: val je eronder? | Cyberdijk",
    desc="Beantwoord drie vragen en zie meteen of je bedrijf waarschijnlijk onder de Cyberbeveiligingswet (NIS2) valt. Gratis, zonder e-mailadres.",
    h1="Val je onder de Cyberbeveiligingswet? Doe de check",
    lede="Drie vragen over je sector, je omvang en je klanten. De uitkomst verschijnt meteen op deze pagina. Er wordt niets opgeslagen of verstuurd.",
    body="""
<h2>Hoe werkt de check?</h2>
<p>De check volgt de hoofdregels van de wet: je sector en je omvang bepalen of je essentieel of belangrijk bent. Enkele uitzonderingen zitten er niet in, bijvoorbeeld voor bepaalde digitale diensten die er ongeacht hun omvang onder vallen. De uitkomst is dus een eerste indicatie.</p>
<p>Voor zekerheid gebruik je de zelfevaluatie en de informatie van de overheid. De uitleg bij de uitkomst lees je op <a href="/nl/cyberbeveiligingswet-nis2/">wat de Cyberbeveiligingswet vraagt</a>.</p>
""",
    sources=[NCSC, DTC],
),
dict(
    path="/nl/regio/roosendaal/", lang="nl-NL", kind="regio", land="nl", crumbs=NL, tags=["nis2", "iso", "leverancier", "regio"],
    title="NIS2 en AVG in Roosendaal: uitleg voor mkb | Cyberdijk",
    desc="Logistiek of productiebedrijf in Roosendaal met klanten in België en Nederland? Lees wat de Cyberbeveiligingswet, CyFun en de AVG van je vragen.",
    h1="Cyberbeveiligingswet en AVG voor bedrijven in Roosendaal",
    lede="Roosendaal ligt op tien minuten van de Belgische grens, en dat merk je in de eisen die klanten stellen. Een Belgische opdrachtgever vraagt naar je CyFun-niveau, een Nederlandse naar ISO 27001 of de Cyberbeveiligingswet. Het gaat om dezelfde zorg voor je informatiebeveiliging, met een ander etiket.",
    body="""
<h2>Wat speelt er in Roosendaal?</h2>
<p>Roosendaal is een logistiek knooppunt tussen Rotterdam en Antwerpen, met grote distributiecentra, transportbedrijven en productiebedrijven. Levensmiddelen, post- en koeriersdiensten en delen van de transportsector staan in de Cyberbeveiligingswet. Wegvervoer en opslag staan er niet rechtstreeks in, maar grote opdrachtgevers leggen wel eisen op aan hun vervoerders, uitzendbureaus, onderhoudsbedrijven en IT-leveranciers.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Je rijdt voor een groot distributiecentrum. De opdrachtgever wil weten hoe je planning- en boordsystemen beveiligd zijn, en wat je doet bij een storing of hack.</li>
<li>Je levert aan klanten in Antwerpen en in Brabant. De Belgische klant vraagt naar CyFun, de Nederlandse naar ISO 27001. Met één risicoanalyse en één set maatregelen beantwoord je beide.</li>
<li>Je hebt meer dan 50 medewerkers en je produceert of verdeelt levensmiddelen, of je bezorgt pakketten. Dan val je waarschijnlijk zelf onder de wet en moet je geregistreerd zijn bij het NCSC.</li>
</ul>
<p>Werk je voor Belgische klanten? Lees dan de uitleg over <a href="/be/nis2-cyfun/">NIS2 en CyFun in België</a>.</p>
""",
    faq=[
        ("Mijn Belgische klant vraagt CyFun. Kan dat als Nederlands bedrijf?", "Ja. CyFun is een openbaar kader van de Belgische overheid en je kunt het ook buiten België toepassen. Vraag je klant welk niveau hij verwacht."),
        ("Waar meld ik een incident?", "Organisaties onder de Cyberbeveiligingswet melden een ernstig incident bij het bevoegde CSIRT en bij hun toezichthouder. Een datalek met persoonsgegevens meld je daarnaast bij de Autoriteit Persoonsgegevens."),
        ("Geldt de wet ook voor een bedrijf met 30 medewerkers?", "In de regel niet rechtstreeks. Via je klanten kun je wel eisen opgelegd krijgen."),
    ],
    sources=[NCSC, DTC, AP],
),
dict(
    path="/nl/regio/bergen-op-zoom/", lang="nl-NL", kind="regio", land="nl", crumbs=NL, tags=["nis2", "iso", "leverancier", "regio"],
    title="NIS2 en ISO 27001 in Bergen op Zoom | Cyberdijk",
    desc="Toeleverancier van procesindustrie of voedingsbedrijven in Bergen op Zoom? Lees wat de Cyberbeveiligingswet en ISO 27001 van je vragen.",
    h1="Informatiebeveiliging voor bedrijven in Bergen op Zoom",
    lede="Bergen op Zoom heeft een stevige procesindustrie en voedingssector, met daaromheen technische dienstverleners en toeleveranciers. Sinds 15 augustus 2026 moeten de grote bedrijven aantonen dat hun digitale beveiliging op orde is, en die eis schuift door naar wie voor hen werkt.",
    body="""
<h2>Wat speelt er in Bergen op Zoom?</h2>
<p>Chemie en levensmiddelen staan allebei in de Cyberbeveiligingswet. In die sectoren draait de productie op industriële besturingssystemen, en een storing heeft meteen gevolgen voor veiligheid en levering. Daarom letten opdrachtgevers scherp op wie toegang krijgt: onderhoudsbedrijven, installateurs, softwareleveranciers en uitzendkrachten.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Je doet onderhoud op een fabrieksterrein. Je monteurs loggen in op systemen van de klant, soms op afstand. De klant vraagt hoe je die toegang beveiligt.</li>
<li>Je levert software of meetapparatuur. In het contract komen eisen over updates, kwetsbaarheden en het melden van incidenten.</li>
<li>Je bent zelf een middelgroot productiebedrijf in voeding of chemie. Dan val je waarschijnlijk onder de wet als belangrijke entiteit.</li>
</ul>
""",
    faq=[
        ("Wat wil een opdrachtgever in de industrie meestal zien?", "Een beveiligingsbeleid, afspraken over toegang op afstand, een procedure voor incidenten, en vaak een ISO 27001-certificaat of een ingevulde vragenlijst."),
        ("Is ISO 27001 genoeg voor industriële systemen?", "Het is de basis. Voor besturingssystemen in de fabriek verwijzen opdrachtgevers vaak ook naar IEC 62443."),
        ("Valt de gemeente ook onder de wet?", "Ja. Overheden vallen onder de Cyberbeveiligingswet en werken met de BIO2 als normenkader."),
    ],
    sources=[NCSC, DTC],
),
dict(
    path="/nl/regio/breda/", lang="nl-NL", kind="regio", land="nl", crumbs=NL, tags=["nis2", "iso", "leverancier", "regio"],
    title="ISO 27001 en NIS2 in Breda: uitleg voor mkb | Cyberdijk",
    desc="Zakelijke dienstverlener, voedings- of logistiek bedrijf in Breda? Lees wanneer ISO 27001 nodig is en wat de Cyberbeveiligingswet vraagt.",
    h1="ISO 27001, NIS2 en AVG voor bedrijven in Breda",
    lede="Breda is de grootste stad van West-Brabant, met veel zakelijke dienstverleners, hoofdkantoren, voedingsbedrijven en logistiek. Hier komt de vraag naar informatiebeveiliging vooral binnen via aanbestedingen en inkoopvoorwaarden.",
    body="""
<h2>Wat speelt er in Breda?</h2>
<p>Softwarebedrijven, IT-dienstverleners, administratiekantoren en marketingbureaus verwerken gegevens van hun klanten. Grote klanten en overheden vragen daarom steeds vaker een ISO 27001-certificaat. IT-dienstverleners die systemen van andere bedrijven beheren, staan bovendien zelf in de Cyberbeveiligingswet.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Je schrijft in op een aanbesteding van een gemeente of zorginstelling. In de eisen staat ISO 27001, of NEN 7510 voor de zorg.</li>
<li>Je bent een softwarebedrijf met klanten in heel Nederland. Elke nieuwe klant stuurt een eigen vragenlijst. Een certificaat vervangt het grootste deel daarvan.</li>
<li>Je beheert de IT van mkb-bedrijven. Vanaf 50 medewerkers of 10 miljoen euro omzet val je als beheerder van ICT-diensten waarschijnlijk zelf onder de wet.</li>
</ul>
""",
    faq=[
        ("Hoe lang duurt ISO 27001 voor een bureau van 20 mensen?", "Reken op zes tot twaalf maanden, afhankelijk van wat er al geregeld is en hoeveel tijd je vrijmaakt."),
        ("Heb ik een FG nodig?", "Alleen als je op grote schaal personen volgt of gevoelige gegevens verwerkt, of als je een overheidsinstantie bent."),
        ("Wat kost begeleiding?", "Mkb-consultants noemen 10.000 tot 18.000 euro voor de begeleiding naar ISO 27001."),
    ],
    sources=[NCSC, AP, MAAS],
),
dict(
    path="/nl/regio/moerdijk/", lang="nl-NL", kind="regio", land="nl", crumbs=NL, tags=["nis2", "iso", "leverancier", "regio"],
    title="NIS2 voor bedrijven in Moerdijk | Cyberdijk",
    desc="Actief op het haven- en industrieterrein Moerdijk, of leverancier van een bedrijf daar? Lees wat de Cyberbeveiligingswet van je vraagt.",
    h1="Cyberbeveiligingswet voor het haven- en industrieterrein Moerdijk",
    lede="Op het haven- en industrieterrein Moerdijk zitten chemie, afvalverwerking en logistiek dicht op elkaar. Chemie, afvalverwerking en havenbeheer staan in de Cyberbeveiligingswet. Wie er produceert, valt er vaak rechtstreeks onder. Wie er onderhoud doet, vervoert of IT levert, krijgt de eisen via het contract.",
    body="""
<h2>Wat speelt er in Moerdijk?</h2>
<p>Chemische bedrijven, afvalverwerkers en terminals werken met installaties waar een digitale storing gevolgen heeft voor veiligheid en milieu. De wet verplicht hen om risico's te beheersen, incidenten snel te melden en hun leveranciers te beoordelen. Voor de vele aannemers en dienstverleners op het terrein betekent dat nieuwe vragen bij elke contractverlenging.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Je bent aannemer of onderhoudsbedrijf met een raamcontract. Naast je veiligheidscertificaat vraagt de klant nu ook naar je digitale beveiliging.</li>
<li>Je vervoert goederen of slaat ze op voor een chemisch bedrijf. Je planning en je koppelingen met de systemen van de klant worden onderdeel van zijn risicoanalyse.</li>
<li>Je bent zelf een productiebedrijf met meer dan 50 medewerkers. Controleer of je sector in de wet staat en of je geregistreerd bent.</li>
</ul>
""",
    faq=[
        ("Wij hebben al een veiligheidscertificaat. Telt dat mee?", "Het toont dat je met procedures kunt werken, maar het gaat over fysieke veiligheid. Voor digitale beveiliging vragen opdrachtgevers ISO 27001 of een eigen vragenlijst."),
        ("Welke toezichthouder controleert?", "Dat hangt af van je sector. De wet wijst per sector een toezichthouder aan."),
        ("Moet ik een incident bij mijn klant melden?", "Als het contract dat vraagt wel, en dat is steeds vaker zo. Leg vast binnen welke termijn en bij wie."),
    ],
    sources=[NCSC, DTC],
),
]
