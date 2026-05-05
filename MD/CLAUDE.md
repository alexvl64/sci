# CLAUDE.md — SparkCore Investment Website

Context and configuration reference for Claude Code sessions on the `alexvl64/sci` repository.

---

## Project overview

- **Site:** sparkcore.fund — static HTML/CSS/JS, bilingual EN/FR
- **Hosting:** Apache/OVH, behind Cloudflare CDN
- **Stack:** Tailwind CSS (local build, `tailwind.min.css?v=1.0`), custom CSS (`style.css?v=1.4`), vanilla JS
- **Entity:** SparkCore.investment OÜ — regulated AIFM (small fund manager), supervised by Finantsinspektsioon (Estonia)
- **Ads:** aucune publicité payante (Google Ads, Meta, LinkedIn, etc.) — site institutionnel YMYL réservé aux investisseurs professionnels

---

## Tracking & Analytics

> Site institutionnel sans pub. Tracking uniquement pour comprendre le comportement (sessions, sources organiques, scroll, clics formulaires/CTA). **Pas de Google Tag Manager** — overkill pour 1 seul tag, pas d'équipe marketing à autoguider.

### Stack tracking

| Élément | Valeur | Localisation |
|---|---|---|
| **GA4 Property** | `530665322` ("SparkCore.investment OÜ") | account `Sparkcore` (`389436882`) |
| **GA4 Measurement ID** | `G-J80NVPQNVZ` | hardcodé `assets/js/analytics.js:3` |
| **Loader** | `gtag.js` direct (pas de GTM container) | `<script defer src="/assets/js/analytics.js">` injecté sur toutes les pages |
| **Consent Mode** | v2, denied par défaut | banner cookie FR/EN auto-localisé via `<html lang>` |
| **Anonymisation IP** | `anonymize_ip: true` | configuré dans le `gtag('config', ...)` |
| **localStorage key** | `sc_cookie_consent_v1` | persiste le choix accept/decline |

### Events tracked

GA4 enhanced measurement actif → events automatiques sans code custom :
- `page_view`, `session_start`, `first_visit`, `user_engagement`
- `scroll` (90% page)
- `click` outbound (FormCarry, app.cal.eu, LinkedIn, jsdelivr, etc.)
- `file_download` (clics PDFs `/ressources/contrats/*.pdf`)
- `form_start` / `form_submit` (sidebar + newsletter FormCarry)

Pas d'events custom (`gtag('event', ...)`) pour l'instant. Si besoin d'instrumenter un CTA spécifique (ex. "Book a discovery call"), ajouter un push manuel dans `assets/js/index.js` puis marquer l'event en **Key event** dans GA4 Admin.

### APIs Google connectées (config `~/.config/claude-seo/projects/sci.json`)

