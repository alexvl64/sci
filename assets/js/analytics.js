(function () {
  // Replace with your GA4 Measurement ID (example: G-XXXXXXXXXX)
  var GA_MEASUREMENT_ID = "G-7DXMS5D9TF";
  var CONSENT_STORAGE_KEY = "sc_cookie_consent_v1";

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

  // Consent Mode v2: denied by default until explicit user action.
  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied"
  });

  gtag("js", new Date());
  gtag("config", GA_MEASUREMENT_ID, {
    anonymize_ip: true
  });

  function updateConsent(consentValue) {
    var granted = consentValue === "granted";
    gtag("consent", "update", {
      ad_storage: granted ? "granted" : "denied",
      ad_user_data: granted ? "granted" : "denied",
      ad_personalization: granted ? "granted" : "denied",
      analytics_storage: granted ? "granted" : "denied"
    });
    try {
      localStorage.setItem(CONSENT_STORAGE_KEY, consentValue);
    } catch (e) {}
  }

  function getConsentLabels() {
    var isFrench = (document.documentElement.lang || "").toLowerCase().indexOf("fr") === 0;
    if (isFrench) {
      return {
        title: "Respect de votre vie privee",
        text: "Nous utilisons des cookies de mesure d'audience pour ameliorer le site. Vous pouvez accepter ou refuser.",
        accept: "Accepter",
        reject: "Refuser",
        privacy: "Politique de confidentialite"
      };
    }
    return {
      title: "Your privacy matters",
      text: "We use analytics cookies to understand site usage and improve the experience. You can accept or decline.",
      accept: "Accept",
      reject: "Decline",
      privacy: "Privacy Policy"
    };
  }

  function removeBanner() {
    var existing = document.getElementById("sc-consent-banner");
    if (existing && existing.parentNode) {
      existing.parentNode.removeChild(existing);
    }
  }

  function renderBanner() {
    if (document.getElementById("sc-consent-banner")) return;
    var labels = getConsentLabels();
    var banner = document.createElement("div");
    banner.id = "sc-consent-banner";
    banner.style.position = "fixed";
    banner.style.left = "16px";
    banner.style.right = "16px";
    banner.style.bottom = "16px";
    banner.style.maxWidth = "720px";
    banner.style.margin = "0 auto";
    banner.style.padding = "14px 16px";
    banner.style.background = "#0E1117";
    banner.style.color = "#FFFFFF";
    banner.style.borderRadius = "8px";
    banner.style.boxShadow = "0 8px 24px rgba(0,0,0,0.25)";
    banner.style.zIndex = "99999";
    banner.style.fontFamily = "Arial, sans-serif";
    banner.innerHTML =
      '<div style="font-weight:600;margin-bottom:6px;">' + labels.title + "</div>" +
      '<div style="font-size:14px;line-height:1.45;margin-bottom:12px;">' + labels.text +
      ' <a href="/privacy-policy" style="color:#DBD1BC;text-decoration:underline;">' + labels.privacy + "</a>.</div>" +
      '<div style="display:flex;gap:8px;flex-wrap:wrap;">' +
      '<button id="sc-consent-accept" style="border:1px solid #DBD1BC;background:#DBD1BC;color:#0E1117;padding:8px 12px;border-radius:6px;cursor:pointer;font-weight:600;">' + labels.accept + "</button>" +
      '<button id="sc-consent-reject" style="border:1px solid #8A9BA8;background:transparent;color:#FFFFFF;padding:8px 12px;border-radius:6px;cursor:pointer;font-weight:600;">' + labels.reject + "</button>" +
      "</div>";

    document.body.appendChild(banner);

    var acceptBtn = document.getElementById("sc-consent-accept");
    var rejectBtn = document.getElementById("sc-consent-reject");
    if (acceptBtn) {
      acceptBtn.addEventListener("click", function () {
        updateConsent("granted");
        removeBanner();
      });
    }
    if (rejectBtn) {
      rejectBtn.addEventListener("click", function () {
        updateConsent("denied");
        removeBanner();
      });
    }
  }

  function initConsent() {
    var consentValue = null;
    try {
      consentValue = localStorage.getItem(CONSENT_STORAGE_KEY);
    } catch (e) {}

    if (consentValue === "granted" || consentValue === "denied") {
      updateConsent(consentValue);
      return;
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", renderBanner);
    } else {
      renderBanner();
    }
  }

  initConsent();
})();
