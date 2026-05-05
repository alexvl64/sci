# Roadmap refonte site sparkcore.fund — 2026

> **Date analyse** : 2026-05-05
> **Auteur** : Claude (analyse demandée par Alexandre Vinal)
> **Statut** : draft pour validation — aucune modification de code effectuée
> **Objectif** : préparer le site en version "institutional-grade" et le rendre prêt pour le lancement public d'Equinoxe (Q3 2026 — date à confirmer)
> **Contexte technique** : repo `alexvl64/sci`, déploiement prévu sur un sous-domaine `beta.` séparé du prod pendant le développement

---

## 0. Résumé exécutif

L'objectif de cette refonte n'est pas de réinventer le site mais de le faire passer du palier "site marketing soigné" au palier **"site de gérant de fonds institutionnel européen"**, comparable visuellement et structurellement à des références comme Hashdex, Bitwise, Pictet AM, Galaxy Asset Management.

Trois priorités structurelles :

1. **Clarifier le positionnement en hero** — passer d'un slogan abstrait à un statement de positionnement institutionnel.
2. **Rendre les signaux réglementaires visibles dès le scroll initial** — bandeau de confiance (régulateur · auditeur · LEI) sous le hero, pas en footer.
3. **Préparer Equinoxe en version beta complète** (page publique + factsheet + capture d'intention pré-lancement) pour qu'une simple bascule de 30 minutes le jour J active le fonds.

Trois recommandations à NE PAS faire :

- Ne pas imiter le pattern "performance hero" de DCY Capital (`3056% ITD return`) — incompatible avec le cadre EFSA + AIFMD pour les pages publiques non-gated.
- Ne pas remplacer le sidebar form par du Calendly seul — garder les deux pour qualifier l'audience.
- Ne pas publier de chiffres de performance bruts hors factsheets gated avant que tous les fonds aient au moins 1 an de track record live.

---

## 1. Diagnostic — état actuel

### 1.1 Atouts à préserver (NE PAS toucher)

| Atout | Détail |
|---|---|
| Palette + typographie | Cream / dark / steel + Funnel Display + Inter — cohérent et sobre, c'est l'ADN visuel |
| Schémas JSON-LD | Organization + FinancialService + FAQPage déjà en place et corrects |
| AEO/GEO | `llms.txt` + `llms-full.txt` publiés, exhaustifs |
| Factsheets gated (DT + CV) | Densité institutionnelle réelle (KPIs, historique mensuel, perf table) — c'est une vraie facture de fonds |
| Bilinguisme EN/FR | Pré-rendu côté serveur (pas de flicker, bot-safe), URL-priority dans `currentLang` correct |
| Defense-in-depth pages gated | Meta `noindex` + `X-Robots-Tag` HTTP + `robots.txt` + retrait `llms.txt` — niveau bancaire |
| Mentions légales pied de page | EFSA + EFIU + LEI + Reg. No. + adresse + KPMG : tout y est |
| Tracking GA4 minimaliste | 6 Key Events sans GTM — choix philosophique défendable |
| Sécurité serveur | CSP via Cloudflare Transform Rule, HSTS, headers `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` |
| Workflow gated PDFs | `secure_pdf.php` avec `hash_equals()` + `Cache-Control: no-store` |

### 1.2 Manques structurels

| Réf | Manque | Impact |
|---|---|---|
| G1 | Hero abstrait ("Security Performance") sans positionnement clair | Perd les 3 secondes initiales d'attention |
| G2 | Pas de bandeau de confiance sous nav (régulateur · auditeur · LEI) | Signaux légaux enterrés en footer |
| G3 | Pas de section "Notre approche / Our investment philosophy" entre hero et fonds | Saute du marketing aux produits sans poser le cadre |
| G4 | Pas de matrice comparative DT / CV / EQ | Comparaison instantanée des 3 fonds impossible |
| G5 | Pas de pages publiques `/funds/<slug>/` | SEO ne capture pas les requêtes nom-de-fonds + pas de page partageable au comité d'invest |
| G6 | Pas de factsheet Equinoxe ni de FR factsheets pour DT/CV | Lacune critique pour le lancement |
| G7 | CTA hero unique ("Contact Us") | Manque le pattern dual standard |
| G8 | Animations AOS partout | Surplus marketing — sites institutionnels en mettent 2-3 max |
| G9 | Newsletter sans aperçu (pas de "what's inside" ni archive) | Faible taux de conversion email |
| G10 | `tailwind.min.css` et `aos.min.css` à 0 octet en local | À vérifier — pipeline Tailwind à reconstruire ou référence morte à nettoyer |

### 1.3 Lacunes Equinoxe (critiques pour D-day)

| Réf | Manque | Action |
|---|---|---|
| EQ1 | Pas de page publique `/funds/equinoxe/` ni concept paper accessible | À créer en beta |
| EQ2 | Pas de factsheet `/factsheets/equinoxe.html` ni version FR | À créer en beta avec données placeholder |
| EQ3 | Pas de chart JS `equinoxe.js` | À cloner depuis `dynamic-trends.js` |
| EQ4 | Card Equinoxe homepage avec CTA passif "available at fund launch" | Remplacer par "Pre-register your interest" cliquable |
| EQ5 | Pas de badge hero "Equinoxe — Q3 2026" | À ajouter en beta, à retirer le jour J |
| EQ6 | Newsletter actuelle ne segmente pas les pre-registered Equinoxe | Ajouter checkbox ou form dédié |
| EQ7 | LPA `lpa_eq_signed.pdf` existe déjà dans `/ressources/contrats/` mais aucun lien depuis le site | Connecter au funnel quand le fonds devient live |

---

## 2. Recommandations P0 — site institutionnel

### P0-1 · Réécrire le hero en positionnement, pas en slogan

**Actuel** : "Security · Performance" + "Reliable investment in the crypto-asset universe."

**Proposé EN** :

> **Regulated crypto-asset investment funds for qualified European investors**
> Estonian AIFM supervised by Finantsinspektsioon — three strategies, one institutional framework.

**Proposé FR** :

> **Fonds d'investissement crypto-actifs réglementés pour investisseurs qualifiés européens**
> AIFM estonien supervisé par la Finantsinspektsioon — trois stratégies, un cadre institutionnel unique.

**CTA dual** :

- Primaire : `Schedule a Discovery Call` → ouvre Cal.eu directement (réduit la friction du formulaire 5 champs)
- Secondaire ghost : `Request Fund Documentation` → ouvre le sidebar form actuel

**Visuel hero** : remplacer `hero-graph-img.webp` (générique) par soit une sparkline réelle DT (cumulative base 100), soit une grille de 4 KPIs sobres (cf. P0-2).

**Note tagline FR** : remplacer aussi "Investissement fiable dans l'univers des crypto-actifs" par "Exposition disciplinée aux marchés des crypto-actifs" — "fiable" + "crypto" est un signal compliance flou, "disciplinée" reste fidèle au métier.

---

### P0-2 · Bandeau de confiance "Institutional credentials" sous hero

Bande pleine largeur, fond `lightGray` (#F3F5F7), 4 colonnes :

| Colonne | Contenu |
|---|---|
| **Regulator** | Finantsinspektsioon (EE) — Small Fund Manager — *lien EFSA registry* |
| **Audit & Accounting** | KPMG Estonia |
| **Legal** | Hedman Partners & Co |
| **LEI** | 8945003BBN0RVNNB0S84 — *lien GLEIF* |

**Spec visuelle** : hauteur ~80 px, typo small-caps `Inter 11px tracking-wide`, sans icônes flashy. Référence : la barre "Custodian / Auditor / Administrator" qu'on retrouve chez Hashdex, Fineqia, Bitwise.

---

### P0-3 · Section "Our approach" entre hero et fund cards

Pose la thèse d'investissement collective avec 3 piliers chiffrables — équivalent sobre du "CEO quote" de DCY mais sans le ton héroïque.

```
H2 — Our approach
    Disciplined, regulated exposure to crypto-asset markets

Intro — At SparkCore, we manage crypto-asset investment funds with the same
operational rigour and regulatory framework you expect from traditional
alternative asset managers. Three principles guide every decision.

Pillar 1 — Regulated by design
    Estonian AIF structure, supervised by the Finantsinspektsioon, with full
    AML/KYC framework and dual MLRO oversight.

Pillar 2 — Risk-budgeted
    Each strategy operates with explicit drawdown targets, position-sizing
    discipline, and an independent algorithmic defensive core.

Pillar 3 — Institutional reporting
    Quarterly NAV with KPMG-audited accounting, monthly investor letters,
    on-demand portfolio transparency.
```

Justification : pose le ton **avant** que l'investisseur regarde les fonds. Légitime aussi le "tu peux comparer mes fonds à ceux de ton family office traditionnel".

---

### P0-4 · Matrice comparative des 3 fonds (above the fold de la section funds)

Sous le H2 "Our crypto investment funds", ajouter une table compacte avant les 3 cards :

| | Dynamic Trends | CryptoVision | Equinoxe |
|---|---|---|---|
| **Risk profile** | High (controlled) | Moderate | Low |
| **Strategy** | Directional | Dual-block | Market-neutral |
| **Benchmark** | Bitcoin | CCi30 | Cash + EUR risk-free |
| **Min. investment** | €50k | €50k | €50k |
| **Liquidity** | Quarterly | Quarterly | Quarterly |
| **Lock-up** | 1 year | 1 year | 1 year |
| **Launch** | Aug 2025 | Feb 2021 (managed acct) → live | Q3 2026 (expected) |
| **Status** | Open | Open | Pre-launch |

Garder ensuite les 3 cards visuelles existantes (très bien faites — ne pas les retoucher).

---

### P0-5 · Créer 3 pages publiques `/funds/<slug>/`

Aujourd'hui le seul point d'atterrissage SEO d'un fonds est le blog. Créer trois pages indexables (`<meta robots="index, follow">`, ajoutées au `sitemap.xml`) :

- `/funds/dynamic-trends/` (EN) + `/fr/fonds/dynamic-trends/` (FR)
- `/funds/cryptovision/` (EN) + `/fr/fonds/cryptovision/` (FR)
- `/funds/equinoxe/` (EN) + `/fr/fonds/equinoxe/` (FR)

**Différence clé avec les factsheets** :

- Pas de chiffres de performance (= public, donc pas de marketing performance per EFSA)
- Stratégie + structure + frais + risque + processus + FAQ + 1 CTA "Request the factsheet" → ouvre le sidebar
- Schema `FinancialProduct` indexable
- Structure courte (1500-2000 mots), 1 page = 1 fonds = 1 query

**Bénéfices** :

1. **SEO** : capture les requêtes "SparkCore Dynamic Trends", "Equinoxe market-neutral fund Estonia", "Bitcoin outperformance fund EU"
2. **Sales funnel** : page non-gated → conversion au factsheet gated
3. **Trust** : un investisseur peut envoyer le lien à son comité d'investissement sans devoir d'abord remplir un form

**Convention URL FR** : à figer (`/fr/fonds/...` ou `/fr/funds/...`). Préférence par défaut : `/fr/fonds/...` cohérent avec la convention `/fr/blog/` existante.

---

### P0-6 · Footer disclaimer en 2 blocs distincts

Actuellement disclaimer + privacy/insights mélangés. Séparer :

**Bloc 1 — Risk warning (encadré, fond pâle, bordure cream)**

> Investment in crypto-asset funds carries a high level of risk including the risk of total capital loss. Past performance does not guarantee future results. Funds are reserved for qualified or professional investors as defined under EU AIFMD. This website does not constitute an offer or solicitation to invest in any jurisdiction where such offer would be unlawful. Please assess your suitability and consult independent advice before investing.

**Bloc 2 — Regulatory & corporate info** (texte plat, comme aujourd'hui)

SparkCore.investment OÜ · Reg. 16265864 · Männimäe 1, Pudisoo · LEI 8945003BBN0RVNNB0S84 · Supervised by Finantsinspektsioon (EFSA) · Financial Institution licence EFIU.

Justification : séparation attendue par les compliance officers qui scannent le site avant due-dil.

---

### P0-7 · Localisation FR des factsheets

Les 2 factsheets existantes (DT, CV) sont en EN avec un `lang-toggle` qui appelle `setLang('fr')` mais qui ne pointe vers rien si la version FR n'existe pas en page séparée.

**Option A (rapide)** : `setLang('fr')` swap les `data-i18n` côté client (dictionnaire FR existe déjà partiellement dans `dynamic-trends.js`).

**Option B (propre, recommandée)** : créer `/factsheets/dynamic-trends-fr.html` (ou `/fr/factsheets/dynamic-trends.html`) pré-rendue en FR, comme le pattern `index.html` ↔ `fr/index.html`. Garder `noindex` sur les deux.

→ Option B aligne avec la convention bilingue actuelle et évite que Google capture une version mal localisée.

---

## 3. Roadmap Equinoxe — beta freeze → live D-day

### 3.1 Phase 1 — Beta (à faire dès maintenant, avant la sortie publique)

**E1 · Page publique `/funds/equinoxe/` (concept page, indexée)**

- Description stratégie delta-neutral / beta-neutral (40/60)
- Risque : low + bandeau "Pre-launch — formal subscription window opens at launch"
- Liste des frais (structure identique aux 2 autres fonds)
- "Expected launch : Q3 2026" (à confirmer — date précise ou trimestre)
- Un seul CTA : `Pre-register interest` → form sidebar avec `data-i18n="eqEarlyAccess"` → tag `cta_origin=equinoxe-prelaunch` dans GA4
- Schema `FinancialProduct` avec `availability: PreOrder` (ou `LimitedAvailability`)

**E2 · Factsheet template `/factsheets/equinoxe.html` + `equinoxe-fr.html`**

- Cloner `dynamic-trends.html` (template prouvé)
- Remplacer specs : delta-neutral 40 % AUM + beta-neutral 60 % AUM, no leverage, USD ref, EUR/USD/MiCA stables, quarterly liquidity, 1-year lock-up, KPMG, Hedman, brokers (à préciser pour EQ — dérivés probablement OKX / Binance / Bybit + custodian crypto)
- KPIs Key Figures : `—` partout au lancement, avec note "Performance data published from first NAV (T+90 jours post-launch)"
- Bandeau orange/cream visible : **"Pre-launch — Strategy paper available on request"**
- Charts : préparer le JS `equinoxe.js` (cloner `dynamic-trends.js`) avec tableau vide + axes prêts pour la première NAV
- Garder gated (noindex + headers + sitemap absent + robots.txt)

**E3 · Card Equinoxe homepage : modifier le CTA**

- Actuel : `Factsheet available at fund launch.` (statique, italique)
- Proposé : ajouter un soft CTA cliquable
  > `Pre-register your interest →`
  → ouvre le sidebar form avec contexte "Equinoxe early access"
- Tag GA4 `factsheet_request_open` avec param `fund=equinoxe` + `stage=prelaunch`

**E4 · Hero homepage : badge discret "Equinoxe — Q3 2026"**

- Petit pill au-dessus du H1 hero : `New strategy launching Q3 2026 — Equinoxe`
- Lien : `/funds/equinoxe/`
- Style : border `#DBD1BC`, text cream, height 26 px
- À retirer le jour où le fonds devient live

**E5 · Mention Equinoxe dans le bloc "Our approach"** (couvert par P0-3).

**E6 · Newsletter capture pré-lancement** : ajouter une checkbox dans le form newsletter "Notify me when Equinoxe launches" (ou un form Equinoxe dédié si funnel séparé souhaité).

### 3.2 Phase 2 — D-day (le jour du lancement)

Procédure de bascule (checklist, ~30 min de prod) :

```
[ ] /factsheets/equinoxe.html       → first NAV inseree, bandeau "Pre-launch" retire
[ ] /factsheets/equinoxe-fr.html    → idem
[ ] /funds/equinoxe/                → status "Open", subscription instructions ajoutees
[ ] Card Equinoxe homepage          → "Pre-register" remplace par "Request the Factsheet →"
[ ] Hero homepage                   → badge "Q3 2026" retire
[ ] Matrice comparative             → status "Open" sur Equinoxe
[ ] Schema FinancialProduct         → availability: InStock, dateModified update
[ ] llms.txt + llms-full.txt        → status Equinoxe "Operational since YYYY-MM-DD"
[ ] sitemap.xml                     → /funds/equinoxe/* lastmod update + IndexNow ping
[ ] Newsletter dedie (one-shot)     → "Equinoxe is live" envoye aux pre-registered
[ ] LinkedIn company post           → annonce officielle
[ ] GA4                             → param fund=equinoxe stage=launched
```

Tout devrait se faire en moins de 30 minutes le jour J si la beta est bien préparée.

### 3.3 Phase 3 — T+30 / T+90 post-launch

- T+30 : première lettre mensuelle Equinoxe (PDF dans `/ressources/letters/equinoxe-2026-MM.pdf`, gated derrière `secure_pdf.php`)
- T+90 : première NAV trimestrielle, mise à jour des KPIs sur factsheet
- T+180 : si Equinoxe atteint Sharpe > 2, ajouter un **callout sur la page CryptoVision** ("Investors looking for lower volatility may also consider Equinoxe →")

---

## 4. Recommandations P1 — qualité institutionnelle (post-Equinoxe live)

### P1-1 · Créer `/insights/` (lettres mensuelles + commentaires de marché)

Aujourd'hui le blog mélange contenu SEO ("Crypto fund vs ETF") et contenu de sustenance (rare). Les institutions attendent un fil "Investor Letters" séparé. Architecture :

- `/insights/letters/` : lettres trimestrielles signées par le PM, gated (PDF via `secure_pdf.php`)
- `/insights/commentary/` : market commentary mensuel public (court, indexable)
- Le `/blog/` reste pour SEO/GEO

### P1-2 · Page `/about/`

Actuellement le bloc "Meet our team" est sur la home. Une page dédiée permet :

- Des bios plus longues (chacune avec un sous-paragraphe "Investment thesis")
- Les agréments individuels (FCA, AMF, ACPR si applicable, OCM Estonia, certifications)
- Un encart "Why we built SparkCore" — narrative courte
- Schema `Person` par membre

### P1-3 · LinkedIn + bandeau social dans header

Aujourd'hui LinkedIn n'apparaît qu'en footer. Mettre une icône LinkedIn discrète dans le header (à droite de "Contact Us"), ou un sous-bandeau de nav avec follower count si > 500. Signal de social proof institutionnel léger.

### P1-4 · Cas client / témoignages anonymisés

Les family offices veulent voir d'autres family offices. Écrire 2-3 vignettes sans nommer :

> *A French family office allocated 4 % of its alternatives sleeve to CryptoVision in 2024 to gain controlled crypto exposure without operational complexity.*

Pas de citations entre guillemets — trop fort sur YMYL crypto. Garder la voix narrative à la 3e personne.

### P1-5 · "Performance evolution" homepage : clarifier le scope

Actuellement le chart noir géant en home présente DT (depuis 2020 base 100, log scale) sans header explicite. Soit :

- Ajouter le titre **"Dynamic Trends — performance vs Bitcoin"**
- Ou remplacer par un **stack de 3 mini-charts** (DT vs BTC, CV vs CCi30, EQ placeholder "Coming Q3 2026") — meilleur pour le storytelling 3-fonds

### P1-6 · Page `/governance/` (Compliance & Governance)

- Diagramme org structure (regulator / fund manager / depositary / auditor / legal counsel)
- Liste des process (KYC/AML, NAV calculation, FATCA/CRS, MiCA touch-points)
- Citations EFSA + EFIU registries
- Schema `WebPage` + `FinancialService.regulatedBy` pointant sur Finantsinspektsioon

Meilleur asset SEO sur "regulated crypto fund Estonia" et rassurant pour due-dil.

---

## 5. Quick wins P2

| Réf | Action | Effort | Bénéfice |
|---|---|---|---|
| QW1 | Tagline FR : "Investissement fiable" → "Exposition disciplinée" | 5 min | Cohérence compliance |
| QW2 | Hero : `Read our latest market commentary →` lien discret sous CTA secondaire | 15 min | Trafic vers blog FR |
| QW3 | Bouton "Schedule a Call" partout en alternative au form sidebar | 30 min | Réduit friction conv pour HNW pressés |
| QW4 | Footer : "Subscribe to investor letters" form séparé du marketing newsletter | 30 min | Sépare audience pro / curieuse |
| QW5 | OG image : remplacer `meta-image.webp` (générique) par 3 variantes par-page | 1 h | Meilleur partage LinkedIn |
| QW6 | Réduire AOS animations à 2-3 sections max (hero + funds cards + team) | 30 min | Tone institutionnel |
| QW7 | Vérifier `tailwind.min.css` 0 octet : rebuild ou nettoyer la référence morte | 30 min | Hygiene code |
| QW8 | Footer : ajouter mention "Dual MLRO" (déjà en white-label, dupliquer 1 ligne) | 5 min | Trust signal AML |
| QW9 | Schema FAQ : ajouter Q "When does Equinoxe launch?" | 10 min | AI search readiness |
| QW10 | Pages 404/403/500 : ajouter `Suggested next step → /funds/` | 10 min | Récupération de bounce |

---

## 6. Anti-patterns — où DCY n'est PAS un bon modèle

| DCY fait | Pourquoi NE PAS copier |
|---|---|
| "3056 % ITD return", "70 % CAGR" en hero | Sous AIFMD + EFSA, performance display sans conditions = problème compliance. Garder les KPIs sur factsheet gated avec disclaimers requis. |
| CEO quote héroïque type "blockchain will transform many industries" | Vague, marketing, pas crédible institutionnel. La structure réglementaire est un meilleur trust signal. |
| "Trader as a Service" | Tu offres déjà White Label — plus institutionnel + plus défensif que "TaaS". Garder le vocabulaire actuel. |
| Logo géant + tagline marketing en plein hero | SparkCore a déjà un logo SVG sobre + Funnel Display soignée. Rester discret — l'institutionnel se mesure à la sobriété. |
| Pas de mention claire du régulateur en home | DCY est aux Caïmans (off-shore), donc ils cachent. SparkCore a le **régulateur EU**, à mettre **en haut** (P0-2). |

### 6.1 Inspirations meilleures pour SparkCore

- **DCY** : structure 3 produits (à reprendre) + KPI bar (à transposer mais en sobre)
- **Hashdex** : page de famille de fonds, séparation "Active" / "Index" / "Pre-launch"
- **Bitwise** : footer avec disclaimer multi-juridiction très propre
- **Galaxy Asset Management** : page "About" avec governance diagram
- **Coinshares** : "Insights" hub séparé du blog
- **Pictet AM** : sobriété générale du site (référence absolue du secteur)

---

## 7. Phasage suggéré

```
Phase A — Site institutional polish (avant Equinoxe)        [2-3 semaines]
  P0-1  Hero rewrite + dual CTA
  P0-2  Trust strip sous nav
  P0-3  "Our approach" section
  P0-4  Matrice comparative
  P0-6  Footer 2 blocs (disclaimer / corporate)
  QW1, QW2, QW6, QW8                                          [quick wins en parallele]

Phase B — Equinoxe beta (en parallele Phase A)               [1-2 semaines]
  E1   Page publique /funds/equinoxe/
  E2   Factsheet equinoxe.html + equinoxe-fr.html
  E3   Card homepage CTA pre-register
  E4   Hero badge "Q3 2026"
  E6   Newsletter capture pre-launch

Phase C — SEO + bilingual (post-Equinoxe beta)               [3-4 semaines]
  P0-5 /funds/<slug>/ x 3 (DT, CV, EQ) en EN + FR
  P0-7 Factsheets FR pour DT et CV
  P1-1 /insights/ split letters / commentary
  P1-2 /about/ team page

Phase D — D-day Equinoxe                                     [1 jour]
  Checklist Phase 2 ci-dessus

Phase E — Polish post-launch                                  [continu]
  P1-3 LinkedIn header
  P1-4 Cas client (1 par trimestre)
  P1-5 Performance home : 3 mini-charts
  P1-6 /governance/ page
  QW3, QW4, QW5, QW9, QW10
```

---

## 8. Ce qu'il NE faut PAS faire

- **Ne pas** ajouter de visuel "performance" en home avant que les 3 fonds aient au moins 1 an de track record live (= 2027 pour DT, post-Q3 2027 pour EQ). En attendant, les chiffres restent sur les factsheets gated.
- **Ne pas** publier de chiffres bruts (ROAS, CAGR, drawdown) en page publique sans le disclaimer EFSA complet et la mention "destinée aux investisseurs qualifiés".
- **Ne pas** ouvrir un compte Twitter/X dédié SparkCore (LinkedIn suffit pour l'audience institutionnelle ; Twitter = bruit retail crypto, dilue le positionnement).
- **Ne pas** remplacer le sidebar form par du Calendly seul. Garder les deux : Cal pour les RDV chauds, form pour la qualification + opt-in marketing.
- **Ne pas** ajouter de chatbot. Anti-institutionnel.
- **Ne pas** retirer le bloc White Label : différenciateur réel vs DCY. Au contraire, P1 long terme : créer une page `/white-label/` standalone (le bloc home ne vit que comme teaser).

---

## 9. Questions ouvertes — inputs requis avant exécution

1. **Date Equinoxe** : Q3 2026 confirmé ou plus précis ? (impacte le badge hero + la copy "Expected launch Q3 2026")
2. **Brokers/custodians Equinoxe** : identiques DT (FundBank · OKX · Binance) ou ajout (Bybit, Deribit pour les options) ?
3. **CryptoVision launch date** : `llms.txt` dit "01/02/2021", le `chart-note` factsheet dit "Fund launched 01/01/2025. Data Feb 2021–Dec 2024 from real strategies on managed accounts" — incohérence à clarifier (interne et externe).
4. **Public AUM** : prêt à publier un total managed AUM en home (style "€X M under management") ou trop tôt ? Reste discrétionnaire EFSA.
5. **`/funds/<slug>/` URLs FR** : `/fr/fonds/...` ou `/fr/funds/...` ? Convention à figer (préférence `/fr/fonds/...`).
6. **Granularité d'exécution** : code généré à validation de la roadmap entière, ou phase par phase / section par section ?

---

## 10. Environnement de développement — beta domain

> Note ajoutée à la demande de l'utilisateur (2026-05-05).

L'utilisateur prévoit de mettre en place un sous-domaine `beta.sparkcore.fund` (ou équivalent) pour développer la refonte sans impacter la prod.

Implications techniques à valider lors du setup :

- **Cloudflare** : ajouter le sous-domaine au zone DNS, activer SSL/TLS edge cert
- **CSP** : la Transform Rule actuelle s'applique à `sparkcore.fund` ; vérifier qu'elle couvre aussi le sous-domaine
- **Robots/indexation** : le sous-domaine `beta.` doit avoir un `robots.txt` strict `User-agent: * / Disallow: /` + auth basic pour éviter toute fuite SEO
- **GA4** : créer un property séparé pour beta (ou désactiver l'envoi d'events si même property — sinon pollution des données prod)
- **GSC** : NE PAS soumettre le beta domain à GSC (pour éviter conflit canonical avec la prod)
- **Hreflang** : les liens hreflang doivent pointer vers `sparkcore.fund` même depuis la beta (sinon Google indexe les mauvais URLs si le beta fuite)
- **Workflow git** : prévoir une branche `beta` ou une convention `feat/<task>` qui déploie sur beta avant merge sur `main` qui déploie sur prod

---

## 11. Statut roadmap

| Phase | Statut | Démarrage prévu |
|---|---|---|
| A — Site institutional polish | À valider | TBD |
| B — Equinoxe beta | À valider | TBD |
| C — SEO + bilingual | À valider | Post-B |
| D — D-day Equinoxe | À planifier | Q3 2026 |
| E — Polish post-launch | À planifier | Continu post-D |

**Prochaine étape attendue** : validation utilisateur de la roadmap (ou amendements), puis plan d'implémentation détaillé fichier-par-fichier pour la Phase A et/ou B selon priorité choisie.
