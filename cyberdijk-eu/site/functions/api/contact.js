// Cloudflare Pages Function: ontvangt het contactformulier en de wachtlijst, mailt ze via Resend naar MELD_EMAIL
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
