// lokale test met nep-DNS
const vals = {
  "voorbeeld.be|TXT": ['"v=spf1 include:_spf.google.com ~all"'], "_dmarc.voorbeeld.be|TXT": ['"v=DMARC1; p=none; rua=mailto:x@y"'],
  "voorbeeld.be|MX": ["10 aspmx.l.google.com."], "google._domainkey.voorbeeld.be|TXT": ['"v=DKIM1; k=rsa; p=MIGf"'],
};
globalThis.caches = { default: { match: async () => null, put: async () => {} } };
globalThis.fetch = async (u, o) => {
  u = String(u);
  if (u.startsWith("https://cloudflare-dns.com")) {
    const q = new URL(u), k = q.searchParams.get("name") + "|" + q.searchParams.get("type");
    const data = vals[k];
    const type = q.searchParams.get("type") === "MX" ? 15 : 16;
    return new Response(JSON.stringify({ Status: data ? 0 : (k.startsWith("bestaatniet") ? 3 : 0), Answer: (data || []).map((d) => ({ type, data: d })) }));
  }
  if (u.includes("bestaatniet")) throw new Error("x");
  const r = new Response("ok", { headers: { "strict-transport-security": "max-age=1" } }); Object.defineProperty(r, "url", { value: u }); return r;
};
const m = await import("./emailcheck_functie.js");
for (const d of ["https://www.Voorbeeld.be/contact", "info@voorbeeld.be", "bestaatniet.be", "x"]) {
  const r = await m.onRequestGet({ request: new Request("https://cyberdijk.eu/api/emailcheck?d=" + encodeURIComponent(d)), waitUntil: () => {} });
  console.log(d, r.status, (await r.text()).slice(0, 400));
}
