// currentLang is declared in translations.js (loaded before this file)
let currentTranslations = translations[currentLang];

// === LANGUAGE SYSTEM ===
function applyTranslations(lang) {
  currentTranslations = translations[lang];
  document.documentElement.lang = lang;

  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    if (currentTranslations[key] !== undefined) el.textContent = currentTranslations[key];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-html');
    if (currentTranslations[key] !== undefined) el.innerHTML = currentTranslations[key];
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-placeholder');
    if (currentTranslations[key] !== undefined) el.placeholder = currentTranslations[key];
  });

  // Update lang toggle buttons in nav and footer
  ['nav', 'footer', 'footer-mobile'].forEach(function(zone) {
    var btnEn = document.getElementById('btn-en-' + zone);
    var btnFr = document.getElementById('btn-fr-' + zone);
    if (btnEn) { btnEn.classList.toggle('active', lang === 'en'); btnEn.setAttribute('aria-pressed', String(lang === 'en')); }
    if (btnFr) { btnFr.classList.toggle('active', lang === 'fr'); btnFr.setAttribute('aria-pressed', String(lang === 'fr')); }
  });
}

function setLang(lang) {
  try { localStorage.setItem('sc_lang', lang); } catch(e) {}
  var path = (window.location.pathname || '/').replace(/\/$/, '') || '/';
  var onFr = path.indexOf('/fr') === 0;
  if (onFr && lang === 'en') {
    window.location.href = '/';
    return;
  }
  if ((path === '/' || path === '/index.html') && lang === 'fr') {
    window.location.href = '/fr/';
    return;
  }
  currentLang = lang;
  applyTranslations(lang);
}

applyTranslations(currentLang);

//  ======== GET VARIABLE ===========

function getUrlParameter(name) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(name);
}

// Récupérer la variable de l'URL (DSM ou PAP)
let sourceTracking = getUrlParameter('source');
if (sourceTracking !== 'DSM' && sourceTracking !== 'PAP') {
	sourceTracking = 'UNKNOWN';
}

//  ======== FORM SIDEBAR ===========
// Get button and sidebar elements
const openSidebarButtons = document.querySelectorAll(".open-sidebar");
const closeSidebarButton = document.getElementById("close-sidebar");
const sidebar = document.getElementById("form-sidebar");

// Lazy-load reCAPTCHA only on first sidebar open
let recaptchaLoaded = false;
function loadRecaptcha() {
  if (recaptchaLoaded) return;
  recaptchaLoaded = true;
  var script = document.createElement("script");
  script.src = "https://www.google.com/recaptcha/api.js";
  script.async = true;
  script.defer = true;
  document.head.appendChild(script);
}

// Open the sidebar for each button
openSidebarButtons.forEach((button) => {
  button.addEventListener("click", () => {
    loadRecaptcha();
    sidebar.classList.remove("-right-full");
    sidebar.classList.add("right-0");
    document.body.classList.add("overflow-hidden");
  });
});

// Close the sidebar
closeSidebarButton.addEventListener("click", () => {
  sidebar.classList.remove("right-0");
  sidebar.classList.add("-right-full");
  document.body.classList.remove("overflow-hidden");
});

// Close sidebar when clicking outside
window.addEventListener("click", (e) => {
  if (
    !sidebar.contains(e.target) &&
    !e.target.closest(".open-sidebar") && // Ensure it's not a sidebar button
    sidebar.classList.contains("right-0")
  ) {
    sidebar.classList.remove("right-0");
    sidebar.classList.add("-right-full");
    document.body.classList.remove("overflow-hidden");
  }
});

// Get form and custom select elements
const form = document.getElementById("contact-form");
const selectInput = document.getElementById("select-input");
const dropdownOptions = document.getElementById("dropdown-options");
const selectArrow = document.getElementById("select-arrow");

// Get input fields
const prenomInput = document.getElementById("prenom");
const nomInput = document.getElementById("nom");
const telephoneInput = document.getElementById("telephone");
const emailInputs = document.getElementById("email");

