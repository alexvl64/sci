(function () {
  // Replace with your GA4 Measurement ID (example: G-XXXXXXXXXX)
  var GA_MEASUREMENT_ID = "G-7DXMS5D9TF";

  // Skip loading in local previews and when ID is not configured.
  if (!GA_MEASUREMENT_ID || GA_MEASUREMENT_ID === "G-XXXXXXXXXX") return;
  if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") return;

  var script = document.createElement("script");
  script.async = true;
  script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_MEASUREMENT_ID);
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  gtag("js", new Date());
  gtag("config", GA_MEASUREMENT_ID, {
    anonymize_ip: true
  });
})();
