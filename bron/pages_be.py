VLAIO = ("VLAIO: kmo-portefeuille", "https://www.vlaio.be/nl/subsidies-financiering/kmo-portefeuille")
CCB = ("Centrum voor Cybersecurity België (CCB)", "https://ccb.belgium.be")
SAW = ("Safeonweb@Work: registratie en hulpmiddelen", "https://atwork.safeonweb.be")
CYFUN = ("CyberFundamentals: het officiële CyFun-kader", "https://www.cyfun.eu")
GBA = ("Gegevensbeschermingsautoriteit", "https://www.gegevensbeschermingsautoriteit.be")
ISO = ("ISO: de norm ISO/IEC 27001", "https://www.iso.org/standard/27001")
CP_AUDIT = ("Cyberplan: cybersecurity voor kmo's, stappenplan en budget", "https://cyberplan.be/artikels/cybersecurity-voor-kmos-waar-te-beginnen-met-een-beperkt-budget/")
CP_ISO = ("Cyberplan: ISO 27001-certificering in België, kosten en traject", "https://cyberplan.be/artikels/iso-27001-certificering-in-belgie-kosten-traject-en-nis2-link/")

BE = [("België", "/be/")]

PAGES = [
dict(
    path="/be/", lang="nl-BE", kind="hub", land="be", alt="/nl/", crumbs=[],
    title="NIS2, CyFun en GDPR voor kmo's in Antwerpen | Cyberdijk",
    desc="Valt je kmo onder NIS2, of vraagt een klant om een CyFun-label? Heldere uitleg voor Antwerpen en de Noorderkempen. Doe de gratis NIS2-check.",
    h1="NIS2, CyFun en GDPR voor kmo's in de regio Antwerpen",
    lede="De Belgische NIS2-wet raakt meer bedrijven dan de meeste zaakvoerders denken. Essentiële entiteiten moeten tegen 18 april 2027 aantonen dat hun maatregelen in orde zijn. Wie er niet rechtstreeks onder valt, krijgt de vragen via klanten die dat wel doen.",
    vragen=[
        ("Val ik onder NIS2?", "Drie vragen over je sector, je grootte en je klanten. Je ziet meteen de uitkomst.", "/be/nis2-check/"),
        ("Welk CyFun-niveau past bij mijn bedrijf?", "Wat de wet vraagt, de niveaus van CyFun en de deadline van 18 april 2027.", "/be/nis2-cyfun/"),
        ("ISO 27001 of CyFun?", "De stappen naar een certificaat, de doorlooptijd en wat het een kmo kost.", "/be/iso-27001/"),
        ("Heb ik een DPO nodig?", "Wanneer een DPO verplicht is en wat elke kmo voor de GDPR moet regelen.", "/be/gdpr-dpo/"),
    ],
    regios=[
        ("Antwerpen", "Stad en haven: chemie, energie, terminals en de kmo's die ervoor werken.", "/be/regio/antwerpen/"),
        ("Noorderkempen", "Essen, Kalmthout, Kapellen, Brasschaat en Wuustwezel: klanten aan beide kanten van de grens.", "/be/regio/noorderkempen/"),
    ],
    body="""
<h2>Steun van de Vlaamse overheid</h2>
<p>Kleine ondernemingen krijgen via de kmo-portefeuille 45% steun op opleiding en advies rond cybersecurity, middelgrote 35%. De dienstverlener moet geregistreerd zijn bij de kmo-portefeuille.</p>
""",
    sources=[CCB, VLAIO],
),
dict(
    path="/be/nis2-cyfun/", lang="nl-BE", kind="uitleg", land="be", alt="/nl/cyberbeveiligingswet-nis2/", crumbs=BE, tags=["nis2", "cyfun", "maatregelen", "registratie"],
    title="NIS2 en CyFun voor kmo's: wat moet je regelen? | Cyberdijk",
    desc="Wie valt onder de Belgische NIS2-wet, wat zijn de CyFun-niveaus en wat moet klaar zijn tegen 18 april 2027? Uitleg in gewone taal, met bronnen.",
    h1="NIS2 en CyFun voor kmo's: wat moet je regelen?",
    lede="NIS2 verplicht bedrijven in aangeduide sectoren om hun digitale beveiliging aantoonbaar op orde te hebben. In België toon je dat aan met CyFun of met ISO 27001.",
    kort=[
        "NIS2 geldt voor bedrijven in aangeduide sectoren vanaf 50 werknemers, of met meer dan 10 miljoen euro omzet en balanstotaal.",
        "CyFun is het Belgische kader waarmee je aantoont dat je maatregelen in orde zijn.",
        "Essentiële entiteiten moeten tegen 18 april 2027 hun conformiteit laten beoordelen.",
    ],
    body="""
<h2>Valt je bedrijf onder NIS2?</h2>
<p>De Belgische NIS2-wet is van kracht sinds 18 oktober 2024. Ze geldt voor organisaties in een reeks sectoren, zoals energie, transport, gezondheidszorg, digitale infrastructuur, chemie, voeding, afvalbeheer en maakindustrie. Daarnaast telt je grootte: vanaf 50 werknemers, of met een jaaromzet en balanstotaal boven 10 miljoen euro, val je er in principe onder. Voor enkele digitale diensten geldt de wet ongeacht de grootte.</p>
<p>Grote organisaties in de meest kritieke sectoren zijn essentiële entiteiten. De andere zijn belangrijke entiteiten. Het verschil zit vooral in het toezicht: essentiële entiteiten worden vooraf en regelmatig beoordeeld, belangrijke entiteiten achteraf. <a href="/be/nis2-check/">Doe de NIS2-check</a> om te zien waar je staat.</p>
<h2>Wat de wet vraagt</h2>
<ul>
<li>Je registreert je bij het Centrum voor Cybersecurity België, via Safeonweb@Work.</li>
<li>Je neemt passende maatregelen op basis van een risicoanalyse, en je kan die aantonen.</li>
<li>Je meldt ernstige incidenten: een eerste waarschuwing binnen 24 uur, een melding binnen 72 uur en een eindverslag binnen een maand.</li>
<li>Het bestuur keurt de maatregelen goed en volgt zelf opleiding.</li>
</ul>
<h2>De CyFun-niveaus</h2>
<p>CyberFundamentals, kort CyFun, is het kader van het CCB. Het vertaalt de wet naar concrete maatregelen op vier niveaus: Small, Basic, Important en Essential. Hoe groter het risico van je organisatie, hoe hoger het niveau. Voor de meeste kmo's is Basic het vertrekpunt. Belangrijke entiteiten mikken op Important, essentiële op Essential. Lees meer in <a href="/kennisbank/cyfun-niveaus/">welk CyFun-niveau je nodig hebt</a>.</p>
<p>Je mag ook ISO 27001 gebruiken in plaats van CyFun. Het verschil lees je op <a href="/be/iso-27001/">ISO 27001 voor kmo's</a>.</p>
<h2>De deadline van 18 april 2027</h2>
<p>Essentiële entiteiten moeten hun conformiteit regelmatig laten beoordelen door een erkende instelling. Tegen 18 april 2027 moet de beoordeling op het niveau Essential rond zijn, of een ISO 27001-certificaat met de juiste scope. Belangrijke entiteiten zijn daartoe niet verplicht, maar moeten bij een controle wel kunnen aantonen dat hun maatregelen kloppen.</p>
<h2>Wat kost het?</h2>
<p>De prijs hangt af van je grootte en van wat er al geregeld is. Als richtprijs noemt de markt 5.000 tot 15.000 euro voor een cybersecurity-audit bij een kmo. Kleine ondernemingen krijgen via de kmo-portefeuille 45% steun op advies en opleiding rond cybersecurity, middelgrote 35%. De dienstverlener moet daarvoor geregistreerd zijn.</p>
""",
    faq=[
        ("Geldt NIS2 ook voor een kmo met minder dan 50 werknemers?", "Meestal niet rechtstreeks. Je krijgt wel vragen van klanten die onder de wet vallen, want zij moeten ook de beveiliging van hun leveranciers bewaken. Een CyFun-niveau Basic is dan een gangbaar antwoord."),
        ("Is een CyFun-label verplicht?", "Voor essentiële entiteiten is een regelmatige beoordeling verplicht, via CyFun, ISO 27001 of een inspectie door het CCB. Voor andere bedrijven is het vrijwillig."),
        ("Wat riskeer ik als ik niets doe?", "De wet voorziet boetes tot 10 miljoen euro of 2% van de wereldwijde omzet voor essentiële entiteiten, en tot 7 miljoen euro of 1,4% voor belangrijke entiteiten. Het bestuur kan aansprakelijk worden gesteld."),
    ],
    sources=[CCB, SAW, CYFUN, VLAIO, CP_AUDIT],
),
dict(
    path="/be/iso-27001/", lang="nl-BE", kind="uitleg", land="be", alt="/nl/iso-27001/", crumbs=BE, tags=["iso", "cyfun", "maatregelen"],
    title="ISO 27001 voor kmo's: stappen, kosten en duur | Cyberdijk",
    desc="Wanneer kies je ISO 27001 en wanneer CyFun? De stappen naar een certificaat, de doorlooptijd en wat het een Belgische kmo kost.",
    h1="ISO 27001 voor kmo's: stappen, kosten en doorlooptijd",
    lede="ISO 27001 is de internationale norm voor informatiebeveiliging. Een onafhankelijke instelling controleert je organisatie en reikt het certificaat uit.",
    kort=[
        "Onder de Belgische NIS2-wet is ISO 27001 een erkend alternatief voor CyFun.",
        "Reken voor een kmo op 15.000 tot 50.000 euro in totaal.",
        "De meeste kmo's hebben zes tot twaalf maanden nodig.",
    ],
    body="""
<h2>ISO 27001 of CyFun?</h2>
<p>Beide tonen aan dat je informatiebeveiliging op orde is. CyFun is Belgisch, gratis beschikbaar en afgestemd op NIS2. ISO 27001 is internationaal bekend en wordt vaak gevraagd door buitenlandse klanten en in aanbestedingen. Werk je vooral voor Belgische klanten, dan is CyFun meestal de kortste weg. Lever je ook in Nederland of verder, dan weegt ISO 27001 zwaarder.</p>
<h2>De stappen</h2>
<ol>
<li>Bepaal de scope: welke activiteiten, locaties en systemen vallen onder het certificaat.</li>
<li>Breng de risico's in kaart en kies de maatregelen. De norm telt 93 beheersmaatregelen. In een verklaring van toepasselijkheid leg je vast welke je toepast.</li>
<li>Voer de maatregelen in en leg beleid en procedures vast.</li>
<li>Doe een interne audit en een directiebeoordeling.</li>
<li>Laat de certificatie-audit uitvoeren, in twee fasen. Het certificaat geldt drie jaar, met elk jaar een controle-audit.</li>
</ol>
<h2>Wat kost het?</h2>
<p>Voor een Belgische kmo ligt het totaal tussen 15.000 en 50.000 euro, afhankelijk van grootte en vertrekpunt. Daarin zitten begeleiding, eigen tijd en de audit. Advies rond cybersecurity komt in aanmerking voor de kmo-portefeuille.</p>
<h2>Hoe lang duurt het?</h2>
<p>De meeste kmo's rekenen op zes tot twaalf maanden. Het systeem moet enkele maanden aantoonbaar werken voor de audit kan slagen.</p>
""",
    faq=[
        ("Is ISO 27001 wettelijk verplicht?", "Nee. Het is een vrijwillige norm. Klanten, aanbestedingen of de NIS2-wet kunnen er wel om vragen als bewijs."),
        ("Dekt ISO 27001 ook NIS2?", "Grotendeels. Voor essentiële entiteiten moeten de scope en de verklaring van toepasselijkheid aansluiten op wat het CCB vraagt."),
        ("Kan een klein bedrijf dit zelf?", "Ja, met voldoende tijd. Veel kmo's laten zich begeleiden voor de risicoanalyse en de documentatie, en doen de invoering zelf."),
    ],
    sources=[ISO, CCB, CP_ISO, VLAIO],
),
dict(
    path="/be/gdpr-dpo/", lang="nl-BE", kind="uitleg", land="be", alt="/nl/avg-fg/", crumbs=BE, tags=["avg", "gdpr", "privacy", "dpo", "datalek", "register"],
    title="GDPR en DPO voor kmo's: wat is verplicht? | Cyberdijk",
    desc="Wanneer is een DPO verplicht, wat moet in je register staan en hoe snel meld je een datalek? De GDPR-basis voor Belgische kmo's.",
    h1="GDPR en DPO voor kmo's: wat is verplicht?",
    lede="Elke onderneming die persoonsgegevens verwerkt, valt onder de GDPR. Een DPO is alleen in drie situaties verplicht, maar een register en een procedure voor datalekken heeft bijna elke kmo nodig.",
    kort=[
        "Een DPO is verplicht voor overheden, en voor bedrijven die op grote schaal personen volgen of gevoelige gegevens verwerken.",
        "Een register van verwerkingsactiviteiten heeft in de praktijk elke kmo nodig.",
        "Een datalek met risico meld je binnen 72 uur bij de Gegevensbeschermingsautoriteit.",
    ],
    body="""
<h2>Wanneer is een DPO verplicht?</h2>
<p>Een functionaris voor gegevensbescherming, de DPO, is verplicht in drie gevallen: je bent een overheidsinstantie, je kernactiviteit bestaat uit het op grote schaal en stelselmatig volgen van personen, of je verwerkt op grote schaal gevoelige gegevens zoals gezondheidsgegevens. De meeste kmo's vallen daar niet onder. Een vast aanspreekpunt voor privacy blijft wel verstandig.</p>
<h2>Wat elke kmo moet hebben</h2>
<ul>
<li>Een register van verwerkingsactiviteiten: welke gegevens, waarvoor, hoe lang en met wie gedeeld.</li>
<li>Een privacyverklaring die klopt met wat je doet.</li>
<li>Verwerkersovereenkomsten met leveranciers die gegevens voor je verwerken, zoals je sociaal secretariaat of je cloudleverancier.</li>
<li>Een DPIA, een risicoanalyse vooraf, bij verwerkingen met een hoog risico.</li>
<li>Een procedure voor verzoeken van betrokkenen en voor datalekken.</li>
</ul>
<h2>Een datalek melden</h2>
<p>Een datalek met een risico voor de betrokkenen meld je binnen 72 uur bij de Gegevensbeschermingsautoriteit. Is het risico hoog, dan verwittig je ook de betrokkenen zelf. Hou elk incident bij in een intern register, ook wanneer je het niet moet melden.</p>
<h2>GDPR en NIS2 samen</h2>
<p>De twee wetten overlappen. NIS2 gaat over de beveiliging van je systemen, de GDPR over persoonsgegevens. Een goede risicoanalyse en een incidentprocedure dienen voor allebei. Lees ook <a href="/be/nis2-cyfun/">NIS2 en CyFun voor kmo's</a>.</p>
""",
    faq=[
        ("Mag een medewerker de DPO zijn?", "Ja, als die persoon voldoende kennis heeft en er geen belangenconflict is. Een zaakvoerder of IT-verantwoordelijke die zelf over de verwerkingen beslist, komt daarom niet in aanmerking."),
        ("Hoe hoog zijn de boetes?", "Tot 20 miljoen euro of 4% van de wereldwijde jaaromzet."),
        ("Moet ik een register hebben met minder dan 250 werknemers?", "In de praktijk wel. De uitzondering voor kleinere organisaties vervalt zodra de verwerking niet incidenteel is, en loon- en klantenadministratie zijn dat nooit."),
    ],
    sources=[GBA],
),
dict(
    path="/be/nis2-check/", lang="nl-BE", kind="check", land="be", alt="/nl/nis2-check/", crumbs=BE, tags=["nis2"],
    title="NIS2-check België: valt mijn bedrijf onder NIS2? | Cyberdijk",
    desc="Beantwoord drie vragen en zie meteen of je Belgische onderneming waarschijnlijk onder de NIS2-wet valt. Gratis, zonder e-mailadres.",
    h1="Valt je bedrijf onder NIS2? Doe de check",
    lede="Drie vragen over je sector, je grootte en je klanten. De uitkomst verschijnt meteen op deze pagina. Er wordt niets opgeslagen of verstuurd.",
    body="""
<h2>Hoe werkt de check?</h2>
<p>De check volgt de hoofdregels van de wet: je sector en je grootte bepalen of je essentieel of belangrijk bent. Enkele uitzonderingen zitten er niet in, bijvoorbeeld voor bepaalde digitale diensten die er ongeacht hun grootte onder vallen. De uitkomst is dus een eerste indicatie.</p>
<p>Voor zekerheid gebruik je de hulpmiddelen van het CCB op Safeonweb@Work. De uitleg bij de uitkomst lees je op <a href="/be/nis2-cyfun/">NIS2 en CyFun voor kmo's</a>.</p>
""",
    sources=[SAW, CCB],
),
dict(
    path="/be/regio/antwerpen/", lang="nl-BE", kind="regio", land="be", crumbs=BE, tags=["nis2", "cyfun", "leverancier", "regio"],
    title="NIS2 en CyFun in Antwerpen: uitleg voor kmo's | Cyberdijk",
    desc="Leverancier van een havenbedrijf, of zelf actief in chemie, voeding of afvalbeheer? Lees wat NIS2 en CyFun vragen van kmo's in Antwerpen.",
    h1="NIS2, CyFun en GDPR voor bedrijven in Antwerpen",
    lede="Wie levert aan een bedrijf in de Antwerpse haven, krijgt vroeg of laat een vragenlijst over cybersecurity. Chemie, energie en havenactiviteiten vallen onder de Belgische NIS2-wet, en die bedrijven moeten ook hun leveranciers beoordelen.",
    body="""
<h2>Wat speelt er in Antwerpen?</h2>
<p>De Antwerpse haven huisvest een van de grootste chemieclusters van Europa en een dicht netwerk van terminals, rederijen, expediteurs en transporteurs. Veel van die sectoren staan in de NIS2-wet: scheepvaart en havenbeheer, energie, chemie, afvalbeheer en voeding. Wegvervoer en opslag staan er niet rechtstreeks in. Rond die grote spelers werkt een brede kring van kmo's: onderhoudsbedrijven, IT-dienstverleners, ingenieursbureaus, uitzendkantoren en toeleveranciers.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Je kmo telt meer dan 50 werknemers en zit zelf in een NIS2-sector, bijvoorbeeld chemie, voeding of afvalbeheer. Dan val je waarschijnlijk rechtstreeks onder de wet en moest je je registreren bij het CCB.</li>
<li>Je bent leverancier van een havenbedrijf. Je klant stuurt een vragenlijst over cybersecurity of vraagt een CyFun-niveau. De wet verplicht hem om de risico's in zijn keten te beheersen.</li>
<li>Je beheert IT voor andere bedrijven. Dienstverleners die ICT beheren, staan zelf in de wet en krijgen strengere vragen van hun klanten.</li>
</ul>
""",
    faq=[
        ("Mijn klant in de haven vraagt een CyFun-niveau. Welk niveau is gebruikelijk?", "Voor de meeste toeleveranciers is Basic het vertrekpunt. Vraag je klant welk niveau hij verwacht en tegen wanneer, en laat dat vastleggen in het contract."),
        ("Kan ik steun krijgen als Antwerpse kmo?", "Ja. De kmo-portefeuille van de Vlaamse overheid geeft kleine ondernemingen 45% en middelgrote 35% steun op advies en opleiding rond cybersecurity, bij een geregistreerde dienstverlener."),
        ("Geldt dit ook als mijn hoofdzetel in Nederland ligt?", "Voor je Belgische vestiging gelden de Belgische regels. Voor je Nederlandse activiteiten geldt de Cyberbeveiligingswet."),
    ],
    sources=[CCB, CYFUN, VLAIO],
),
dict(
    path="/be/regio/noorderkempen/", lang="nl-BE", kind="regio", land="be", crumbs=BE, tags=["nis2", "cyfun", "gdpr", "regio"],
    title="Cybersecurity en GDPR in de Noorderkempen | Cyberdijk",
    desc="Uitleg over NIS2, CyFun en GDPR voor kmo's in Essen, Kalmthout, Kapellen, Brasschaat en Wuustwezel, met klanten aan beide kanten van de grens.",
    h1="Informatiebeveiliging voor kmo's in de Noorderkempen",
    lede="In Essen, Kalmthout, Kapellen, Brasschaat en Wuustwezel werken veel kmo's voor klanten aan beide kanten van de grens. Dat betekent twee stellen regels: de Belgische NIS2-wet met CyFun, en de Nederlandse Cyberbeveiligingswet.",
    body="""
<h2>Wat speelt er in de Noorderkempen?</h2>
<p>De regio telt vooral kleinere bedrijven in bouw, transport, handel, tuinbouw en dienstverlening. De meeste vallen door hun grootte niet rechtstreeks onder NIS2. Ze merken de wet wel via hun klanten: de haven van Antwerpen in het zuiden, en logistieke en industriële bedrijven rond Roosendaal, Bergen op Zoom en Moerdijk in het noorden.</p>
<h2>Drie herkenbare situaties</h2>
<ul>
<li>Een transportbedrijf met Belgische en Nederlandse opdrachtgevers krijgt van de ene een vraag naar CyFun en van de andere naar ISO 27001. Eén goed onderbouwd beveiligingsbeleid dient voor beide.</li>
<li>Een installatie- of onderhoudsbedrijf heeft toegang tot systemen of gebouwen van een grote klant. Die klant wil weten hoe je omgaat met wachtwoorden, laptops en toegangsbadges.</li>
<li>Een boekhoud- of administratiekantoor verwerkt gegevens van honderden klanten. Daar weegt de GDPR het zwaarst: register, verwerkersovereenkomsten en een procedure voor datalekken.</li>
</ul>
<p>Werk je ook voor Nederlandse klanten? Lees dan de uitleg over de <a href="/nl/cyberbeveiligingswet-nis2/">Cyberbeveiligingswet</a>.</p>
""",
    faq=[
        ("Ik heb maar tien medewerkers. Moet ik iets met NIS2?", "Rechtstreeks meestal niet. Zorg wel dat de basis op orde is: updates, back-ups, tweestapsverificatie en duidelijke afspraken met je IT-partner. Dat is ook wat CyFun op de laagste niveaus vraagt."),
        ("Welke regels gelden als ik in België gevestigd ben en in Nederland werk?", "Je onderneming valt onder de Belgische wet. Je Nederlandse klanten kunnen daarnaast eigen eisen stellen in het contract, vaak op basis van ISO 27001."),
        ("Waar vind ik het CyFun-kader?", "Op cyfun.eu, de officiële site van het Centrum voor Cybersecurity België. Het kader en de zelfevaluatie zijn gratis."),
    ],
    sources=[CCB, CYFUN, GBA],
),
]
