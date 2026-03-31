# CLAUDE.md — SparkCore Investment Website

Context and configuration reference for Claude Code sessions on the `alexvl64/sci` repository.

---

## Project overview

- **Site:** sparkcore.fund — static HTML/CSS/JS, bilingual EN/FR
- **Hosting:** Apache/OVH, behind Cloudflare CDN
- **Stack:** Tailwind CSS (local build, `tailwind.min.css?v=1.0`), custom CSS (`style.css?v=1.4`), vanilla JS
- **Entity:** SparkCore Investment OÜ — regulated AIFM (small fund manager), supervised by Finantsinspektsioon (Estonia)

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
| `.htaccess` | Managed locally — not deployed via git |
| `CLAUDE.md` | Local reference only |
| `MD/` | Source markdown files — not deployed |

---

## Apache / OVH server configuration (.htaccess)

The `.htaccess` is **gitignored** — it lives only on the local machine and on the OVH server (managed manually). Do not commit it.

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
# Blocage des fichiers PHP (inaccessible en statique)
# Important : OVH n'autorise pas toujours `<FilesMatch>` en `.htaccess`.
# On bloque donc aussi via `mod_rewrite` pour fiabiliser.
# ----------------------------------------------------------------
RewriteCond %{REQUEST_URI} \.php$ [NC]
RewriteRule ^ - [F,L]
RewriteRule ^.*\.php$ - [F,L]

# ----------------------------------------------------------------
# Blocage des PDF sensibles (accès direct interdit)
# ----------------------------------------------------------------
RewriteCond %{REQUEST_URI} ^/ressources/instruction_depot.*\.pdf$ [NC]
RewriteRule ^ - [F,L]
RewriteRule ^ressources/instruction_depot.*\.pdf$ - [F,L]
RewriteRule ^resources/instruction_depot.*\.pdf$ - [F,L]

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
default-src 'self'; script-src 'self' https://cdn.jsdelivr.net https://www.google.com https://www.gstatic.com https://www.googletagmanager.com https://rum.cronitor.io 'unsafe-inline'; style-src 'self' https://fonts.googleapis.com https://cdn.jsdelivr.net 'unsafe-inline'; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://formcarry.com https://docs.google.com https://www.google-analytics.com https://analytics.google.com https://rum.cronitor.io https://a.nel.cloudflare.com; frame-src https://www.google.com; report-uri /csp-report
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

## Blog article conventions

- Schema: `"@type": "BlogPosting"` (not `Article`)
- Publisher logo: `https://sparkcore.fund/assets/images/png/favicon-192x192.png`
- `"inLanguage": "en"` on all EN articles
- Footer year script: `<script src="/assets/js/set-year.js"></script>`
- External link class: `class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200" target="_blank" rel="noopener noreferrer"`
- Internal link class: `class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200"`
- Author: Alexandre VINAL — `https://www.linkedin.com/in/alexandrevinal/`
