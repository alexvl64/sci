# Security Audit Report — SparkCore Investment (sparkcore.fund)

**Date:** 2026-04-15  
**Scope:** Full repository (`/github-projets/sci/`)  
**Auditor:** Claude Code — 8 specialist agents (parallel)  
**Overall Score:** 48/100 — Grade D  

---

## Executive Summary

| Category | Agent | Weight | Score |
|----------|-------|--------|-------|
| Vulnerability Scanner | Agent 1 | 20% | 35/100 |
| Authorization Reviewer | Agent 2 | 15% | 55/100 |
| Secret Scanner | Agent 3 | 10% | 10/100 |
| Dependency Auditor | Agent 4 | 10% | 70/100 |
| IaC Scanner | Agent 5 | 10% | 60/100 |
| Threat Intelligence | Agent 6 | 15% | 82/100 |
| AI Code Pattern Auditor | Agent 7 | 10% | 65/100 |
| Business Logic Reviewer | Agent 8 | 10% | 40/100 |

**No malicious code detected.** The codebase is a legitimate financial services website. All findings are misconfiguration or implementation quality issues.

---

## Critical Findings

### [VULN-001] Cloudflare Turnstile Secret Key Committed to Git
**Severity:** CRITICAL (95/100) | **Confidence:** HIGH  
**CWE:** CWE-798 (Hard-coded Credentials) | **OWASP:** A02:2025 | **MITRE:** T1552.001

**Location:** `form_config.php:3`

```php
define('TURNSTILE_SECRET_KEY', '0x4AAAAAACy5d8wNWaVnVMuea4IKtJwL1QA');
```

**WHAT:** The live Cloudflare Turnstile secret key is hardcoded in `form_config.php` and committed to the git repository. It has appeared in at least 3 commits.

**WHY:** Anyone with repository access (or if the repo is public) can extract this key, call the Turnstile verification API directly, and bypass all bot protection on the contact form. The key is also never used server-side — `proxy.php` does not include `form_config.php` — meaning the CAPTCHA provides zero actual protection.

**FIX:**
1. Rotate the key immediately in the Cloudflare dashboard.
2. Add `form_config.php` to `.gitignore`.
3. Purge from git history:
   ```bash
   git filter-repo --path form_config.php --invert-paths
   git push origin --force --all
   ```
4. Load the key from environment variable or `.env` (gitignored):
   ```php
   define('TURNSTILE_SECRET_KEY', getenv('TURNSTILE_SECRET_KEY'));
   ```
5. Wire the Turnstile verification into `proxy.php` — currently the CAPTCHA is never validated server-side.

---

### [VULN-002] Investor Legal Documents Publicly Accessible via HTTP
**Severity:** CRITICAL (90/100) | **Confidence:** HIGH  
**CWE:** CWE-284 (Improper Access Control) | **OWASP:** A01:2025

**Location:** `.htaccess` + `/ressources/contrats/`

**WHAT:** Signed LPA contracts and investor legal documents in `/ressources/contrats/` are directly accessible via HTTP. The `.htaccess` protection only covers `instruction_depot*.pdf` patterns and misses:
- The `/contrats/` subdirectory entirely
- Actual filenames use `instructions_depot_` (with trailing 's'), not matched by the regex

**WHY:** Signed legal documents (LPAs, subscription agreements) containing investor PII, financial commitments, and signatures are accessible to anyone who can guess or enumerate filenames. This is a GDPR violation and a regulatory risk under AIFMD.

**FIX:** Replace the selective `.htaccess` deny with a blanket block on all PDFs in `/ressources/`:
```apache
# Block all PDF files in /ressources/ subtree
<FilesMatch "\.pdf$">
    Require all denied
</FilesMatch>
```
Then serve them exclusively via `secure_pdf.php` (after hardening — see VULN-004).

---

### [VULN-003] Open Unauthenticated HTTP Proxy (`proxy.php`)
**Severity:** CRITICAL (85/100) | **Confidence:** HIGH  
**CWE:** CWE-918 (SSRF) | **OWASP:** A04:2025 | **MITRE:** T1090

**Location:** `proxy.php:1-end`

**WHAT:** `proxy.php` is an open HTTP proxy that forwards all methods, all headers, and any body to a hardcoded target URL. It has no authentication, no method allowlist, no header sanitization, no SSL peer verification, no timeout, and no rate limiting. It also leaks the raw upstream response on JSON parse error:
```php
'raw_response' => $response
```

**WHY:** Any unauthenticated caller can use this endpoint to:
- Proxy requests through the server to mask their origin (privacy/legal risk)
- Relay malicious traffic using the server's IP reputation
- Cause the server to make arbitrary requests (if the target URL were configurable)
- Extract partial response data via the `raw_response` leak

The `robots.txt` file explicitly lists `proxy.php` as a Disallow entry, advertising its existence to attackers.

