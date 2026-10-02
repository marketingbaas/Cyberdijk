# -*- coding: utf-8 -*-
"""Bouwt de site van cyberdijk.eu in de map ../site. Gebruik: python3 build.py

Uitgangspunten: statische HTML, geen cookies, geen externe scripts, één lettertype (eigen bestand), CSS in de pagina
(geen extra verzoek, met een CSP-hash in _headers), JavaScript alleen op de checkpagina's. Elke pagina krijgt
titel, meta-omschrijving, canonical, hreflang (be/nl), Open Graph, JSON-LD en een kruimelpad.
De build controleert titels (max. 60), meta's (max. 155), dode links, ankers, hreflang en het aantal h1's.
"""
import os, json, html, shutil, base64, re, hashlib, datetime
from pages_be import PAGES as P_BE
from pages_nl import PAGES as P_NL
from pages_misc import PAGES as P_MISC, ARTIKELS
from pages_kennis import BEGRIPPEN

BRAND = "Cyberdijk"
DOMAIN = "cyberdijk.eu"
BASE = "https://" + DOMAIN
EMAIL = "info@" + DOMAIN
LEGAL = "Manufakt"
KBO = "BE 0772.333.596"
ADRES = ""            # vestigingsadres: invullen voor de lancering
DATUM = "2026-10-01"
DATUM_TEKST = "1 oktober 2026"
JAAR = DATUM[:4]
MB_URL = "https://www.marketingbaas.com/"
SAMEAS = []           # later: LinkedIn-bedrijfspagina, Google Bedrijfsprofiel, enz.
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(SRC), "site")
PAGES = P_MISC[:1] + P_BE + P_NL + P_MISC[1:]
BY_PATH = {p["path"]: p for p in PAGES}
e = html.escape