| API | Statut | Notes |
|---|---|---|
| GA4 Data API | ✅ | property `530665322` |
| GSC Search Analytics | ✅ | `sc-domain:sparkcore.fund` |
| GSC URL Inspection | ✅ | |
| GSC Indexing API | ✅ | |
| PageSpeed Insights | ⚠️ | bug script `audit_details` côté skill (credentials OK) |
| CrUX history | ⚠️ | trafic Chrome insuffisant — normal pour site récent |
| Google Ads | ❌ | non applicable (pas d'ads) |

Service Account partagé : `claude-seo@sparkcore-projet-1733486598578.iam.gserviceaccount.com` (Viewer sur GA4, Full sur GSC).

> ⚠️ **Note historique 2026-05-02** : la config sci pointait par erreur vers `properties/529476067` (orphelin, 0 row). Corrigé vers `530665322` après triangulation : repo `analytics.js:3` + `curl https://sparkcore.fund/assets/js/analytics.js` + GA4 admin `dataStreams.list`. Toujours croiser ces 3 sources avant de déclarer le tracking en panne.

### Vérifier le tracking depuis le navigateur

1. **DevTools Network** : F12 → filtre `collect` → recharger → requête `https://www.google-analytics.com/g/collect?v=2&tid=G-J80NVPQNVZ&...`
2. **Console JS** : `window.dataLayer.find(x => x[0] === 'config')` → `['config', 'G-J80NVPQNVZ', { anonymize_ip: true }]`
3. **GA4 Realtime** : property `SparkCore.investment OÜ` → Reports → Realtime → +1 user dans les 30s

### Bots & exclusions

- Tracking ne tourne **pas en localhost** (`localhost`/`127.0.0.1` skipped en début de `analytics.js`)
- Pas d'exclusion bot custom dans GA4 (filtres bot par défaut activés au niveau property)
- Auto-redirect `/` ↔ `/fr/` via `lang-redirect-{en,fr}.js` skip une longue liste de bots (Googlebot, ClaudeBot, GPTBot, PerplexityBot, etc.) — ces requêtes ne sont jamais redirigées

### Bing Webmaster Tools (mis en place 2026-05-05)

| Élément | Valeur |
|---|---|
| **Compte Bing WMT** | `sparkcore.public.df59f6@gmail.com` (Owner) |
| **Vérification** | `BingSiteAuth.xml` à la racine, GUID `0739094849505C87C0C6BCFDCA094258` |
| **API key** | stockée dans `~/.config/claude-seo/backlinks-projects/sci.json` (chmod 600) |
| **Sitemap soumis** | `https://sparkcore.fund/sitemap.xml` (27 URLs, last crawl ~ daily) |
| **Sitemap obsolète** | `https://www.sparkcore.fund/sitemap.xml` (10 URLs, à supprimer côté UI Bing — cosmétique) |

Le skill `seo-backlinks` lit la config via le symlink `~/.config/claude-seo/backlinks-api.json` qui suit le projet actif (switch via `~/.config/claude-seo/switch.sh sci`). **Connexion à GSC depuis Bing WMT NON nécessaire** — le site est déjà vérifié et indexé indépendamment.

### IndexNow (mis en place 2026-05-05)

Protocole de ping pour notifier Bing/Yandex/Seznam/Yep/Naver des URLs nouvelles ou modifiées (indépendant de Bing WMT API).

| Élément | Valeur |
|---|---|
| **Clé IndexNow** | `27994a06b868d24820429dc36c1bafee` |
| **Fichier servi** | `https://sparkcore.fund/27994a06b868d24820429dc36c1bafee.txt` (HTTP 200, `text/plain`, 32 octets) |
| **Script** | `scripts/ops/indexnow_ping.py` (stdlib only, pas de dépendances) |
| **Log** | `logs/indexnow.log` (gitignored, rotation 30j auto) |
| **Premier ping live** | 2026-05-05 — HTTP 202 Accepted (key validation pending, comportement normal) |

Usage :
```bash
# Après publication d'un nouvel article :
python3 scripts/ops/indexnow_ping.py \
  https://sparkcore.fund/blog/new-slug \
  https://sparkcore.fund/fr/blog/new-slug

# Ré-ping global depuis sitemap.xml :
python3 scripts/ops/indexnow_ping.py --all

# Inspection sans envoi :
python3 scripts/ops/indexnow_ping.py --all --dry-run
```

> **Ne PAS partager la clé** entre projets — chaque domaine doit avoir sa propre clé. Celle de dsungkur (`e3fe89c6...a2bd`) est isolée et ne doit jamais apparaître ici.

### Microsoft Clarity — décision 2026-05-05 : non installé

Décision argumentée de **ne PAS installer Clarity** sur sparkcore.fund :
- **Volume insuffisant** : 2 sessions / 28j en GA4 → heatmaps et session replays ont besoin de 100+ sessions/mois pour produire des insights non-anecdotiques
- **YMYL financier régulé** (Finantsinspektsioon) : ajouter Microsoft comme sous-traitant data demande update DPA + cookie policy + privacy-policy.html
- **Audience HNW institutionnelle** : session replay capture des comportements sensibles sur le formulaire discovery-call
- **Stack minimaliste par design** (pas de GTM) : ajouter Clarity contredirait cette philosophie

À reconsidérer **uniquement si** : trafic > 100 sessions/mois pendant 3 mois consécutifs ET point de friction CRO identifié ET bandwidth pour mettre à jour le compliance legal.

---

## Git workflow

- Always create a **new branch from `main`** for each task
- Branch naming: `claude/<short-description>`
- Commit, push, create PR, then merge (squash)
- Never push directly to `main`

---

## Files intentionally excluded from git

The following files are gitignored and must never be committed or pushed:

| File | Reason |
|---|---|
| `node_modules/` | Build artifacts |
| `request_limit.db` | Runtime data |
| `form_config.php` | Contains secrets — never commit |
| `.env`, `*.env`, `*.key`, `*.pem` | Sensitive config patterns |

> The `MD/` directory and `.htaccess` ARE tracked in git (since 2026-04-15) and deployed automatically via GitHub → server. `.htaccess` blocks HTTP access to `/MD/` so the markdown reference files are versioned but never web-accessible.

---

## Security architecture

### Backend PHP — état actuel (post audit 2026-04-15)

Un seul fichier PHP en production : **`secure_pdf.php`** (sert les PDFs d'instructions de dépôt avec vérification SHA-256). Tout le reste a été supprimé comme code mort.

| Fichier | État | Pourquoi |
|---|---|---|
| `proxy.php` | ❌ Supprimé | Code mort — jamais référencé en JS/HTML, le formulaire de contact appelle FormCarry directement |
| `form_config.php` | ❌ Supprimé | Code mort — jamais inclus, la clé Turnstile est gérée côté FormCarry |
| `secure_pdf.php` | ✅ Conservé + hardenisé | Sert les PDFs avec hash SHA-256 (utilise `hash_equals()` contre timing attacks) |

### Formulaires de contact

Les deux formulaires (sidebar + newsletter) appellent **FormCarry directement** depuis le JS, sans backend PHP intermédiaire :
- Sidebar : `fetch("https://formcarry.com/s/oHdZL-AalnM", ...)` (`assets/js/index.js:233`)
- Newsletter : `fetch("https://formcarry.com/s/_xD89dyxiXb", ...)` (`assets/js/index.js:380`)

Le token Turnstile (`cf-turnstile-response`) est joint au FormData. La validation server-side est faite par FormCarry (clé secrète configurée dans leur dashboard).

### Headers de sécurité actifs (via `.htaccess`)

| Header | Valeur | But |
|---|---|---|
| `X-Frame-Options` | `SAMEORIGIN` | Anti-clickjacking |
| `X-Content-Type-Options` | `nosniff` | Anti MIME-sniffing |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limite la fuite d'URL referrer |
| `Permissions-Policy` | `geolocation=(), microphone=(), camera=()` | Coupe l'accès aux APIs sensibles |
| `X-Powered-By` | *unset* | Masque la version PHP |
| `X-Robots-Tag` (sur PDFs) | `noindex, nofollow, noarchive` | Empêche l'indexation des PDFs |

### `secure_pdf.php` — sécurité

- Comparaison de hash via `hash_equals()` (pas `!==`) → résistant aux timing attacks
- Headers ajoutés : `Cache-Control: no-store`, `Pragma: no-cache`, `X-Content-Type-Options: nosniff`, `X-Robots-Tag: noindex`
- `Content-Disposition: inline; filename="..."` (consultation navigateur, pas téléchargement forcé)

### PDF blocking — règles `.htaccess`

- Tout fichier PDF dont le nom commence par `instructions_depot_*` (FR) ou `deposit_*` (EN) est bloqué en accès HTTP direct → forcé via `secure_pdf.php`
- Les contrats `/ressources/contrats/*.pdf` restent accessibles via URL directe (partage par email uniquement, conforme au modèle de menace)
- Tous les PDFs ont `X-Robots-Tag: noindex` → jamais indexés par Google/Bing/AI crawlers

### Décisions de sécurité explicites (assumées, non corrigées)

| Item | Audit | Décision | Justification |
|---|---|---|---|
| **SRI sur scripts CDN** (ApexCharts, Toastify) | HIGH (65/100) | ❌ Skipped | Coût maintenance perpétuelle (regénération hash à chaque update) > bénéfice (jsdelivr jamais compromis en 10 ans). À reconsidérer si on commence à traiter des paiements ou auth. |
| **CSP `'unsafe-inline'`** | HIGH (60/100) | ✅ Conservé | Nécessaire pour le site statique sans Workers. À retirer si migration vers Cloudflare Workers. |
| **Contrats `/ressources/contrats/` accessibles par URL directe** | CRITICAL (90/100) | ✅ Conservé | Modèle de menace assumé : URLs partagées uniquement par email, documents non-critiques, `X-Robots-Tag: noindex` empêche l'indexation. |

### Actions de remediation : aucune en attente

L'audit recommandait initialement :
- ~~Rotate la clé Turnstile~~
- ~~Mettre à jour la nouvelle clé dans FormCarry~~
- ~~Purger l'historique git de `form_config.php`~~

**Décision : non requis.** Le repo `alexvl64/sci` est **privé** sur GitHub. La clé Turnstile présente dans l'historique git de `form_config.php` n'est accessible qu'aux collaborateurs autorisés du repo. Combiné avec le fait que :
- La clé permet uniquement la *validation* de tokens (pas la génération de faux tokens)
- `form_config.php` n'a jamais été inclus en prod (code mort)
- FormCarry gère sa propre validation Turnstile avec sa propre clé

→ Le risque résiduel est négligeable. Aucune action requise.

---

## Apache / OVH server configuration (.htaccess)

The `.htaccess` is **tracked in git** (since 2026-04-15) and deployed automatically via GitHub → OVH server. No manual sync needed.

Current configuration:

```apache
# ============================================================
# .htaccess — sparkcore.fund
# ============================================================

Options -Indexes

# ----------------------------------------------------------------
# Moteur de réécriture
# ----------------------------------------------------------------
RewriteEngine On

# ----------------------------------------------------------------
# HTTP → HTTPS + www → non-www
# COMMENTÉ pour les tests sur le domaine temporaire OVH
# À décommenter avant la bascule DNS vers sparkcore.fund
# ----------------------------------------------------------------
 RewriteCond %{HTTPS} off [OR]
 RewriteCond %{HTTP_HOST} ^www\. [NC]
 RewriteRule ^ https://sparkcore.fund%{REQUEST_URI} [R=301,L]

# ----------------------------------------------------------------
# Headers de sécurité
# ----------------------------------------------------------------

<IfModule mod_headers.c>
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
    # Suppression de l'info de version PHP exposée par défaut
    Header always unset X-Powered-By
    Header unset X-Powered-By
</IfModule>

# ----------------------------------------------------------------
# Cache des assets statiques (équivalent Nginx)
# ----------------------------------------------------------------
<IfModule mod_headers.c>
    <FilesMatch "\.(css|js|webp|png|svg|ico|woff2?|ttf|eot|jpg|jpeg|gif)$">
        Header set Cache-Control "public, max-age=31536000, immutable"
    </FilesMatch>
    <FilesMatch "\.(json|xml|txt|html)$">
        Header set Cache-Control "public, max-age=3600"
    </FilesMatch>
</IfModule>

<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css                      "access plus 1 year"
    ExpiresByType application/javascript        "access plus 1 year"
    ExpiresByType image/webp                    "access plus 1 year"
    ExpiresByType image/png                     "access plus 1 year"
    ExpiresByType image/svg+xml                 "access plus 1 year"
    ExpiresByType image/x-icon                  "access plus 1 year"
    ExpiresByType font/woff2                    "access plus 1 year"
    ExpiresByType font/woff                     "access plus 1 year"
    ExpiresByType font/ttf                      "access plus 1 year"
    ExpiresByType application/vnd.ms-fontobject "access plus 1 year"
    ExpiresByType image/jpeg                    "access plus 1 year"
    ExpiresByType image/gif                     "access plus 1 year"
    ExpiresByType application/json              "access plus 1 year"
    ExpiresByType application/xml               "access plus 1 year"
    ExpiresByType text/xml                      "access plus 1 year"
    ExpiresByType text/plain                    "access plus 1 year"
    ExpiresByType text/html                     "access plus 1 hour"
</IfModule>

# ----------------------------------------------------------------
# Blocage des fichiers cachés (.git, .env, etc.)
# ----------------------------------------------------------------
RewriteCond %{REQUEST_URI} (^|/)\. [NC]
RewriteRule ^ - [R=404,L]
RewriteRule ^\..* - [R=404,L]

# ----------------------------------------------------------------
# Blocage du répertoire MD/ (référence interne — jamais accessible en HTTP)
# ----------------------------------------------------------------
RewriteRule ^MD(/|$) - [F,L]

# ----------------------------------------------------------------
# Blocage des fichiers PHP (inaccessible en statique)
# Important : OVH n'autorise pas toujours `<FilesMatch>` en `.htaccess`.
# On bloque donc aussi via `mod_rewrite` pour fiabiliser.
# Exception : secure_pdf.php est accessible (sert les PDFs avec vérification hash)
# ----------------------------------------------------------------
# Règle 1 : bloque si URI se termine par .php ET n'est pas secure_pdf.php
RewriteCond %{REQUEST_URI} \.php$ [NC]
RewriteCond %{REQUEST_URI} !^/secure_pdf\.php$ [NC]
RewriteRule ^ - [F,L]

# Règle 2 : même chose — RewriteCond ne s'applique qu'à la règle qui suit immédiatement
RewriteCond %{REQUEST_URI} !^/secure_pdf\.php$ [NC]
RewriteRule ^.*\.php$ - [F,L]

# ----------------------------------------------------------------
# PDFs : pas d'indexation par les moteurs (défense en profondeur vs robots.txt)
# ----------------------------------------------------------------
<IfModule mod_headers.c>
    <FilesMatch "\.pdf$">
        Header set X-Robots-Tag "noindex, nofollow, noarchive"
    </FilesMatch>
</IfModule>

# ----------------------------------------------------------------
# Blocage des instructions de dépôt (accès direct interdit — doivent passer par secure_pdf.php)
# Couvre versions FR (instructions_depot_*) et EN (deposit_*)
# ----------------------------------------------------------------
RewriteCond %{REQUEST_URI} ^/ressources/(instructions_depot|deposit).*\.pdf$ [NC]
RewriteRule ^ - [F,L]
RewriteRule ^ressources/(instructions_depot|deposit).*\.pdf$ - [F,L]

# ----------------------------------------------------------------
# Equivalent Nginx try_files $uri $uri/ $uri.html =404;
# ----------------------------------------------------------------
DirectoryIndex index.html

# 1) Si un fichier existe, Apache le sert directement
RewriteCond %{REQUEST_FILENAME} -f
RewriteRule ^ - [L]

# 2) Si c'est un dossier et que l'URL finit déjà par '/', Apache le sert directement
RewriteCond %{REQUEST_FILENAME} -d
RewriteCond %{REQUEST_URI} /$
RewriteRule ^ - [L]

# 3) Si c'est un dossier mais que l'URL n'a pas de '/', on ajoute un '/' en réécriture interne
RewriteCond %{REQUEST_FILENAME} -d
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(.+)$ $1/ [L]

# 2) Sinon, si un fichier *.html existe, on le sert
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L]

# 3) Sinon 404
RewriteRule ^ - [R=404,L]

# ----------------------------------------------------------------
# Pages d'erreur personnalisées
# ----------------------------------------------------------------
ErrorDocument 403 /403.html
ErrorDocument 404 /404.html
ErrorDocument 500 /500.html
ErrorDocument 502 /500.html
ErrorDocument 503 /500.html
ErrorDocument 504 /500.html
```

---

## Cloudflare configuration

All settings below are live on the `sparkcore.fund` zone.

### Caching → Configuration

| Parameter | Value |
|---|---|
| Browser Cache TTL | **1 year** |

> Set to 1 year. Cloudflare instructs browsers to cache static assets (CSS, JS, images, fonts) for 1 year. HTML is not cached by Cloudflare on the free plan by default, so pages remain always fresh.

### SSL/TLS → Edge Certificates — HSTS

| Parameter | Value |
|---|---|
| Enable HSTS | ✅ |
| Max-age | 12 months (31 536 000 s) |
| Include Subdomains | ✅ |
| No-sniff | ✅ |
| Preload | ❌ deferred — enable after several weeks of confirmed stability |

### Rules → Transform Rules → Modify Response Header

**Rule name:** `Add Content-Security-Policy`
**Condition:** All incoming requests
**Header:** `Content-Security-Policy`
**Value:**
```
default-src 'self'; script-src 'self' https://cdn.jsdelivr.net https://challenges.cloudflare.com https://www.googletagmanager.com https://rum.cronitor.io https://static.cloudflareinsights.com https://app.cal.eu 'unsafe-inline'; style-src 'self' https://fonts.googleapis.com https://cdn.jsdelivr.net https://app.cal.eu 'unsafe-inline'; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://formcarry.com https://docs.google.com https://www.google-analytics.com https://analytics.google.com https://rum.cronitor.io https://a.nel.cloudflare.com https://cdn.jsdelivr.net https://app.cal.eu; frame-src https://challenges.cloudflare.com https://app.cal.eu; report-uri /csp-report
```

> Note: `'unsafe-inline'` is intentional for a static site with no user authentication. Replace with nonces only if moving to Cloudflare Workers.

### Rules → Redirect Rules

**Rule name:** `Remove trailing slash — blog articles`
**Type:** Wildcard pattern

| Field | Value |
|---|---|
| Source URL | `https://sparkcore.fund/blog/*/` |
| Target URL | `https://sparkcore.fund/blog/$1` |
| Status code | 301 |

### Network

| Feature | Status |
|---|---|
| HTTP/3 (QUIC) | Not available — free plan only |
| HTTP/2 | ✅ enabled by Cloudflare automatically |

---

## Internationalization (EN / FR)

The site is bilingual with **English as the base language** and a dedicated `/fr/` page for SEO. Both pages are statically pre-rendered in their own language — do not assume the FR body is generated by JS.

### Architecture

| File | Role |
|---|---|
| `/index.html` | English homepage — full body in English |
| `/fr/index.html` | French homepage — **full body pre-rendered in French**, with French `<head>`, French JSON-LD `FinancialService`, and `data-i18n` attributes still present (so the JS layer is a no-op in steady state) |
| `assets/js/translations.js` | Translation dictionary (EN+FR) and `currentLang` detection |
| `assets/js/index.js` | `applyTranslations()` and `setLang()` — runs on DOMContentLoaded, swaps text via `data-i18n` |
| `assets/js/lang-redirect-en.js` | Loaded on `/` only — auto-redirects FR browsers to `/fr/` on first visit |
| `assets/js/lang-redirect-fr.js` | Loaded on `/fr/` only — sends explicit-EN users back to `/` |
| `sitemap.xml` | Declares `xhtml:link hreflang` alternates (`en`, `fr`, `x-default`) for `/` and `/fr/` |

### Language detection rules (`translations.js`)

`currentLang` is computed in this order — **URL path first, always**:

1. If `location.pathname` starts with `/fr` → `fr`
2. Else if `localStorage.sc_lang` is `'en'` or `'fr'` → that value
3. Else if `navigator.language` starts with `fr` → `fr`
4. Else → `en`

> ⚠️ This URL-priority is **critical**: it guarantees Googlebot (whose `navigator.language` is `en`) renders `/fr/` in French. Do not reorder these rules.

### Auto-redirect rules (`lang-redirect-{en,fr}.js`)

Both scripts:
- **Skip bots** via a wide regex: `bot|crawl|spider|slurp|…|gptbot|claudebot|perplexitybot|ccbot|google-extended|oai-searchbot|bytespider|amazonbot|headlesschrome|…`
- **Guard with `sessionStorage['sc_lang_redirected']`** — only redirect once per tab so the Back button and manual EN↔FR navigation work
- **Never run on blog articles** (English only)

The auto-redirect from `/` → `/fr/` for FR-language browsers is intentional and must be preserved.

### When editing FR content

- **Edit `/fr/index.html` directly** — the body is already in French. Don't rely on `translations.js` to translate it at runtime.
- If you add a new section to `/index.html`, you must also add the French version to `/fr/index.html` manually.
- The FR JSON-LD (`FinancialService` block in `/fr/index.html`) must mirror the EN one with `url: https://sparkcore.fund/fr/` and a French `description`.
- The active `lang-btn` is FR on `/fr/` and EN on `/` — set via the `active` class on the `<button>`.
- No French blog. Blog articles are EN-only with `"inLanguage": "en"`.

### Common pitfalls

- ❌ Reverting `/fr/index.html` to a copy of `/index.html` with `data-i18n` placeholders only — this breaks the snippet Google captures
- ❌ Removing the URL-first check in `translations.js` `currentLang` IIFE
- ❌ Narrowing the bot regex in `lang-redirect-{en,fr}.js` (Googlebot/AI crawlers must never be redirected)
- ❌ Forgetting to update `sitemap.xml` `lastmod` after meaningful FR/EN content changes

---

## Blog article conventions

- Schema: `"@type": "BlogPosting"` (not `Article`)
- Publisher logo: `https://sparkcore.fund/assets/images/png/favicon-192x192.png`
- `"inLanguage": "en"` on all EN articles
- Footer year script: `<script src="/assets/js/set-year.js"></script>`
- External link class: `class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200" target="_blank" rel="noopener noreferrer"`
- Internal link class: `class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200"`
- Author: Alexandre VINAL — `https://www.linkedin.com/in/alexandrevinal/`

---

# Instructions pour Claude Code — SparkCore / site statique

## Conversion Markdown → HTML (skill md-to-html)

### Rôle
Convertir un article Markdown en page HTML statique cohérente avec le site existant. La structure, les classes CSS, le `<head>`, la nav, le footer et le disclaimer doivent être copiés à l'identique depuis un article HTML de référence du repo. Seuls le contenu, le titre, la description, le canonical, les OG tags et le JSON-LD changent.

### Règle fondamentale : jamais de sortie HTML complète en un seul bloc
Toujours procéder par étapes successives avec des remplacements ciblés (`str_replace_editor` ou `write_file` partiel). Cela évite de saturer le contexte et permet de valider à chaque étape.

---

### Workflow obligatoire

**0. Lecture du template de référence**
Avant toute génération, lire **obligatoirement** `blog/do-crypto-fund-managers-need-mica-casp-license.html` comme article de référence (ou `blog/bitcoin-outperformance-strategy-fund.html` en secours).
Extraire et mémoriser :
- Le `<head>` complet (meta, CSS, fonts, scripts)
- La structure `<nav>`
- Les classes CSS des conteneurs d'article (`font-inter`, `font-funnel-display`, etc.)
- Le footer et le disclaimer

> ⚠️ **Ne jamais écrire le footer de mémoire.** Copier littéralement le bloc `<footer>…</footer>` depuis l'article de référence. Le footer correct contient exactement : logo (sans LinkedIn), `@<span id="year">`, séparateur `bg-paleBlue`, [FSA link] + [Licence: EFIU] dans le même `flex gap-3` **sans séparateur `&mdash;` entre eux**, puis Reg. No./LEI, Disclaimer, Privacy Policy. Pas de LinkedIn, pas de Terms of Use.

**Étape A — Squelette**
Créer `blog/<slug>.html` avec :
- `<!DOCTYPE html>` → `</head>` (copié du template)
- `<nav>` (copié du template)
- `<article>` avec titre, meta-ligne, puis **obligatoirement dans cet ordre** :
  1. Paragraphes d'introduction
  2. **Image hero** : `<figure class="mt-6 mb-12"><img src="..." alt="..." class="w-full rounded-lg object-cover max-h-[420px]" loading="lazy" width="1260" height="750" decoding="async" /></figure>`
  3. **Bloc Key Takeaways** : `<div class="border-l-4 border-steelBlue bg-[#F9FAFB] pl-5 py-4 pr-4 mb-8 rounded-r-lg"><p class="font-inter text-sm font-semibold text-darkGray mb-3">Key takeaways</p><ul class="font-inter text-base text-mediumGray leading-160 list-disc pl-5 space-y-2">...</ul></div>`
  4. Marqueurs de contenu :
     - `<!-- BODY_PART_1 -->`
     - `<!-- BODY_PART_2 -->`
     - `<!-- BODY_PART_3 -->`
- Footer + disclaimer (copiés du template)

> **Image hero** : utiliser l'URL de `coverImage` du frontmatter MD si disponible, sinon une URL Unsplash pertinente (`https://images.unsplash.com/photo-XXXX?w=1260&h=750&fit=crop&q=80`). Ne jamais omettre l'image hero.
>
> **Key Takeaways** : reprendre les bullets du bloc `> **Key Takeaways**` du MD source. Ne jamais omettre ce bloc.

Valider que le fichier s'ouvre avant de continuer.

**Étape B — Remplacement BODY_PART_1**
Remplacer `<!-- BODY_PART_1 -->` par le HTML de la première section (intro, H2/H3, paragraphes, tableaux, listes). Ne pas toucher au head ni au footer.

**Étape C — Remplacement BODY_PART_2**
Idem pour `<!-- BODY_PART_2 -->` (sections suivantes, SVG, tableaux longs).

**Étape D — Remplacement BODY_PART_3**
Idem pour `<!-- BODY_PART_3 -->` (FAQ, conclusion, sources).

**Validation finale**
```bash
grep -n "BODY_PART" blog/<slug>.html
# Doit retourner 0 ligne
```

---

### Règles de conversion du contenu

**Classes CSS**
Reprendre exactement les classes des autres articles du repo. Ne pas inventer de classes.

**Placeholders `[INTERNAL-LINK: …]`**
- Ne jamais laisser le texte brut dans le HTML final.
- Rechercher l'URL réelle : `grep -r "keyword" blog/`
- Remplacer par `<a href="/blog/slug.html">texte ancre</a>`

**SVG sur fond sombre**
Encapsuler dans :
```html
<div class="rounded-lg bg-[#0f172a] p-4">
  <!-- SVG ici -->
</div>
```

**Métadonnées à mettre à jour**
- `<title>`, `<meta name="description">`, `<link rel="canonical">`
- OG tags : `og:title`, `og:description`, `og:url`, `og:image`
- JSON-LD `Article` : `headline`, `description`, `url`, `datePublished`, `dateModified`, `author`

---

### Ce qu'il ne faut pas faire
- ❌ Sortir l'intégralité du HTML en une seule réponse
- ❌ Réécrire le markdown en prose libre
- ❌ Inventer des classes CSS absentes du repo
- ❌ Laisser des placeholders `[INTERNAL-LINK: …]` non résolus
- ❌ Modifier le head, la nav ou le footer entre les étapes B/C/D
- ❌ Omettre l'image hero (`<figure class="mt-6 mb-12">`)
- ❌ Omettre le bloc Key Takeaways (`border-l-4 border-steelBlue bg-[#F9FAFB]`)
- ❌ Créer des SVGs avec fond clair (`fill="#f9fafb"`) — toujours fond sombre (`fill="#0f1117"`) dans `<figure class="... rounded-lg bg-[#0f172a] p-4 sm:p-6 overflow-x-auto">`
- ❌ Écrire le footer de mémoire — toujours copier depuis `blog/do-crypto-fund-managers-need-mica-casp-license.html`
- ❌ Ajouter LinkedIn, Terms of Use, ou des séparateurs `&mdash;` dans le footer

---

### Livrable attendu
`blog/<slug>.html` cohérent avec le site, sans placeholders résiduels, avec métadonnées SEO complètes, produit en 4 étapes max.