// Get error message elements
const prenomError = document.getElementById("prenom-error");
const nomError = document.getElementById("nom-error");
const emailError = document.getElementById("email-error");
const telephoneError = document.getElementById("telephone-error");
const selectError = document.getElementById("select-error");

// Handle Custom Select Dropdown
selectInput.addEventListener("click", () => {
  dropdownOptions.classList.toggle("hidden");
  selectArrow.classList.toggle("rotate-180");
});

dropdownOptions.addEventListener("click", (event) => {
  const selectedOption = event.target;

  // Update the displayed text and store value
  const selectText = selectInput.querySelector("p");
  selectText.textContent = selectedOption.textContent;
  selectInput.dataset.value = selectedOption.dataset.value;

  // Hide the error
  selectError.style.display = "none";

  // Close the dropdown
  dropdownOptions.classList.add("hidden");
  selectArrow.classList.remove("rotate-180");
});

// Close the dropdown if clicked outside
document.addEventListener("click", (event) => {
  if (
    !selectInput.contains(event.target) &&
    !dropdownOptions.contains(event.target)
  ) {
    dropdownOptions.classList.add("hidden");
    selectArrow.classList.remove("rotate-180");
  }
});

// FORM VALIDATION
form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const prenom = prenomInput.value.trim();
  const nom = nomInput.value.trim();
  const telephone = telephoneInput.value.trim() || "Non renseigné";
  const email = emailInputs.value.trim();
  const source = selectInput.dataset.value; // Utiliser la valeur sélectionnée

  let isValid = true;

  // Validation des champs obligatoires
  if (!prenom) {
    prenomError.style.display = "block";
    isValid = false;
  } else {
    prenomError.style.display = "none";
  }

  if (!nom) {
    nomError.style.display = "block";
    isValid = false;
  } else {
    nomError.style.display = "none";
  }

  if (!email || !isValidEmail(email)) {
    emailError.style.display = "block";
    isValid = false;
  } else {
    emailError.style.display = "none";
  }

  if (!source) {
    selectError.style.display = "block";
    isValid = false;
  } else {
    selectError.style.display = "none";
  }

  // Si un champ est invalide, on stoppe la soumission
  if (!isValid) {
    return;
  }

  // Récupérez le token reCAPTCHA
  const recaptchaToken = grecaptcha.getResponse();
  if (!recaptchaToken) {
    Toastify({
      text: currentTranslations.recaptchaError,
      duration: 5000,
      gravity: "bottom",
      position: "right",
      avatar: "/assets/images/svg/error-icon.svg",
      stopOnFocus: true,
    }).showToast();
    return;
  }

  // Créer les données à envoyer
  const formData = new FormData();
  formData.append("prenom", prenom);
  formData.append("nom", nom);
  formData.append("telephone", telephone);
  formData.append("email", email);
  formData.append("source", source);
  formData.append("source_tracking", sourceTracking);
  formData.append("g-recaptcha-response", recaptchaToken);

  // Désactivez le bouton pour éviter les doubles soumissions
  const submitButton = event.target.querySelector("[type='submit']");
  submitButton.disabled = true;
  submitButton.textContent = currentTranslations.formSubmitLoading;

  try {
    // Envoi via Formcarry
    const response = await fetch("https://formcarry.com/s/oHdZL-AalnM", {
      method: "POST",
      body: formData,
      headers: {
        Accept: "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();

    if (data.status === "success") {
      form.reset();
      grecaptcha.reset();

      // Masquer la sidebar
      sidebar.classList.remove("right-0");
      sidebar.classList.add("-right-full");

      Toastify({
        text: currentTranslations.formSubmitSuccess,
        duration: 5000,
        gravity: "bottom",
        position: "right",
        avatar: "/assets/images/svg/success-icon.svg",
        stopOnFocus: true,
      }).showToast();
    } else {
      Toastify({
        text: currentTranslations.formSubmitError,
        duration: 5000,
        gravity: "bottom",
        position: "right",
        avatar: "/assets/images/svg/error-icon.svg",
        stopOnFocus: true,
      }).showToast();
    }
  } catch (error) {
    console.error("Error:", error);

    Toastify({
      text: currentTranslations.connectionError,
      duration: 5000,
      gravity: "bottom",
      position: "right",
      avatar: "/assets/images/svg/error-icon.svg",
      stopOnFocus: true,
    }).showToast();
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = currentTranslations.contactButton;
  }
});

prenomInput.addEventListener("input", () => {
  if (prenomInput.value) {
    prenomError.style.display = "none";
  } else {
    prenomError.style.display = "block";
  }
});

nomInput.addEventListener("input", () => {
  if (nomInput.value) {
    nomError.style.display = "none";
  } else {
    nomError.style.display = "block";
  }
});
selectInput.addEventListener("select", () => {
  if (selectInput.value) {
    selectError.style.display = "none";
  } else {
    selectError.style.display = "block";
  }
});

emailInputs.addEventListener("input", () => {
  const emailValue = emailInputs.value.trim();

  if (!emailValue || !isValidEmail(emailValue)) {
    emailError.style.display = "block";
  } else {
    emailError.style.display = "none";
  }
});

// FORM NEWSLETTER
document.addEventListener("DOMContentLoaded", () => {

  // Elements
  const emailInput = document.getElementById("emailInput");
  const subscribeButton = document.getElementById("subscribeButton");
  const errorText = document.getElementById("errorText");

  // Handle Email Input Validation
  emailInput.addEventListener("input", () => {
    const emailValue = emailInput.value.trim();
    if (isValidEmail(emailValue)) {
      errorText.classList.add("hidden");
      emailInput.classList.remove("border-red-500");
    } else {
      errorText.classList.remove("hidden");
      emailInput.classList.add("border-red-500");
    }
  });

  // Handle Form Submission
  subscribeButton.addEventListener("click", async (event) => {
    event.preventDefault();
    const emailValue = emailInput.value.trim();

    if (!isValidEmail(emailValue)) {
      errorText.classList.remove("hidden");
      emailInput.classList.add("border-red-500");
      return;
    }

    errorText.classList.add("hidden");
    emailInput.classList.remove("border-red-500");

    subscribeButton.disabled = true;
    subscribeButton.textContent = currentTranslations.subscribeLoading;

    // Créer les données à envoyer
    const formData = new FormData();
    formData.append("email", emailValue);
    formData.append("source_tracking", sourceTracking);

    try {
      const response = await fetch("https://formcarry.com/s/_xD89dyxiXb", {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
      }

      const data = await response.json();

      if (data.status === "success") {
        emailInput.value = "";

        Toastify({
          text: currentTranslations.subscribeSuccess,
          duration: 5000,
          gravity: "bottom",
          position: "right",
          avatar: "/assets/images/svg/success-icon.svg",
          stopOnFocus: true,
        }).showToast();
      } else {
        Toastify({
          text: currentTranslations.subscribeError,
          duration: 5000,
          gravity: "bottom",
          position: "right",
          avatar: "/assets/images/svg/error-icon.svg",
          stopOnFocus: true,
        }).showToast();
      }
    } catch (error) {
      console.error("Error:", error);

      Toastify({
        text: currentTranslations.connectionError,
        duration: 5000,
        gravity: "bottom",
        position: "right",
        avatar: "/assets/images/svg/error-icon.svg",
        stopOnFocus: true,
      }).showToast();
    } finally {
      subscribeButton.disabled = false;
      subscribeButton.textContent = currentTranslations.subscribeButton;
    }
  });
});

// EMAIL VALIDATION FUNCTION (GLOBAL)
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// FOOTER
let copyYear = document.querySelector("#year");
let year = new Date().getFullYear();
copyYear.textContent = year;

// BACK TO TOP
let mybutton = document.getElementById("back-top");
window.onscroll = function () {
  scrollFunction();
};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.classList.add("!block");
  } else {
    mybutton.classList.remove("!block");
  }
}
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