# ---------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:"Archivo Head";src:url("__FONT__") format("woff2");font-weight:600 700;font-style:normal;font-display:swap}
@font-face{font-family:"Archivo Head Fallback";src:local("Arial Bold"),local("Arial-BoldMT"),local("Helvetica Neue Bold"),local("Liberation Sans Bold");size-adjust:111.4%;ascent-override:78.8%;descent-override:18.8%;line-gap-override:0%}
:root{--ink:#12343B;--muted:#4A6066;--paper:#FFFFFF;--mist:#EEF3F4;--mist-2:#E2EBEE;--line:#C9D6D9;--water:#1B6A85;--water-soft:#D6E9EF;--gras:#4E7F35;--peil:#F2B705;--on-peil:#12343B;--dijk:#12343B;--kaart:#FFFFFF;--schaduw:0 12px 32px rgba(18,52,59,.10);--voet:#101A22;--voet-tekst:#B9C6CF;--kop:"Archivo Head","Archivo Head Fallback",Arial,sans-serif;--tekst:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#E7F1F2;--muted:#A9BEC2;--paper:#0D2327;--mist:#143138;--mist-2:#183A42;--line:#2C4C53;--water:#7FC6DD;--water-soft:#173F4B;--gras:#8FC06F;--dijk:#C9D6D9;--kaart:#11303A;--schaduw:0 12px 32px rgba(0,0,0,.35)}}
:root[data-theme="dark"]{--ink:#E7F1F2;--muted:#A9BEC2;--paper:#0D2327;--mist:#143138;--mist-2:#183A42;--line:#2C4C53;--water:#7FC6DD;--water-soft:#173F4B;--gras:#8FC06F;--dijk:#C9D6D9;--kaart:#11303A;--schaduw:0 12px 32px rgba(0,0,0,.35)}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:5rem}
body{margin:0;font:1.0625rem/1.65 var(--tekst);color:var(--ink);background:var(--paper)}
a{color:var(--water);text-underline-offset:.18em}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--peil);outline-offset:2px}
img,svg{max-width:100%;height:auto}
.wrap{max-width:72rem;margin-inline:auto;padding-inline:clamp(1rem,4vw,2.5rem)}
.skip{position:absolute;left:-999rem}
.skip:focus{left:1rem;top:1rem;background:var(--paper);padding:.5rem .75rem;z-index:50}
h1,h2,h3{font-family:var(--kop);font-weight:700;line-height:1.12;text-wrap:balance;letter-spacing:-.01em;overflow-wrap:anywhere;hyphens:auto}
h1{font-size:clamp(2rem,1.2rem + 3.4vw,3.3rem);margin:0 0 1rem}
h2{font-size:clamp(1.45rem,1.2rem + .9vw,1.9rem);margin:2.4rem 0 .7rem}
h3{font-size:1.15rem;margin:1.5rem 0 .4rem}
p{margin:0 0 1rem}
ul,ol{margin:0 0 1rem;padding-left:1.3rem}
li{margin-bottom:.45rem}
.lede{font-size:clamp(1.1rem,1rem + .4vw,1.3rem);line-height:1.55;color:var(--muted);max-width:40rem}
.kolom{max-width:44rem}
.kolom p,.kolom li{max-width:70ch}
.klein{font-size:.92rem;color:var(--muted)}
.label{color:var(--muted);font-size:.92rem}
/* header */
.top{position:sticky;top:0;z-index:30;background:var(--paper);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:.75rem 1.25rem;padding-block:.7rem;flex-wrap:wrap}
.merk{display:flex;align-items:center;gap:.6rem;font:700 1.4rem/1 var(--kop);color:var(--ink);text-decoration:none;margin-right:auto;letter-spacing:-.01em}
.merk b{font-weight:inherit}.merk b span{color:var(--water)}
.merk svg{width:2.3rem;height:2.3rem;flex:none}
.m-t{fill:var(--ink)}.m-d{fill:var(--peil)}.m-w{fill:none;stroke:#7FC6DD;stroke-width:3.5;stroke-linecap:round}.m-g{stroke:var(--gras);stroke-width:3.5;stroke-linecap:round}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .m-t{fill:#1B6A85}}
:root[data-theme="dark"] .m-t{fill:#1B6A85}
.menu-schakel{position:absolute;opacity:0;width:1px;height:1px;pointer-events:none}
.menu-knop{display:inline-flex;align-items:center;gap:.45rem;font-weight:700;padding:.55rem .8rem;border:2px solid var(--line);border-radius:.5rem;cursor:pointer;background:var(--paper);color:var(--ink);order:3}
.menu-knop span{display:block;width:1.1rem;height:2px;background:currentColor;box-shadow:0 -5px 0 currentColor,0 5px 0 currentColor}
.menu-schakel:focus-visible+.menu-knop{outline:3px solid var(--peil);outline-offset:2px}
.top nav{display:none;order:4;flex-basis:100%;padding-top:.5rem;border-top:1px solid var(--line);margin-top:.4rem}
.menu-schakel:checked~nav{display:block}
.top nav ul{display:flex;flex-direction:column;gap:.1rem;list-style:none;margin:0;padding:0}
.top nav li{margin:0}
.top nav a{display:block;color:var(--ink);text-decoration:none;font-weight:600;padding:.6rem .25rem;border-bottom:1px solid var(--line)}
.top nav li:last-child a{border-bottom:0}
.top nav a:hover,.top nav a[aria-current]{text-decoration:underline;text-decoration-thickness:3px;text-decoration-color:var(--peil);text-underline-offset:.25em}
.top .knop{order:2;padding:.6rem .9rem;font-size:.95rem;white-space:nowrap}
@media (min-width:56rem){.menu-knop{display:none}.top nav{display:block;order:1;flex-basis:auto;padding:0;border:0;margin:0 .5rem 0 auto}.top nav ul{flex-direction:row;gap:.2rem 1.2rem}.top nav a{padding:.3rem 0;border:0}.merk{margin-right:0}.top .knop{padding:.7rem 1.1rem;font-size:1rem}}
/* knoppen */
.knop{display:inline-flex;align-items:center;gap:.5rem;background:var(--peil);color:var(--on-peil);font:700 1rem/1.2 var(--tekst);padding:.85rem 1.3rem;border-radius:.5rem;text-decoration:none;border:2px solid var(--peil);cursor:pointer;transition:transform .15s,box-shadow .15s}
.knop:hover{transform:translateY(-1px);box-shadow:0 6px 18px rgba(242,183,5,.35)}
.knop:focus-visible{outline-color:var(--ink)}
.knop.licht{background:transparent;color:var(--ink);border-color:var(--ink)}
.knop.licht:hover{box-shadow:0 6px 18px rgba(18,52,59,.15)}
.band-knop .knop.licht{color:#fff;border-color:#fff}
main{padding-block:0 4rem}
/* hero */
.hero{background:linear-gradient(180deg,var(--mist) 0,var(--paper) 100%);border-bottom:1px solid var(--line)}
.hero .wrap{display:grid;gap:2rem;padding-block:2.5rem 2rem;align-items:center}
.hero h1{margin-bottom:.9rem}
.hero .acties{display:flex;flex-wrap:wrap;gap:.75rem 1rem;margin:1.4rem 0 1rem}
.kicker{display:inline-flex;align-items:center;gap:.5rem;font-weight:700;font-size:.85rem;letter-spacing:.06em;text-transform:uppercase;color:var(--water);margin-bottom:1rem}
.kicker::before{content:"";width:1.6rem;height:4px;border-radius:2px;background:var(--peil)}
.vinkjes{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;list-style:none;padding:0;margin:0;font-size:.95rem;color:var(--muted)}
.vinkjes li{display:flex;align-items:center;gap:.45rem;margin:0}
.vinkjes svg{width:1.1rem;height:1.1rem;color:var(--gras);flex:none}
.teller{display:inline-flex;align-items:center;gap:.6rem;background:var(--kaart);border:1px solid var(--line);border-radius:2rem;padding:.45rem 1rem .45rem .7rem;font-size:.92rem;color:var(--muted);margin:0 0 1.1rem}
.teller span[data-dag]{color:var(--ink);font-weight:700}
.stip{width:.6rem;height:.6rem;border-radius:50%;background:#B23A3A;flex:none;box-shadow:0 0 0 0 rgba(178,58,58,.5);animation:stip 2s ease-out infinite}
@keyframes stip{to{box-shadow:0 0 0 .6rem rgba(178,58,58,0)}}
.bronnenstrip{border-bottom:1px solid var(--line);background:var(--paper)}
.bronnenstrip .wrap{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;align-items:center;padding-block:.8rem;font-size:.88rem;color:var(--muted)}
.bronnenstrip strong{color:var(--ink);font-weight:700}
.plak{display:none}
@media (max-width:56rem){.plak{display:block;position:fixed;left:0;right:0;bottom:0;z-index:40;padding:.6rem 1rem calc(.6rem + env(safe-area-inset-bottom,0px));background:var(--paper);border-top:1px solid var(--line);box-shadow:0 -8px 24px rgba(0,0,0,.08)}.plak .knop{width:100%;justify-content:center}body{padding-bottom:4.6rem}}
@media (min-width:52rem){.hero .wrap{grid-template-columns:1.1fr .9fr;padding-block:3.5rem 3rem}.hero h1{font-size:clamp(2rem,1rem + 2.6vw,2.9rem)}.hero .beeld{order:2}}
.hero-land .wrap{display:block;padding-block:1rem 2.5rem}
/* dijk-illustratie */
.beeld{position:relative}
.dijk{display:block;width:100%;height:auto;max-height:28rem}
.d-w{fill:var(--water-soft)}.d-wl{fill:none;stroke:var(--water);stroke-width:4;stroke-linecap:round}.d-l{fill:var(--mist-2)}.d-d{fill:var(--dijk)}.d-g{stroke:var(--gras);stroke-width:10;stroke-linecap:round}.d-p{fill:var(--peil)}.d-b{fill:var(--paper);stroke:var(--ink);stroke-width:4}.d-r{fill:var(--peil)}
.golf{animation:golf 9s linear infinite}
.golf-2{animation:golf 14s linear infinite reverse;opacity:.55}
@keyframes golf{to{transform:translateX(-600px)}}
.peil-lamp{animation:peil 2.6s ease-in-out infinite}
@keyframes peil{0%,100%{opacity:.35}50%{opacity:1}}
.schild{animation:schild 6s ease-in-out infinite}
@keyframes schild{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.t-v{fill:#fff;stroke:#B23A3A;stroke-width:2.5;stroke-linejoin:round}.t-l{fill:none;stroke:#B23A3A;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}
.t-dreiging{opacity:0;transform-box:fill-box;transform-origin:center;animation:dreiging linear infinite}
@keyframes dreiging{0%{transform:translate(0,0) rotate(-8deg);opacity:0}8%{opacity:1}82%{transform:translate(calc(var(--dx)*.92),calc(var(--dy)*.92)) rotate(10deg);opacity:1}100%{transform:translate(var(--dx),var(--dy)) rotate(14deg) scale(.1);opacity:0}}
.v-r{fill:var(--gras)}.v-l{fill:none;stroke:#fff;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.veilig{transform-box:fill-box;transform-origin:center;animation:veilig 4s ease-in-out infinite}
@keyframes veilig{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
/* secties */
.sectie{padding-block:3rem}
.sectie-mist{background:var(--mist)}
.sectie h2:first-child{margin-top:0}
.sectie-kop{max-width:44rem;margin-bottom:1.6rem}
.sectie-kop h2{margin:0 0 .5rem}
.sectie-kop p{color:var(--muted);margin:0}
.kaarten{display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr))}
.kaart{position:relative;background:var(--kaart);border:1px solid var(--line);border-radius:1rem;padding:1.4rem 1.5rem;box-shadow:var(--schaduw);display:flex;flex-direction:column;transition:transform .2s,border-color .2s}
.kaart:hover{transform:translateY(-3px);border-color:var(--water)}
.kaart h2,.kaart h3{margin:0 0 .5rem;font-size:1.2rem}
.kaart p{margin:0 0 .75rem;color:var(--muted)}
.kaart p:last-child{margin:0}
.kaart .pijl{margin-top:auto;font-weight:700;text-decoration:none;color:var(--water)}
.kaart .pijl::after{content:" →"}
.kaart .pijl:hover{text-decoration:underline}
.kaart-link{text-decoration:none;color:inherit}
.kaart-link h3{color:var(--ink)}
.kaart-link:hover h3{color:var(--water)}
.kaart .vlag{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--water);margin-bottom:.5rem}
.kaart-land{border-width:2px;border-color:var(--ink)}
.kaart-land ul{margin:.25rem 0 1.25rem;padding-left:1.1rem;color:var(--muted)}
.kaart-land .knop{align-self:flex-start;margin-top:auto}
.landen{display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr))}
.kies{display:flex;flex-wrap:wrap;gap:.75rem 1rem;align-items:center}
/* cijfers */
.cijfers{background:var(--ink);color:#fff;padding-block:2.5rem}
.cijfers .wrap{display:grid;gap:1.5rem 2rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,12rem),1fr))}
.cijfer b{display:block;font:700 clamp(1.7rem,1.3rem + 1.4vw,2.4rem)/1.1 var(--kop);color:var(--peil);margin-bottom:.3rem;letter-spacing:-.01em}
.cijfer span{display:block;color:#C9D6D9;font-size:.95rem;max-width:18rem}
/* stappen */
.stappen{list-style:none;padding:0;margin:0;display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr));counter-reset:stap}
.stappen li{counter-increment:stap;margin:0;padding:1.3rem 1.4rem 1.3rem 4.2rem;position:relative;background:var(--kaart);border:1px solid var(--line);border-radius:1rem}
.stappen li::before{content:counter(stap);position:absolute;left:1.2rem;top:1.15rem;width:2.1rem;height:2.1rem;border-radius:50%;background:var(--peil);color:var(--on-peil);font:700 1.1rem/2.1rem var(--kop);text-align:center}
.stappen h3{margin:0 0 .35rem;font-size:1.1rem}
.stappen p{margin:0;color:var(--muted)}
/* kruimels, lijsten, blokken */
.kruimel{font-size:.92rem;color:var(--muted);margin:1.5rem 0 1.1rem}
.kruimel ol{list-style:none;display:flex;flex-wrap:wrap;gap:.3rem .5rem;padding:0;margin:0}
.kruimel li{margin:0}
.kruimel li+li::before{content:"/";margin-right:.5rem;color:var(--line)}
.kruimel a{color:var(--muted)}
.kort{background:var(--mist);border-left:6px solid var(--peil);border-radius:0 .75rem .75rem 0;padding:1.1rem 1.35rem;margin:1.5rem 0}
.kort h2{font-size:1.05rem;margin:0 0 .5rem}
.kort ul{margin:0}
.inhoud{margin:1.5rem 0 .5rem;font-size:.95rem}
.inhoud strong{display:block;margin-bottom:.35rem}
.inhoud ol{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.4rem}
.inhoud li{margin:0}
.inhoud a{display:inline-block;background:var(--mist);border:1px solid var(--line);border-radius:2rem;padding:.25rem .8rem;text-decoration:none;color:var(--ink)}
.inhoud a:hover{border-color:var(--water);color:var(--water)}
.vragen{list-style:none;padding:0;margin:1.5rem 0 0}
.vragen li{border-top:1px solid var(--line);padding:.95rem 0;margin:0}
.vragen li:last-child{border-bottom:1px solid var(--line)}
.vragen a{font-weight:700;font-size:1.1rem}
.vragen span{display:block;color:var(--muted)}
details{border-top:1px solid var(--line);padding:.85rem 0}
details:last-of-type{border-bottom:1px solid var(--line)}
summary{font-weight:700;cursor:pointer;list-style:none;position:relative;padding-right:2rem}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";position:absolute;right:.25rem;top:0;font:700 1.3rem/1.3 var(--kop);color:var(--water)}
details[open] summary::after{content:"–"}
details p{margin:.6rem 0 0;max-width:70ch}
.cta{background:var(--mist);border:2px solid var(--ink);border-radius:1rem;padding:1.5rem 1.6rem;margin-top:2.5rem}
.cta h2{margin:0 0 .5rem;font-size:1.35rem}
.cta p:last-child{margin:0;display:flex;flex-wrap:wrap;gap:.75rem 1.25rem;align-items:center}
.band-knop{background:var(--ink);color:#fff;padding-block:3rem;text-align:center}
.band-knop h2{margin:0 0 .6rem;color:#fff}
.band-knop p{color:#C9D6D9;max-width:40rem;margin-inline:auto}
.band-knop .kies{justify-content:center;margin-top:1.4rem}
.bronnen{font-size:.95rem}
.nota{font-size:.92rem;color:var(--muted);border-top:1px solid var(--line);margin-top:2.5rem;padding-top:1rem}
.lees-ook{margin-top:2.5rem}
.lees-ook ul{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
.lees-ook li{margin:0}
.lees-ook a{font-weight:600}
.lees-ook span{display:block;color:var(--muted);font-size:.9rem}
/* artikel met zijkolom */
.lees{display:grid;gap:2.5rem;align-items:start}
@media (min-width:62rem){.lees{grid-template-columns:minmax(0,44rem) 17rem;gap:4rem}.zij{position:sticky;top:5rem}}
.zij .kaart{margin-bottom:1.25rem}
.zij .kaart h2{font-size:1.05rem}
.zij .kaart .knop{width:100%;justify-content:center;margin-top:.4rem}
.zij ul{list-style:none;padding:0;margin:0}
.zij li{margin:0 0 .6rem;padding-left:1rem;position:relative}
.zij li::before{content:"→";position:absolute;left:0;color:var(--peil);font-weight:700}
.zij li a{text-decoration:none;color:var(--ink);font-weight:600;overflow-wrap:anywhere;hyphens:auto}
.zij li a:hover{color:var(--water);text-decoration:underline}
/* begrippen */
.begrippen{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,19rem),1fr));margin:1.5rem 0}
.begrippen div{background:var(--kaart);border:1px solid var(--line);border-radius:.9rem;padding:1.1rem 1.25rem}
.begrippen dt{font:700 1.05rem var(--kop);margin:0 0 .35rem}
.begrippen dd{margin:0;color:var(--muted);font-size:.97rem}
/* formulieren */
form label,legend{display:block;font-weight:700;margin:1.1rem 0 .3rem;padding:0}
fieldset{border:0;padding:0;margin:0}
fieldset label{font-weight:400;margin:.4rem 0;display:flex;gap:.7rem;align-items:flex-start;padding:.7rem .9rem;border:1.5px solid var(--line);border-radius:.6rem;background:var(--kaart);cursor:pointer}
fieldset label:hover{border-color:var(--water)}
fieldset label:has(input:checked){border-color:var(--water);background:var(--mist)}
fieldset input{margin-top:.35rem;accent-color:var(--water)}
input:not([type=radio]),select,textarea{width:100%;padding:.7rem .75rem;border:2px solid var(--line);border-radius:.5rem;font:inherit;background:var(--kaart);color:var(--ink)}
input:not([type=radio]):focus,select:focus,textarea:focus{border-color:var(--water);outline:none;box-shadow:0 0 0 3px var(--water-soft)}
.verborgen{position:absolute;left:-999rem}
form .knop{margin-top:1.2rem}
.uitkomst{margin-top:1.75rem;border:2px solid var(--ink);border-radius:1rem;padding:1.25rem 1.4rem;background:var(--kaart)}
.uitkomst h2{margin:0 0 .25rem;font-size:1.35rem}
.schaal{display:grid;grid-template-columns:repeat(3,1fr);gap:.35rem;margin:.6rem 0 1rem}
.schaal span{height:.6rem;background:var(--line);border-radius:.2rem}
.schaal span.aan{background:var(--peil)}
.contact-blok{display:grid;gap:2.5rem;align-items:start}
@media (min-width:62rem){.contact-blok{grid-template-columns:minmax(0,40rem) 18rem}}
/* footer in de stijl van marketingbaas.com */
.voet{background:var(--voet);color:var(--voet-tekst);padding:3rem 0 2rem;font-size:.92rem}
.voet .wrap{display:grid;gap:2rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,13rem),1fr))}
.voet .merkblok{grid-column:1/-1}
@media (min-width:62rem){.voet .wrap{grid-template-columns:1.3fr 1fr 1fr 1fr}.voet .merkblok{grid-column:auto}}
.voet h2{color:#fff;font:700 .95rem/1.3 var(--tekst);margin:0 0 .6rem}
.voet ul{list-style:none;padding:0;margin:0}
.voet li{margin-bottom:.3rem}
.voet a{color:#fff;text-decoration:none}
.voet a:hover{text-decoration:underline}
.voet p{margin:0 0 .75rem}
.voet .merk{color:#fff;margin:0 0 .7rem}
.voet .merk b span{color:var(--peil)}
.voet .m-t{fill:#1B6A85}
.voet .onder{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.14);margin-top:.5rem;padding-top:1.1rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem 1.5rem}
.voet .onder p{margin:0}
.band{background:var(--peil);color:var(--on-peil);font-size:.92rem;padding:.4rem 1rem;text-align:center}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
"""

# ---------------------------------------------------------------- JS (alleen op de checkpagina's)
CONTACT_FUNCTIE = r"""// Cloudflare Pages Function: ontvangt het contactformulier en de wachtlijst, mailt ze via Resend naar MELD_EMAIL
// en stuurt de bezoeker door naar /contact/bedankt/. Vereist in Cloudflare Pages > Settings > Variables and Secrets:
//   RESEND_API_KEY (geheim)   MELD_EMAIL (standaard info@cyberdijk.eu)   MAIL_FROM (bv. "Cyberdijk <formulier@cyberdijk.eu>", domein geverifieerd bij Resend)
const MAX = { naam: 80, email: 120, bedrijf: 80, land: 20, dienst: 40, vraag: 3000 };
const schoon = (v, m) => String(v == null ? "" : v).replace(/[\u0000-\u0008\u000B-\u001F]+/g, " ").trim().slice(0, m);

export async function onRequestPost({ request, env }) {
  const naar = env.MELD_EMAIL || "info@cyberdijk.eu";
  let d;
  try { d = await request.formData(); } catch { return Response.redirect(new URL("/contact/", request.url), 303); }
  if (d.get("website")) return Response.redirect(new URL("/contact/bedankt/", request.url), 303);   // honeypot: bot, stil doorsturen
  const v = {};
  for (const k of Object.keys(MAX)) v[k] = schoon(d.get(k), MAX[k]);
  const soort = d.get("form-name") === "wachtlijst" ? "wachtlijst" : "contact";
  if (v.naam.length < 2 || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.email)) return Response.redirect(new URL("/contact/", request.url), 303);
  const regels = [`Naam: ${v.naam}`, `E-mail: ${v.email}`, v.bedrijf && `Bedrijf: ${v.bedrijf}`, v.land && `Land: ${v.land}`, v.dienst && `Dienst: ${v.dienst}`, v.vraag && `\nVraag:\n${v.vraag}`].filter(Boolean);
  const onderwerp = soort === "wachtlijst" ? `Wachtlijst Cyberdijk: ${v.naam}${v.bedrijf ? " (" + v.bedrijf + ")" : ""}` : `Vraag via cyberdijk.eu: ${v.naam}${v.bedrijf ? " (" + v.bedrijf + ")" : ""}`;
  if (env.RESEND_API_KEY) {
    try {
      const r = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: { authorization: "Bearer " + env.RESEND_API_KEY, "content-type": "application/json" },
        body: JSON.stringify({ from: env.MAIL_FROM || "Cyberdijk <onboarding@resend.dev>", to: [naar], reply_to: v.email, subject: onderwerp, text: regels.join("\n") }),
      });
      console.log("resend", r.status);
    } catch (e) { console.log("resend fout", e.message); }
  } else {
    console.log("RESEND_API_KEY ontbreekt; bericht niet verstuurd:", onderwerp);
  }
  return Response.redirect(new URL("/contact/bedankt/", request.url), 303);
}

