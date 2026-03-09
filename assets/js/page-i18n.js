// Minimal i18n for secondary pages (validation, error pages).
// Requires translations.js to be loaded first (sets currentLang & translations).

function applyPageTranslations(lang) {
  var t = translations[lang];
  document.documentElement.lang = lang;

  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) el.textContent = t[key];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-html');
    if (t[key] !== undefined) el.innerHTML = t[key];
  });
  document.querySelectorAll('[data-i18n-href]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-href');
    if (t[key] !== undefined) el.setAttribute('href', t[key]);
  });

  // Update lang toggle buttons
  ['nav', 'footer', 'footer-mobile'].forEach(function(zone) {
    var btnEn = document.getElementById('btn-en-' + zone);
    var btnFr = document.getElementById('btn-fr-' + zone);
    if (btnEn) { btnEn.classList.toggle('active', lang === 'en'); btnEn.setAttribute('aria-pressed', String(lang === 'en')); }
    if (btnFr) { btnFr.classList.toggle('active', lang === 'fr'); btnFr.setAttribute('aria-pressed', String(lang === 'fr')); }
  });
}

function setPageLang(lang) {
  currentLang = lang;
  try { localStorage.setItem('sc_lang', lang); } catch(e) {}
  applyPageTranslations(lang);
}

// Footer year
document.addEventListener('DOMContentLoaded', function() {
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});

applyPageTranslations(currentLang);
