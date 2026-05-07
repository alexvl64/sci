// AOS
AOS.init({
  duration: 400,
});

//   =========== CHART JS ========
const period = [];
const dynamicTrendsValue = [];
const btcBase100 = [];
// Raw date objects, kept aligned with `period[]` indexes — used to compute
// `As of …` corner label and YTD performance captions in the hero.
const rawDates = [];
//const currentLang = window.location.pathname.includes('/en/') ? 'en' : 'fr';

async function fetchJsonData() {
  const sheetID = "1GyKIEU3OS1QQVZ-Qm7EafRlZerNs3nZNHxuFFtkpQPk";
  const gid = "0";
  const url = `https://docs.google.com/spreadsheets/d/${sheetID}/gviz/tq?tqx=out:json&gid=${gid}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const text = await response.text();

    const jsonData = JSON.parse(text.substring(47).slice(0, -2));
    const rows = jsonData.table.rows;

    rows.forEach((row) => {
      const date = row.c[0]?.v;
      const dynamic_trends_base100 = row.c[1]?.v;
      const btc_base100 = row.c[2]?.v;

      const regex = /^Date\((\d+),(\d+),(\d+)\)$/;
      const match = date.match(regex);

      let formattedDate = "";
      let parsedDate = null;
      if (match) {
        const year = match[1];
        const month = match[2] - 1;
        const day = match[3];

        parsedDate = new Date(year, month, day);

        // Utilise currentLang pour définir dynamiquement la langue
        formattedDate = parsedDate.toLocaleDateString(
          currentLang === "en" ? "en-US" : "fr-FR",
          {
            year: "numeric",
            month: "long",
          }
        );
      }

      period.push(formattedDate);
      rawDates.push(parsedDate);

      dynamicTrendsValue.push(parseFloat(dynamic_trends_base100) || 0);
      btcBase100.push(parseFloat(btc_base100) || 0);
    });

    renderChart(period, dynamicTrendsValue, btcBase100);
    populateChartCaptions(rawDates, dynamicTrendsValue, btcBase100);
  } catch (error) {
    console.error("Error fetching data:", error);
    const dataContainer = document.getElementById("data-container");
    if (dataContainer) {
      dataContainer.textContent = "Failed to load data.";
    }
  }
}

/**
 * Inject "As of <date>" + YTD/inception captions into the hero chart frame
 * if the corresponding placeholder elements exist on the page.
 *
 * - #chart-as-of           → last data point date, formatted per locale
 * - #chart-ytd-caption     → YTD perf (Dynamic Trends + BTC) since Jan 1 of current year
 * - #chart-inception-caption → full inception return for both series (if present)
 */
function populateChartCaptions(dates, dyn, btc) {
  if (!Array.isArray(dates) || dates.length === 0) return;

  // ----- AS OF (last point) -----
  const lastIdx = dates.length - 1;
  const lastDate = dates[lastIdx];
  const asOfEl = document.getElementById("chart-as-of");
  if (asOfEl && lastDate instanceof Date && !isNaN(lastDate)) {
    asOfEl.textContent = lastDate.toLocaleDateString(
      currentLang === "en" ? "en-US" : "fr-FR",
      { year: "numeric", month: "short", day: "numeric" }
    );
  }

  // ----- Helpers -----
  const fmtPct = (v) => {
    if (!isFinite(v)) return "—";
    const sign = v >= 0 ? "+" : "";
    return sign + v.toFixed(1) + " %";
  };

  // ----- YTD: from first data point of current year to last point -----
  const currentYear = (lastDate instanceof Date && !isNaN(lastDate))
    ? lastDate.getFullYear()
    : new Date().getFullYear();

  let ytdStartIdx = -1;
  for (let i = 0; i < dates.length; i++) {
    const d = dates[i];
    if (d instanceof Date && !isNaN(d) && d.getFullYear() === currentYear) {
      ytdStartIdx = i;
      break;
    }
  }

  const ytdEl = document.getElementById("chart-ytd-caption");
  if (ytdEl && ytdStartIdx !== -1 && ytdStartIdx < lastIdx) {
    const dynStart = dyn[ytdStartIdx];
    const btcStart = btc[ytdStartIdx];
    const dynEnd = dyn[lastIdx];
    const btcEnd = btc[lastIdx];
    if (dynStart > 0 && btcStart > 0) {
      const dynYtd = (dynEnd / dynStart - 1) * 100;
      const btcYtd = (btcEnd / btcStart - 1) * 100;
      const ytdLabel = currentLang === "en" ? "YTD" : "YTD";
      ytdEl.textContent = `${ytdLabel} ${currentYear}: Dynamic Trends ${fmtPct(dynYtd)} · BTC ${fmtPct(btcYtd)}`;
    }
  }

  // ----- Inception (base 100 → current value) -----
  const incEl = document.getElementById("chart-inception-caption");
  if (incEl) {
    const dynEnd = dyn[lastIdx];
    const btcEnd = btc[lastIdx];
    if (dynEnd > 0 && btcEnd > 0) {
      const dynInc = (dynEnd / 100 - 1) * 100;
      const btcInc = (btcEnd / 100 - 1) * 100;
      const incLabel = currentLang === "en" ? "Since inception" : "Depuis lancement";
      incEl.textContent = `${incLabel}: Dynamic Trends ${fmtPct(dynInc)} · BTC ${fmtPct(btcInc)}`;
    }
  }
}

function renderChart(dates, dynamicTrends, btcBase) {
  const chartTarget = document.querySelector("#chart");
  if (!chartTarget) return;

  const isMobile = window.innerWidth <= 768;
  const options = {
    series: [
      {
        name: "Dynamic Trends",
        data: dynamicTrends,
      },
      {
        name: "Bitcoin",
        data: btcBase,
      },
    ],
    chart: {
      // Hero-friendly compact heights (was 300/538 in legacy "Performance Evolution" placement).
      height: isMobile ? 280 : 460,
      type: "line",
      zoom: { enabled: false },
      toolbar: {
        show: false,
      },
      animations: {
        enabled: false,
      },
      background: "transparent",
    },
    stroke: {
      width: [2, 1.5],
      dashArray: [0, 6],
    },
    xaxis: {
      categories: dates,
      stepSize: 4,
      tickAmount: window.innerWidth <= 500 ? 3 : 5,
      offsetX: 18,
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
      labels: {
        hideOverlappingLabels: true,
        showDuplicates: false,
        rotate: 0,
        maxHeight: 50,
        style: {
          colors: "#6B7B8D",
        },
      },
    },
    yaxis: {
      logarithmic: true,
      labels: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
    grid: {
      borderColor: "#1E2530",
      yaxis: {
        lines: { show: false },
      },
      xaxis: {
        lines: { show: false },
      },
      padding: {
        left: 25,
        right: 25,
      },
    },
    colors: ["#DBD1BC", "#545047"],
    legend: {
      position: "bottom",
      horizontalAlign: "left",
      // Smaller legend for hero context (overridden via .hero-chart-canvas .apexcharts-legend-text in CSS too).
      fontSize: isMobile ? "12px" : "13px",
      labels: {
        colors: "#DBD1BC",
      },
      markers: {
        shape: "square",
        size: isMobile ? 9 : 12,
        strokeWidth: 0,
      },
    },
    tooltip: {
      theme: "dark",
    },
  };

  const chart = new ApexCharts(chartTarget, options);
  chart.render();
}
fetchJsonData();