export function onRequestGet({ request }) {
  return Response.redirect(new URL("/contact/", request.url), 302);
}
"""

CHECK_JS = r"""
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
"""
JS_VERSIE = hashlib.sha256(CHECK_JS.strip().encode("utf-8")).hexdigest()[:8]
TELLER_JS = r"""window.initTeller=function(){var n=new Date();n.setHours(0,0,0,0);var l=document.querySelectorAll("[data-dag]");for(var i=0;i<l.length;i++){var el=l[i],d=new Date(el.getAttribute("data-dag")+"T00:00:00"),v=Math.round((d-n)/864e5),t=el.getAttribute(v>0?"data-voor":"data-na");if(t&&v!==0){el.textContent=t.replace("%d",Math.abs(v));}}};window.initTeller();"""
TELLER_VERSIE = hashlib.sha256(TELLER_JS.encode("utf-8")).hexdigest()[:8]
TELLER = {
    "be": '<p class="teller"><span class="stip"></span><span data-dag="2027-04-18" data-voor="Nog %d dagen tot 18 april 2027" data-na="De deadline van 18 april 2027 is %d dagen voorbij">Deadline: 18 april 2027</span> voor de verplichte beoordeling van essentiële entiteiten in België.</p>',
    "nl": '<p class="teller"><span class="stip"></span><span data-dag="2026-08-15" data-voor="Over %d dagen geldt de Cyberbeveiligingswet" data-na="De Cyberbeveiligingswet geldt al %d dagen">De Cyberbeveiligingswet geldt sinds 15 augustus 2026</span>, zonder overgangsperiode.</p>',
}
TELLER["eu"] = TELLER["be"]

# ---------------------------------------------------------------- beeldmerk en illustratie
MARK = ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect class="m-t" width="64" height="64" rx="14"/>'
        '<path class="m-w" d="M7 47q5-5 10 0t10 0"/><path class="m-w" d="M11 38q4-4 8 0t8 0" opacity=".55"/>'
        '<path class="m-d" d="M23 55 36 18h10l13 37z"/><path class="m-g" d="M36.5 19.5h9"/></svg>')
WOORD = '<b>Cyber<span>dijk</span></b>'
VINK = '<svg viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5l4 4 8-9"/></svg>'


def _golf(y, amp=9, stap=75, breedte=1800):
    """Een golvende lijn van x=0 tot x=breedte, in een vaste herhaling zodat ze naadloos kan schuiven."""
    d = "M0 %d" % y
    x = 0
    boven = True
    while x < breedte:
        cx, nx = x + stap / 2, x + stap
        d += " Q%d %d %d %d" % (cx, y - amp if boven else y + amp, nx, y)
        boven = not boven
        x = nx
    return d


# De golven schuiven 600 px naar links en herhalen zich om de 2 x stap px; 600 is een veelvoud van 150 en van 120.
def _dreigingen():
    """Phishingmails, malware en waarschuwingen vallen uit de lucht, botsen op de dijk en spatten uiteen."""
    vormen = {
        "mail": '<rect x="-13" y="-9" width="26" height="18" rx="3" class="t-v"/><path d="M-13 -7l13 10 13-10" class="t-l"/>',
        "bug": '<ellipse rx="9" ry="11" class="t-v"/><path d="M-9 -4h-6M9 -4h6M-10 3h-6M10 3h6M-7 9l-4 5M7 9l4 5M-4 -11l-3-5M4 -11l3-5" class="t-l"/>',
        "waarschuwing": '<path d="M0 -13l14 24h-28z" class="t-v"/><path d="M0 -4v8M0 8v1" class="t-l"/>',
        "slot": '<rect x="-9" y="-3" width="18" height="15" rx="2" class="t-v"/><path d="M-5 -3v-5a5 5 0 0 1 10 0" class="t-l"/>',
    }
    plan = [("mail", 250, 235, 0.0, 4.6), ("bug", 330, 190, 1.1, 5.2), ("waarschuwing", 420, 150, 2.3, 4.2), ("slot", 300, 262, 3.4, 5.0),
            ("mail", 470, 125, 4.4, 4.8), ("bug", 215, 275, 5.6, 4.4), ("waarschuwing", 365, 205, 6.7, 5.4)]
    uit = []
    for naam, x0, y_eind, vertraging, duur in plan:
        x_eind = 460 + (300 - y_eind) * 140 / 210 - 6      # punt op de linkerhelling van de dijk
        uit.append('<g class="t-dreiging" style="--dx:%dpx;--dy:%dpx;animation-delay:%.1fs;animation-duration:%.1fs" transform="translate(%d -30)">%s</g>'
                   % (x_eind - x0, y_eind + 30, vertraging, duur, x0, vormen[naam]))
    return "".join(uit)


DIJK = ('<svg class="dijk" viewBox="0 0 1000 430" role="img" aria-label="Een dijk houdt phishing en malware tegen; de bedrijven erachter blijven droog">'
        '<defs><clipPath id="d-clip"><rect x="0" y="0" width="640" height="300"/></clipPath></defs><g transform="translate(-140 130)">'
        '<rect class="d-l" x="700" y="200" width="500" height="100" rx="4"/>'
        '<rect class="d-b" x="880" y="150" width="70" height="50"/><rect class="d-b" x="968" y="112" width="56" height="88"/><rect class="d-b" x="1040" y="160" width="96" height="40"/>'
        '<path class="d-r" d="M905 165h20v4h-20zM905 177h20v4h-20zM983 128h26v4h-26zM983 140h26v4h-26zM983 152h26v4h-26zM1060 172h56v4h-56z"/>'
        '<g class="schild"><path class="d-p" d="M1010 62l16 6v14c0 10-7 18-16 21-9-3-16-11-16-21V68z"/><path d="M1002 80l6 6 11-12" fill="none" stroke="#12343B" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>'
        '<g clip-path="url(#d-clip)"><rect class="d-w" x="0" y="150" width="640" height="150"/>'
        '<path class="d-w golf-2" d="' + _golf(136, 7, 60) + ' V300 H0 Z"/>'
        '<path class="d-w golf" d="' + _golf(142, 9, 75) + ' V300 H0 Z"/>'
        '<path class="d-wl golf" d="' + _golf(142, 9, 75) + '"/></g>'
        '<path class="d-d" d="M460 300 600 90h130l170 210z"/><path class="d-g" d="M598 92h134"/>'
        '<rect class="d-p" x="472" y="262" width="22" height="7" rx="2"/><rect class="d-p" x="500" y="222" width="22" height="7" rx="2"/><rect class="d-p" x="528" y="182" width="22" height="7" rx="2"/><rect class="d-p peil-lamp" x="556" y="142" width="22" height="7" rx="2"/>'
        + _dreigingen() +
        '<g class="veilig"><circle cx="1060" cy="236" r="13" class="v-r"/><path d="M1053 236l5 5 9-10" class="v-l"/></g>'
        '</g></svg>')

NAV = [("België", "/be/"), ("Nederland", "/nl/"), ("Kennisbank", "/kennisbank/"), ("Diensten", "/diensten/"), ("Over", "/over/"), ("Contact", "/contact/")]
VOET_BE = [("NIS2 en CyFun", "/be/nis2-cyfun/"), ("ISO 27001 voor kmo's", "/be/iso-27001/"), ("GDPR en DPO", "/be/gdpr-dpo/"), ("NIS2-check België", "/be/nis2-check/"), ("NIS2-registratie bij het CCB", "/kennisbank/nis2-registratie-ccb/"), ("CyFun-zelfevaluatie", "/kennisbank/cyfun-zelfevaluatie/"), ("Regio Antwerpen", "/be/regio/antwerpen/"), ("Regio Noorderkempen", "/be/regio/noorderkempen/")]
VOET_NL = [("Cyberbeveiligingswet", "/nl/cyberbeveiligingswet-nis2/"), ("ISO 27001 voor mkb", "/nl/iso-27001/"), ("AVG en FG", "/nl/avg-fg/"), ("Cyberbeveiligingswet-check", "/nl/nis2-check/"), ("Roosendaal", "/nl/regio/roosendaal/"), ("Bergen op Zoom", "/nl/regio/bergen-op-zoom/"), ("Breda", "/nl/regio/breda/"), ("Moerdijk", "/nl/regio/moerdijk/")]
VOET_KB = [("Alle artikels", "/kennisbank/"), ("De tien maatregelen van NIS2", "/kennisbank/nis2-maatregelen/"), ("NIS2-meldplicht", "/kennisbank/nis2-meldplicht-incident/"), ("NIS2-boetes", "/kennisbank/nis2-boetes/"), ("ISO 27001: de 93 maatregelen", "/kennisbank/iso-27001-maatregelen/"), ("Verwerkingsregister", "/kennisbank/verwerkingsregister/"), ("Datalek melden", "/kennisbank/datalek-melden-72-uur/"), ("AI Act voor kmo's en mkb", "/kennisbank/ai-act-kmo-mkb/"), ("Begrippenlijst", "/kennisbank/begrippen/")]
VOET_CD = [("Diensten (in voorbereiding)", "/diensten/"), ("Over Cyberdijk", "/over/"), ("Contact", "/contact/"), ("Privacyverklaring", "/privacy/"), ("Cookies", "/cookies/")]

DOEN = {
 "be": '<h2>Wat je nu kan doen</h2><ul><li><a href="/be/nis2-check/">Doe de NIS2-check</a> en zie of je onderneming onder de wet valt.</li><li>Lees <a href="/be/nis2-cyfun/">wat NIS2 en CyFun vragen</a>, of wanneer <a href="/be/iso-27001/">ISO 27001</a> de betere keuze is.</li><li>Verwerk je klant- of personeelsgegevens? Lees <a href="/be/gdpr-dpo/">wat de GDPR verplicht</a>.</li><li><a href="/contact/">Stel je vraag</a>. Je krijgt binnen twee werkdagen antwoord.</li></ul>',
 "nl": '<h2>Wat je nu kunt doen</h2><ul><li><a href="/nl/nis2-check/">Doe de check</a> en zie of je bedrijf onder de wet valt.</li><li>Lees <a href="/nl/cyberbeveiligingswet-nis2/">wat de Cyberbeveiligingswet vraagt</a>, en wanneer <a href="/nl/iso-27001/">ISO 27001</a> zinvol is.</li><li>Verwerk je klant- of personeelsgegevens? Lees <a href="/nl/avg-fg/">wat de AVG verplicht</a>.</li><li><a href="/contact/">Stel je vraag</a>. Je krijgt binnen twee werkdagen antwoord.</li></ul>',
}
CTA = {
 "be": '<div class="cta"><h2>Weet je niet of je bedrijf onder NIS2 valt?</h2><p>Drie vragen, meteen een antwoord, zonder e-mailadres.</p><p><a class="knop" href="/be/nis2-check/">Doe de NIS2-check</a> <a href="/contact/">Of stel je vraag</a></p></div>',
 "nl": '<div class="cta"><h2>Weet je niet of je onder de Cyberbeveiligingswet valt?</h2><p>Drie vragen, meteen een antwoord, zonder e-mailadres.</p><p><a class="knop" href="/nl/nis2-check/">Doe de check</a> <a href="/contact/">Of stel je vraag</a></p></div>',
 "eu": '<div class="cta"><h2>Weet je niet of je bedrijf onder NIS2 valt?</h2><p>Drie vragen, meteen een antwoord, zonder e-mailadres.</p><p><a class="knop" href="/be/nis2-check/">Check voor België</a> <a class="knop licht" href="/nl/nis2-check/">Check voor Nederland</a> <a href="/contact/">Of stel je vraag</a></p></div>',
}
NOTA = '<p class="nota">Laatst gecontroleerd op ' + DATUM_TEKST + '. Deze pagina geeft uitleg, geen juridisch advies. Cyberdijk beantwoordt vragen; begeleiding start na afronding van de certificering.</p>'
LAND_NAAM = {"be": "België", "nl": "Nederland", "eu": "België en Nederland"}

SECTOREN = [("Meest kritieke sectoren", [("1-energie", "Energie"), ("1-transport", "Transport: luchtvaart, spoor, scheepvaart, havens, wegbeheer"), ("1-bank", "Bankwezen en financiële markten"), ("1-zorg", "Gezondheidszorg"), ("1-water", "Drinkwater en afvalwater"), ("1-digi", "Digitale infrastructuur: datacenters, cloud, telecom"), ("1-ict", "Beheer van ICT-diensten voor bedrijven"), ("1-overheid", "Overheid"), ("1-ruimte", "Ruimtevaart")]),
            ("Andere kritieke sectoren", [("2-post", "Post- en koeriersdiensten"), ("2-afval", "Afvalbeheer"), ("2-chemie", "Chemie: productie en distributie"), ("2-voeding", "Levensmiddelen: productie, verwerking, groothandel"), ("2-maak", "Maakindustrie: machines, voertuigen, elektronica, medische hulpmiddelen"), ("2-digitaal", "Digitale aanbieders: marktplaatsen, zoekmachines, sociale netwerken"), ("2-onderzoek", "Onderzoek")])]

HOME_VRAGEN = [
    ("Val ik onder NIS2?", "Je sector en je grootte bepalen het. Grote klanten geven de eisen door aan hun leveranciers, ook aan kleine.", [("Check België", "/be/nis2-check/"), ("Check Nederland", "/nl/nis2-check/")]),
    ("Welk CyFun-niveau heb ik nodig?", "Small, Basic, Important of Essential. Val je onder NIS2, dan volgt het niveau uit je statuut; anders bepaalt je klant het.", [("CyFun-niveaus", "/kennisbank/cyfun-niveaus/"), ("NIS2 en CyFun", "/be/nis2-cyfun/")]),
    ("Heb ik ISO 27001 nodig?", "Niet verplicht, wel steeds vaker gevraagd in aanbestedingen en inkoopvoorwaarden. Stappen, kosten en doorlooptijd.", [("Voor kmo's", "/be/iso-27001/"), ("Voor mkb", "/nl/iso-27001/")]),
    ("Heb ik een DPO of FG nodig?", "Alleen in drie situaties. Een verwerkingsregister en een procedure voor datalekken heeft bijna elk bedrijf nodig.", [("GDPR en DPO", "/be/gdpr-dpo/"), ("AVG en FG", "/nl/avg-fg/")]),
    ("Geldt de AI Act voor mijn bedrijf?", "Ja, zodra je AI gebruikt: AI-geletterdheid en transparantie gelden al. De strenge hoogrisico-regels komen later.", [("AI Act voor kmo's en mkb", "/kennisbank/ai-act-kmo-mkb/")]),
    ("Wat kost het als ik niets doe?", "NIS2: tot 10 miljoen euro of 2% van de omzet. AVG: tot 20 miljoen of 4%. En een klant die afhaakt, kost vaak meer.", [("NIS2-boetes", "/kennisbank/nis2-boetes/")]),
]
HOME_FAQ = [
    ("Wat is NIS2 in het kort?", "NIS2 is de Europese richtlijn die bedrijven in kritieke sectoren verplicht om hun digitale beveiliging aantoonbaar op orde te hebben: registratie, maatregelen, meldplicht en betrokkenheid van het bestuur. België zette ze om in de NIS2-wet van 2024, Nederland in de Cyberbeveiligingswet die geldt sinds 15 augustus 2026."),
    ("Geldt NIS2 ook voor een klein bedrijf?", "Rechtstreeks meestal niet: de wet geldt in de regel vanaf 50 werknemers of meer dan 10 miljoen euro omzet en balanstotaal. Kleine bedrijven merken de wet via klanten die wel onder de wet vallen en hun leveranciers moeten beoordelen."),
    ("Wat is het verschil tussen CyFun en ISO 27001?", "CyFun is het Belgische kader van het CCB, gratis en afgestemd op NIS2. ISO 27001 is de internationale norm, met een certificaat van een geaccrediteerde instelling. Voor Belgische klanten volstaat CyFun meestal; voor Nederlandse en internationale klanten weegt ISO 27001 zwaarder."),
    ("Wat kost Cyberdijk?", "Niets. De uitleg, de check en het antwoord op je vraag zijn gratis. Begeleiding start na afronding van de certificering; tot dan verwijzen we voor formeel advies naar de officiële bronnen en erkende dienstverleners."),
]
LAND_PUNTEN = {
    "be": ["NIS2-wet sinds 18 oktober 2024", "CyFun of ISO 27001 als bewijs", "Essentiële entiteiten: beoordeling tegen 18 april 2027", "45% steun via de kmo-portefeuille"],
    "nl": ["Cyberbeveiligingswet sinds 15 augustus 2026", "Zorgplicht, meldplicht en registratie bij het NCSC", "Geen overgangsperiode", "ISO 27001 als gangbare route"],
}


# ---------------------------------------------------------------- bouwstenen
def check_form(land):
    wn = "werknemers" if land == "be" else "medewerkers"
    opts = '<option value="">Kies je sector</option>'
    for groep, items in SECTOREN:
        opts += '<optgroup label="%s">%s</optgroup>' % (e(groep), "".join('<option value="%s">%s</option>' % (v, e(l)) for v, l in items))
    opts += '<option value="0-ander">Een andere sector</option>'
    return ('<form id="check" data-land="%s" novalidate>'
            '<label for="sector">1. In welke sector is je bedrijf actief?</label><select id="sector" name="sector">%s</select>'
            '<p class="klein">Wegvervoer, opslag, bouw en handel staan niet in de wet. Kies dan een andere sector.</p>'
            '<fieldset><legend>2. Hoe groot is je bedrijf?</legend>'
            '<label><input type="radio" name="grootte" value="klein"> Minder dan 50 %s, en omzet en balanstotaal tot 10 miljoen euro</label>'
            '<label><input type="radio" name="grootte" value="midden"> 50 tot 249 %s, of omzet en balanstotaal boven 10 miljoen euro</label>'
            '<label><input type="radio" name="grootte" value="groot"> 250 of meer %s, of omzet boven 50 miljoen en balanstotaal boven 43 miljoen euro</label></fieldset>'
            '<fieldset><legend>3. Lever je aan bedrijven in deze sectoren, of aan de overheid?</legend>'
            '<label><input type="radio" name="keten" value="ja"> Ja</label><label><input type="radio" name="keten" value="nee"> Nee</label></fieldset>'
            '<button class="knop" type="submit">Toon mijn uitkomst</button></form>'
            '<div id="uitkomst" class="uitkomst" tabindex="-1" aria-live="polite" hidden></div>') % (land, opts, wn, wn, wn)


CONTACT_FORM = ('<form name="contact" method="post" action="/api/contact">'
                '<input type="hidden" name="form-name" value="contact">'
                '<p class="verborgen"><label>Laat dit veld leeg <input name="website" tabindex="-1" autocomplete="off"></label></p>'
                '<label for="naam">Naam</label><input id="naam" name="naam" autocomplete="name" required>'
                '<label for="email">E-mailadres</label><input id="email" name="email" type="email" autocomplete="email" required>'
                '<label for="bedrijf">Bedrijf (optioneel)</label><input id="bedrijf" name="bedrijf" autocomplete="organization">'
                '<label for="land">Waar is je bedrijf gevestigd?</label><select id="land" name="land"><option>België</option><option>Nederland</option></select>'
                '<label for="vraag">Je vraag</label><textarea id="vraag" name="vraag" rows="6" required></textarea>'
                '<p class="klein">Je gegevens dienen alleen om je vraag te beantwoorden. Lees de <a href="/privacy/">privacyverklaring</a>.</p>'
                '<button class="knop" type="submit">Verstuur je vraag</button></form>')
CONTACT_ZIJ = ('<aside class="zij"><div class="kaart"><h2>Liever mailen?</h2><p><a href="mailto:%s">%s</a></p><p>Je krijgt binnen twee werkdagen antwoord.</p></div>'
               '<div class="kaart"><h2>Eerst zelf kijken?</h2><ul><li><a href="/be/nis2-check/">NIS2-check voor België</a></li><li><a href="/nl/nis2-check/">Check voor Nederland</a></li><li><a href="/kennisbank/">Kennisbank</a></li><li><a href="/kennisbank/begrippen/">Begrippenlijst</a></li></ul></div>'
               '<p class="klein">Cyberdijk geeft uitleg en beantwoordt vragen. Dat is geen juridisch advies. Begeleiding start na afronding van de certificering.</p></aside>') % (EMAIL, EMAIL)

PRIVACY = ('<h2>Wie is verantwoordelijk?</h2><p>Cyberdijk is een handelsnaam van %(l)s, ondernemingsnummer %(k)s. Voor vragen over je gegevens mail je naar <a href="mailto:%(m)s">%(m)s</a>.</p>'
           '<h2>Welke gegevens, en waarvoor?</h2><ul>'
           '<li>Contactformulier en e-mail: je naam, je e-mailadres, eventueel je bedrijfsnaam en je vraag. Die gegevens dienen alleen om je vraag te beantwoorden. De grondslag is het gerechtvaardigd belang om op je bericht te reageren.</li>'
           '<li>Serverlogboeken: de hostingpartij registreert technische gegevens zoals IP-adres en tijdstip, om de site te beveiligen en storingen op te lossen.</li>'
           '<li>De NIS2-check: je antwoorden blijven in je browser en worden niet verstuurd of bewaard.</li></ul>'
           '<h2>Hoe lang?</h2><p>Berichten worden twaalf maanden na het laatste contact verwijderd.</p>'
           '<h2>Met wie?</h2><p>De site draait bij hostingpartij Cloudflare en de berichten uit het formulier worden bezorgd via e-maildienst Resend. Beide treden op als verwerker en zijn gevestigd in de Verenigde Staten; de doorgifte is geregeld in hun verwerkersovereenkomsten en standaardcontractbepalingen. Je gegevens worden niet verkocht en niet gebruikt voor reclame.</p>'
           '<h2>Je rechten</h2><p>Je kan je gegevens inzien, laten verbeteren of laten wissen, en je kan bezwaar maken tegen de verwerking. Mail naar <a href="mailto:%(m)s">%(m)s</a>; je krijgt binnen een maand antwoord. Ben je het niet eens met het antwoord, dan kan je een klacht indienen bij de <a href="https://www.gegevensbeschermingsautoriteit.be" rel="noopener">Gegevensbeschermingsautoriteit</a>.</p>'
           '<h2>Cookies</h2><p>Deze site plaatst geen cookies. Lees meer op de pagina <a href="/cookies/">Cookies</a>.</p>'
           '<p class="nota">Laatst bijgewerkt op %(d)s.</p>') % {"l": LEGAL, "k": KBO, "m": EMAIL, "d": DATUM_TEKST}


def slug(t):
    t = t.lower().translate(str.maketrans("éèëêáàäâóòöôúùüûíìïîç", "eeeeaaaaoooouuuuiiiic"))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def kruimel(p):
    if p["kind"] == "home":
        return ""
    items = [("Home", "/")] + list(p.get("crumbs", []))
    lis = "".join('<li><a href="%s">%s</a></li>' % (u, e(n)) for n, u in items)
    return '<nav class="kruimel" aria-label="Kruimelpad"><ol>%s<li aria-current="page">%s</li></ol></nav>' % (lis, e(p["h1"]))


def bronnen(p):
    if not p.get("sources"):
        return ""
    return '<h2>Bronnen</h2><ul class="bronnen">%s</ul>' % "".join('<li><a href="%s" rel="noopener">%s</a></li>' % (u, e(n)) for n, u in p["sources"])


def faq(items, kop="Veelgestelde vragen"):
    if not items:
        return ""
    return "<h2>%s</h2>" % kop + "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in items)


def vraag_kaarten(items):
    return '<div class="kaarten">%s</div>' % "".join('<a class="kaart kaart-link" href="%s"><h3>%s</h3><p>%s</p><span class="pijl">Lees verder</span></a>' % (u, e(q), e(d)) for q, d, u in items)


def regio_kaarten(items):
    return '<div class="kaarten">%s</div>' % "".join('<a class="kaart kaart-link" href="%s"><span class="vlag">Regio</span><h3>%s</h3><p>%s</p><span class="pijl">Uitleg voor %s</span></a>' % (u, e(n), e(d), e(n)) for n, d, u in items)


def artikel_kaarten(lijst, max_n=None):
    lijst = lijst[:max_n] if max_n else lijst
    return '<div class="kaarten">%s</div>' % "".join('<a class="kaart kaart-link" href="%s"><span class="vlag">%s</span><h3>%s</h3><p>%s</p><span class="pijl">Lees het artikel</span></a>' % (u, e(l), e(t), e(d)) for u, t, l, d in lijst)


def artikels_voor(land):
    """Artikels die voor dit land gelden: het eigen land plus de artikels voor beide landen. Nieuwste eerst."""
    naam = LAND_NAAM[land]
    return [a for a in reversed(ARTIKELS) if a[2] == naam or a[2] == "België en Nederland"]


def met_ids(body):
    """Geeft elke h2 in de tekst een id en levert de inhoudsopgave op."""
    koppen = []

    def vervang(m):
        tekst = re.sub(r"<[^>]+>", "", m.group(1))
        i = slug(tekst)
        koppen.append((i, tekst))
        return '<h2 id="%s">%s</h2>' % (i, m.group(1))
    body = re.sub(r"<h2>(.*?)</h2>", vervang, body, flags=re.S)
    return body, koppen


def inhoud(koppen):
    if len(koppen) < 3:
        return ""
    return '<nav class="inhoud" aria-label="Op deze pagina"><strong>Op deze pagina</strong><ol>%s</ol></nav>' % "".join('<li><a href="#%s">%s</a></li>' % (i, e(t)) for i, t in koppen)


def gerelateerd(p, n=4):
    """Pagina's met dezelfde tags, uit hetzelfde land of voor beide landen. Regiopagina's alleen bij regiopagina's."""
    tags = set(p.get("tags", []))
    land = p.get("land")
    uit = []
    for q in PAGES:
        if q is p or q["kind"] not in ("uitleg", "artikel", "regio") or q.get("noindex"):
            continue
        if q["kind"] == "regio" and p["kind"] != "regio":
            continue
        ql = q.get("land")
        if land in ("be", "nl") and ql not in (land, "eu"):
            continue
        score = len(tags & set(q.get("tags", [])))
        if score == 0:
            continue
        if ql == land:
            score += .5
        uit.append((score, q))
    uit.sort(key=lambda x: -x[0])
    return [q for _, q in uit[:n]]


