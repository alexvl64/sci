(function(){
  // Only act on the English root page
  var path = (window.location.pathname || '/').replace(/\/$/, '') || '/';
  if (path !== '/' && path !== '/index.html') return;

  // Bots & crawlers: never redirect — let them index this exact URL
  var ua = navigator.userAgent || '';
  var BOT_RE = /bot|crawl|spider|slurp|mediapartners|facebookexternalhit|facebookcatalog|whatsapp|telegrambot|linkedinbot|twitterbot|discordbot|slackbot|applebot|pinterest|embedly|quora link preview|vkshare|w3c_validator|redditbot|yahoo|duckduckgo|baidu|yandex|sogou|exabot|ia_archiver|gptbot|claudebot|claude-web|perplexitybot|oai-searchbot|ccbot|google-extended|anthropic-ai|chatgpt|bytespider|amazonbot/i;
  if (BOT_RE.test(ua)) return;
  // Headless automation (Puppeteer/Playwright default UA) — skip as well
  if (/headlesschrome|phantomjs|jsdom/i.test(ua)) return;

  // Only auto-redirect once per tab, so the Back button works
  if (sessionStorage.getItem('sc_lang_redirected')) return;

  try {
    var saved = localStorage.getItem('sc_lang');
    if (saved === 'fr') {
      sessionStorage.setItem('sc_lang_redirected', '1');
      window.location.replace('/fr/');
      return;
    }
    if (!saved && navigator.language && navigator.language.toLowerCase().indexOf('fr') === 0) {
      localStorage.setItem('sc_lang', 'fr');
      sessionStorage.setItem('sc_lang_redirected', '1');
      window.location.replace('/fr/');
    }
  } catch(e) {}
})();
