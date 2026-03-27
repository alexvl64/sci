(function(){
  var path = (window.location.pathname || '/').replace(/\/$/, '') || '/';
  if (path !== '/' && path !== '/index.html') return;
  if (/googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot/i.test(navigator.userAgent || '')) return;
  try {
    var saved = localStorage.getItem('sc_lang');
    if (saved === 'fr') { window.location.replace('/fr/'); return; }
    if (!saved && navigator.language && navigator.language.toLowerCase().indexOf('fr') === 0) {
      localStorage.setItem('sc_lang', 'fr');
      window.location.replace('/fr/');
    }
  } catch(e) {}
})();
