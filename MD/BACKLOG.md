# SparkCore — Backlog technique

> Items différés, non bloquants. Source de vérité des tâches « à faire plus tard » hors audits SEO datés (`MD/seo/audit-*/`).

---

## BL-001 — Nettoyage des commentaires verbeux / sur-informatifs (code + llms.txt)

- **Ajouté** : 2026-05-29
- **Origine** : demande user (passe d'hygiène code, en marge du retrait KPMG)
- **Priorité** : Medium (un sous-item = sécurité, voir ci-dessous)
- **Statut** : à planifier

**Objectif** : retirer des pages/JS publics les commentaires inutiles et ceux qui exposent trop de détail d'implémentation ou de structure interne. Réviser `llms.txt` pour la même sur-divulgation.

### 1. Sécurité — commentaires qui annoncent le mécanisme anti-spam (quick win)
Annoncer un honeypot dans le HTML public le rend trivial à contourner par les bots.
- `index.html:518` + `index.html:1116` — `<!-- Honeypot anti-spam -->`
- `fr/index.html:490` + `fr/index.html:1089` — `<!-- Honeypot anti-spam -->`
- **Action** : supprimer les 4 commentaires. Optionnel (plus profond) : renommer `id="honeypot"` / `id="honeypot-newsletter"` en libellé neutre (ex. `id="contact-extra"`) — vérifier la dépendance dans `main.js` / handler de form avant de renommer.

### 2. JS — commentaires de rationale verbeux (dev → prod)
Utiles en revue de code, superflus en source servie publiquement.
- `assets/js/main.js:1-7` — bloc explicatif AOS `once:true` (7 lignes)
- `assets/js/main.js` — passer en revue les autres blocs `// ===== SECTION =====` et rationales longs
- **Action** : condenser (1 ligne max) ou retirer. Garder uniquement ce qui aide la maintenance.

### 3. llms.txt — sur-divulgation de structure interne
`llms.txt` doit informer les IA sans exposer d'organisation interne fine.
- `llms.txt:36` — « AML supervision: dual MLRO structure — internal officer (FIU) and external officer (France) » → évaluer si la granularité interne/externe + localisation est nécessaire publiquement.
- `llms.txt:58` — bio fondateur : vérifier le niveau de détail.
- **Action** : arbitrer entre transparence réglementaire (utile YMYL) et minimisation de divulgation. Décision user requise par ligne.

### 4. HTML — commentaires de section
Les marqueurs `<!-- === SECTION === -->` sont OK (lisibilité). Ne pas sur-nettoyer : ne retirer que ceux décrivant une logique d'implémentation (ex. `index.html:44` critical-CSS rationale, `index.html:57` lazy ApexCharts).

**Note** : tâche à faire en une passe dédiée (PR séparée du retrait KPMG), avec décision user sur les arbitrages llms.txt §3.