def lees_ook(p):
    rel = gerelateerd(p)
    if not rel:
        return ""
    return '<div class="lees-ook"><h2>Lees ook</h2><ul>%s</ul></div>' % "".join('<li><a href="%s">%s</a><span>%s</span></li>' % (q["path"], e(q["h1"]), e(LAND_NAAM.get(q.get("land"), ""))) for q in rel)


def zijkolom(p):
    land = p.get("land") or "eu"
    if land == "be":
        knoppen = '<a class="knop" href="/be/nis2-check/">Doe de NIS2-check</a>'
    elif land == "nl":
        knoppen = '<a class="knop" href="/nl/nis2-check/">Doe de check</a>'
    else:
        knoppen = '<a class="knop" href="/be/nis2-check/">Check voor België</a><a class="knop licht" href="/nl/nis2-check/">Check voor Nederland</a>'
    if p["kind"] == "check":
        eerste = '<div class="kaart"><h2>Wat de check doet</h2><p>Drie vragen, meteen een antwoord. Er wordt niets opgeslagen of verstuurd.</p></div>'
    else:
        eerste = '<div class="kaart"><h2>Waar staat je bedrijf?</h2><p>Drie vragen, meteen een antwoord. Gratis en zonder e-mailadres.</p>%s</div>' % knoppen
    rel = gerelateerd(p)
    lijst = ('<div class="kaart"><h2>Lees ook</h2><ul>%s</ul></div>' % "".join('<li><a href="%s">%s</a></li>' % (q["path"], e(q["h1"])) for q in rel)) if rel else ""
    return ('<aside class="zij">%s%s<div class="kaart"><h2>Een vraag?</h2><p>Je krijgt binnen twee werkdagen antwoord per e-mail.</p><a class="knop licht" href="/contact/">Stel je vraag</a></div></aside>') % (eerste, lijst)


