# -*- coding: utf-8 -*-
"""Kennisbankartikels die voor België en Nederland samen gelden (land="eu"), plus enkele landspecifieke.
Elk artikel: titel max. 60 tekens, meta max. 155 tekens, bronnen, veelgestelde vragen en tags voor 'Lees ook'."""
from pages_be import CCB, SAW, CYFUN, GBA, ISO, VLAIO
from pages_nl import NCSC, DTC, AP

NIS2_RL = ("Richtlijn (EU) 2022/2555 (NIS2) op EUR-Lex", "https://eur-lex.europa.eu/eli/dir/2022/2555/oj")
AVG = ("Verordening (EU) 2016/679 (GDPR/AVG) op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2016/679/oj")
KB = [("Kennisbank", "/kennisbank/")]

PAGES = [
dict(
    path="/kennisbank/nis2-maatregelen/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["nis2", "maatregelen", "cyfun", "iso"],
    title="De tien maatregelen van NIS2 uitgelegd | Cyberdijk",
    desc="NIS2 verplicht tien soorten maatregelen, van risicoanalyse tot tweestapsverificatie. Wat elke maatregel in de praktijk betekent voor je bedrijf.",
    h1="De tien maatregelen van NIS2: wat moet je bedrijf regelen?",
    lede="Artikel 21 van de NIS2-richtlijn somt tien soorten maatregelen op die elke essentiële en belangrijke entiteit moet nemen. België en Nederland hebben die lijst overgenomen. Dit is wat elke maatregel in de praktijk betekent.",
    kort=[
        "De tien maatregelen staan in artikel 21 van de richtlijn en gelden in België en Nederland.",
        "Ze vragen geen specifieke producten, wel aantoonbare afspraken, procedures en controles.",
        "CyFun en ISO 27001 vertalen de lijst naar concrete controlepunten.",
    ],
    body="""
<h2>Waar de lijst vandaan komt</h2>
<p>NIS2 schrijft niet voor welke software of leverancier je kiest. De richtlijn vraagt passende en evenredige maatregelen op basis van je risico's, en somt tien domeinen op die daar minstens in moeten zitten. De Belgische NIS2-wet en de Nederlandse Cyberbeveiligingswet nemen die lijst over. Toezichthouders toetsen dus op deze tien punten.</p>
<h2>De tien maatregelen</h2>
<ol>
<li><strong>Risicoanalyse en beveiligingsbeleid.</strong> Je brengt in kaart welke systemen en gegevens belangrijk zijn, wat er mis kan gaan en wat dat zou kosten. Op basis daarvan leg je in een beleid vast wat je doet. Dit is het vertrekpunt voor alle andere maatregelen.</li>
<li><strong>Incidentafhandeling.</strong> Een procedure die zegt wie wat doet bij een hack, een besmetting of een storing: beoordelen, indammen, herstellen en melden. Zie ook de <a href="/kennisbank/nis2-meldplicht-incident/">meldplicht van NIS2</a>.</li>
<li><strong>Bedrijfscontinuïteit.</strong> Back-ups die je ook echt terugzet, een herstelplan en afspraken voor crisisbeheer. De vraag is niet of je een back-up hebt, maar hoe snel je weer draait.</li>
<li><strong>Beveiliging van de toeleveringsketen.</strong> Je beoordeelt de risico's bij leveranciers en dienstverleners die toegang hebben tot je systemen of gegevens, en legt afspraken vast in contracten. Daarom krijgen ook kleinere leveranciers <a href="/kennisbank/nis2-vragenlijst-leverancier/">vragenlijsten</a>.</li>
<li><strong>Beveiliging bij aankoop, ontwikkeling en onderhoud.</strong> Nieuwe systemen koop je met beveiligingseisen, updates installeer je op tijd en je hebt een manier om kwetsbaarheden te ontvangen en af te handelen.</li>
<li><strong>Beleid om de doeltreffendheid te beoordelen.</strong> Je controleert regelmatig of je maatregelen werken: interne audits, tests, oefeningen of een externe beoordeling.</li>
<li><strong>Cyberhygiëne en opleiding.</strong> Basisregels voor iedereen, zoals sterke wachtwoorden, updates en voorzichtigheid met bijlagen en links, plus opleiding voor medewerkers en bestuur.</li>
<li><strong>Cryptografie en encryptie.</strong> Een beleid over wanneer je gegevens versleutelt, bijvoorbeeld op laptops, in back-ups en bij verzending, en hoe je sleutels beheert.</li>
<li><strong>Personeelsbeveiliging, toegangsbeheer en activabeheer.</strong> Wie krijgt welke toegang, wat gebeurt er bij in- en uitdiensttreding, en welke apparaten, systemen en gegevens heb je eigenlijk in huis.</li>
<li><strong>Multifactorauthenticatie en beveiligde communicatie.</strong> Tweestapsverificatie waar het past, en beveiligde kanalen voor spraak, video en tekst, ook in noodsituaties.</li>
</ol>
<h2>Hoe je dit praktisch aanpakt</h2>
<p>De lijst lijkt lang, maar de meeste kmo's en mkb-bedrijven hebben al een deel geregeld zonder het zo te noemen. Het verschil zit in het aantonen: een toezichthouder of klant wil beleid, procedures en bewijs zien. Werk daarom met een kader dat de tien domeinen al vertaald heeft. In België is dat <a href="/be/nis2-cyfun/">CyFun</a>, internationaal is dat <a href="/kennisbank/iso-27001-maatregelen/">ISO 27001</a>. Beide dekken de tien punten en geven je een lijst om tegen af te vinken.</p>
<p>Val je niet rechtstreeks onder de wet? Dan is deze lijst alsnog een goede leidraad, omdat klanten die wel onder NIS2 vallen precies deze punten bij hun leveranciers controleren.</p>
""",
    faq=[
        ("Moet ik alle tien maatregelen volledig invoeren?", "De maatregelen moeten passend en evenredig zijn. Je risicoanalyse bepaalt hoe ver je gaat. Wat je niet doet, moet je kunnen uitleggen."),
        ("Zijn er verschillen tussen België en Nederland?", "De lijst is dezelfde. België werkt met het CyFun-kader als referentie, Nederland verwijst naar de zorgplicht en voor de overheid naar de BIO2."),
        ("Is tweestapsverificatie verplicht?", "De richtlijn noemt multifactorauthenticatie uitdrukkelijk, waar passend. In de praktijk verwachten toezichthouders en klanten het minstens voor e-mail, beheerdersaccounts en toegang op afstand."),
    ],
    sources=[NIS2_RL, CCB, NCSC],
),
dict(
    path="/kennisbank/nis2-meldplicht-incident/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["nis2", "incident", "meldplicht", "datalek"],
    title="NIS2-meldplicht: 24 uur, 72 uur en een maand | Cyberdijk",
    desc="Welke incidenten moet je onder NIS2 melden, bij wie en binnen welke termijn? De drie stappen van de meldplicht en het verschil met een datalek.",
    h1="NIS2-meldplicht: wat meld je binnen 24 uur, 72 uur en een maand?",
    lede="Val je onder NIS2, dan meld je elk significant incident in drie stappen. De termijnen zijn kort en lopen ook in het weekend. Zo zit de meldplicht in elkaar, en zo bereid je je voor.",
    kort=[
        "Een eerste waarschuwing binnen 24 uur, een melding binnen 72 uur en een eindverslag binnen een maand.",
        "In België meld je bij het CCB, in Nederland bij het CSIRT en de toezichthouder van je sector.",
        "Een datalek met persoonsgegevens meld je daarnaast apart bij de privacytoezichthouder.",
    ],
    body="""
<h2>Welke incidenten moet je melden?</h2>
<p>De meldplicht geldt voor significante incidenten. Dat is een incident dat een ernstige verstoring van je dienstverlening of een aanzienlijk financieel verlies veroorzaakt of kan veroorzaken, of dat andere personen of organisaties aanzienlijke schade toebrengt. Een ransomware-aanval die je productie stillegt, valt daar duidelijk onder. Een phishingmail die niemand opende, niet. Twijfel je, dan is melden het veiligste.</p>
<h2>De drie stappen</h2>
<ol>
<li><strong>Vroegtijdige waarschuwing, binnen 24 uur</strong> nadat je het incident hebt vastgesteld. Je geeft aan of je een kwaadwillige oorzaak vermoedt en of er gevolgen over de grens kunnen zijn. Meer hoef je nog niet te weten.</li>
<li><strong>Incidentmelding, binnen 72 uur.</strong> Je werkt de waarschuwing bij met een eerste beoordeling van de ernst en de gevolgen, en met de technische aanwijzingen die je al hebt.</li>
<li><strong>Eindverslag, binnen een maand</strong> na de melding. Daarin staan een gedetailleerde beschrijving, de oorzaak, de genomen maatregelen en de eventuele gevolgen over de grens. Loopt het incident dan nog, dan volgt eerst een voortgangsverslag en komt het eindverslag een maand na afloop.</li>
</ol>
<p>De toezichthouder kan tussendoor om een tussentijds verslag vragen. In sommige gevallen moet je ook je klanten of gebruikers op de hoogte brengen van een ernstige dreiging.</p>
<h2>Waar meld je?</h2>
<p>In België meld je bij het Centrum voor Cybersecurity België via Safeonweb@Work. In Nederland meld je bij het CSIRT dat voor je sector is aangewezen en bij je sectorale toezichthouder; voor veel sectoren is dat het NCSC. Leg vooraf vast wie in je organisatie meldt en waar het meldformulier staat, zodat je er niet om drie uur 's nachts naar hoeft te zoeken.</p>
<h2>Het verschil met een datalek</h2>
<p>Zijn er persoonsgegevens betrokken, dan geldt daarnaast de AVG: je meldt het datalek binnen 72 uur bij de Gegevensbeschermingsautoriteit of de Autoriteit Persoonsgegevens. Dat is een aparte melding met een eigen formulier. Lees het <a href="/kennisbank/datalek-melden-72-uur/">stappenplan voor een datalek</a>.</p>
<h2>Zo bereid je je voor</h2>
<ul>
<li>Schrijf een korte incidentprocedure: wie beoordeelt, wie beslist, wie meldt, wie communiceert.</li>
<li>Zet de contactgegevens van je toezichthouder, je IT-partner en je verzekeraar op één plek, ook op papier.</li>
<li>Oefen het scenario één keer per jaar aan tafel. Een oefening van een uur toont meteen waar het schuurt.</li>
<li>Houd een logboek bij van elk incident, ook van wat je niet hoefde te melden. Dat is bewijs van een werkend proces.</li>
</ul>
""",
    faq=[
        ("Telt een storing zonder hacker ook mee?", "Ja. Een incident is elke gebeurtenis die de beschikbaarheid, integriteit of vertrouwelijkheid van je systemen of gegevens aantast, ook een technische storing. Beslissend is of de gevolgen significant zijn."),
        ("Vanaf wanneer lopen de 24 uur?", "Vanaf het moment dat je kennis hebt van het incident. Daarom hoort in je procedure wie dat moment vaststelt."),
        ("Wat als ik te laat meld?", "Te laat of niet melden is een inbreuk op de wet en kan tot een boete leiden. De toezichthouder kijkt wel naar de omstandigheden en naar wat je gedaan hebt om het incident te beperken."),
    ],
    sources=[NIS2_RL, CCB, SAW, NCSC],
),
dict(
    path="/kennisbank/nis2-bestuur-aansprakelijkheid/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["nis2", "bestuur", "aansprakelijkheid"],
    title="NIS2 en het bestuur: plichten en aansprakelijkheid",
    desc="NIS2 legt de verantwoordelijkheid bij het bestuur: maatregelen goedkeuren, toezien en opleiding volgen. Wat zaakvoerders en directies riskeren.",
    h1="NIS2 en het bestuur: wat moeten zaakvoerders en directies doen?",
    lede="NIS2 maakt informatiebeveiliging een zaak van het bestuur. Bestuurders keuren de maatregelen goed, zien toe op de uitvoering en volgen zelf opleiding. Doen ze dat niet, dan kunnen ze persoonlijk aansprakelijk zijn.",
    kort=[
        "Het bestuur keurt de beveiligingsmaatregelen goed en houdt toezicht op de uitvoering.",
        "Bestuurders moeten opleiding volgen om cyberrisico's te kunnen beoordelen.",
        "Bij nalatigheid kan het bestuur aansprakelijk zijn; bij essentiële entiteiten kan de toezichthouder vragen om een bestuurder tijdelijk te schorsen.",
    ],
    body="""
<h2>Drie plichten voor het bestuur</h2>
<p>Artikel 20 van de richtlijn is kort, maar duidelijk. Het bestuursorgaan van een essentiële of belangrijke entiteit moet:</p>
<ul>
<li>de maatregelen voor het beheer van cyberrisico's <strong>goedkeuren</strong>;</li>
<li><strong>toezien</strong> op de uitvoering ervan;</li>
<li><strong>opleiding volgen</strong> om risico's en de gevolgen voor de organisatie te kunnen inschatten, en soortgelijke opleiding aanbieden aan medewerkers.</li>
</ul>
<p>Beveiliging delegeren aan de IT-verantwoordelijke of een externe partner mag, de verantwoordelijkheid delegeren niet. Het bestuur moet weten welke risico's er zijn, welke keuzes gemaakt zijn en waarom.</p>
<h2>Wat aansprakelijk betekent</h2>
<p>De richtlijn bepaalt dat bestuurders aansprakelijk kunnen worden gesteld als de organisatie haar plichten niet nakomt. Hoe dat concreet uitpakt, volgt uit het nationale recht. De toezichthouder kan de organisatie opdragen om de verantwoordelijke personen bekend te maken, en bij essentiële entiteiten kan hij vragen om een bestuurder of wettelijke vertegenwoordiger tijdelijk te verbieden zijn functie uit te oefenen, zolang de inbreuk duurt. Daarnaast lopen de gewone regels van bestuurdersaansprakelijkheid door: wie als bestuurder kennelijk onzorgvuldig handelt, kan ook door de vennootschap of door schuldeisers worden aangesproken.</p>
<h2>Wat dit in de praktijk vraagt</h2>
<ol>
<li>Zet informatiebeveiliging minstens twee keer per jaar op de agenda van het bestuur, en notuleer wat besproken en beslist is.</li>
<li>Laat het bestuur de risicoanalyse en het beveiligingsbeleid formeel goedkeuren, met datum en handtekening.</li>
<li>Vraag een periodiek rapport: welke maatregelen staan, welke incidenten waren er, welke audits of tests zijn gedaan.</li>
<li>Plan een opleiding voor het voltallige bestuur en bewaar het bewijs van deelname. Een halve dag is een realistisch begin.</li>
<li>Leg vast wie het bestuur vervangt bij een incident en wie extern mag communiceren.</li>
</ol>
<h2>Ook als je er niet onder valt</h2>
<p>Voor bedrijven buiten de wet geldt de gewone zorgvuldigheidsplicht van het bestuur. Verzekeraars en grote klanten stellen intussen dezelfde vragen: is er beleid, is het goedgekeurd, wordt het gecontroleerd? Een bestuur dat die vragen kan beantwoorden, staat sterker bij een schadeclaim of een aanbesteding.</p>
""",
    faq=[
        ("Geldt dit ook voor een zaakvoerder van een kmo?", "Als je kmo onder NIS2 valt, ja. De plichten gelden voor het bestuursorgaan, ongeacht of dat één zaakvoerder is of een raad van bestuur."),
        ("Welke opleiding is goed genoeg?", "De wet schrijft geen inhoud voor. Een opleiding die uitlegt wat cyberrisico's zijn, welke maatregelen de wet vraagt en hoe je als bestuurder toezicht houdt, volstaat. Bewaar het attest."),
        ("Kan de IT-verantwoordelijke de goedkeuring tekenen?", "Nee. De goedkeuring is een beslissing van het bestuur zelf. De IT-verantwoordelijke bereidt voor en voert uit."),
    ],
    sources=[NIS2_RL, CCB, NCSC],
),
dict(
    path="/kennisbank/nis2-boetes/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["nis2", "boetes", "toezicht"],
    title="NIS2-boetes en sancties: wat riskeer je? | Cyberdijk",
    desc="Essentiële entiteiten riskeren onder NIS2 boetes tot 10 miljoen euro of 2% van de omzet, belangrijke tot 7 miljoen of 1,4%. Plus de andere sancties.",
    h1="NIS2-boetes en sancties: wat riskeer je als je niets doet?",
    lede="NIS2 kent hoge maximumboetes, maar de boete is zelden de eerste stap. Toezichthouders beginnen met waarschuwingen en bindende instructies. Dit zijn de sancties, van licht naar zwaar.",
    kort=[
        "Essentiële entiteiten: tot 10 miljoen euro of 2% van de wereldwijde jaaromzet, het hoogste bedrag telt.",
        "Belangrijke entiteiten: tot 7 miljoen euro of 1,4% van de wereldwijde jaaromzet.",
        "Daarnaast: waarschuwingen, bindende instructies, verplichte publicatie en, bij essentiële entiteiten, schorsing van een certificaat of bestuurder.",
    ],
    body="""
<h2>De maximumboetes</h2>
<p>De richtlijn legt minimale maxima vast die België en Nederland hebben overgenomen. Voor essentiële entiteiten gaat het om minstens 10 miljoen euro of 2% van de totale wereldwijde jaaromzet van de groep, afhankelijk van welk bedrag hoger is. Voor belangrijke entiteiten is dat minstens 7 miljoen euro of 1,4%. Het zijn plafonds: de toezichthouder weegt de ernst, de duur, de schade, eerdere inbreuken en de medewerking van de organisatie.</p>
<h2>Andere maatregelen van de toezichthouder</h2>
<ul>
<li>Een waarschuwing of een bindende instructie om een tekortkoming binnen een termijn weg te werken.</li>
<li>Het bevel om de inbreuk te staken, of om een audit te laten uitvoeren en de aanbevelingen op te volgen.</li>
<li>Het bevel om klanten of het publiek te informeren over een dreiging, of om de inbreuk openbaar te maken.</li>
<li>Bij essentiële entiteiten, als andere maatregelen niet helpen: de tijdelijke schorsing van een certificaat of vergunning, en de vraag om een bestuurder tijdelijk te verbieden zijn functie uit te oefenen.</li>
</ul>
<h2>Hoe het toezicht verschilt</h2>
<p>Essentiële entiteiten staan onder proactief toezicht: regelmatige audits, inspecties en in België een verplichte conformiteitsbeoordeling tegen 18 april 2027. Belangrijke entiteiten worden achteraf gecontroleerd, bijvoorbeeld na een incident of een klacht. In beide gevallen is de eerste vraag van de toezichthouder dezelfde: toon je risicoanalyse, je beleid en je bewijs.</p>
<h2>Boetes stapelen</h2>
<p>Een incident met persoonsgegevens kan tegelijk een inbreuk zijn op de AVG. Die kent eigen boetes tot 20 miljoen euro of 4% van de omzet. De richtlijn voorkomt dat je voor hetzelfde feit twee keer een boete krijgt onder NIS2 en de AVG, maar andere sancties blijven mogelijk.</p>
<h2>Wat je beter kan doen dan rekenen op mildheid</h2>
<p>Toezichthouders kijken naar inspanning. Een organisatie die haar maatregelen kan aantonen, incidenten correct meldt en meewerkt, krijgt een ander gesprek dan een organisatie zonder dossier. Begin met de <a href="/kennisbank/nis2-maatregelen/">tien maatregelen van NIS2</a> en met een werkende <a href="/kennisbank/nis2-meldplicht-incident/">meldprocedure</a>.</p>
""",
    faq=[
        ("Krijg ik meteen een boete als ik niet geregistreerd ben?", "Niet automatisch. Registratie is wel een plicht, en het ontbreken ervan is een inbreuk. Registreer je alsnog en documenteer waarom het later gebeurde."),
        ("Gelden de boetes ook voor leveranciers die niet onder de wet vallen?", "Nee. Voor hen gelden de afspraken in het contract met hun klant. Een klant kan wel een contract beëindigen of schade verhalen."),
        ("Zijn de bedragen in België en Nederland gelijk?", "Beide landen hanteren de maxima uit de richtlijn: 10 miljoen euro of 2% voor essentiële en 7 miljoen euro of 1,4% voor belangrijke entiteiten."),
    ],
    sources=[NIS2_RL, CCB, NCSC],
),
dict(
    path="/kennisbank/nis2-vragenlijst-leverancier/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["nis2", "leverancier", "keten", "cyfun", "iso"],
    title="NIS2-vragenlijst van je klant: zo antwoord je | Cyberdijk",
    desc="Grote klanten moeten onder NIS2 hun leveranciers beoordelen. Daarom krijg je een vragenlijst over cybersecurity. Wat erin staat en hoe je goed antwoordt.",
    h1="Je klant stuurt een NIS2-vragenlijst: zo beantwoord je ze",
    lede="Steeds meer kleine bedrijven krijgen een vragenlijst over cybersecurity van een grote klant. Niet omdat ze zelf onder NIS2 vallen, maar omdat hun klant zijn keten moet beoordelen. Zo pak je die vragenlijst aan zonder te overdrijven of te onderschatten.",
    kort=[
        "Je klant moet onder NIS2 de risico's bij zijn leveranciers beheersen; de vragenlijst is zijn bewijs.",
        "Antwoord eerlijk: beloof niets wat je niet kan aantonen, want het wordt een contractuele afspraak.",
        "Een vast beveiligingsdossier bespaart je werk bij elke volgende vragenlijst.",
    ],
    body="""
<h2>Waarom je deze vragenlijst krijgt</h2>
<p>Een van de <a href="/kennisbank/nis2-maatregelen/">tien verplichte maatregelen</a> van NIS2 is de beveiliging van de toeleveringsketen. Een bedrijf dat onder de wet valt, moet weten welke risico's zijn leveranciers meebrengen en daar afspraken over maken. Vooral leveranciers met toegang tot systemen, gebouwen of gegevens komen in beeld: IT-dienstverleners, onderhoudsbedrijven, installateurs, transporteurs, softwareleveranciers en uitzendkantoren.</p>
<h2>Wat er meestal in staat</h2>
<ul>
<li>Heb je een beveiligingsbeleid en wie is verantwoordelijk?</li>
<li>Gebruik je tweestapsverificatie, en hoe beheer je wachtwoorden en toegangsrechten?</li>
<li>Hoe snel installeer je updates en hoe bescherm je laptops en telefoons?</li>
<li>Maak je back-ups, waar staan ze en heb je het terugzetten getest?</li>
<li>Wat doe je bij een incident en binnen welke termijn verwittig je ons?</li>
<li>Werk je met onderaannemers en gelden voor hen dezelfde regels?</li>
<li>Heb je een certificaat of label, zoals ISO 27001 of een CyFun-niveau?</li>
</ul>
<h2>Zo beantwoord je ze goed</h2>
<ol>
<li><strong>Lees eerst het contract.</strong> Vaak hangt de vragenlijst aan een bijlage met beveiligingseisen. Wat je antwoordt, wordt een afspraak. Beloof dus niets wat je niet doet.</li>
<li><strong>Antwoord eerlijk, ook bij nee.</strong> Schrijf erbij wat je wel doet of wanneer je het regelt. Een klant waardeert een eerlijk 'nog niet, gepland voor maart' meer dan een 'ja' dat bij de eerste controle sneuvelt.</li>
<li><strong>Verwijs naar bewijs.</strong> Voeg je beleid, je back-upprocedure of een schermafbeelding van je instellingen toe. Bewijs maakt het verschil tussen een vinkje en vertrouwen.</li>
<li><strong>Leg je antwoorden vast in een beveiligingsdossier.</strong> De volgende klant stelt dezelfde vragen. Met een dossier van tien pagina's beantwoord je elke vragenlijst in een uur.</li>
<li><strong>Overweeg een label.</strong> In België is <a href="/kennisbank/cyfun-niveaus/">CyFun Basic</a> het gangbare antwoord voor toeleveranciers. Lever je ook aan Nederlandse of internationale klanten, dan weegt <a href="/kennisbank/iso-27001-maatregelen/">ISO 27001</a> zwaarder. Een label vervangt een groot deel van de vragenlijsten.</li>
</ol>
<h2>Wat je niet moet doen</h2>
<p>Blind ja aankruisen, de vragenlijst aan je IT-leverancier doorsturen zonder zelf te kijken, of de lijst laten liggen. Een onbeantwoorde vragenlijst leidt bij veel inkopers tot een lagere score, en bij een contractverlenging tot vragen die je liever niet had.</p>
""",
    faq=[
        ("Mag mijn klant eisen dat ik ISO 27001 haal?", "Ja, als contractvoorwaarde. Vraag dan naar een realistische termijn en of een lichter alternatief, zoals een CyFun-niveau of een ingevulde vragenlijst met bewijs, ook aanvaard wordt."),
        ("Moet ik mijn eigen leveranciers ook bevragen?", "Als zij toegang hebben tot systemen of gegevens van je klant, verwacht je klant dat je dezelfde afspraken doorschuift. Begin met je IT-partner en je softwareleveranciers."),
        ("Kan ik hulp krijgen bij het invullen?", "Ja. Een IT-partner of een adviseur kan de technische vragen beantwoorden. De beleidsvragen en de beloftes blijven jouw verantwoordelijkheid."),
    ],
    sources=[NIS2_RL, CYFUN, DTC],
),
dict(
    path="/kennisbank/nis2-registratie-ccb/", lang="nl-BE", kind="artikel", land="be", crumbs=KB, tags=["nis2", "registratie", "ccb"],
    title="NIS2-registratie bij het CCB: zo werkt het | Cyberdijk",
    desc="Valt je onderneming onder de Belgische NIS2-wet, dan registreer je ze bij het CCB via Safeonweb@Work. Wie, welke gegevens en welke termijnen.",
    h1="NIS2-registratie bij het CCB: wie, hoe en tegen wanneer?",
    lede="Elke essentiële en belangrijke entiteit moet zich registreren bij het Centrum voor Cybersecurity België. De eerste termijnen zijn verstreken, maar registreren blijft verplicht. Zo doe je het.",
    kort=[
        "Registreren gebeurt online via Safeonweb@Work, het portaal van het CCB.",
        "De eerste termijn liep af op 18 maart 2025; voor digitale dienstverleners al op 18 december 2024.",
        "Niet geregistreerd? Doe het alsnog, want registratie is een wettelijke plicht.",
    ],
    body="""
<h2>Wie moet zich registreren?</h2>
<p>Elke onderneming die onder de Belgische NIS2-wet valt, als essentiële of als belangrijke entiteit. Je bepaalt dat zelf op basis van je sector en je grootte; de wet werkt met zelfidentificatie. Weet je het niet zeker, <a href="/be/nis2-check/">doe dan eerst de NIS2-check</a> of lees <a href="/kennisbank/valt-mijn-bedrijf-onder-nis2/">hoe je het controleert</a>.</p>
<h2>De termijnen</h2>
<p>De wet trad in werking op 18 oktober 2024. Entiteiten kregen vijf maanden om zich te registreren, tot 18 maart 2025. Voor aanbieders van digitale diensten gold een kortere termijn van twee maanden, tot 18 december 2024: onder meer DNS-dienstverleners, registers van topleveldomeinen, cloud- en datacenterdiensten, aanbieders van beheerde diensten en beheerde beveiligingsdiensten, onlinemarktplaatsen, zoekmachines en sociale netwerken. Val je later onder de wet, bijvoorbeeld omdat je groeit of je activiteiten uitbreidt, dan registreer je je zodra je aan de criteria voldoet.</p>
<h2>Hoe registreer je?</h2>
<ol>
<li>Maak een account aan op Safeonweb@Work, het portaal van het CCB.</li>
<li>Vul de gegevens van je onderneming in: naam, ondernemingsnummer, adres en contactgegevens, waaronder een e-mailadres en telefoonnummer dat ook buiten de kantooruren bereikbaar is.</li>
<li>Geef je sector en subsector op, en de lidstaten waar je diensten levert.</li>
<li>Duid aan of je essentieel of belangrijk bent, en bevestig.</li>
</ol>
<p>Hou je gegevens actueel. Een wijziging van contactpersoon of adres geef je door, want het CCB gebruikt deze gegevens om je te waarschuwen bij dreigingen en om je meldingen te verwerken.</p>
<h2>Wat na de registratie?</h2>
<p>Registratie is het begin. Daarna volgen de <a href="/kennisbank/nis2-maatregelen/">maatregelen</a>, de <a href="/kennisbank/nis2-meldplicht-incident/">meldprocedure</a> en voor essentiële entiteiten de conformiteitsbeoordeling tegen 18 april 2027. Het CCB stelt via Safeonweb@Work het CyFun-kader en de zelfevaluatie gratis ter beschikking. Lees <a href="/kennisbank/cyfun-zelfevaluatie/">hoe je de CyFun-zelfevaluatie doorloopt</a>.</p>
""",
    faq=[
        ("Ik heb de termijn gemist. Wat nu?", "Registreer je alsnog zo snel mogelijk. Een laattijdige registratie is beter dan geen registratie, en het CCB kijkt bij een controle naar wat je sindsdien hebt gedaan."),
        ("Moet elke vestiging apart registreren?", "Je registreert de juridische entiteit. Heeft je groep meerdere vennootschappen die elk onder de wet vallen, dan registreert elke vennootschap zich."),
        ("Mag mijn IT-partner de registratie doen?", "Ja, maar de onderneming blijft verantwoordelijk voor de juistheid van de gegevens. Controleer dus wat er ingevuld wordt en bewaar de bevestiging."),
    ],
    sources=[SAW, CCB],
),
dict(
    path="/kennisbank/cyfun-zelfevaluatie/", lang="nl-BE", kind="artikel", land="be", crumbs=KB, tags=["cyfun", "nis2", "zelfevaluatie"],
    title="CyFun-zelfevaluatie: zo pak je het aan | Cyberdijk",
    desc="Met de CyFun-zelfevaluatie van het CCB zie je waar je bedrijf staat. Stap voor stap: niveau kiezen, maatregelen scoren, actieplan maken, verifiëren.",
    h1="CyFun-zelfevaluatie: zo doorloop je ze stap voor stap",
    lede="De zelfevaluatie is de eerste stap van elk CyFun-traject, verplicht of niet. Ze is gratis, maar vraagt eerlijkheid en tijd. Dit is hoe je ze aanpakt en wat je eruit haalt.",
    kort=[
        "Het CyFun-kader en het zelfevaluatie-instrument staan gratis op cyfun.eu en Safeonweb@Work.",
        "Je scoort elke maatregel op volwassenheid; het resultaat is een lijst met kloven en een actieplan.",
        "Voor een officieel label laat je de zelfevaluatie verifiëren door een erkende instelling.",
    ],
    body="""
<h2>Wat je nodig hebt</h2>
<p>Het CyberFundamentals-kader bestaat uit een lijst maatregelen per niveau en een zelfevaluatie-instrument waarin je die maatregelen scoort. Het kader is gebouwd op de vijf functies van het NIST Cybersecurity Framework: identificeren, beschermen, detecteren, reageren en herstellen. Je hebt verder een halve tot een hele dag nodig, en de mensen die je systemen kennen: je IT-verantwoordelijke of je IT-partner, en iemand van de directie.</p>
<h2>Stap 1: kies je niveau</h2>
<p>Val je onder NIS2, dan volgt het niveau uit je statuut: Important voor belangrijke entiteiten, Essential voor essentiële. Val je er niet onder, kies dan Basic, of Small als je een heel kleine onderneming bent. Twijfel je, dan helpt het hulpmiddel van het CCB om je risiconiveau te bepalen. Lees meer in <a href="/kennisbank/cyfun-niveaus/">welk CyFun-niveau je nodig hebt</a>.</p>
<h2>Stap 2: verzamel je bewijs</h2>
<p>Zoek vooraf bij elkaar wat je al hebt: beleidsdocumenten, een lijst van je systemen en toestellen, je back-upinstellingen, je contract met je IT-partner, je procedure bij incidenten. Veel maatregelen blijken al deels geregeld, alleen nergens opgeschreven.</p>
<h2>Stap 3: scoor elke maatregel</h2>
<p>Per maatregel geef je aan hoe ver je staat, van niet aanwezig tot volledig ingevoerd en gecontroleerd. Scoor eerlijk. Een te hoge score helpt niemand: bij een verificatie valt ze door de mand en bij een incident ontbreekt de maatregel echt. Noteer bij elke score waar het bewijs staat.</p>
<h2>Stap 4: maak een actieplan</h2>
<p>Het instrument toont waar je onder de drempel van je niveau zit. Zet die punten op een lijst met een eigenaar, een datum en een budget. Begin met wat het meeste risico wegneemt en het minst kost: tweestapsverificatie, geteste back-ups en updates staan meestal bovenaan.</p>
<h2>Stap 5: laat verifiëren of certificeren</h2>
<p>Wil je een officieel CyFun-label, dan laat je je zelfevaluatie op het niveau Basic of Important verifiëren door een erkende conformiteitsbeoordelingsinstantie. Voor het niveau Essential volgt een certificatie-audit. Essentiële entiteiten zijn daartoe verplicht tegen 18 april 2027; voor alle andere bedrijven is het een keuze, vaak op vraag van een klant.</p>
<h2>Herhaal elk jaar</h2>
<p>Een zelfevaluatie is een foto, geen film. Plan ze jaarlijks in, of na elke grote verandering: een nieuw systeem, een nieuwe IT-partner, een incident. Zo blijft je actieplan bij en heb je bij een vraag van een klant altijd een recent antwoord.</p>
""",
    faq=[
        ("Hoe lang duurt een zelfevaluatie?", "Reken op een halve tot een hele dag voor het niveau Basic, als je de documenten vooraf verzameld hebt. De niveaus Important en Essential vragen meer tijd en meestal begeleiding."),
        ("Is de zelfevaluatie zelf al een label?", "Nee. Een label krijg je pas na verificatie door een erkende instelling. De zelfevaluatie is wel een bruikbaar antwoord op een vragenlijst van een klant."),
        ("Kan ik steun krijgen voor begeleiding?", "Advies rond cybersecurity door een geregistreerde dienstverlener komt in aanmerking voor de kmo-portefeuille."),
    ],
    sources=[CYFUN, SAW, CCB, VLAIO],
),
dict(
    path="/kennisbank/iso-27001-maatregelen/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["iso", "maatregelen", "nis2"],
    title="ISO 27001:2022: de 93 maatregelen uitgelegd | Cyberdijk",
    desc="ISO 27001:2022 telt 93 maatregelen in vier thema's: organisatorisch, mensen, fysiek en technologisch. Wat erin zit en hoe je kiest welke voor jou gelden.",
    h1="ISO 27001:2022: de 93 maatregelen in vier thema's",
    lede="De norm ISO/IEC 27001 bestaat uit twee delen: de eisen aan je managementsysteem en een bijlage met 93 beheersmaatregelen. Dit is wat er in die bijlage staat en hoe je kiest welke maatregelen voor jou gelden.",
    kort=[
        "Bijlage A van ISO 27001:2022 telt 93 maatregelen: 37 organisatorische, 8 voor mensen, 14 fysieke en 34 technologische.",
        "In de verklaring van toepasselijkheid leg je vast welke maatregelen je toepast en waarom de andere niet.",
        "Certificaten op de versie van 2013 zijn sinds 31 oktober 2025 niet meer geldig; je werkt dus met de versie van 2022.",
    ],
    body="""
<h2>Twee delen: het systeem en de maatregelen</h2>
<p>De hoofdstukken 4 tot en met 10 van de norm beschrijven het managementsysteem voor informatiebeveiliging, kortweg ISMS: context en scope, leiderschap, planning met risicoanalyse, middelen en documentatie, uitvoering, evaluatie en verbetering. Bijlage A bevat de maatregelen waaruit je kiest om je risico's te behandelen. Beide delen worden geauditeerd.</p>
<h2>De vier thema's</h2>
<ul>
<li><strong>Organisatorisch (37 maatregelen):</strong> beleid, rollen, leveranciersbeheer, incidentbeheer, continuïteit, naleving van wetten en contracten, bescherming van persoonsgegevens, dreigingsinformatie en beveiliging bij clouddiensten.</li>
<li><strong>Mensen (8 maatregelen):</strong> screening, arbeidsvoorwaarden, bewustwording en opleiding, disciplinaire procedure, afspraken bij vertrek, geheimhouding, thuiswerken en het melden van incidenten.</li>
<li><strong>Fysiek (14 maatregelen):</strong> beveiligde zones, toegang tot gebouwen, bescherming tegen brand en wateroverlast, apparatuur, bekabeling, onderhoud en het veilig afvoeren van apparatuur.</li>
<li><strong>Technologisch (34 maatregelen):</strong> toegangsbeheer, authenticatie, malwarebescherming, kwetsbaarhedenbeheer, back-ups, logging, netwerkbeveiliging, versleuteling, veilig ontwikkelen en testen.</li>
</ul>
<h2>De verklaring van toepasselijkheid</h2>
<p>Je hoeft niet alle 93 maatregelen in te voeren. In de verklaring van toepasselijkheid, in het Engels de Statement of Applicability, staat per maatregel of je ze toepast, hoe je dat doet en, als je ze niet toepast, waarom dat verantwoord is. Een bedrijf zonder eigen softwareontwikkeling kan de maatregelen rond veilig ontwikkelen bijvoorbeeld uitsluiten. De auditor toetst of je keuzes kloppen met je risicoanalyse.</p>
<h2>Versie 2022 in plaats van 2013</h2>
<p>De versie van 2022 bracht de 114 maatregelen van 2013 terug tot 93, in vier thema's in plaats van veertien, en voegde elf nieuwe toe, onder meer rond dreigingsinformatie, clouddiensten, dataclassificatie en het voorkomen van gegevenslekken. Sinds 31 oktober 2025 zijn certificaten op de versie van 2013 niet meer geldig. Start je nu, dan werk je dus met de versie van 2022.</p>
<h2>Hoe dit samenhangt met NIS2</h2>
<p>De <a href="/kennisbank/nis2-maatregelen/">tien maatregelen van NIS2</a> vind je allemaal terug in bijlage A. Daarom aanvaardt België ISO 27001 als alternatief voor CyFun, en sluit de Nederlandse zorgplicht nauw aan op de norm. Lees de praktische stappen, kosten en doorlooptijd op <a href="/be/iso-27001/">ISO 27001 voor kmo's</a> of <a href="/nl/iso-27001/">ISO 27001 voor mkb</a>.</p>
""",
    faq=[
        ("Moet ik de norm kopen?", "Ja, de tekst van de norm is niet gratis. Je bestelt ze bij het nationale normalisatie-instituut, in België het NBN en in Nederland NEN, of bij ISO zelf."),
        ("Wat is het verschil met ISO 27002?", "ISO 27002 is de leidraad die elke maatregel uit bijlage A uitgebreid toelicht. Je certificeert tegen 27001; 27002 gebruik je als handboek."),
        ("Hoeveel maatregelen passen de meeste kmo's toe?", "De grote meerderheid. Uitsluitingen komen vooral voor bij softwareontwikkeling, eigen datacenters of specifieke technologie die je niet gebruikt."),
    ],
    sources=[ISO, NCSC, CCB],
),
dict(
    path="/kennisbank/verwerkingsregister/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "register", "privacy"],
    title="Verwerkingsregister: wat moet erin? | Cyberdijk",
    desc="Bijna elk bedrijf moet een verwerkingsregister bijhouden. Welke gegevens erin horen, wanneer de uitzondering geldt en hoe je het in een middag opzet.",
    h1="Verwerkingsregister: wat moet erin en hoe zet je het op?",
    lede="Het register van verwerkingsactiviteiten is het fundament van je privacybeleid. Het is verplicht voor bijna elk bedrijf en het is het eerste wat een toezichthouder opvraagt. Zo zet je het op in een middag.",
    kort=[
        "Het register beschrijft per activiteit welke persoonsgegevens je verwerkt, waarvoor, hoe lang en met wie.",
        "De uitzondering voor bedrijven onder 250 medewerkers geldt bijna nooit, omdat loon- en klantenadministratie niet incidenteel zijn.",
        "Een register hoeft geen boekwerk te zijn: een tabel per activiteit volstaat.",
    ],
    body="""
<h2>Wat de wet vraagt</h2>
<p>Artikel 30 van de AVG verplicht de verwerkingsverantwoordelijke om een register bij te houden van alle verwerkingsactiviteiten. Per activiteit, bijvoorbeeld personeelsadministratie of klantenbeheer, noteer je:</p>
<ul>
<li>de naam en contactgegevens van je onderneming, en van je DPO of FG als je er een hebt;</li>
<li>het doel van de verwerking;</li>
<li>de categorieën betrokkenen en de categorieën persoonsgegevens, bijvoorbeeld werknemers met hun identiteits-, loon- en aanwezigheidsgegevens;</li>
<li>de ontvangers, zoals je sociaal secretariaat of salarisadministrateur, je boekhouder en je cloudleverancier;</li>
<li>doorgiften buiten de Europese Economische Ruimte, met de waarborg die je daarvoor gebruikt;</li>
<li>de bewaartermijn, of de regel waarmee je die bepaalt;</li>
<li>een algemene beschrijving van de beveiligingsmaatregelen.</li>
</ul>
<p>Ben je verwerker voor anderen, bijvoorbeeld als IT-dienstverlener of administratiekantoor, dan houd je daarnaast een register bij van de verwerkingen die je voor elke klant uitvoert.</p>
<h2>De uitzondering die bijna nooit geldt</h2>
<p>De verplichting geldt niet voor organisaties met minder dan 250 medewerkers, tenzij de verwerking een risico inhoudt voor de betrokkenen, niet incidenteel is, of gevoelige of strafrechtelijke gegevens omvat. Loonadministratie, klantenbeheer en facturatie zijn nooit incidenteel. In de praktijk heeft daarom elk bedrijf met personeel of klanten een register nodig.</p>
<h2>Zo zet je het op in een middag</h2>
<ol>
<li>Maak een lijst van alles wat je met persoonsgegevens doet: personeel, sollicitanten, klanten, leveranciers, prospects, website, camerabewaking, toegangsbadges.</li>
<li>Vul per activiteit de zeven punten hierboven in. Een rij per activiteit in een spreadsheet is genoeg.</li>
<li>Kijk welke leveranciers gegevens voor je verwerken. Voor elk daarvan heb je een <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomst</a> nodig.</li>
<li>Bepaal per activiteit een bewaartermijn en controleer of je ze ook toepast.</li>
<li>Leg vast wie het register bijhoudt en wanneer je het herziet: minstens jaarlijks en bij elke nieuwe verwerking.</li>
</ol>
<h2>Waarom het meer is dan een plicht</h2>
<p>Het register is het vertrekpunt voor je privacyverklaring, voor de beoordeling of je een <a href="/kennisbank/dpia-wanneer-verplicht/">DPIA</a> nodig hebt, en voor je antwoord bij een <a href="/kennisbank/datalek-melden-72-uur/">datalek</a>. Wie het register op orde heeft, beantwoordt de meeste vragen van een toezichthouder of een klant uit het hoofd.</p>
""",
    faq=[
        ("Moet ik het register ergens indienen?", "Nee. Je houdt het intern bij en legt het voor als de toezichthouder erom vraagt."),
        ("Is er een model?", "Ja. De Gegevensbeschermingsautoriteit en de Autoriteit Persoonsgegevens bieden allebei uitleg en een model aan."),
        ("Welke software heb ik nodig?", "Geen. Een spreadsheet of een document volstaat, zolang het volledig en actueel is."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/datalek-melden-72-uur/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "datalek", "incident", "privacy"],
    title="Datalek melden binnen 72 uur: stappenplan | Cyberdijk",
    desc="Een datalek meld je binnen 72 uur bij de GBA of de Autoriteit Persoonsgegevens. Wat je meteen doet, wat je meldt en wanneer je de betrokkenen informeert.",
    h1="Datalek melden binnen 72 uur: het stappenplan",
    lede="Een verkeerd verstuurde mail, een gestolen laptop, een hack: allemaal datalekken. De AVG geeft je 72 uur om te melden, en die tijd gaat snel. Dit is wat je doet, in volgorde.",
    kort=[
        "Beperk eerst de schade, beoordeel dan het risico en meld binnen 72 uur bij de toezichthouder als er een risico is voor de betrokkenen.",
        "Is het risico hoog, dan informeer je ook de betrokkenen zelf, zonder onnodige vertraging.",
        "Documenteer elk datalek intern, ook als je het niet hoeft te melden.",
    ],
    body="""
<h2>Wat is een datalek?</h2>
<p>Een inbreuk in verband met persoonsgegevens is elke inbreuk op de beveiliging waardoor persoonsgegevens onbedoeld of onrechtmatig worden vernietigd, verloren, gewijzigd, bekendgemaakt of ingezien. Ook een laptop zonder versleuteling die uit een auto gestolen wordt, een mail met het verkeerde bestand of een ransomware-aanval die je gegevens versleutelt, zijn datalekken.</p>
<h2>Stap 1: beperk de schade</h2>
<p>Sluit het lek: blokkeer accounts, koppel systemen los, vraag de ontvanger een verkeerd verstuurde mail te wissen en laat dat bevestigen. Noteer meteen de tijd waarop je het lek ontdekte, want vanaf dan lopen de 72 uur.</p>
<h2>Stap 2: beoordeel het risico</h2>
<p>Welke gegevens, van hoeveel mensen, en wat kan iemand ermee doen? Een lijst met namen en e-mailadressen is iets anders dan medische gegevens of kopieën van identiteitskaarten. Beoordeel de kans op schade voor de betrokkenen: fraude, discriminatie, reputatieschade, financieel verlies. Betrek je DPO of FG als je er een hebt.</p>
<h2>Stap 3: meld bij de toezichthouder</h2>
<p>Is er een risico voor de betrokkenen, dan meld je het datalek binnen 72 uur na de ontdekking. In België doe je dat bij de Gegevensbeschermingsautoriteit, in Nederland bij de Autoriteit Persoonsgegevens; beide hebben een online meldformulier. Je meldt de aard van het lek, de categorieën en het aantal betrokkenen, de mogelijke gevolgen, de maatregelen die je nam en een contactpersoon. Weet je nog niet alles, meld dan wat je weet en vul later aan. Alleen als het onwaarschijnlijk is dat er een risico is, mag je de melding achterwege laten, en dan leg je die beslissing vast.</p>
<h2>Stap 4: informeer de betrokkenen</h2>
<p>Is het risico hoog, dan verwittig je ook de mensen zelf, in gewone taal: wat er gebeurde, wat de gevolgen kunnen zijn, wat jij doet en wat zij kunnen doen, zoals een wachtwoord wijzigen. Dat hoeft niet als de gegevens versleuteld waren en de sleutel veilig is, of als je nadien maatregelen nam die het hoge risico wegnemen.</p>
<h2>Stap 5: documenteer</h2>
<p>Elk datalek komt in een intern register: de feiten, de gevolgen en de maatregelen. Ook de lekken die je niet meldde. De toezichthouder kan dat register opvragen om te controleren of je de regels naleeft.</p>
<h2>Als je verwerker bent</h2>
<p>Verwerk je gegevens voor een klant en ontdek je een lek, dan meld je het zonder onnodige vertraging aan die klant. De klant beslist over de melding bij de toezichthouder. Leg in je <a href="/kennisbank/verwerkersovereenkomst/">verwerkersovereenkomst</a> vast hoe snel en hoe je dat doet.</p>
<h2>Ook NIS2?</h2>
<p>Val je onder NIS2 en is het lek een significant incident, dan geldt daarnaast de <a href="/kennisbank/nis2-meldplicht-incident/">meldplicht van NIS2</a>, met een eerste waarschuwing binnen 24 uur. Twee meldingen dus, bij twee instanties.</p>
""",
    faq=[
        ("Loopt de termijn ook in het weekend?", "Ja. De 72 uur zijn kalenderuren, geen werkdagen. Ontdek je het lek op vrijdagavond, dan moet de melding maandagavond binnen zijn."),
        ("Moet ik een verkeerd verstuurde mail melden?", "Dat hangt af van de inhoud en het risico. Een factuur naar de verkeerde klant is meestal een laag risico; een personeelsdossier of medische gegevens niet. Documenteer in elk geval je beoordeling."),
        ("Wat kost een laattijdige melding?", "Het niet of te laat melden is op zich een inbreuk waarvoor de toezichthouder een boete kan opleggen, naast de beoordeling van het lek zelf."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/verwerkersovereenkomst/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "verwerker", "privacy", "leverancier"],
    title="Verwerkersovereenkomst: wat moet erin? | Cyberdijk",
    desc="Laat je een leverancier persoonsgegevens verwerken, dan is een verwerkersovereenkomst verplicht. De acht afspraken uit artikel 28 AVG en met wie.",
    h1="Verwerkersovereenkomst: wat moet erin en met wie heb je er een nodig?",
    lede="Je sociaal secretariaat, je boekhoudsoftware, je cloudleverancier en je IT-partner verwerken persoonsgegevens voor jou. Met elk van hen heb je een verwerkersovereenkomst nodig. Dit is wat erin moet staan.",
    kort=[
        "Een verwerkersovereenkomst is verplicht zodra een leverancier persoonsgegevens verwerkt in jouw opdracht.",
        "Artikel 28 van de AVG schrijft de inhoud voor: instructies, geheimhouding, beveiliging, onderaannemers, hulp, wissen en controle.",
        "Grote leveranciers bieden hun eigen overeenkomst aan; lees ze na op onderaannemers en doorgiften.",
    ],
    body="""
<h2>Verantwoordelijke en verwerker</h2>
<p>Jij bepaalt waarom en hoe persoonsgegevens worden verwerkt: jij bent de verwerkingsverantwoordelijke. Een leverancier die dat in jouw opdracht doet, zonder er zelf over te beslissen, is een verwerker. Typische verwerkers zijn de salarisadministratie of het sociaal secretariaat, boekhoud- en facturatiesoftware, e-mail- en cloudplatformen, een IT-beheerder met toegang tot je systemen, een nieuwsbriefdienst en een webbureau dat je site host. Een boekhouder die eigen wettelijke taken uitvoert, of een advocaat, is meestal zelf verantwoordelijke en geen verwerker.</p>
<h2>De verplichte afspraken</h2>
<p>Artikel 28 van de AVG vraagt een schriftelijke overeenkomst met het onderwerp en de duur van de verwerking, de aard en het doel, het soort persoonsgegevens en de categorieën betrokkenen. Daarnaast moet de verwerker zich verbinden tot het volgende:</p>
<ol>
<li>Hij verwerkt alleen op jouw gedocumenteerde instructies, ook bij doorgifte buiten de EER.</li>
<li>Zijn medewerkers zijn tot geheimhouding verplicht.</li>
<li>Hij neemt passende beveiligingsmaatregelen.</li>
<li>Hij schakelt alleen onderaannemers in met jouw toestemming, en legt hen dezelfde verplichtingen op.</li>
<li>Hij helpt je bij verzoeken van betrokkenen, zoals inzage of wissing.</li>
<li>Hij helpt je bij de beveiliging, bij datalekken en bij een DPIA.</li>
<li>Hij wist of retourneert de gegevens na afloop van de dienst.</li>
<li>Hij geeft je de informatie die nodig is om de naleving aan te tonen, en laat audits toe.</li>
</ol>
<h2>In de praktijk</h2>
<p>Grote leveranciers hebben een standaardovereenkomst die je online aanvaardt. Lees ze na op drie punten: de lijst van onderaannemers, de landen waar de gegevens staan en de termijn waarbinnen een <a href="/kennisbank/datalek-melden-72-uur/">datalek</a> aan jou gemeld wordt. Bij kleinere leveranciers, zoals een lokale IT-partner, stel je zelf een overeenkomst voor. De Gegevensbeschermingsautoriteit en de Autoriteit Persoonsgegevens bieden uitleg en voorbeelden aan.</p>
<p>Zet je verwerkers in je <a href="/kennisbank/verwerkingsregister/">verwerkingsregister</a> en bewaar elke overeenkomst op één plek. Bij een controle of een vragenlijst van een klant is dit het eerste bewijs dat je toont.</p>
<h2>Verwerker voor je eigen klanten?</h2>
<p>Verwerk je zelf gegevens voor klanten, bijvoorbeeld als IT-dienstverlener, administratiekantoor of softwarebedrijf, dan ben je de verwerker en vragen je klanten jou om deze overeenkomst. Zorg voor een eigen model dat je aan elke klant kan aanbieden, met een duidelijke lijst van je eigen onderaannemers.</p>
""",
    faq=[
        ("Is een clausule in de algemene voorwaarden genoeg?", "Ja, als alle verplichte afspraken erin staan en de leverancier ze schriftelijk aanvaardt. Een apart document is wel overzichtelijker bij een controle."),
        ("Wat als een leverancier weigert te tekenen?", "Dan mag je hem geen persoonsgegevens laten verwerken. Zoek een leverancier die de wet wel naleeft, of beperk de gegevens die hij ziet."),
        ("Heb ik ook een overeenkomst nodig met mijn boekhouder?", "Meestal niet: een boekhouder of accountant bepaalt zelf hoe hij zijn wettelijke taken uitvoert en is dan verantwoordelijke. Voert hij louter je loonadministratie uit op jouw instructies, dan wel."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/dpia-wanneer-verplicht/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["avg", "gdpr", "dpia", "privacy"],
    title="DPIA: wanneer verplicht en hoe doe je het? | Cyberdijk",
    desc="Een DPIA is verplicht bij verwerkingen met een hoog risico. Wanneer dat zo is, wat erin moet staan en wanneer je de toezichthouder vooraf raadpleegt.",
    h1="DPIA: wanneer is een gegevensbeschermingseffectbeoordeling verplicht?",
    lede="Voor sommige verwerkingen vraagt de AVG dat je vooraf de risico's voor de betrokkenen beoordeelt en opschrijft. Dat heet een DPIA. Dit is wanneer je er een nodig hebt en hoe je ze aanpakt zonder er een project van te maken.",
    kort=[
        "Een DPIA is verplicht als een verwerking waarschijnlijk een hoog risico inhoudt voor de betrokkenen, bijvoorbeeld bij grootschalige gevoelige gegevens of systematische monitoring.",
        "De toezichthouders publiceren lijsten van verwerkingen waarvoor een DPIA altijd verplicht is.",
        "Blijft er na je maatregelen een hoog risico over, dan raadpleeg je de toezichthouder vooraf.",
    ],
    body="""
<h2>Wanneer is een DPIA verplicht?</h2>
<p>Artikel 35 van de AVG verplicht een DPIA wanneer een verwerking, vooral met nieuwe technologie, waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van personen. De wet noemt drie gevallen uitdrukkelijk: een systematische en uitgebreide beoordeling van persoonlijke aspecten met beslissingen die mensen in aanmerkelijke mate treffen, zoals profilering; grootschalige verwerking van gevoelige gegevens of van strafrechtelijke gegevens; en stelselmatige en grootschalige monitoring van openbaar toegankelijke ruimten.</p>
<p>Daarnaast hebben de Gegevensbeschermingsautoriteit en de Autoriteit Persoonsgegevens elk een lijst gepubliceerd van verwerkingen waarvoor een DPIA altijd verplicht is. Daarop staan onder meer biometrische identificatie, het volgen van locatie of gedrag, cameratoezicht op werknemers, grootschalige verwerking van gezondheidsgegevens en het gebruik van gegevens voor kredietscores. Voor kmo's en mkb-bedrijven zijn camerabewaking, GPS-tracking in voertuigen en personeelsmonitoring de meest voorkomende aanleidingen.</p>
<h2>Wat erin moet staan</h2>
<ol>
<li>Een systematische beschrijving van de verwerking en het doel, en als dat van toepassing is, het gerechtvaardigd belang.</li>
<li>Een beoordeling van de noodzaak en de evenredigheid: kan het met minder gegevens, minder lang, minder ingrijpend?</li>
<li>Een beoordeling van de risico's voor de betrokkenen.</li>
<li>De maatregelen om die risico's aan te pakken, en het risico dat daarna overblijft.</li>
</ol>
<p>Je vraagt het advies van je DPO of FG als je er een hebt, en waar passend de mening van de betrokkenen of hun vertegenwoordigers, bijvoorbeeld de personeelsvertegenwoordiging bij monitoring van werknemers.</p>
<h2>Zo pak je het aan</h2>
<p>Een DPIA voor een kmo is zelden meer dan tien pagina's. Begin bij je <a href="/kennisbank/verwerkingsregister/">verwerkingsregister</a>: daar staat al wat je verwerkt en waarom. Beschrijf dan per risico wat er mis kan gaan, hoe waarschijnlijk dat is en hoe erg. Kies maatregelen die het risico verkleinen: minder gegevens, kortere bewaartermijn, versleuteling, beperkte toegang, duidelijke informatie aan de betrokkenen. Leg het resultaat vast met een datum en de naam van wie het goedkeurde.</p>
<h2>Voorafgaande raadpleging</h2>
<p>Blijft er ondanks je maatregelen een hoog risico over, dan raadpleeg je de toezichthouder voordat je start. Die heeft in beginsel acht weken om te antwoorden. In de praktijk is dat zeldzaam: meestal verkleinen de maatregelen het risico genoeg.</p>
<h2>Herzien</h2>
<p>Een DPIA herzie je wanneer het risico verandert: een nieuw systeem, een nieuwe leverancier, een ander doel. Spreek een vaste herziening af, bijvoorbeeld om de drie jaar.</p>
""",
    faq=[
        ("Moet ik een DPIA doen voor mijn website?", "Niet voor een gewone website met een contactformulier. Wel als je bezoekers uitgebreid profileert of volgt met technieken die als hoogrisicoverwerking op de lijst van de toezichthouder staan."),
        ("Moet ik de DPIA indienen?", "Nee. Je bewaart ze zelf en toont ze op vraag van de toezichthouder. Alleen bij een overblijvend hoog risico vraag je vooraf advies."),
        ("Is er een sjabloon?", "Ja. Beide toezichthouders bieden uitleg en modellen aan. Een eenvoudig document met de vier verplichte onderdelen volstaat."),
    ],
    sources=[AVG, GBA, AP],
),
dict(
    path="/kennisbank/ai-act-kmo-mkb/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["ai", "avg", "gdpr", "bestuur", "maatregelen"],
    title="AI Act voor kmo's en mkb: wat moet je nu doen? | Cyberdijk",
    desc="De AI Act geldt in stappen: verboden praktijken en AI-geletterdheid sinds 2025, transparantie sinds 2026, hoogrisico later. Wat een kmo nu moet regelen.",
    h1="AI Act voor kmo's en mkb: wat moet je nu al doen?",
    lede="Bijna elk bedrijf gebruikt intussen AI: een chatbot op de website, een tool die sollicitaties voorsorteert, een assistent die mails schrijft. De Europese AI-verordening legt daar regels aan op, in stappen. Dit geldt nu al, en dit komt eraan.",
    kort=[
        "Verboden AI-praktijken en de plicht tot AI-geletterdheid gelden sinds 2 februari 2025.",
        "Transparantieplichten, zoals chatbots die zeggen dat ze AI zijn, gelden sinds 2 augustus 2026.",
        "De regels voor hoogrisico-AI zijn uitgesteld: verwacht vanaf eind 2027 en 2028. Controleer de definitieve tekst.",
    ],
    body="""
<h2>Gebruiker of aanbieder?</h2>
<p>De AI Act maakt onderscheid tussen wie een AI-systeem ontwikkelt en op de markt brengt (de aanbieder) en wie het gebruikt in zijn bedrijf (de gebruiksverantwoordelijke). De meeste kmo's en mkb-bedrijven zijn gebruiker: ze kopen of abonneren zich op een tool. Dat betekent lichtere plichten, maar niet geen plichten.</p>
<h2>Wat nu al geldt</h2>
<ul>
<li><strong>Verboden praktijken</strong> (sinds 2 februari 2025): onder meer emotieherkenning op de werkvloer, sociale scoring en manipulatieve technieken. Gebruik je zo'n systeem, dan moet het weg.</li>
<li><strong>AI-geletterdheid</strong> (sinds 2 februari 2025): wie AI inzet, zorgt dat zijn medewerkers genoeg weten om er verantwoord mee om te gaan. Een korte interne opleiding plus een paar afspraken volstaat voor de meeste kmo's, maar leg vast dat het gebeurd is.</li>
<li><strong>Regels voor algemene AI-modellen</strong> (sinds 2 augustus 2025): die gelden voor de makers van grote modellen, niet voor jou als gebruiker.</li>
<li><strong>Transparantie</strong> (sinds 2 augustus 2026): een chatbot of AI-assistent die met klanten praat, maakt duidelijk dat het om AI gaat. Door AI gemaakte of bewerkte beelden, audio en video die echt lijken, worden gemarkeerd.</li>
</ul>
<h2>Hoogrisico-AI: later, maar bereid je voor</h2>
<p>Voor AI in gevoelige domeinen gelden strengere regels: werving en selectie, beoordeling van werknemers, kredietbeoordeling, toegang tot onderwijs, kritieke infrastructuur en AI die in gereguleerde producten zit. De oorspronkelijke datum van 2 augustus 2026 is via de Digital Omnibus uitgesteld; de verwachting is 2 december 2027 voor zelfstandige hoogrisicosystemen en 2 augustus 2028 voor AI in gereguleerde producten. Gebruik je zo'n systeem, bijvoorbeeld software die sollicitanten rangschikt, dan krijg je plichten rond menselijk toezicht, logging, instructies van de aanbieder en informatie aan de betrokkenen.</p>
<h2>Vijf stappen voor een kmo</h2>
<ol>
<li>Maak een lijst van alle AI die je gebruikt, ook de AI die in bestaande software zit, zoals je hr-pakket of je klantenservice.</li>
<li>Streep verboden toepassingen weg en markeer wat mogelijk hoogrisico is.</li>
<li>Regel de transparantie: laat chatbots zich bekendmaken en markeer gegenereerde beelden.</li>
<li>Organiseer AI-geletterdheid: een opleiding van een halve dag en een korte gebruiksregel, met bewijs van deelname.</li>
<li>Koppel het aan je privacy- en beveiligingsbeleid: AI die persoonsgegevens verwerkt, valt ook onder de <a href="/kennisbank/verwerkingsregister/">AVG</a>, en een nieuw systeem kan een <a href="/kennisbank/dpia-wanneer-verplicht/">DPIA</a> vragen.</li>
</ol>
<h2>Hoe Cyberdijk hiermee verder gaat</h2>
<p>AI-governance wordt het derde spoor van Cyberdijk, naast informatiebeveiliging en privacy. De certificering AIGP (Artificial Intelligence Governance Professional, IAPP) staat gepland zodra de hoogrisico-verplichtingen in zicht komen. Tot dan vind je hier uitleg en kan je <a href="/contact/">je vraag stellen</a>.</p>
""",
    faq=[
        ("Geldt de AI Act ook als ik alleen ChatGPT of Copilot gebruik?", "Ja, als gebruiker. Je zorgt voor AI-geletterdheid bij je medewerkers en je let op wat je er met persoonsgegevens en vertrouwelijke informatie in stopt. Zwaardere plichten komen pas bij hoogrisicotoepassingen."),
        ("Moet mijn chatbot zeggen dat hij AI is?", "Ja. Sinds 2 augustus 2026 moet een AI-systeem dat met mensen praat, duidelijk maken dat het om AI gaat, tenzij dat uit de context al vanzelfsprekend is."),
        ("Wat riskeer ik?", "De boetes lopen tot 35 miljoen euro of 7% van de omzet voor verboden praktijken, en tot 15 miljoen euro of 3% voor andere inbreuken. Voor kmo's gelden lagere plafonds, afgestemd op hun omvang."),
    ],
    sources=[("Verordening (EU) 2024/1689 (AI Act) op EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"), ("Europese Commissie: AI Act Service Desk", "https://ai-act-service-desk.ec.europa.eu"), ("DQS: nieuwe deadlines na het stop-de-klok-mechanisme", "https://www.dqsglobal.com/nl/over/nieuws/eu-ai-wet-parlement-raad-align-on-postponing-high-risk-ai-verplichtingen")],
),
dict(
    path="/kennisbank/spf-dkim-dmarc/", lang="nl", kind="artikel", land="eu", crumbs=KB, tags=["email", "phishing", "maatregelen"],
    title="SPF, DKIM en DMARC instellen: zo werkt het | Cyberdijk",
    desc="Stop vervalste mails uit naam van je bedrijf. Wat SPF, DKIM en DMARC doen, in welke volgorde je ze instelt en hoe je je eigen mail niet blokkeert.",
    h1="SPF, DKIM en DMARC: zo stop je vervalste mails uit naam van je bedrijf",
    lede="Iedereen kan een mail sturen met jouw adres als afzender, tenzij je domein zegt dat het niet mag. Dat doe je met drie DNS-records. Dit is wat ze doen en in welke volgorde je ze instelt.",
    kort=[
        "SPF zegt welke servers namens je domein mogen mailen, DKIM zet een handtekening op elke mail.",
        "DMARC zegt wat ontvangers moeten doen als een mail die controles niet doorstaat.",
        "Begin DMARC in meetstand (p=none) en ga pas na enkele weken naar quarantine of reject.",
    ],
    body="""
<h2>Waarom je dit nodig hebt</h2>
<p>E-mail is gebouwd in een tijd waarin niemand aan oplichters dacht. Het afzenderadres is gewoon tekst: wie wil, zet er factuur@jouwbedrijf.be in. Criminelen gebruiken dat voor valse facturen, nepbetaalverzoeken van "de zaakvoerder" en phishing naar je klanten. SPF, DKIM en DMARC geven ontvangers een manier om na te gaan of een mail echt van jou komt, en zeggen wat ze moeten doen als dat niet zo is.</p>
<p>Er is ook een tweede reden: grote mailproviders stellen eisen. Google vraagt van alle afzenders naar Gmail-adressen SPF of DKIM, en van wie veel mailt ook DMARC. Wie dat niet heeft, ziet zijn echte mails sneller in de spam belanden.</p>
<h2>SPF: wie mag namens jou mailen?</h2>
<p>SPF is één TXT-record op je domein met de lijst van servers die voor jou mogen mailen. Denk aan je mailbox (Microsoft 365, Google Workspace, je hostingbedrijf), maar ook aan je boekhoudpakket dat facturen mailt, je webshop en je nieuwsbriefprogramma. Een voorbeeld:</p>
<p><code>v=spf1 include:spf.protection.outlook.com include:_spf.google.com ~all</code></p>
<p>Let op twee dingen. Er mag maar één SPF-record zijn: twee records maken SPF ongeldig. En het record eindigt op <code>~all</code> of <code>-all</code>, zodat andere servers niet meetellen. Een record met <code>+all</code> laat iedereen toe en is erger dan niets.</p>
<h2>DKIM: een handtekening op elke mail</h2>
<p>Met DKIM zet je mailserver een digitale handtekening op elke uitgaande mail. De bijhorende publieke sleutel staat in je DNS, onder een naam die je leverancier kiest (een selector, zoals <code>selector1._domainkey</code> bij Microsoft of <code>google._domainkey</code> bij Google). DKIM zet je aan in het beheer van je mailleverancier; die geeft je de records die je in je DNS plaatst. Doe dat voor elke dienst die namens jou mailt.</p>
<h2>DMARC: wat moet er gebeuren met vervalste mails?</h2>
<p>DMARC verbindt de twee. Het zegt: een mail die van mijn domein beweert te komen, moet SPF of DKIM doorstaan voor mijn eigen domein. Lukt dat niet, doe dan dit. Dat "dit" is het beleid:</p>
<ul>
<li><code>p=none</code>: niets doen, alleen rapporteren. Handig om te meten, maar het houdt niets tegen.</li>
<li><code>p=quarantine</code>: de mail als spam behandelen.</li>
<li><code>p=reject</code>: de mail weigeren.</li>
</ul>
<p>Een DMARC-record staat op <code>_dmarc.jouwbedrijf.be</code> en ziet er bijvoorbeeld zo uit: <code>v=DMARC1; p=none; rua=mailto:dmarc@jouwbedrijf.be</code>. Het rua-adres krijgt dagelijks rapporten van de grote mailproviders: welke servers mailden namens jouw domein, en slaagden ze voor SPF en DKIM?</p>
<h2>In welke volgorde, zonder je eigen mail te blokkeren</h2>
<ol>
<li><strong>Maak een lijst van alles wat namens je mailt:</strong> mailbox, boekhouding, facturatie, webshop, nieuwsbrief, offerteprogramma, de printer op kantoor.</li>
<li><strong>Zet SPF goed:</strong> één record met al die diensten erin, eindigend op <code>~all</code>.</li>
<li><strong>Zet DKIM aan</strong> bij elke dienst die het ondersteunt.</li>
<li><strong>Zet DMARC op p=none met een rapportadres</strong> en lees twee tot vier weken de rapporten. Duikt er een echte dienst op die faalt? Voeg die toe aan SPF of zet er DKIM aan.</li>
<li><strong>Ga naar p=quarantine,</strong> en na nog een paar weken zonder problemen naar <strong>p=reject</strong>.</li>
</ol>
<p>Gebruik je een domein niet om te mailen, bijvoorbeeld een extra .com of .nl? Zet dan meteen <code>v=spf1 -all</code> en <code>v=DMARC1; p=reject</code>. Ook ongebruikte domeinen worden misbruikt.</p>
<h2>Controleer het resultaat</h2>
<p>Met de <a href="/email-check/">gratis e-mailcheck</a> zie je in tien seconden hoe je domein ervoor staat. Wil je een uitgebreidere test, dan kan dat ook op internet.nl.</p>
""",
    faq=[
        ("Kan ik mijn eigen mail blokkeren met DMARC?", "Ja, als je meteen op p=reject gaat terwijl een dienst die namens jou mailt nog niet in SPF staat of geen DKIM heeft. Begin daarom altijd met p=none en lees de rapporten."),
        ("Hoe lang duurt het instellen?", "Het plaatsen van de records duurt een kwartier. De meetperiode met p=none duurt best twee tot vier weken, afhankelijk van hoeveel diensten namens je mailen."),
        ("Moet een kleine zaak dit ook doen?", "Ja. Oplichters kiezen niet op grootte. Een valse factuur vanaf het domein van een lokale aannemer werkt even goed als een vanaf een groot bedrijf."),
    ],
    sources=[("Google: richtlijnen voor e-mailafzenders", "https://support.google.com/mail/answer/81126?hl=nl"),
             ("NCSC: handreiking Bescherm domeinnamen tegen phishing", "https://www.ncsc.nl/documenten/factsheets/2019/juni/01/factsheet-bescherm-domeinnamen-tegen-phishing"),
             ("Internet.nl: uitleg over DMARC, DKIM en SPF", "https://internet.nl/faqs/mailauth/"),
             ("RFC 7489: DMARC", "https://www.rfc-editor.org/rfc/rfc7489"),
             ("RFC 7208: SPF", "https://www.rfc-editor.org/rfc/rfc7208")],
),
]

from pages_avg import PAGES as _AVG_PAGES
PAGES = PAGES + _AVG_PAGES
from pages_ai import PAGES as _AI_PAGES
PAGES = PAGES + _AI_PAGES

# Begrippenlijst: term, uitleg. Wordt een aparte pagina met DefinedTermSet-schema.
BEGRIPPEN = [
    ("NIS2", "Europese richtlijn (EU) 2022/2555 over de beveiliging van netwerk- en informatiesystemen. Elk land zet ze om in een eigen wet: in België de NIS2-wet van 2024, in Nederland de Cyberbeveiligingswet."),
    ("Cyberbeveiligingswet", "De Nederlandse wet die NIS2 omzet. In werking sinds 15 augustus 2026. Kent een zorgplicht, een meldplicht en een registratieplicht."),
    ("Essentiële entiteit", "Grote organisatie in een van de meest kritieke sectoren, zoals energie, transport, zorg of digitale infrastructuur. Staat onder proactief toezicht en moet in België tegen 18 april 2027 een conformiteitsbeoordeling laten uitvoeren."),
    ("Belangrijke entiteit", "Organisatie die onder NIS2 valt maar niet essentieel is: middelgrote bedrijven uit de meest kritieke sectoren en bedrijven uit de andere kritieke sectoren. Wordt achteraf gecontroleerd."),
    ("CCB", "Centrum voor Cybersecurity België: de nationale autoriteit voor cybersecurity en de toezichthouder voor NIS2 in België."),
    ("Safeonweb@Work", "Portaal van het CCB waar Belgische entiteiten zich registreren voor NIS2, incidenten melden en het CyFun-kader vinden."),
    ("NCSC", "Nationaal Cyber Security Centrum: het Nederlandse centrum voor cybersecurity, dat onder meer het entiteitenregister van de Cyberbeveiligingswet beheert."),
    ("CSIRT", "Computer Security Incident Response Team: het team waar je onder NIS2 een significant incident meldt. In België is dat het CCB, in Nederland het team dat voor je sector is aangewezen."),
    ("CyFun", "CyberFundamentals: het Belgische kader van het CCB met concrete beveiligingsmaatregelen op vier niveaus: Small, Basic, Important en Essential. Gratis beschikbaar op cyfun.eu."),
    ("CyFun-label", "Officiële bevestiging dat je voldoet aan een CyFun-niveau, na verificatie door een erkende instelling (Basic en Important) of certificatie (Essential)."),
    ("Conformiteitsbeoordelingsinstantie", "Onafhankelijke, erkende instelling die controleert of je voldoet aan een kader of norm, zoals CyFun of ISO 27001, en daarover een verklaring of certificaat afgeeft."),
    ("ISO/IEC 27001", "Internationale norm voor een managementsysteem voor informatiebeveiliging. Een geaccrediteerde instelling reikt het certificaat uit; het geldt drie jaar met jaarlijkse controle-audits."),
    ("ISMS", "Information Security Management System: het geheel van beleid, risicoanalyse, maatregelen, controles en verbetering waarmee je informatiebeveiliging beheert. De kern van ISO 27001."),
    ("Verklaring van toepasselijkheid", "Document binnen ISO 27001 waarin je per maatregel uit bijlage A vastlegt of je ze toepast en waarom. In het Engels: Statement of Applicability."),
    ("Certificatie-audit", "Audit in twee fasen waarmee een certificerende instelling controleert of je managementsysteem aan de norm voldoet. Daarna volgen jaarlijkse controle-audits en na drie jaar een hercertificatie."),
    ("GDPR / AVG", "De Algemene Verordening Gegevensbescherming, in België meestal GDPR genoemd. Europese verordening over de verwerking van persoonsgegevens, rechtstreeks van toepassing in elk land."),
    ("DPO / FG", "Data Protection Officer of functionaris voor gegevensbescherming: de verplichte of vrijwillige toezichthouder op privacy binnen een organisatie. Verplicht voor overheden en voor organisaties die op grote schaal personen volgen of gevoelige gegevens verwerken."),
    ("Verwerkingsverantwoordelijke", "De organisatie die bepaalt waarom en hoe persoonsgegevens worden verwerkt. Draagt de eindverantwoordelijkheid onder de AVG."),
    ("Verwerker", "Een leverancier die persoonsgegevens verwerkt in opdracht van de verwerkingsverantwoordelijke, zoals een cloudleverancier of een salarisadministrateur. Vereist een verwerkersovereenkomst."),
    ("Verwerkingsregister", "Verplicht overzicht van alle verwerkingsactiviteiten van een organisatie: doelen, gegevens, ontvangers, bewaartermijnen en beveiliging. Artikel 30 van de AVG."),
    ("DPIA", "Data Protection Impact Assessment of gegevensbeschermingseffectbeoordeling: verplichte risicoanalyse vooraf bij verwerkingen met een waarschijnlijk hoog risico. Artikel 35 van de AVG."),
    ("Datalek", "Inbreuk op de beveiliging waardoor persoonsgegevens verloren gaan, gewijzigd worden of in verkeerde handen komen. Meld je binnen 72 uur bij de toezichthouder als er een risico is voor de betrokkenen."),
    ("Gegevensbeschermingsautoriteit", "De Belgische privacytoezichthouder, kortweg GBA. Hier meld je datalekken en kunnen betrokkenen klacht indienen."),
    ("Autoriteit Persoonsgegevens", "De Nederlandse privacytoezichthouder, kortweg AP. Hier meld je datalekken en kunnen betrokkenen klacht indienen."),
    ("BIO2", "Baseline Informatiebeveiliging Overheid, versie 2: het normenkader voor informatiebeveiliging bij de Nederlandse overheid, gebaseerd op ISO 27001 en 27002."),
    ("NEN 7510", "Nederlandse norm voor informatiebeveiliging in de zorg, gebouwd op ISO 27001 met extra eisen voor zorginstellingen."),
    ("IEC 62443", "Internationale normenreeks voor de beveiliging van industriële besturingssystemen, zoals in fabrieken en havens. Wordt vaak gevraagd naast ISO 27001."),
    ("Multifactorauthenticatie", "Tweestapsverificatie: inloggen met een wachtwoord plus een tweede bewijs, zoals een code op je telefoon. Uitdrukkelijk genoemd in NIS2 en de basis van elk CyFun-niveau."),
    ("AI Act", "Verordening (EU) 2024/1689 over kunstmatige intelligentie. Verbiedt bepaalde toepassingen, vraagt AI-geletterdheid en transparantie, en legt strenge regels op aan hoogrisico-AI. Geldt in stappen sinds 2025."),
    ("AI-geletterdheid", "Plicht uit de AI Act, sinds 2 februari 2025: wie AI inzet, zorgt dat medewerkers genoeg kennis hebben om er verantwoord mee om te gaan."),
    ("Hoogrisico-AI", "AI in gevoelige domeinen zoals werving, personeelsbeoordeling, kredietverlening of kritieke infrastructuur. Krijgt onder de AI Act de strengste regels: menselijk toezicht, logging en informatieplichten."),
    ("AIGP", "Artificial Intelligence Governance Professional, de certificering van IAPP voor wie AI-governance en de AI Act in een organisatie invoert."),
    ("Kmo-portefeuille", "Vlaamse subsidie voor opleiding en advies bij geregistreerde dienstverleners. Kleine ondernemingen krijgen 45% steun op advies rond cybersecurity, middelgrote 35%."),
]

BEGRIPPEN_PAGE = dict(
    path="/kennisbank/begrippen/", lang="nl", kind="begrippen", land="eu", crumbs=KB, tags=["nis2", "cyfun", "iso", "avg", "gdpr"],
    title="Begrippenlijst: NIS2, CyFun, ISO 27001, AVG en AI Act",
    desc="Alle begrippen uit de wetgeving over informatiebeveiliging, privacy en AI in gewone taal: van essentiële entiteit en CyFun-label tot DPIA en AI Act.",
    h1="Begrippenlijst: informatiebeveiliging en privacy in gewone taal",
    lede="Wetten en normen zitten vol afkortingen. Dit zijn de begrippen die je tegenkomt bij NIS2, CyFun, ISO 27001 en de GDPR/AVG, elk in twee zinnen uitgelegd.",
    body="",
)

# Overzicht voor de startpagina en de kennisbank: (pad, titel, land, korte omschrijving). Nieuwste eerst.
def artikels():
    uit = []
    for p in PAGES:
        uit.append((p["path"], p["h1"], {"be": "België", "nl": "Nederland"}.get(p["land"], "België en Nederland"), p["kort"][0] if p.get("kort") else p["desc"]))
    return uit
