(function(){
  if (/googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot/i.test(navigator.userAgent || '')) return;
  try {
    var saved = localStorage.getItem('sc_lang');
    if (saved === 'en') { window.location.replace('/'); return; }
    localStorage.setItem('sc_lang', 'fr');
  } catch(e) {}
})();