def kies_land_knoppen():
    return '<p class="kies"><a class="knop" href="/be/nis2-check/">Check voor België</a><a class="knop licht" href="/nl/nis2-check/">Check voor Nederland</a></p>'


DIENSTEN = [
    ("NIS2 en CyFun voor kmo's", "Bepalen of je onder de wet valt, de CyFun-zelfevaluatie doorlopen, een actieplan opstellen en je voorbereiden op verificatie of certificatie.", ["nis2", "cyfun"]),
    ("ISO 27001 begeleiding", "Scope, risicoanalyse, verklaring van toepasselijkheid, beleid en procedures, interne audit en voorbereiding op de certificatie-audit. Voor kmo's en mkb.", ["iso"]),
    ("GDPR/AVG op orde", "Verwerkingsregister, privacyverklaring, verwerkersovereenkomsten, DPIA en een procedure voor datalekken. Op termijn ook DPO of FG als externe dienst.", ["avg", "gdpr"]),
    ("Opleiding voor het bestuur", "De opleiding die NIS2 van bestuurders vraagt: wat de wet verwacht, welke risico's er zijn en hoe je als bestuur toezicht houdt. Met attest van deelname.", ["nis2", "bestuur"]),
    ("AI Act en AI-governance", "Inventaris van je AI-gebruik, AI-geletterdheid voor je medewerkers, transparantie en de voorbereiding op de hoogrisico-regels. Na de AIGP-certificering, verwacht eind 2027.", ["ai"]),
]
WACHTLIJST_FORM = ('<form name="wachtlijst" method="post" action="/api/contact">'
                   '<input type="hidden" name="form-name" value="wachtlijst">'
                   '<p class="verborgen"><label>Laat dit veld leeg <input name="website" tabindex="-1" autocomplete="off"></label></p>'
                   '<label for="w-naam">Naam</label><input id="w-naam" name="naam" autocomplete="name" required>'
                   '<label for="w-email">E-mailadres</label><input id="w-email" name="email" type="email" autocomplete="email" required>'
                   '<label for="w-bedrijf">Bedrijf</label><input id="w-bedrijf" name="bedrijf" autocomplete="organization">'
                   '<label for="w-dienst">Waar heb je hulp bij nodig?</label><select id="w-dienst" name="dienst"><option>NIS2 en CyFun</option><option>ISO 27001</option><option>GDPR/AVG</option><option>Opleiding voor het bestuur</option><option>AI Act en AI-governance</option><option>Weet ik nog niet</option></select>'
                   '<p class="klein">We gebruiken je gegevens alleen om je te verwittigen wanneer de begeleiding start. Lees de <a href="/privacy/">privacyverklaring</a>.</p>'
                   '<button class="knop" type="submit">Zet mij op de lijst</button></form>')


