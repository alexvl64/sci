/**
 * Cloudflare Pages Function — 410 Gone for the retired FR blog cluster
 *
 * The French blog cluster (/fr/blog/*) was removed on 2026-06-23 (the site
 * consolidated on the English blog). The 6 articles + index were indexed and
 * served impressions, so we return a genuine HTTP 410 (Gone) rather than a
 * 404 or a soft-404 301-to-homepage: 410 tells Google the URLs are permanently
 * removed with no equivalent, which de-indexes them fastest and cleanly.
 *
 * Scope: this catch-all owns the whole /fr/blog/* namespace (index + articles +
 * any trailing-slash variant). The FR homepage (/fr/) is unaffected — it is a
 * static asset outside this path. The root _middleware.js passes 410 through
 * untouched (410 is not in its ERROR_MAP), so no branded-error rewrite applies.
 */

const GONE_HTML = `<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Page supprimée — SparkCore</title>
<style>
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
       background:#0E1117;color:#F3F5F7;font-family:'Inter',system-ui,sans-serif;text-align:center;padding:24px;}
  .box{max-width:480px}
  h1{font-size:20px;font-weight:600;margin:0 0 12px}
  p{font-size:14px;line-height:1.6;color:#8FA3B8;margin:0 0 24px}
  a{color:#DBD1BC;text-decoration:none;border:1px solid rgba(219,209,188,.35);
    border-radius:4px;padding:10px 18px;font-size:14px;display:inline-block;margin:4px}
  a:hover{background:rgba(219,209,188,.12)}
</style>
</head>
<body>
  <div class="box">
    <h1>Cette page n'existe plus</h1>
    <p>Nos analyses sont désormais publiées en anglais. This page has been permanently removed; our insights are now published in English.</p>
    <a href="/blog/">Read the blog</a>
    <a href="/fr/">Accueil</a>
  </div>
</body>
</html>`;

export function onRequest() {
  return new Response(GONE_HTML, {
    status: 410,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Robots-Tag': 'noindex',
    },
  });
}
