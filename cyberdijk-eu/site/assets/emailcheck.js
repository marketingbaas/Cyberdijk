(function(){
var MB="https://www.marketingbaas.com/e-mail-beveiligen/";
function el(t,txt,c){var n=document.createElement(t);if(txt){n.textContent=txt;}if(c){n.className=c;}return n;}
function schoon(v){v=(v||"").trim().toLowerCase().replace(/^[a-z]+:\/\//,"").replace(/^.*@/,"").split(/[\/?#:]/)[0].replace(/^www\./,"").replace(/\.$/,"");return v;}
function rij(uit,status,kop,tekst,tip){var r=el("div","","ec-rij");var b=el("span",status==="goed"?"✓":status==="matig"?"!":"✕","ec-bol ec-"+status);b.setAttribute("aria-hidden","true");r.appendChild(b);
var d=el("div");var h=el("h3",kop);var sr=el("span",status==="goed"?" (in orde)":status==="matig"?" (kan beter)":" (niet in orde)","verborgen");h.appendChild(sr);d.appendChild(h);d.appendChild(el("p",tekst));if(tip){d.appendChild(el("p",tip,"klein"));}r.appendChild(d);uit.appendChild(r);}
function toon(uit,j){uit.textContent="";var d=j.domein;
var kop=el("div","","ec-kop "+(j.vervalsbaar?"ec-rood":"ec-groen"));
kop.appendChild(el("p",j.vervalsbaar?"Iedereen kan mailen als @"+d:"Vervalste mails van @"+d+" worden tegengehouden","ec-titel"));
kop.appendChild(el("p","Score: "+j.score+"/100","ec-score"));uit.appendChild(kop);
var m=j.dmarc;
if(m.p==="geen"){rij(uit,"slecht","DMARC: ontbreekt","Er staat geen DMARC-record. Mailservers weten dan niet wat ze moeten doen met een mail die zich voordoet als @"+d+": de meeste laten hem gewoon door.","Voeg een DMARC-record toe, eerst in meetstand (p=none) met rapporten, en zet het na enkele weken op quarantine of reject.");}
else if(m.p==="none"){rij(uit,"matig","DMARC: alleen meten (p=none)","Je DMARC-record houdt niets tegen. Het verzamelt hooguit rapporten"+(m.rua?"":", maar er staat geen rapportadres (rua) in")+". Vervalste mails komen dus nog steeds aan.","Bekijk de rapporten en zet het record daarna op p=quarantine en later p=reject.");}
else{rij(uit,m.pct<100?"matig":"goed","DMARC: "+m.p+(m.pct<100?" voor "+m.pct+"% van de mails":""),m.pct<100?"Je DMARC-beleid geldt maar voor een deel van de mails. De rest komt nog door.":"Mails die niet van je eigen servers komen, worden "+(m.p==="reject"?"geweigerd":"als spam behandeld")+". Goed zo.",m.rua?"":"Tip: voeg een rapportadres (rua) toe, dan zie je wie namens jou probeert te mailen.");}
var s=j.spf;
var spfT={geen:["slecht","SPF: ontbreekt","Er staat geen SPF-record. Ontvangers kunnen niet nagaan welke servers voor @"+d+" mogen mailen."],
dubbel:["slecht","SPF: meer dan één record","Er staan meerdere SPF-records. Dan is SPF ongeldig en telt het niet mee. Voeg ze samen tot één record."],
open:["slecht","SPF: staat open (+all)","Je SPF-record laat elke server toe. Dat is hetzelfde als geen SPF."],
zwak:["matig","SPF: zwak","Je SPF-record eindigt niet op ~all of -all. Ontvangers weten dan niet wat ze moeten doen met mail van andere servers."],
zacht:["goed","SPF: in orde (~all)","Je SPF-record zegt welke servers voor @"+d+" mogen mailen."],
streng:["goed","SPF: in orde (-all)","Je SPF-record zegt welke servers voor @"+d+" mogen mailen, en weigert de rest."]}[s.code];
rij(uit,spfT[0],spfT[1],spfT[2],s.record?"Record: "+s.record:"");
if(j.dkim.length){rij(uit,"goed","DKIM: gevonden","Je mails krijgen een digitale handtekening (gevonden onder: "+j.dkim.join(", ")+").");}
else{rij(uit,"matig","DKIM: niet gevonden onder de gangbare namen","We vonden geen DKIM-sleutel onder de namen die Google, Microsoft en de bekende mailprogramma's gebruiken. Mogelijk staat hij onder een andere naam.","Vraag je mailleverancier"+(j.mx.leverancier?" ("+j.mx.leverancier+")":"")+" om DKIM aan te zetten.");}
if(j.mx.hosts.length){rij(uit,"goed","Mailserver: "+(j.mx.leverancier||j.mx.hosts[0]),"Mails naar @"+d+" komen binnen bij "+j.mx.hosts.join(", ")+".");}
else{rij(uit,"matig","Mailserver: geen gevonden","Dit domein ontvangt geen mail. Ook dan kunnen oplichters ermee mailen.","Gebruik je het domein niet voor mail? Zet SPF op 'v=spf1 -all' en DMARC op p=reject.");}
var w=j.web;rij(uit,w.https?(w.hsts?"goed":"matig"):"slecht","Website: "+(w.https?(w.hsts?"HTTPS in orde":"HTTPS, maar niet verplicht"):"niet bereikbaar via HTTPS"),w.https?(w.hsts?"De website gebruikt HTTPS en verplicht dat ook (HSTS).":"De website gebruikt HTTPS, maar verplicht het niet (geen HSTS-header)."):"We konden de website niet veilig (https://) openen.");
var cta=el("div","","kaart ec-cta");cta.appendChild(el("h2",j.vervalsbaar?"Dit los je in één keer op":"Wil je het nog strakker?"));
cta.appendChild(el("p","Zelf doen? Lees het stappenplan voor SPF, DKIM en DMARC. Laten doen? Marketingbaas, ook van Manufakt, zet het voor je in orde voor €149 excl. btw, eenmalig. Eerst meten, dan pas strenger zetten, zodat er geen echte mail verloren gaat."));
var p=el("p","","kies");var a1=el("a","Lees het stappenplan","knop licht");a1.href="/kennisbank/spf-dkim-dmarc/";
var a2=el("a","Laat het in orde zetten","knop");a2.href=MB+"?d="+encodeURIComponent(d)+"&s="+j.score+"&v="+(j.vervalsbaar?1:0)+"&via=cyberdijk";a2.rel="noopener";
p.appendChild(a2);p.appendChild(a1);cta.appendChild(p);uit.appendChild(cta);
uit.appendChild(el("p","Getest op "+new Date(j.getest).toLocaleString("nl-BE")+". De check leest alleen openbare DNS-gegevens en bewaart niets.","klein"));}
window.initEmailcheck=function(){var f=document.getElementById("emailcheck");if(!f||f.getAttribute("data-klaar")){return;}f.setAttribute("data-klaar","1");
var inp=f.querySelector("input"),uit=document.getElementById("ec-uitkomst"),knop=f.querySelector("button");
function start(){var d=schoon(inp.value);uit.hidden=false;uit.textContent="";
if(!d||d.indexOf(".")<0){uit.appendChild(el("p","Geef je domeinnaam of e-mailadres in, bijvoorbeeld jouwbedrijf.be."));uit.focus();return;}
inp.value=d;knop.disabled=true;uit.appendChild(el("p","Bezig met "+d+" te controleren…"));
fetch("/api/emailcheck?d="+encodeURIComponent(d)).then(function(r){return r.json();}).then(function(j){knop.disabled=false;if(j.fout){uit.textContent="";uit.appendChild(el("p",j.fout));}else{toon(uit,j);}uit.focus();
try{history.replaceState(null,"",location.pathname+"?d="+encodeURIComponent(d));}catch(e){}})
.catch(function(){knop.disabled=false;uit.textContent="";uit.appendChild(el("p","De check lukte even niet. Probeer het zo meteen opnieuw."));});}
f.addEventListener("submit",function(ev){ev.preventDefault();start();});
var q=new URLSearchParams(location.search).get("d");if(q){inp.value=schoon(q);start();}};
if(document.readyState!=="loading"){window.initEmailcheck();}else{document.addEventListener("DOMContentLoaded",window.initEmailcheck);}
})();