def main_diensten(p):
    hero = ('<section class="hero hero-land"><div class="wrap">%s<p class="kicker">In voorbereiding</p><h1>%s</h1><p class="lede">%s</p></div></section>') % (kruimel(p), e(p["h1"]), e(p["lede"]))
    kaarten = "".join('<div class="kaart"><span class="vlag">Vanaf 2027</span><h3>%s</h3><p>%s</p></div>' % (e(n), e(d)) for n, d, _ in DIENSTEN)
    midden = ('<section class="sectie"><div class="wrap"><div class="sectie-kop"><h2>Waarmee Cyberdijk je straks helpt</h2><p>Begeleiding start na afronding van de certificering. Tot dan: gratis uitleg, de check en een antwoord op je vraag.</p></div>'
              '<div class="kaarten">%s</div></div></section>') % kaarten
    waarom = ('<section class="sectie sectie-mist"><div class="wrap"><div class="lees"><div class="kolom">%s%s</div>'
              '<aside class="zij"><div class="kaart"><h2>Zet je op de wachtlijst</h2><p>Je hoort het als eerste wanneer de begeleiding start, en je krijgt een voorrangstarief als eerste klant.</p>%s</div></aside></div></div></section>') % (
        p["body"], faq(p.get("faq")), WACHTLIJST_FORM)
    return hero + midden + waarom + '<section class="sectie"><div class="wrap"><div class="kolom">%s%s</div></div></section>' % (CTA["eu"], NOTA)

# ---------------------------------------------------------------- pagina-inhoud per soort
def main_home(p):
    vink = "".join("<li>%s%s</li>" % (VINK, e(t)) for t in ("Gratis, zonder e-mailadres", "Geen cookies, geen trackers", "Bronnen en datum bij elk artikel", "Antwoord binnen twee werkdagen"))
    hero = ('<section class="hero"><div class="wrap"><div><p class="kicker">NIS2 · CyFun · ISO 27001 · GDPR/AVG · AI Act</p><h1>%s</h1><p class="lede">%s</p>%s'
            '<div class="acties"><a class="knop" href="#check">Doe de gratis NIS2-check</a><a class="knop licht" href="/contact/">Stel je vraag</a></div>'
            '<ul class="vinkjes">%s</ul></div><div class="beeld">%s</div></div></section>'
            '<div class="bronnenstrip"><div class="wrap"><strong>Uitleg op basis van de officiële bronnen</strong><span>Centrum voor Cybersecurity België</span><span>Safeonweb@Work</span><span>NCSC</span><span>Digital Trust Center</span><span>Gegevensbeschermingsautoriteit</span><span>Autoriteit Persoonsgegevens</span></div></div>') % (e(p["h1"]), e(p["lede"]), TELLER["eu"], vink, DIJK)
    landen = '<section class="sectie" id="kies-je-land"><div class="wrap"><div class="sectie-kop"><h2>Kies je land</h2><p>De regels komen uit Europa, maar België en Nederland vullen ze elk anders in. Kies de uitleg die voor jouw bedrijf geldt.</p></div><div class="landen">'
    for land, kop, knop in (("be", "België", "Uitleg voor België"), ("nl", "Nederland", "Uitleg voor Nederland")):
        landen += '<section class="kaart kaart-land"><span class="vlag">%s</span><h2>%s</h2><ul>%s</ul><a class="knop" href="/%s/">%s</a></section>' % (
            "NIS2-wet · CyFun · GDPR" if land == "be" else "Cyberbeveiligingswet · ISO 27001 · AVG", kop, "".join("<li>%s</li>" % e(x) for x in LAND_PUNTEN[land]), land, knop)
    landen += "</div></div></section>"
    check = ('<section class="sectie sectie-mist" id="check"><div class="wrap"><div class="sectie-kop"><h2>Weet je niet of je bedrijf onder NIS2 valt?</h2>'
             '<p>Doe de gratis check in vijf minuten. Drie vragen over je sector, je grootte en je klanten. Je krijgt meteen een antwoord, zonder je e-mailadres achter te laten.</p></div>%s</div></section>') % kies_land_knoppen()
    cijfers = ('<section class="cijfers"><div class="wrap">'
               '<div class="cijfer"><b>18 april 2027</b><span>Deadline voor essentiële entiteiten in België om hun conformiteit te laten beoordelen.</span></div>'
               '<div class="cijfer"><b>15 augustus 2026</b><span>De Cyberbeveiligingswet geldt in Nederland, zonder overgangsperiode.</span></div>'
               '<div class="cijfer"><b>24 uur</b><span>Termijn voor de eerste waarschuwing bij een significant incident onder NIS2.</span></div>'
               '<div class="cijfer"><b>72 uur</b><span>Termijn om een datalek met risico te melden bij de privacytoezichthouder.</span></div>'
               '</div></section>')
    kaarten = '<section class="sectie"><div class="wrap"><div class="sectie-kop"><h2>Vier vragen die ondernemers ons het vaakst stellen</h2><p>Korte antwoorden, met per land de uitgebreide uitleg.</p></div><div class="kaarten">'
    for kop, tekst, links in HOME_VRAGEN:
        kaarten += '<div class="kaart"><h3>%s</h3><p>%s</p><p class="kies">%s</p></div>' % (e(kop), e(tekst), " ".join('<a href="%s">%s</a>' % (u, e(n)) for n, u in links))
    kaarten += "</div></div></section>"
    stappen = ('<section class="sectie sectie-mist"><div class="wrap"><div class="sectie-kop"><h2>Zo werkt Cyberdijk</h2><p>Geen verkooppraatje, wel een duidelijk pad.</p></div><ol class="stappen">'
               '<li><h3>Doe de check</h3><p>In vijf minuten weet je of je bedrijf waarschijnlijk onder de wet valt, en op welk niveau.</p></li>'
               '<li><h3>Lees wat je moet regelen</h3><p>Per land en per onderwerp: wat de wet vraagt, wat het kost en hoe lang het duurt. Met bronnen.</p></li>'
               '<li><h3>Stel je vraag</h3><p>Blijf je met een vraag zitten? Stuur ze in. Je krijgt binnen twee werkdagen een antwoord in gewone taal.</p></li>'
               '</ol></div></section>')
    kb = '<section class="sectie"><div class="wrap"><div class="sectie-kop"><h2>Uit de kennisbank</h2><p>Elke week een artikel dat één vraag beantwoordt.</p></div>%s<p class="kies" style="margin-top:1.5rem"><a class="knop licht" href="/kennisbank/">Alle artikels</a><a href="/kennisbank/begrippen/">Begrippenlijst</a></p></div></section>' % artikel_kaarten(list(reversed(ARTIKELS)), 6)
    vr = '<section class="sectie sectie-mist"><div class="wrap"><div class="kolom">%s</div></div></section>' % faq(HOME_FAQ)
    band = '<section class="band-knop"><div class="wrap"><h2>Klaar om te weten waar je staat?</h2><p>De check is gratis en bewaart niets. Daarna lees je per onderwerp wat je moet regelen.</p>%s</div></section>' % kies_land_knoppen()
    return hero + landen + check + cijfers + kaarten + stappen + kb + vr + band


def main_hub(p):
    land = p["land"]
    knop = ("/be/nis2-check/", "Doe de NIS2-check") if land == "be" else ("/nl/nis2-check/", "Doe de check")
    hero = ('<section class="hero hero-land"><div class="wrap">%s<p class="kicker">%s</p><h1>%s</h1><p class="lede">%s</p>%s'
            '<div class="acties"><a class="knop" href="%s">%s</a><a class="knop licht" href="/contact/">Stel je vraag</a></div></div></section>') % (
        kruimel(p), " · ".join(LAND_PUNTEN[land][:2]), e(p["h1"]), e(p["lede"]), TELLER[land], knop[0], knop[1])
    kaarten = '<section class="sectie"><div class="wrap"><div class="sectie-kop"><h2>Waar wil je antwoord op?</h2></div>%s</div></section>' % vraag_kaarten(p["vragen"])
    regios = '<section class="sectie sectie-mist"><div class="wrap"><div class="sectie-kop"><h2>Uitleg per regio</h2><p>Wat er speelt in jouw streek en welke vragen bedrijven daar krijgen.</p></div>%s</div></section>' % regio_kaarten(p["regios"])
    rest = ""
    if p.get("body", "").strip():
        rest = '<section class="sectie"><div class="wrap"><div class="kolom">%s</div></div></section>' % p["body"]
    kb = '<section class="sectie%s"><div class="wrap"><div class="sectie-kop"><h2>Uit de kennisbank voor %s</h2></div>%s<p class="kies" style="margin-top:1.5rem"><a class="knop licht" href="/kennisbank/">Alle artikels</a></p></div></section>' % (
        " sectie-mist" if rest else "", LAND_NAAM[land], artikel_kaarten(artikels_voor(land), 6))
    br = '<section class="sectie"><div class="wrap"><div class="kolom">%s%s</div></div></section>' % (CTA[land], bronnen(p))
    return hero + kaarten + regios + rest + kb + br


