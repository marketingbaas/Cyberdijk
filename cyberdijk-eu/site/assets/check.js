(function(){
var T={be:{o3:"Je sector staat bij de meest kritieke sectoren en je onderneming is groot. Je valt dan onder het strengste toezicht: registratie bij het CCB, maatregelen op het niveau CyFun Essential of ISO 27001, en een beoordeling tegen 18 april 2027.",o2:"Je sector staat in de wet en je onderneming is minstens middelgroot. Je moet je registreren bij het CCB, passende maatregelen nemen en incidenten melden. Het toezicht gebeurt achteraf. CyFun Important is het gangbare niveau.",ja:"Je levert wel aan bedrijven die eronder vallen. Reken op vragenlijsten of een gevraagd CyFun-niveau, meestal Basic.",link:"/be/nis2-cyfun/"},
nl:{o3:"Je sector staat bij de meest kritieke sectoren en je organisatie is groot. Je valt dan onder het strengste toezicht: registratie bij het NCSC, de zorgplicht en de meldplicht.",o2:"Je sector staat in de wet en je organisatie is minstens middelgroot. Je moet je registreren bij het NCSC, de zorgplicht invullen en incidenten melden. Het toezicht gebeurt achteraf.",ja:"Je levert wel aan organisaties die eronder vallen. Reken op vragenlijsten, eisen in het contract of de vraag naar ISO 27001.",link:"/nl/cyberbeveiligingswet-nis2/"}};
function el(t,txt,c){var n=document.createElement(t);if(txt){n.textContent=txt;}if(c){n.className=c;}return n;}
function keuze(f,naam){var r=f.querySelector('input[name="'+naam+'"]:checked');return r?r.value:"";}
window.initCheck=function(){
var f=document.getElementById("check");if(!f||f.getAttribute("data-klaar")){return;}
f.setAttribute("data-klaar","1");
var uit=document.getElementById("uitkomst"),t=T[f.getAttribute("data-land")]||T.be;
f.addEventListener("submit",function(ev){ev.preventDefault();
var s=f.querySelector("select").value,g=keuze(f,"grootte"),k=keuze(f,"keten");
uit.textContent="";uit.hidden=false;
if(!s||!g||!k){uit.appendChild(el("p","Beantwoord eerst de drie vragen."));uit.focus();return;}
var lijst=s.charAt(0),niveau=1,titel="Waarschijnlijk niet rechtstreeks",tekst;
if(lijst==="0"){tekst="Je sector staat niet in de wet.";}
else if(g==="klein"){tekst="Je sector staat in de wet, maar je onderneming is te klein om er in de regel onder te vallen. Let op de uitzonderingen voor bepaalde digitale diensten.";}
else if(lijst==="1"&&g==="groot"){niveau=3;titel="Waarschijnlijk een essentiële entiteit";tekst=t.o3;}
else{niveau=2;titel="Waarschijnlijk een belangrijke entiteit";tekst=t.o2;}
uit.appendChild(el("h2",titel));
var sch=el("div","","schaal");for(var i=1;i<=3;i++){sch.appendChild(el("span","",i<=niveau?"aan":""));}
sch.setAttribute("role","img");sch.setAttribute("aria-label","Niveau "+niveau+" van 3");
uit.appendChild(sch);uit.appendChild(el("p",tekst));
if(k==="ja"&&niveau===1){uit.appendChild(el("p",t.ja));}
if(k==="nee"&&niveau===1){uit.appendChild(el("p","Zorg toch dat de basis op orde is: updates, back-ups en tweestapsverificatie."));}
var p=el("p"),a=el("a","Lees wat je moet regelen");a.href=t.link;p.appendChild(a);uit.appendChild(p);
uit.appendChild(el("p","Dit is een indicatie op basis van de hoofdregels, geen juridisch advies.","klein"));
uit.focus();});};
if(document.readyState!=="loading"){window.initCheck();}else{document.addEventListener("DOMContentLoaded",window.initCheck);}
})();