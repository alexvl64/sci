/**
 * CF Pages Function — Indice géo pour le sélecteur d'indicatif téléphonique.
 *
 * Renvoie le pays du visiteur (ISO-3166 alpha-2) détecté au niveau edge
 * Cloudflare (en-tête `CF-IPCountry` / `request.cf.country`). Aucune requête
 * IP externe, aucune clé, gratuit. Ne renvoie jamais d'erreur (défaut : "").
 *
 * Réponse : 200 { "country": "FR" }  (ou { "country": "" } si inconnu)
 */
export function onRequestGet({ request }) {
  const raw =
    request.headers.get("CF-IPCountry") ||
    (request.cf && request.cf.country) ||
    "";
  // Filtrer les valeurs non-pays : XX (inconnu), T1 (Tor), etc.
  const country = /^[A-Z]{2}$/.test(raw) && raw !== "XX" && raw !== "T1" ? raw : "";
  return Response.json(
    { country },
    { headers: { "Cache-Control": "no-store" } }
  );
}
