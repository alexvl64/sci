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
