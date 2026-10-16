// Cloudflare Pages Function: /api/emailcheck?d=domein.be
// Leest alleen openbare DNS-gegevens (SPF, DMARC, DKIM, MX, MTA-STS) via DNS-over-HTTPS en kijkt of de website
// via HTTPS bereikbaar is. Er wordt niets opgeslagen of gelogd. Antwoord: JSON, 10 minuten in de cache.
const DOH = "https://cloudflare-dns.com/dns-query";
const SELECTORS = ["google", "selector1", "selector2", "default", "k1", "k2", "s1", "s2", "mail", "dkim", "resend",
  "smtp", "sig1", "key1", "zoho", "protonmail", "fm1", "mandrill", "mxvault", "sendgrid"];
const PROVIDERS = [["google.com", "Google Workspace"], ["googlemail.com", "Google Workspace"], ["outlook.com", "Microsoft 365"],
  ["mx.cloudflare.net", "Cloudflare Email Routing"], ["mailprotect.be", "Combell"], ["one.com", "one.com"], ["ovh.net", "OVH"],
  ["hostinger", "Hostinger"], ["zoho.eu", "Zoho"], ["zoho.com", "Zoho"], ["protonmail.ch", "Proton"], ["transip.email", "TransIP"],
  ["antagonist.nl", "Antagonist"], ["vimexx", "Vimexx"], ["mijndomein", "Mijndomein"], ["versio", "Versio"], ["strato", "Strato"],
  ["ionos", "IONOS"], ["kpnmail", "KPN"], ["telenet", "Telenet"], ["proximus", "Proximus"], ["skynet.be", "Proximus"],
  ["easyhost.be", "Easyhost"], ["mailcluster", "Easyhost/Combell"], ["icloud.com", "iCloud"], ["yahoodns", "Yahoo"]];

const geldig = (d) => /^(?=.{4,100}$)([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,24}$/.test(d);

async function dns(naam, type) {
  try {
    const r = await fetch(DOH + "?name=" + encodeURIComponent(naam) + "&type=" + type, { headers: { accept: "application/dns-json" } });
    const j = await r.json();
    return { status: j.Status, antwoorden: (j.Answer || []).map((a) => ({ type: a.type, data: String(a.data || "") })) };
  } catch (e) {
    return { status: -1, antwoorden: [] };
  }
}
const txt = (res) => res.antwoorden.filter((a) => a.type === 16).map((a) => a.data.replace(/^"|"$/g, "").replace(/"\s*"/g, ""));

function spfOordeel(lijst) {
  const spf = lijst.filter((t) => /^v=spf1(\s|$)/i.test(t));
  if (!spf.length) return { status: "slecht", code: "geen" };
  if (spf.length > 1) return { status: "slecht", code: "dubbel", record: spf.join(" | ") };
  const r = spf[0], all = (r.match(/([~+?-])?all\b/i) || [])[0] || "";
  if (all === "-all") return { status: "goed", code: "streng", record: r };
  if (all === "~all") return { status: "goed", code: "zacht", record: r };
  if (/\+all|^all/i.test(all)) return { status: "slecht", code: "open", record: r };
  return { status: "matig", code: "zwak", record: r };
}

function dmarcOordeel(lijst) {
  const rec = lijst.find((t) => /^v=dmarc1/i.test(t));
  if (!rec) return { status: "slecht", p: "geen" };
  const tag = (k) => ((rec.match(new RegExp("(?:^|;)\\s*" + k + "\\s*=\\s*([^;]+)", "i")) || [])[1] || "").trim().toLowerCase();
  const p = tag("p") || "none", pct = parseInt(tag("pct") || "100", 10), rua = !!tag("rua");
  let status = p === "reject" || p === "quarantine" ? (pct < 100 ? "matig" : "goed") : p === "none" ? "matig" : "slecht";
  return { status, p, pct: isNaN(pct) ? 100 : pct, rua, record: rec };
}

async function website(d) {
  for (const host of [d, "www." + d]) {
    try {
      const r = await fetch("https://" + host + "/", { redirect: "follow", signal: AbortSignal.timeout(7000),
        headers: { "user-agent": "Mozilla/5.0 (compatible; CyberdijkCheck/1.0; +https://cyberdijk.eu/email-check/)" } });
      const eind = new URL(r.url);
      return { https: eind.protocol === "https:", hsts: !!r.headers.get("strict-transport-security"), status: r.status, host };
    } catch (e) { /* volgende proberen */ }
  }
  return { https: false, hsts: false, status: 0 };
}

export async function onRequestGet({ request, waitUntil }) {
  const url = new URL(request.url);
  let d = (url.searchParams.get("d") || "").trim().toLowerCase();
  d = d.replace(/^[a-z]+:\/\//, "").replace(/^.*@/, "").split(/[/?#:]/)[0].replace(/^www\./, "").replace(/\.$/, "");
  const kop = { "content-type": "application/json; charset=utf-8", "cache-control": "public, max-age=600", "x-robots-tag": "noindex" };
  if (!geldig(d)) return new Response(JSON.stringify({ fout: "Geef een geldige domeinnaam in, bijvoorbeeld jouwbedrijf.be." }), { status: 400, headers: kop });
  const sleutel = new Request("https://cyberdijk.eu/__emailcheck/" + d);
  const cache = caches.default;
  const bewaard = await cache.match(sleutel);
  if (bewaard) return bewaard;

  const [root, dmarcRes, mx, sts, web, ...dkim] = await Promise.all([
    dns(d, "TXT"), dns("_dmarc." + d, "TXT"), dns(d, "MX"), dns("_mta-sts." + d, "TXT"), website(d),
    ...SELECTORS.map((s) => dns(s + "._domainkey." + d, "TXT")),
  ]);
  if (root.status === 3 && mx.status === 3) {
    return new Response(JSON.stringify({ fout: "Dit domein bestaat niet. Controleer de schrijfwijze." }), { status: 404, headers: kop });
  }
  const mxHosts = mx.antwoorden.filter((a) => a.type === 15).map((a) => a.data.split(" ").pop().replace(/\.$/, "").toLowerCase());
  const leverancier = (PROVIDERS.find(([k]) => mxHosts.some((h) => h.includes(k))) || [])[1] || (mxHosts[0] || "");
  const dkimGevonden = SELECTORS.filter((s, i) => txt(dkim[i]).some((t) => /v=dkim1|(^|;)\s*p=/i.test(t)));
  const spf = spfOordeel(txt(root));
  const dmarc = dmarcOordeel(txt(dmarcRes));
  const mtaSts = txt(sts).some((t) => /^v=stsv1/i.test(t));

  let score = { reject: 45, quarantine: 35, none: 10 }[dmarc.p] || 0;
  if (dmarc.pct < 100 && score > 10) score -= 10;
  score += spf.status === "goed" ? 25 : spf.status === "matig" ? 10 : 0;
  score += dkimGevonden.length ? 15 : 0;
  score += web.https ? 10 : 0;
  score += web.hsts ? 5 : 0;
  const vervalsbaar = !(["reject", "quarantine"].includes(dmarc.p) && dmarc.pct === 100);

  const uit = { domein: d, score, vervalsbaar, spf, dmarc, dkim: dkimGevonden, mx: { hosts: mxHosts.slice(0, 5), leverancier },
    mtaSts, web, getest: new Date().toISOString() };
  const res = new Response(JSON.stringify(uit), { headers: kop });
  waitUntil(cache.put(sleutel, res.clone()));
  return res;
}
