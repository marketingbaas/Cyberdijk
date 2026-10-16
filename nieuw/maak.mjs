const vals = {
  "voorbeeld.be|TXT": ['"v=spf1 include:_spf.google.com ~all"'], "_dmarc.voorbeeld.be|TXT": ['"v=DMARC1; p=none"'],
  "voorbeeld.be|MX": ["10 aspmx.l.google.com.", "20 alt1.aspmx.l.google.com."],
};
globalThis.caches = { default: { match: async () => null, put: async () => {} } };
globalThis.fetch = async (u) => { u = String(u);
  if (u.startsWith("https://cloudflare-dns.com")) { const q = new URL(u), k = q.searchParams.get("name") + "|" + q.searchParams.get("type");
    const t = q.searchParams.get("type") === "MX" ? 15 : 16; return new Response(JSON.stringify({ Status: 0, Answer: (vals[k] || []).map((d) => ({ type: t, data: d })) })); }
  const r = new Response("ok"); Object.defineProperty(r, "url", { value: u }); return r; };
const m = await import("./emailcheck_functie.js");
const r = await m.onRequestGet({ request: new Request("https://cyberdijk.eu/api/emailcheck?d=voorbeeld.be"), waitUntil: () => {} });
process.stdout.write(await r.text());
