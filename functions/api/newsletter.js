/**
 * CF Pages Function — Newsletter subscribe (replaces FormCarry + Make + SM)
 *
 * The newsletter email field POSTs here (multipart FormData). Validates the
 * honeypot + Cloudflare Turnstile token SERVER-SIDE, normalises the payload,
 * and forwards it server-to-server to the SparkCore Admin app API. The Admin
 * app owns every downstream action: store prospect, subscribe to the Mailjet
 * list (the job the SM used to do), confirmation email (tpl 6564289).
 * No team notification, no Telegram.
 *
 * Response contract is kept identical to the old FormCarry one:
 *   200 { status: "success" }  on success (and on honeypot trip — silent)
 *   4xx/5xx { status: "error" } otherwise
 *
 * Env vars: TURNSTILE_SECRET_KEY, ADMIN_API_BASE, ADMIN_API_SECRET
 * Spec / contract: MD/admin-app/PROSPECT-NEWSLETTER-PIPELINE.md
 */

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });

async function verifyTurnstile(token, secret, ip) {
  if (!token || !secret) return false;
  const body = new FormData();
  body.append('secret', secret);
  body.append('response', token);
  if (ip) body.append('remoteip', ip);
  try {
    const r = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      body,
    });
    const data = await r.json();
    return data.success === true;
  } catch {
    return false;
  }
}

export async function onRequestPost(context) {
  const { request, env } = context;

  let form;
  try {
    form = await request.formData();
  } catch {
    return json({ status: 'error', message: 'bad request' }, 400);
  }

  // Honeypot — accept silently, never forward.
  if ((form.get('website') || '').toString().trim() !== '') {
    return json({ status: 'success' });
  }

  // Cloudflare Turnstile (server-side siteverify)
  const token = (form.get('cf-turnstile-response') || '').toString();
  const ip = request.headers.get('CF-Connecting-IP') || '';
  if (!(await verifyTurnstile(token, env.TURNSTILE_SECRET_KEY, ip))) {
    return json({ status: 'error', message: 'captcha' }, 403);
  }

  // Canonical payload (see spec §2-B)
  const email = (form.get('email') || '').toString().trim();
  if (!email) return json({ status: 'error', message: 'missing email' }, 422);

  const payload = {
    type: 'newsletter',
    email,
    source_tracking: (form.get('source_tracking') || '').toString().trim(),
    lang: (form.get('lang') || 'en').toString().trim().toLowerCase() === 'fr' ? 'fr' : 'en',
  };

  if (!env.ADMIN_API_BASE || !env.ADMIN_API_SECRET) {
    return json({ status: 'error', message: 'not configured' }, 503);
  }

  try {
    const r = await fetch(`${env.ADMIN_API_BASE.replace(/\/$/, '')}/prospects/newsletter`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${env.ADMIN_API_SECRET}`,
      },
      body: JSON.stringify(payload),
    });
    if (!r.ok) return json({ status: 'error', message: 'upstream' }, 502);
    return json({ status: 'success' });
  } catch {
    return json({ status: 'error', message: 'upstream unreachable' }, 502);
  }
}
// Only POST is handled; CF Pages auto-returns 405 for other methods.