**FIX:**
```php
// 1. Method allowlist
$allowed_methods = ['GET', 'POST'];
if (!in_array($_SERVER['REQUEST_METHOD'], $allowed_methods, true)) {
    http_response_code(405);
    exit;
}

// 2. Origin check (restrict to your domain)
$allowed_origins = ['https://sparkcore.fund', 'https://www.sparkcore.fund'];
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if (!in_array($origin, $allowed_origins, true)) {
    http_response_code(403);
    exit;
}

// 3. Header allowlist — only forward safe headers
$safe_headers = ['Content-Type', 'Accept', 'Accept-Language'];

// 4. SSL verification + timeout
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, false);

// 5. Remove raw_response from error output
// Replace: 'raw_response' => $response
// With: nothing — remove this line entirely
```

---

## High Severity Findings

### [VULN-004] Timing-Unsafe Token Comparison in `secure_pdf.php`
**Severity:** HIGH (70/100) | **Confidence:** HIGH  
**CWE:** CWE-208 (Observable Timing Discrepancy) | **OWASP:** A07:2025

**Location:** `secure_pdf.php`

**WHAT:** The access token is compared with `!==` instead of `hash_equals()`, enabling timing side-channel attacks. The SHA-256 of file content is used as a static, permanent access token — it never expires and appears in server logs.

**FIX:**
```php
// Replace !== comparison
if (!hash_equals($expected_token, $provided_token)) {
    http_response_code(403);
    exit;
}

// Add security headers
header('Content-Disposition: attachment; filename="' . basename($file) . '"');
header('Cache-Control: no-store, no-cache, must-revalidate');
header('X-Content-Type-Options: nosniff');
```

For stronger security, replace static SHA-256 tokens with time-limited HMAC-signed tokens:
```php
// Generate: valid for 1 hour
$token = hash_hmac('sha256', $filename . ':' . (time() / 3600), SECRET_KEY);

// Verify:
$expected = hash_hmac('sha256', $filename . ':' . (time() / 3600), SECRET_KEY);
if (!hash_equals($expected, $provided_token)) { ... }
```

---

### [VULN-005] Missing Subresource Integrity (SRI) on CDN Scripts
**Severity:** HIGH (65/100) | **Confidence:** HIGH  
**CWE:** CWE-829 (Inclusion of Functionality from Untrusted Control Sphere) | **OWASP:** A08:2025

**Location:** HTML templates loading ApexCharts and Toastify from CDN

**WHAT:** External JavaScript libraries are loaded from CDNs without `integrity` attributes. If the CDN is compromised, malicious JavaScript executes in every visitor's browser with full access to the DOM, form data, and financial information.

**FIX:** Generate SRI hashes and add them to every external script/stylesheet:
```bash
# Generate hash for a CDN resource
curl -s https://cdn.jsdelivr.net/npm/apexcharts@latest/dist/apexcharts.min.js | \
  openssl dgst -sha384 -binary | openssl base64 -A
```
```html
<!-- Before -->
<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>

<!-- After -->
<script src="https://cdn.jsdelivr.net/npm/apexcharts@3.54.0/dist/apexcharts.min.js"
        integrity="sha384-[generated-hash]"
        crossorigin="anonymous"></script>
```

---

### [VULN-006] Content Security Policy Weakened by `'unsafe-inline'`
**Severity:** HIGH (60/100) | **Confidence:** HIGH  
**CWE:** CWE-79 (XSS) | **OWASP:** A05:2025

**Location:** Cloudflare-delivered CSP header

**WHAT:** The CSP `script-src` directive includes `'unsafe-inline'`, which allows inline `<script>` execution and nullifies XSS protection. If an attacker can inject any string into the HTML (via a template variable, API response reflected in the page, etc.), they can execute arbitrary JavaScript.

**FIX:** Migrate inline scripts to external files and use nonces:
```
Content-Security-Policy: 
  default-src 'self';
  script-src 'self' 'nonce-{random-per-request}' https://cdn.jsdelivr.net https://challenges.cloudflare.com;
  style-src 'self' 'nonce-{random-per-request}';
  img-src 'self' data: https:;
  connect-src 'self' https://api.sparkcore.fund;
  frame-ancestors 'none';
```

---

### [VULN-007] `robots.txt` Discloses Sensitive Endpoints
**Severity:** HIGH (55/100) | **Confidence:** HIGH  
**CWE:** CWE-200 (Information Exposure) | **OWASP:** A01:2025

**Location:** `robots.txt`

**WHAT:** `robots.txt` lists `proxy.php` and `secure_pdf.php` as Disallow entries. This is publicly indexed by search engines and actively aids attacker reconnaissance — it's the first place a security researcher or attacker looks.

**FIX:** Remove sensitive paths from `robots.txt`. Disallow entries do not provide security — only obscurity is lost. Protect endpoints with server-side authentication, not `robots.txt`.

