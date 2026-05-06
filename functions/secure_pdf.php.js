/**
 * Backward-compatibility redirect for old secure_pdf.php URLs.
 * /secure_pdf.php?file=FILENAME&h=HASH → /ressources/FILENAME?h=HASH
 * The /ressources/ Function handles hash verification.
 */
export async function onRequest({ request }) {
  const url = new URL(request.url);
  const file = url.searchParams.get('file') || '';
  const h = url.searchParams.get('h') || '';

  const basename = file.split('/').pop().split('\\').pop();
  if (!basename || !/\.pdf$/i.test(basename)) {
    return new Response('Not Found', { status: 404 });
  }

  const target = new URL(request.url);
  target.pathname = `/ressources/${basename}`;
  target.search = h ? `?h=${encodeURIComponent(h)}` : '';

  return Response.redirect(target.toString(), 301);
}
