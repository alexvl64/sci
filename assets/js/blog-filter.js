/* SparkCore - blog index category filter
 * Usage: requires .filter-chip[data-cat] buttons + .blog-card[data-category] anchors
 * URL deep-link: ?cat=<slug>  ('all' or absent = show all)
 */
(function () {
  "use strict";

  const chips = document.querySelectorAll(".filter-chip");
  const cards = document.querySelectorAll(".blog-card");
  if (!chips.length || !cards.length) return;

  function applyFilter(cat, updateHistory) {
    chips.forEach(function (c) {
      const active = c.dataset.cat === cat;
      c.classList.toggle("active", active);
      c.setAttribute("aria-pressed", active ? "true" : "false");
    });
    cards.forEach(function (card) {
      const match = cat === "all" || card.dataset.category === cat;
      card.style.display = match ? "" : "none";
    });
    if (updateHistory) {
      const url = new URL(location.href);
      if (cat === "all") url.searchParams.delete("cat");
      else url.searchParams.set("cat", cat);
      history.replaceState(null, "", url.pathname + url.search + url.hash);
    }
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      applyFilter(chip.dataset.cat, true);
    });
  });

  window.addEventListener("popstate", function () {
    const cat = new URL(location.href).searchParams.get("cat") || "all";
    applyFilter(cat, false);
  });

  const initialCat = new URL(location.href).searchParams.get("cat") || "all";
  applyFilter(initialCat, false);
})();