---

## Medium Severity Findings

### [VULN-008] No Server-Side Rate Limiting on Contact Form
**Severity:** MEDIUM (50/100) | **Confidence:** MEDIUM  
**CWE:** CWE-799 (Improper Control of Interaction Frequency) | **OWASP:** A10:2025

**Location:** `proxy.php` (form submission handler)

The form relies solely on Cloudflare Turnstile for bot protection, but the secret is compromised (VULN-001) and never verified server-side. Implement PHP-side rate limiting (IP + email fingerprint, sliding window via APCu or Redis).

---

### [VULN-009] Missing Security Headers
**Severity:** MEDIUM (45/100) | **Confidence:** HIGH

Missing or misconfigured headers:
- `Permissions-Policy` — not set (allows camera/microphone/geolocation access)
- `Referrer-Policy` — not set (leaks full URLs to external domains)
- `X-Frame-Options` — absent on some pages (clickjacking risk)
- `Cache-Control` on `secure_pdf.php` — missing `no-store`

---

### [VULN-010] Signed Contracts Appear in Server Logs
**Severity:** MEDIUM (40/100) | **Confidence:** HIGH  
**CWE:** CWE-532 (Information Exposure Through Log Files)

**Location:** `secure_pdf.php`

Requests to `secure_pdf.php?file=contrat_lpa_investor_john_doe.pdf&token=abc123` include the filename and token in the access log. Anyone with server log access can reconstruct the access tokens and file list. Mitigated by switching to POST-based or signed-URL token delivery.

---

## Low / Info Findings

### [VULN-011] PHP Version Exposure via `X-Powered-By`
**Severity:** LOW  
Add `expose_php = Off` in `php.ini` or via Cloudflare header transform to suppress `X-Powered-By: PHP/x.x.x`.

### [VULN-012] No `Content-Disposition: attachment` on PDF Downloads  
**Severity:** LOW  
`secure_pdf.php` serves PDFs inline, allowing them to be rendered and cached by the browser. Add `Content-Disposition: attachment` to force download and prevent browser caching of sensitive documents.

### [VULN-013] `.gitignore` Missing Sensitive Patterns  
**Severity:** LOW  
Current `.gitignore` lacks: `form_config.php`, `.env`, `*.env`, `*.key`, `*.pem`. Add these as a defense-in-depth measure.

---

## Threat Intelligence Summary

**No malicious code detected.** Score: 82/100

- No backdoors, reverse shells, or C2 communication patterns
- No cryptominer indicators
- No obfuscated code blocks
- No supply chain compromise indicators in PHP dependencies

The codebase is a legitimate financial services website with no evidence of third-party tampering.

---

## Dependency Audit Summary

Score: 70/100

- No PHP package manager (Composer) in use — reduces supply chain attack surface but also means no automated vulnerability scanning
- JavaScript dependencies loaded via CDN without SRI (see VULN-005)
- No `package.json` or `node_modules` in production scope
- Static HTML/PHP architecture limits dependency exposure

---

## Compliance Risk Assessment

| Regulation | Status | Primary Risk |
|-----------|--------|--------------|
| **GDPR** | At Risk | Investor PII in publicly accessible PDFs (VULN-002) |
| **AIFMD** | At Risk | Investor documents not access-controlled |
| **DORA** | At Risk | No logging on PDF access, no incident response for credential exposure |
| **AMF/CSSF** | At Risk | Signed contracts accessible without authentication |

---

## Prioritized Remediation Roadmap

### Immediate (within 24h)
1. **Rotate Turnstile secret key** — Cloudflare dashboard → Turnstile → regenerate key
2. **Remove `form_config.php` from git** — `git filter-repo --path form_config.php --invert-paths`
3. **Block `/ressources/` PDF access** — Update `.htaccess` with blanket deny on `*.pdf`

### Short-term (within 1 week)
4. **Harden `proxy.php`** — Method allowlist, origin check, SSL verify, timeout, remove `raw_response`
5. **Add SRI hashes** to all CDN scripts (ApexCharts, Toastify)
6. **Fix CSP** — Remove `'unsafe-inline'`, implement nonces
7. **Wire Turnstile verification** server-side in `proxy.php`

### Medium-term (within 1 month)
8. **Replace static PDF tokens** with HMAC-signed time-limited tokens
9. **Implement server-side rate limiting** on form submissions
10. **Add missing security headers** (`Permissions-Policy`, `Referrer-Policy`, `Cache-Control`)
11. **Clean `robots.txt`** — Remove `proxy.php` and `secure_pdf.php` entries
12. **Suppress PHP version** via `expose_php = Off`

---

*Report generated by Claude Code — 8 parallel specialist agents*  
*Audit date: 2026-04-15 | Scope: full | Stack: PHP/Apache/Cloudflare*
