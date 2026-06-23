/**
 * CF Pages Function — Contact form intake (replaces FormCarry + Make + SM)
 *
 * The sidebar contact form POSTs here (multipart FormData). This function
 * validates the honeypot + Cloudflare Turnstile token SERVER-SIDE, normalises
 * the payload, and forwards it server-to-server to the SparkCore Admin app API
 * (authenticated with a shared secret). The Admin app owns every downstream
 * action: store prospect, Telegram, Mailjet emails (tpl 6562257 + 7461276),
 * Mailjet list subscription.
 *
 * Response contract is kept identical to the old FormCarry one so the existing
 * JS success handler (assets/js/index.js) is unchanged:
 *   200 { status: "success" }  on success (and on honeypot trip — silent)
 *   4xx/5xx { status: "error" } otherwise
 *
 * Env vars (CF Pages → Settings → Environment variables):
 *   TURNSTILE_SECRET_KEY  — Cloudflare Turnstile secret (siteverify)
 *   ADMIN_API_BASE        — base URL of the Admin app API (no trailing slash needed)
 *   ADMIN_API_SECRET      — shared secret for the server-to-server call
 *
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

  // Honeypot — accept silently (do not tip off bots), never forward.
  if ((form.get('website') || '').toString().trim() !== '') {
    return json({ status: 'success' });
  }

  // Cloudflare Turnstile (server-side siteverify)
  const token = (form.get('cf-turnstile-response') || '').toString();
  const ip = request.headers.get('CF-Connecting-IP') || '';
  if (!(await verifyTurnstile(token, env.TURNSTILE_SECRET_KEY, ip))) {
    return json({ status: 'error', message: 'captcha' }, 403);
  }

  // Canonical payload (see spec §2-A)
  const payload = {
    type: 'contact',
    prenom: (form.get('prenom') || '').toString().trim(),
    nom: (form.get('nom') || '').toString().trim(),
    telephone: (form.get('telephone') || '').toString().trim(),
    email: (form.get('email') || '').toString().trim(),
    source: (form.get('source') || '').toString().trim(),
    source_tracking: (form.get('source_tracking') || '').toString().trim(),
    lang: (form.get('lang') || 'en').toString().trim().toLowerCase() === 'fr' ? 'fr' : 'en',
  };

  if (!payload.email || !payload.prenom || !payload.nom) {
    return json({ status: 'error', message: 'missing fields' }, 422);
  }

  if (!env.ADMIN_API_BASE || !env.ADMIN_API_SECRET) {
    return json({ status: 'error', message: 'not configured' }, 503);
  }

  try {
    const r = await fetch(`${env.ADMIN_API_BASE.replace(/\/$/, '')}/prospects/contact`, {
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
