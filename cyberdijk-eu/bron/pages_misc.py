from pages_be import CCB, SAW, CYFUN
from pages_nl import NCSC, RIJK, DTC, FM
import pages_kennis

KB = [("Kennisbank", "/kennisbank/")]

# Overzicht van alle artikels: (pad, titel, land, korte omschrijving). De eerste drie zijn de oudste, dan de nieuwe reeks.
ARTIKELS = [
    ("/kennisbank/valt-mijn-bedrijf-onder-nis2/", "Valt mijn bedrijf onder NIS2? Zo controleer je het", "België", "In drie stappen weet je of je Belgische onderneming onder de NIS2-wet valt."),
    ("/kennisbank/cyberbeveiligingswet-wat-nu/", "Cyberbeveiligingswet sinds 15 augustus 2026: wat moet je nu doen?", "Nederland", "Vijf stappen voor organisaties die onder de Nederlandse wet vallen."),
    ("/kennisbank/cyfun-niveaus/", "CyFun Basic, Important of Essential: welk niveau heb je nodig?", "België", "De vier niveaus van het Belgische kader en hoe je het juiste kiest."),
] + pages_kennis.artikels()

PAGES = [
dict(
    path="/", lang="nl", kind="home", land=None, crumbs=[],
    title="NIS2, ISO 27001 en GDPR/AVG helder uitgelegd | Cyberdijk",
    desc="Heldere uitleg over NIS2, CyFun, ISO 27001 en GDPR/AVG voor kmo's en mkb tussen Antwerpen en Breda. Doe de gratis NIS2-check in vijf minuten.",
    h1="NIS2, ISO 27001 en privacy, helder uitgelegd voor bedrijven tussen Antwerpen en Breda",
    lede="Klanten, verzekeraars en toezichthouders vragen steeds vaker bewijs dat je beveiliging op orde is. Cyberdijk legt uit wat de wet van jouw bedrijf vraagt en hoe je dat stap voor stap regelt, zonder jargon.",
    body="",
),
dict(
    path="/kennisbank/", lang="nl", kind="lijst", land=None, crumbs=[],
    title="Kennisbank: NIS2, CyFun, ISO 27001 en privacy | Cyberdijk",
    desc="Praktische artikels over NIS2, CyFun, de Cyberbeveiligingswet, ISO 27001 en GDPR/AVG voor bedrijven in België en Nederland.",
    h1="Kennisbank",
    lede="Elke week een nieuw artikel dat één vraag beantwoordt. Bij elk artikel staat voor welk land het geldt, welke bronnen gebruikt zijn en wanneer het voor het laatst is gecontroleerd.",
    body="",
),
dict(
    path="/kennisbank/valt-mijn-bedrijf-onder-nis2/", lang="nl-BE", kind="artikel", land="be", crumbs=KB, tags=["nis2", "registratie"],
    title="Valt mijn bedrijf onder NIS2? Zo check je het | Cyberdijk",
    desc="In drie stappen weet je of je Belgische onderneming onder de NIS2-wet valt: sector, grootte en uitzonderingen. Met de officiële bronnen.",
    h1="Valt mijn bedrijf onder NIS2? Zo controleer je het",
    lede="Je valt onder de Belgische NIS2-wet als je onderneming actief is in een aangeduide sector en minstens middelgroot is. Hieronder doorloop je de drie stappen.",
    body="""
<h2>Stap 1: je sector</h2>
<p>De wet werkt met twee lijsten. De eerste bevat de meest kritieke sectoren: energie, transport (luchtvaart, spoor, scheepvaart en havens, wegbeheer), bankwezen en financiële markten, gezondheidszorg, drinkwater en afvalwater, digitale infrastructuur, beheer van ICT-diensten voor bedrijven, overheid en ruimtevaart. De tweede bevat andere kritieke sectoren: post- en koeriersdiensten, afvalbeheer, chemie, voeding, maakindustrie, digitale aanbieders en onderzoek.</p>
<p>Staat je activiteit in geen van beide lijsten, dan val je er niet rechtstreeks onder. Dat geldt bijvoorbeeld voor wegvervoer, opslag, bouw en de meeste handel.</p>
<h2>Stap 2: je grootte</h2>
<p>Binnen die sectoren geldt de wet vanaf een middelgrote onderneming: minstens 50 werknemers, of een jaaromzet en een balanstotaal boven 10 miljoen euro. Hoort je onderneming bij een groep, dan worden de cijfers in veel gevallen samengeteld.</p>
<h2>Stap 3: de uitzonderingen</h2>
<p>Enkele diensten vallen onder de wet ongeacht hun grootte, zoals aanbieders van openbare elektronische communicatie, vertrouwensdiensten en domeinnaamregisters. De overheid kan ook een organisatie aanduiden die de enige aanbieder is van een essentiële dienst.</p>
<h2>Essentieel of belangrijk?</h2>
<p>Een grote onderneming uit de eerste lijst is een essentiële entiteit: minstens 250 werknemers, of meer dan 50 miljoen euro omzet en meer dan 43 miljoen euro balanstotaal. Middelgrote ondernemingen uit de eerste lijst, en alle ondernemingen uit de tweede lijst die onder de wet vallen, zijn belangrijke entiteiten.</p>
<h2>En als je er niet onder valt?</h2>
<p>Dan heb je geen wettelijke plichten uit NIS2. Je klanten kunnen wel bewijs vragen van je beveiliging, omdat zij de risico's in hun keten moeten beheersen. Het CyFun-niveau Basic is daarvoor een gangbaar antwoord. <a href="/be/nis2-check/">Doe de NIS2-check</a> voor een eerste indicatie, of lees <a href="/be/nis2-cyfun/">wat NIS2 en CyFun vragen</a>.</p>
""",
    sources=[CCB, SAW],
),
dict(
    path="/kennisbank/cyberbeveiligingswet-wat-nu/", lang="nl-NL", kind="artikel", land="nl", crumbs=KB, tags=["nis2", "meldplicht", "registratie", "bestuur", "maatregelen"],
    title="Cyberbeveiligingswet geldt: wat moet je nu doen? | Cyberdijk",
    desc="De Cyberbeveiligingswet geldt sinds 15 augustus 2026, zonder overgangsperiode. Vijf stappen voor organisaties die eronder vallen.",
    h1="Cyberbeveiligingswet sinds 15 augustus 2026: wat moet je nu doen?",
    lede="De Cyberbeveiligingswet kent geen overgangsperiode. Val je eronder, dan gelden de plichten nu. Deze vijf stappen brengen je op orde.",
    body="""
<h2>1. Bepaal of je eronder valt</h2>
<p>Kijk naar je sector en je omvang. De wet geldt in de regel vanaf 50 medewerkers, of meer dan 10 miljoen euro omzet en balanstotaal, in aangewezen sectoren. <a href="/nl/nis2-check/">Doe de check</a> voor een eerste indicatie.</p>
<h2>2. Registreer je organisatie</h2>
<p>Val je eronder, dan registreer je je in het entiteitenregister van het NCSC. Die plicht geldt sinds 15 augustus 2026.</p>
<h2>3. Leg je risicoanalyse en maatregelen vast</h2>
<p>De zorgplicht vraagt passende maatregelen. Begin met een risicoanalyse en leg vast wat je doet aan toegangsbeheer, back-ups, updates, leveranciers en continuïteit. Zonder documentatie kun je bij een controle niets aantonen.</p>
<h2>4. Regel de meldprocedure</h2>
<p>Spreek af wie een incident beoordeelt, wie meldt en hoe je de termijnen haalt: een eerste waarschuwing binnen 24 uur, de melding binnen 72 uur en het eindverslag binnen een maand.</p>
<h2>5. Betrek het bestuur</h2>
<p>Bestuurders keuren de maatregelen goed en moeten genoeg kennis hebben om de risico's te beoordelen. Plan de opleiding in en leg vast dat ze gevolgd is.</p>
<h2>Val je er niet onder?</h2>
<p>Dan kun je de eisen via je klanten krijgen. Zorg dat je een beveiligingsbeleid, een incidentprocedure en een overzicht van je maatregelen kunt laten zien. Lees <a href="/nl/cyberbeveiligingswet-nis2/">wat de Cyberbeveiligingswet vraagt</a> en wanneer <a href="/nl/iso-27001/">ISO 27001</a> zinvol is.</p>
""",
    sources=[NCSC, RIJK, DTC, FM],
),
dict(
    path="/kennisbank/cyfun-niveaus/", lang="nl-BE", kind="artikel", land="be", crumbs=KB, tags=["cyfun", "nis2", "zelfevaluatie"],
    title="CyFun-niveaus: Basic, Important of Essential? | Cyberdijk",
    desc="CyFun kent vier niveaus: Small, Basic, Important en Essential. Lees welk niveau bij je bedrijf past en hoe je het laat beoordelen.",
    h1="CyFun Basic, Important of Essential: welk niveau heb je nodig?",
    lede="Val je onder NIS2, dan volgt je CyFun-niveau uit je statuut. Val je er niet onder, dan bepaalt je klant het niveau, en dat is meestal Basic.",
    body="""
<h2>Wat is CyFun?</h2>
<p>CyberFundamentals is het kader van het Centrum voor Cybersecurity België. Het bundelt maatregelen uit bekende normen in één lijst, gegroepeerd per niveau. Het kader en de hulpmiddelen staan gratis op cyfun.eu.</p>
<h2>De vier niveaus</h2>
<ul>
<li>Small: de absolute basis voor kleine ondernemingen, zoals updates, back-ups en tweestapsverificatie.</li>
<li>Basic: de standaardmaatregelen voor elke onderneming. Dit is wat klanten meestal van een toeleverancier vragen.</li>
<li>Important: bedoeld voor belangrijke entiteiten onder NIS2 en voor bedrijven met een hoger risico.</li>
<li>Essential: het hoogste niveau, voor essentiële entiteiten.</li>
</ul>
<h2>Hoe kies je het niveau?</h2>
<p>Val je onder NIS2, dan volgt het niveau uit je statuut: belangrijke entiteiten mikken op Important, essentiële op Essential. Twijfel je, dan helpt het CCB je met een hulpmiddel om je risico in te schatten. Val je er niet onder, dan bepaalt je klant het niveau. Vraag wat hij verwacht en tegen wanneer.</p>
<h2>Zelfevaluatie, verificatie of certificatie</h2>
<p>Je begint altijd met een zelfevaluatie. Voor de niveaus Basic en Important kan een erkende instelling die zelfevaluatie controleren; dat heet verificatie. Voor het niveau Essential volgt een certificatie-audit. Essentiële entiteiten zijn tot zo'n beoordeling verplicht, tegen 18 april 2027.</p>
<p>Lees verder: <a href="/be/nis2-cyfun/">NIS2 en CyFun voor kmo's</a> en <a href="/be/iso-27001/">ISO 27001 of CyFun</a>.</p>
""",
    sources=[CYFUN, CCB, SAW],
),
] + pages_kennis.PAGES + [pages_kennis.BEGRIPPEN_PAGE] + [
dict(
    path="/email-check/", lang="nl", kind="emailcheck", land="eu", crumbs=[], tags=["email", "phishing", "maatregelen"],
    title="Gratis e-mailcheck: SPF, DKIM en DMARC | Cyberdijk",
    desc="Kan iemand mailen uit naam van je bedrijf? Test gratis je SPF, DKIM en DMARC en zie meteen wat je moet doen. Er wordt niets bewaard.",
    h1="Kan iemand mailen uit naam van jouw bedrijf?",
    lede="Oplichters sturen valse facturen en betaalverzoeken die van je eigen domein lijken te komen. Drie DNS-records houden dat tegen: SPF, DKIM en DMARC. Test in tien seconden of ze bij jou goed staan.",
    body="""
<h2>Wat de check controleert</h2>
<ul>
<li><strong>DMARC:</strong> zegt aan mailservers wat ze moeten doen met een mail die zich voordoet als jouw domein maar de controles niet doorstaat. Pas met <code>p=quarantine</code> of <code>p=reject</code> worden vervalste mails echt tegengehouden.</li>
<li><strong>SPF:</strong> de lijst van servers die namens jouw domein mogen mailen, zoals je mailbox, je boekhoudpakket of je nieuwsbriefprogramma.</li>
<li><strong>DKIM:</strong> een digitale handtekening op elke mail, zodat de ontvanger ziet dat de mail onderweg niet is aangepast.</li>
<li><strong>Mailserver en website:</strong> bij wie je mail binnenkomt en of je website via HTTPS werkt.</li>
</ul>
<h2>Waarom dit ertoe doet</h2>
<p>Een valse mail vanaf je eigen domein is de eenvoudigste manier om je klanten een vervalste factuur met een ander rekeningnummer te sturen. Zonder DMARC in een strenge stand komt zo'n mail vaak gewoon aan. Daarnaast eisen grote mailproviders zoals Gmail steeds vaker dat afzenders SPF, DKIM en DMARC hebben; anders belanden ook je echte mails sneller in de spam.</p>
<p>Voor bedrijven onder NIS2 hoort e-mailbeveiliging bij de basismaatregelen voor cyberhygiëne. Maar ook voor een kleine zaak is het een kwartier werk met een groot effect.</p>
<h2>En daarna?</h2>
<p>Lees <a href="/kennisbank/spf-dkim-dmarc/">hoe je SPF, DKIM en DMARC stap voor stap instelt</a>. Begin DMARC altijd in meetstand en zet het pas strenger als je zeker weet dat al je echte mail slaagt; anders blokkeer je je eigen facturen.</p>
""",
    faq=[
        ("Wordt mijn domein of e-mailadres bewaard?", "Nee. De check vraagt alleen openbare DNS-gegevens op en toont het resultaat. Er wordt niets opgeslagen en je hoeft geen e-mailadres achter te laten."),
        ("Mijn score is laag, maar mijn mail werkt toch?", "Dat kan. De check gaat er niet over of jouw mails aankomen, maar of iemand anders mails kan sturen die van jouw domein lijken te komen."),
        ("De check vindt geen DKIM. Klopt dat?", "Niet altijd. DKIM staat onder een naam (selector) die per mailleverancier verschilt. We testen de gangbare namen van Google, Microsoft en de bekende mailprogramma's. Vraag het bij twijfel na bij je leverancier."),
        ("Is p=none voldoende?", "Nee. Met p=none verzamel je alleen rapporten; vervalste mails komen nog steeds aan. Het is een goede eerste stap om te meten, niet het eindpunt."),
    ],
    sources=[("Google: richtlijnen voor e-mailafzenders", "https://support.google.com/mail/answer/81126?hl=nl"),
             ("NCSC: handreiking Bescherm domeinnamen tegen phishing", "https://www.ncsc.nl/documenten/factsheets/2019/juni/01/factsheet-bescherm-domeinnamen-tegen-phishing"),
             ("Internet.nl: uitleg over DMARC, DKIM en SPF", "https://internet.nl/faqs/mailauth/"),
             ("RFC 7489: DMARC", "https://www.rfc-editor.org/rfc/rfc7489")],
),
dict(
    path="/diensten/", lang="nl", kind="diensten", land="eu", crumbs=[], tags=["nis2", "cyfun", "iso", "avg", "gdpr", "bestuur"],
    title="NIS2-, ISO 27001- en GDPR-begeleiding voor kmo's | Cyberdijk",
    desc="Begeleiding bij NIS2 en CyFun, ISO 27001, GDPR/AVG en de bestuursopleiding voor kmo's en mkb tussen Antwerpen en Breda. Zet je op de wachtlijst.",
    h1="Begeleiding bij NIS2, ISO 27001 en GDPR voor kmo's en mkb",
    lede="Cyberdijk is vandaag een kennissite. Begeleiding start na afronding van de certificering, verwacht in 2027. Wil je er als eerste bij zijn? Zet je op de wachtlijst, dan hoor je het meteen en krijg je een voorrangstarief.",
    body="""
<h2>Waarom wachten tot de certificering?</h2>
<p>Je vertrouwt je beveiliging en je persoonsgegevens niet toe aan iemand die het "wel ongeveer weet". Daarom begint Cyberdijk pas met betaalde begeleiding wanneer de certificaten ISO/IEC 27001 Lead Implementer en CIPP/E behaald zijn. Tot dan krijg je wat nu al kan: eerlijke uitleg, een gratis check en een antwoord op je vraag.</p>
<h2>Voor wie</h2>
<p>Kmo's en mkb-bedrijven tussen Antwerpen en Breda die onder NIS2 of de Cyberbeveiligingswet vallen, of die van een grote klant een vragenlijst, een CyFun-niveau of een ISO 27001-certificaat gevraagd krijgen. Geen technische installaties, wel beleid, risico, documentatie en bewijs.</p>
<h2>Hoe de begeleiding eruitziet</h2>
<ol>
<li>Een intake van een uur: waar sta je, wat vraagt de wet of je klant, en wat is de kortste weg.</li>
<li>Een vaste prijs per traject, vooraf. Geen uurtje-factuurtje.</li>
<li>Je eigen mensen doen het werk waar dat kan; Cyberdijk structureert, schrijft mee en controleert.</li>
<li>Een dossier dat je kan tonen aan een toezichthouder, een klant of een auditor.</li>
</ol>
<p>Kleine ondernemingen in Vlaanderen kunnen 45% steun krijgen via de kmo-portefeuille voor advies rond cybersecurity bij een geregistreerde dienstverlener. Registratie bij de kmo-portefeuille is gepland zodra de begeleiding start.</p>
""",
    faq=[
        ("Wanneer start de begeleiding?", "Na afronding van de certificering, verwacht in 2027. Wie op de wachtlijst staat, hoort het als eerste."),
        ("Wat kost het?", "Elk traject krijgt een vaste prijs, vooraf. De richtprijzen in de markt staan in de artikels over NIS2 en ISO 27001; Cyberdijk mikt op de kant van de kmo."),
        ("Kan ik nu al iets doen?", "Ja. Doe de NIS2-check, lees de uitleg per onderwerp en stel je vraag via het contactformulier. Dat is gratis."),
    ],
),
dict(
    path="/over/", lang="nl", kind="vast", land=None, crumbs=[],
    title="Over Cyberdijk: wie, en welke certificaten | Cyberdijk",
    desc="Cyberdijk legt informatiebeveiliging en privacy uit voor bedrijven tussen Antwerpen en Breda. Wie erachter zit en welke certificaten in opleiding zijn.",
    h1="Over Cyberdijk",
    lede="Cyberdijk legt informatiebeveiliging en privacy uit voor bedrijven in de grensregio tussen Antwerpen en Breda. De regels komen uit Europa, maar België en Nederland vullen ze elk anders in.",
    body="""
<h2>Wie zit erachter?</h2>
<p>Achter Cyberdijk zit een ondernemer met meer dan tien jaar ervaring in online marketing en websites voor zelfstandigen, die zich omschoolt tot specialist in informatiebeveiliging en privacy. Niet vanuit de techniek, maar vanuit beleid, risico en organisatie: de kant waar NIS2, CyFun, ISO 27001 en de GDPR over gaan.</p>
<h2>Opleiding en certificering</h2>
<p>Cyberdijk kiest voor erkende, internationale certificaten. De opleidingen lopen; zodra een certificaat behaald is, staat het hier met datum.</p>
<ul>
<li><strong>ISO/IEC 27001 Lead Implementer</strong> (PECB): de norm voor een managementsysteem voor informatiebeveiliging, van scope tot certificatie-audit. In opleiding, examen gepland voor begin 2027.</li>
<li><strong>CIPP/E</strong> (IAPP): Certified Information Privacy Professional/Europe, de referentie voor de GDPR en het Europese privacyrecht. In opleiding, examen gepland voor begin 2027.</li>
<li><strong>CyberFundamentals</strong> (CCB): het Belgische kader voor NIS2, inclusief de zelfevaluatie op de niveaus Small tot Essential. Zelfstudie, lopend.</li>
<li><strong>Daarna:</strong> CIPM (IAPP) voor de rol van DPO of FG en NIS2 Lead Implementer België.</li>
<li><strong>AIGP</strong> (IAPP, Artificial Intelligence Governance Professional): het derde spoor, AI-governance en de AI Act. Gepland tegen de hoogrisico-verplichtingen van de AI Act, verwacht eind 2027. Lees alvast <a href="/kennisbank/ai-act-kmo-mkb/">wat de AI Act nu al van een kmo vraagt</a>.</li>
</ul>
<h2>Wat je nu van Cyberdijk mag verwachten</h2>
<p>Op dit moment: heldere uitleg, een gratis check en een antwoord op je vraag. Begeleiding bij NIS2, CyFun, ISO 27001 en GDPR/AVG start na de certificering. Tot dan verwijst Cyberdijk voor formeel advies naar de officiële bronnen en naar erkende dienstverleners.</p>
<h2>Hoe de uitleg tot stand komt</h2>
<p>Elke pagina vermeldt haar bronnen en de datum van de laatste controle. Wijzigt de regelgeving, dan wordt de pagina bijgewerkt. Zie je een fout? Meld het via <a href="/contact/">het contactformulier</a>.</p>
""",
),
dict(
    path="/contact/", lang="nl", kind="contact", land=None, crumbs=[],
    title="Contact: stel je vraag | Cyberdijk",
    desc="Stel je vraag over NIS2, CyFun, de Cyberbeveiligingswet, ISO 27001 of GDPR/AVG. Je krijgt binnen twee werkdagen antwoord per e-mail.",
    h1="Stel je vraag",
    lede="Heb je een vraag over NIS2, CyFun, de Cyberbeveiligingswet, ISO 27001 of GDPR/AVG? Je krijgt binnen twee werkdagen antwoord per e-mail.",
    body="",
),
dict(
    path="/contact/bedankt/", lang="nl", kind="vast", land=None, crumbs=[], noindex=True,
    title="Je vraag is verstuurd | Cyberdijk",
    desc="Je vraag is verstuurd. Je krijgt binnen twee werkdagen antwoord per e-mail.",
    h1="Je vraag is verstuurd",
    lede="Je krijgt binnen twee werkdagen antwoord per e-mail.",
    body="""<p><a href="/kennisbank/">Lees intussen verder in de kennisbank</a>.</p>""",
),
dict(
    path="/privacy/", lang="nl", kind="vast", land=None, crumbs=[],
    title="Privacyverklaring | Cyberdijk",
    desc="Welke persoonsgegevens Cyberdijk verwerkt, waarvoor, hoe lang en met wie. Deze site plaatst geen cookies en gebruikt geen trackers.",
    h1="Privacyverklaring",
    lede="Cyberdijk verwerkt zo weinig persoonsgegevens als mogelijk. Deze site plaatst geen cookies en gebruikt geen trackers.",
    body="__PRIVACY__",
),
dict(
    path="/cookies/", lang="nl", kind="vast", land=None, crumbs=[],
    title="Cookies | Cyberdijk",
    desc="Deze site plaatst geen cookies en laadt geen lettertypes, scripts of afbeeldingen van andere partijen.",
    h1="Cookies",
    lede="Deze site plaatst geen cookies. Daarom zie je ook geen cookiebanner.",
    body="""
<p>De site laadt geen lettertypes, scripts of afbeeldingen van andere partijen. De NIS2-check draait volledig in je browser en bewaart of verstuurt niets.</p>
<p>Verandert dat later, bijvoorbeeld door bezoekersstatistieken, dan staat het eerst op deze pagina. Niet-noodzakelijke cookies worden pas geplaatst na je toestemming.</p>
""",
),
]