def main_lijst(p):
    groepen = [("België en Nederland", "Voor België en Nederland"), ("België", "Voor België"), ("Nederland", "Voor Nederland")]
    delen = ""
    for sleutel, kop in groepen:
        lijst = [a for a in reversed(ARTIKELS) if a[2] == sleutel]
        delen += '<div class="sectie-kop" style="margin-top:2.5rem"><h2>%s</h2></div>%s' % (e(kop), artikel_kaarten(lijst))
    uit = [("NIS2 en CyFun voor kmo's", "België. Wat de wet vraagt, de CyFun-niveaus en de deadline.", "/be/nis2-cyfun/"), ("ISO 27001 voor kmo's", "België. Stappen, kosten en doorlooptijd.", "/be/iso-27001/"), ("GDPR en DPO voor kmo's", "België. Wat verplicht is.", "/be/gdpr-dpo/"),
           ("Cyberbeveiligingswet voor mkb", "Nederland. Zorgplicht, meldplicht en registratie.", "/nl/cyberbeveiligingswet-nis2/"), ("ISO 27001 voor mkb", "Nederland. Stappen, kosten en doorlooptijd.", "/nl/iso-27001/"), ("AVG en FG voor mkb", "Nederland. Wat verplicht is.", "/nl/avg-fg/")]
    kop = '<div class="wrap">%s<div class="kolom"><h1>%s</h1><p class="lede">%s</p><p class="kies"><a class="knop licht" href="/kennisbank/begrippen/">Begrippenlijst</a><a href="/feed.xml">RSS-feed</a></p></div>' % (kruimel(p), e(p["h1"]), e(p["lede"]))
    return kop + delen + '<div class="sectie-kop" style="margin-top:3rem"><h2>Uitleg per onderwerp</h2></div>' + vraag_kaarten(uit) + "</div>"


def main_begrippen(p):
    dl = '<dl class="begrippen">%s</dl>' % "".join('<div id="%s"><dt>%s</dt><dd>%s</dd></div>' % (slug(t), e(t), e(u)) for t, u in BEGRIPPEN)
    return ('<div class="wrap">%s<div class="kolom"><h1>%s</h1><p class="lede">%s</p></div>%s<div class="kolom">%s%s</div></div>') % (kruimel(p), e(p["h1"]), e(p["lede"]), dl, CTA["eu"], NOTA)


def main_inner(p):
    k, land = p["kind"], p.get("land")
    if k == "home":
        return main_home(p)
    if k == "hub":
        return main_hub(p)
    if k == "lijst":
        return main_lijst(p)
    if k == "begrippen":
        return main_begrippen(p)
    if k == "diensten":
        return main_diensten(p)
    kop = '%s<h1>%s</h1><p class="lede">%s</p>' % (kruimel(p), e(p["h1"]), e(p["lede"]))
    body = p.get("body", "")
    if k == "check":
        return '<div class="wrap"><div class="lees"><div class="kolom">%s%s%s%s%s</div>%s</div></div>' % (kop, check_form(land), body, bronnen(p), NOTA, zijkolom(p))
    if k == "contact":
        return '<div class="wrap"><div class="contact-blok"><div class="kolom">%s%s</div>%s</div></div>' % (kop, CONTACT_FORM, CONTACT_ZIJ)
    if k == "vast":
        if body == "__PRIVACY__":
            body = PRIVACY
        if p["path"] == "/over/":
            body += '<p class="nota">Cyberdijk is een handelsnaam van %s, ondernemingsnummer %s.</p>' % (LEGAL, KBO)
        return '<div class="wrap"><div class="kolom">%s%s</div></div>' % (kop, body)
    # uitleg, regio, artikel
    kort = ""
    if p.get("kort"):
        kort = '<div class="kort"><h2>In het kort</h2><ul>%s</ul></div>' % "".join("<li>%s</li>" % e(x) for x in p["kort"])
    meta = ""
    if k == "artikel":
        meta = '<p class="label">Geldt voor %s. Gepubliceerd op %s.</p>' % (LAND_NAAM[land], DATUM_TEKST)
    body, koppen = met_ids(body)
    doen = DOEN[land] if k == "regio" else ""
    art = '<article class="kolom">%s%s%s%s%s%s%s%s%s%s%s</article>' % (kop, meta, kort, inhoud(koppen), body, doen, faq(p.get("faq")), CTA[land], lees_ook(p), bronnen(p), NOTA)
    return '<div class="wrap"><div class="lees">%s%s</div></div>' % (art, zijkolom(p))


# ---------------------------------------------------------------- kop en voet
def header(p):
    land = p.get("land")
    sec = "/be/" if land == "be" and p["kind"] != "artikel" else "/nl/" if land == "nl" and p["kind"] != "artikel" else "/" + p["path"].strip("/").split("/")[0] + "/"
    lis = "".join('<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="true"' if u == sec else "", e(n)) for n, u in NAV)
    knop = {"be": ("/be/nis2-check/", "Doe de NIS2-check"), "nl": ("/nl/nis2-check/", "Doe de check")}.get(land, ("/#check", "Doe de check"))
    return ('<a class="skip" href="#inhoud">Naar de inhoud</a><header class="top"><div class="wrap"><a class="merk" href="/">%s%s</a>'
            '<a class="knop" href="%s">%s</a><input class="menu-schakel" type="checkbox" id="menu" aria-label="Menu openen of sluiten"><label class="menu-knop" for="menu"><span></span>Menu</label>'
            '<nav aria-label="Hoofdmenu"><ul>%s</ul></nav></div></header>') % (MARK, WOORD, knop[0], knop[1], lis)


def kolom(titel, items):
    return "<div><h2>%s</h2><ul>%s</ul></div>" % (titel, "".join('<li><a href="%s">%s</a></li>' % (u, e(n)) for n, u in items))


def footer():
    merk = ('<div class="merkblok"><a class="merk" href="/">%s%s</a>'
            '<p>Heldere uitleg over NIS2, CyFun, ISO 27001, GDPR/AVG en de AI Act voor kmo\'s en mkb tussen Antwerpen en Breda. Gratis check, geen cookies, bronnen bij elk artikel.</p>'
            '<p>%s is een handelsnaam van %s<br>Ondernemingsnummer %s%s<br><a href="mailto:%s">%s</a></p>'
            '<p>Ook van %s: <a href="%s" rel="noopener">Marketingbaas</a>, websites voor zelfstandigen in Vlaanderen en Nederland.</p></div>') % (
        MARK, WOORD, BRAND, LEGAL, KBO, ("<br>" + e(ADRES)) if ADRES else "", EMAIL, EMAIL, LEGAL, MB_URL)
    onder = ('<div class="onder"><p>© %s %s · <a href="/privacy/">Privacyverklaring</a> · <a href="/cookies/">Cookies</a> · <a href="/.well-known/security.txt">security.txt</a></p>'
             '<p>Website door <a href="%s" rel="noopener">Marketingbaas</a></p></div>') % (JAAR, BRAND, MB_URL)
    return '<footer class="voet"><div class="wrap">%s%s%s%s%s</div></footer>' % (merk, kolom("België", VOET_BE), kolom("Nederland", VOET_NL), kolom("Kennisbank en Cyberdijk", VOET_KB + VOET_CD), onder)


# ---------------------------------------------------------------- head, JSON-LD, pagina
def jsonld(p):
    url = BASE + p["path"]
    org = {"@type": "Organization", "@id": BASE + "/#organisatie", "name": BRAND, "url": BASE + "/", "email": EMAIL, "legalName": LEGAL, "vatID": KBO.replace(" ", "").replace(".", ""),
           "logo": BASE + "/assets/og.png", "parentOrganization": {"@type": "Organization", "name": LEGAL}, **({"sameAs": SAMEAS} if SAMEAS else {}),
           "areaServed": ["Antwerpen", "Noorderkempen", "Roosendaal", "Bergen op Zoom", "Breda", "Moerdijk"],
           "knowsAbout": ["NIS2", "CyberFundamentals", "Cyberbeveiligingswet", "ISO/IEC 27001", "GDPR", "AVG", "AI Act"]}
    out = []
    if p["kind"] == "home":
        out.append({"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "name": BRAND, "url": BASE + "/", "inLanguage": "nl", "publisher": {"@id": BASE + "/#organisatie"}})
    if p["kind"] in ("home", "hub", "contact") or p["path"] == "/over/":
        out.append(dict({"@context": "https://schema.org"}, **org))
    if p["kind"] != "home":
        items = [("Home", "/")] + list(p.get("crumbs", [])) + [(p["h1"], p["path"])]
        out.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(items)]})
    if p["kind"] in ("uitleg", "regio", "artikel"):
        woorden = len(re.sub(r"<[^>]+>", " ", p.get("body", "")).split())
        out.append({"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"], "inLanguage": p["lang"], "datePublished": DATUM, "dateModified": p.get("updated", DATUM),
                    "wordCount": woorden, "articleSection": LAND_NAAM.get(p.get("land"), "Kennisbank"), "keywords": ", ".join(p.get("tags", [])), "image": BASE + "/assets/og.png",
                    "mainEntityOfPage": url, "author": {"@id": BASE + "/#organisatie", "@type": "Organization", "name": BRAND}, "publisher": {"@id": BASE + "/#organisatie", "@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": BASE + "/assets/og.png"}}})
    vragen_ld = p.get("faq") or (HOME_FAQ if p["kind"] == "home" else None)
    if vragen_ld:
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in vragen_ld]})
    if p["kind"] == "diensten":
        out.append({"@context": "https://schema.org", "@type": "ItemList", "name": p["h1"], "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "Service", "name": n, "description": d, "provider": {"@id": BASE + "/#organisatie"}, "areaServed": ["BE", "NL"], "serviceType": "Informatiebeveiliging en privacy"}} for i, (n, d, _) in enumerate(DIENSTEN)]})
    if p["kind"] == "begrippen":
        out.append({"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": url, "name": p["h1"], "inLanguage": "nl",
                    "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": u, "url": url + "#" + slug(t)} for t, u in BEGRIPPEN]})
    return "".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in out)


