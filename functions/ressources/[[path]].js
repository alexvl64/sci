/**
 * Cloudflare Pages Function — /ressources/** gate
 *
 * Replaces secure_pdf.php: intercepts all /ressources/** requests.
 * Protected PDFs (instructions_depot_*, deposit_*) require ?h=<sha256> query param.
 * Other files (contrats/) are served directly from the static asset store.
 *
 * Hash verification replicates PHP hash_equals() semantics using XOR to
 * avoid short-circuit evaluation (timing-safe for hex strings of fixed length).
 */

// SHA-256 hashes of protected PDFs — computed via: sha256sum <file>
// Re-run when a PDF is replaced and update the corresponding entry.
const PROTECTED_PDFS = {
  'instructions_depot_dynamic_trends.pdf':
    '6dd4b62679ebe03a60acca7d1d0ed853a52becfffa61515de03fb0958209d3f8',
  'instructions_depot_cryptovision.pdf':
    'bbe56dfa98a64d40b195d8ff548300e8fdf4ac8e66ab4b78b78c81621ee43e55',
  'deposit_instructions_quants_space.pdf':
    '660385624f4f305eab4b0b4a3a2f940d88816d06427efceff1bb70d3d40fe0a2',
};

function timingSafeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string') return false;
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return diff === 0;
}

export async function onRequest({ request, env, params }) {
  // params.path is an array of segments after /ressources/
  // e.g. ['instructions_depot_dynamic_trends.pdf'] or ['contrats', 'lpa_dt_signed.pdf']
  const segments = Array.isArray(params.path) ? params.path : [params.path || ''];
  const fullPath = segments.join('/');

  // Only protected files are at the root of /ressources/ (no subdirectory)
  const isProtected = segments.length === 1 && fullPath in PROTECTED_PDFS;

  if (!isProtected) {
    // Not a protected file — pass through to static asset store
    return env.ASSETS.fetch(request);
  }

  // Protected PDF: verify hash
  const url = new URL(request.url);
  const givenHash = url.searchParams.get('h') || '';
  const expectedHash = PROTECTED_PDFS[fullPath];

  if (!givenHash || !timingSafeEqual(givenHash, expectedHash)) {
    return new Response('Forbidden', {
      status: 403,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' },
    });
  }

  // Hash valid — fetch file from asset store (strip query string for lookup)
  const cleanUrl = new URL(request.url);
  cleanUrl.search = '';
  const assetResponse = await env.ASSETS.fetch(new Request(cleanUrl.toString(), request));

  if (!assetResponse.ok) {
    return new Response('Not Found', { status: 404 });
  }

  return new Response(assetResponse.body, {
    status: 200,
    headers: {
      'Content-Type': 'application/pdf',
      'Content-Disposition': `inline; filename="${fullPath}"`,
      'Cache-Control': 'no-store, no-cache, must-revalidate, private',
      'Pragma': 'no-cache',
      'X-Content-Type-Options': 'nosniff',
      'X-Robots-Tag': 'noindex, nofollow, noarchive',
    },
  });
}
