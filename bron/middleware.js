// Eén adres voor Google: www.cyberdijk.eu stuurt permanent door naar https://cyberdijk.eu
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www.cyberdijk.eu") {
    url.hostname = "cyberdijk.eu";
    url.protocol = "https:";
    url.port = "";
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