def head(p, css):
    url = BASE + p["path"]
    h = ['<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">', "<title>%s</title>" % e(p["title"]),
         '<meta name="description" content="%s">' % e(p["desc"])]
    if p.get("noindex"):
        h.append('<meta name="robots" content="noindex">')
    else:
        h.append('<meta name="robots" content="index, follow, max-image-preview:large">')
        h.append('<link rel="canonical" href="%s">' % url)
    if p.get("alt"):
        other = BY_PATH[p["alt"]]
        for q in (p, other):
            h.append('<link rel="alternate" hreflang="%s" href="%s">' % (q["lang"], BASE + q["path"]))
        h.append('<link rel="alternate" hreflang="x-default" href="%s/">' % BASE)
    loc = {"nl-BE": "nl_BE", "nl-NL": "nl_NL"}.get(p["lang"], "nl_BE")
    h += ['<meta property="og:type" content="%s">' % ("article" if p["kind"] in ("uitleg", "regio", "artikel") else "website"), '<meta property="og:title" content="%s">' % e(p["title"]),
          '<meta property="og:description" content="%s">' % e(p["desc"]), '<meta property="og:url" content="%s">' % url, '<meta property="og:locale" content="%s">' % loc,
          '<meta property="og:site_name" content="%s">' % BRAND, '<meta property="og:image" content="%s/assets/og.png">' % BASE, '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
          '<meta property="og:image:alt" content="%s: informatiebeveiliging en privacy, helder uitgelegd">' % BRAND, '<meta name="twitter:card" content="summary_large_image">',
          '<meta name="theme-color" content="#12343B">', '<link rel="icon" href="/favicon.svg" type="image/svg+xml">', '<link rel="alternate" type="application/rss+xml" title="%s kennisbank" href="/feed.xml">' % BRAND,
          '<link rel="preload" href="/assets/fonts/archivo-head.woff2" as="font" type="font/woff2" crossorigin>', "<style>%s</style>" % css]
    if p["kind"] == "check":
        h.append('<script src="/assets/check.js?v=%s" defer></script>' % JS_VERSIE)
    if p["kind"] in ("home", "hub"):
        h.append('<script src="/assets/teller.js?v=%s" defer></script>' % TELLER_VERSIE)
    h.append(jsonld(p))
    return "".join(h)


def css_site():
    return CSS.replace("__FONT__", "/assets/fonts/archivo-head.woff2").strip()


def plakknop(p):
    """Vaste knop onderaan op telefoons, behalve op de check- en contactpagina's zelf."""
    if p["kind"] in ("check", "contact") or p.get("noindex"):
        return ""
    land = p.get("land")
    u, t = {"be": ("/be/nis2-check/", "Doe de gratis NIS2-check"), "nl": ("/nl/nis2-check/", "Doe de gratis check")}.get(land, ("/be/nis2-check/", "Doe de gratis NIS2-check"))
    return '<div class="plak"><a class="knop" href="%s">%s</a></div>' % (u, t)


def page(p, css=None):
    css = css or css_site()
    return '<!doctype html><html lang="%s"><head>%s</head><body>%s<main id="inhoud">%s</main>%s%s</body></html>' % (p["lang"], head(p, css), header(p), main_inner(p), footer(), plakknop(p))


# ---------------------------------------------------------------- schrijven
def write(rel, content, mode="w"):
    fn = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    with open(fn, mode, **({} if "b" in mode else {"encoding": "utf-8"})) as f:
        f.write(content)


def feed():
    items = []
    for u, t, l, d in reversed(ARTIKELS):
        p = BY_PATH[u]
        dag = datetime.datetime.strptime(p.get("updated", DATUM), "%Y-%m-%d").strftime("%a, %d %b %Y 08:00:00 +0200")
        items.append("<item><title>%s</title><link>%s%s</link><guid>%s%s</guid><pubDate>%s</pubDate><category>%s</category><description>%s</description></item>" % (e(t), BASE, u, BASE, u, dag, e(l), e(d)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>%s kennisbank</title><link>%s/kennisbank/</link>'
            '<description>Praktische artikels over NIS2, CyFun, de Cyberbeveiligingswet, ISO 27001 en GDPR/AVG voor bedrijven in België en Nederland.</description><language>nl</language>%s</channel></rss>\n') % (BRAND, BASE, "".join(items))


def build():
    shutil.rmtree(OUT, ignore_errors=True)
    css = css_site()
    css_hash = base64.b64encode(hashlib.sha256(css.encode("utf-8")).digest()).decode()
    for p in PAGES:
        write(p["path"] + "index.html", page(p, css))
    nf = dict(path="/404/", lang="nl", kind="vast", land=None, crumbs=[], noindex=True, title="Pagina niet gevonden | Cyberdijk", desc="Deze pagina bestaat niet of is verplaatst.",
              h1="Deze pagina bestaat niet", lede="De pagina is verplaatst of het adres klopt niet.", body='<p>Ga naar de <a href="/">startpagina</a>, naar de <a href="/kennisbank/">kennisbank</a> of <a href="/contact/">stel je vraag</a>.</p>')
    write("/404.html", page(nf, css))
    write("/assets/site.css", css)                       # ter inzage; de pagina's gebruiken de ingebouwde versie
    write("/assets/check.js", CHECK_JS.strip())
    write("/assets/teller.js", TELLER_JS)
    os.makedirs(os.path.join(OUT, "assets/fonts"), exist_ok=True)
    shutil.copy(os.path.join(SRC, "fonts/archivo-head.woff2"), os.path.join(OUT, "assets/fonts/archivo-head.woff2"))
    shutil.copy(os.path.join(SRC, "fonts/OFL.txt"), os.path.join(OUT, "assets/fonts/OFL.txt"))
    shutil.copy(os.path.join(SRC, "og.png"), os.path.join(OUT, "assets/og.png"))
    write("/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#12343B"/><path d="M6 44q5-5 10 0t10 0" fill="none" stroke="#7FC6DD" stroke-width="4" stroke-linecap="round"/><path d="M22 54 34 18h12l14 36z" fill="#F2B705"/></svg>')
    idx = [p for p in PAGES if not p.get("noindex")]
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (BASE, p["path"], p.get("updated", DATUM)) for p in idx))
    write("/feed.xml", feed())
    write("/robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
    write("/llms.txt", "# %s\n\n> Heldere uitleg over NIS2, CyFun, ISO 27001 en GDPR/AVG voor kmo's en mkb in België en Nederland. Gratis NIS2-check, geen cookies, bronnen bij elk artikel.\n\n## Pagina's\n\n%s\n" % (
        BRAND, "\n".join("- [%s](%s%s): %s" % (p["h1"], BASE, p["path"], p["desc"]) for p in idx)))
    write("/.well-known/security.txt", "Contact: mailto:%s\nExpires: 2027-10-01T00:00:00.000Z\nPreferred-Languages: nl, en\nCanonical: %s/.well-known/security.txt\n" % (EMAIL, BASE))
    write("/_headers", ("/*\n  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload\n  X-Content-Type-Options: nosniff\n  X-Frame-Options: DENY\n"
                        "  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Cross-Origin-Opener-Policy: same-origin\n"
                        "  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self' 'sha256-%s'; script-src 'self'; font-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'; object-src 'none'; upgrade-insecure-requests\n"
                        "/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/check.js\n  Cache-Control: public, max-age=31536000, immutable\n/assets/teller.js\n  Cache-Control: public, max-age=31536000, immutable\n/assets/*\n  Cache-Control: public, max-age=604800\n/favicon.svg\n  Cache-Control: public, max-age=604800\n") % css_hash)
    write("/functions/api/contact.js", CONTACT_FUNCTIE.strip() + "\n")
    write("/_redirects", "# Omleidingen per domein (cyberdijk.be -> /be/, cyberdijk.nl -> /nl/, www -> zonder www) staan in Cloudflare als Redirect Rules; zie LEES-MIJ.txt.\n/index.html / 301\n")
    return idx


def preview():
    font = base64.b64encode(open(os.path.join(SRC, "fonts/archivo-head.woff2"), "rb").read()).decode()
    css = CSS.replace("__FONT__", "data:font/woff2;base64," + font)
    css += ':root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}'
    tpl = "".join('<template data-path="%s" data-title="%s" data-land="%s">%s</template>' % (p["path"], e(p["title"]), p.get("land") or "", main_inner(p)) for p in PAGES)
    home = BY_PATH["/"]
    router = r"""
(function(){
var view=document.getElementById("weergave"),knop=document.getElementById("topknop"),menu=document.getElementById("menu");
function toon(pad){var t=document.querySelector('template[data-path="'+pad+'"]');if(!t){return false;}
view.textContent="";view.appendChild(t.content.cloneNode(true));document.title=t.getAttribute("data-title");
var l=t.getAttribute("data-land");knop.setAttribute("href",l==="be"?"/be/nis2-check/":l==="nl"?"/nl/nis2-check/":"/#check");knop.textContent=l==="be"?"Doe de NIS2-check":"Doe de check";
if(menu){menu.checked=false;}window.scrollTo(0,0);if(window.initCheck){window.initCheck();}if(window.initTeller){window.initTeller();}return true;}
document.addEventListener("click",function(ev){var a=ev.target.closest("a");if(!a){return;}var h=a.getAttribute("href")||"";
if(h.charAt(0)==="#"){return;}
if(h.charAt(0)==="/"){ev.preventDefault();var deel=h.split("#");toon(deel[0]||"/");if(deel[1]){var el=document.getElementById(deel[1]);if(el){el.scrollIntoView();}}}
else if(h.indexOf("http")===0){a.setAttribute("target","_blank");}});
document.addEventListener("submit",function(ev){var f=ev.target;if(f.getAttribute("action")==="/api/contact"){ev.preventDefault();toon("/contact/bedankt/");}});
toon("/");
})();
"""
    hdr = header(home).replace('<a class="knop" href="/#check">', '<a class="knop" id="topknop" href="/#check">')
    doc = ('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>Cyberdijk: voorbeeld van de website</title>'
           '<style>%s</style></head><body><div class="band">Voorbeeld van cyberdijk.eu. De site staat nog niet online.</div>%s<main id="inhoud"><div id="weergave"></div></main>%s%s<script>%s</script><script>%s</script><script>%s</script></body></html>') % (
        css, hdr, footer(), tpl, CHECK_JS, router, TELLER_JS)
    with open(os.path.join(os.path.dirname(SRC), "cyberdijk-voorbeeld.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    return len(doc)


def controle(idx):
    fouten = []
    css = css_site()
    for p in PAGES:
        h = page(p, css)
        if len(p["title"]) > 60:
            fouten.append("title te lang (%d): %s" % (len(p["title"]), p["path"]))
        if len(p["desc"]) > 155:
            fouten.append("meta te lang (%d): %s" % (len(p["desc"]), p["path"]))
        if h.count("<h1") != 1:
            fouten.append("h1-aantal: " + p["path"])
        for href in re.findall(r'href="(/[^"#]*)', h):
            if href.startswith("/assets/") or href in ("/favicon.svg", "/feed.xml", "/.well-known/security.txt"):
                continue
            if href not in BY_PATH:
                fouten.append("dode link %s op %s" % (href, p["path"]))
        for anker in re.findall(r'href="#([^"]+)"', h):
            if 'id="%s"' % anker not in h:
                fouten.append("dood anker #%s op %s" % (anker, p["path"]))
        if p.get("alt") and BY_PATH[p["alt"]].get("alt") != p["path"]:
            fouten.append("hreflang niet wederzijds: " + p["path"])
    woorden = {p["path"]: len(re.sub(r"<[^>]+>", " ", main_inner(p)).split()) for p in PAGES}
    return fouten, woorden


if __name__ == "__main__":
    idx = build()
    fouten, woorden = controle(idx)
    n = preview()
    print("pagina's:", len(PAGES), "| in sitemap:", len(idx), "| voorbeeld bytes:", n)
    print("fouten:", fouten or "geen")
    for k, v in woorden.items():
        print("%4d  %s" % (v, k))
