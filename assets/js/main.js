// AOS — once: true ensures animations play exactly once and elements remain
// visible after their first reveal, even if scrolled out and back in. Without
// this, AOS may re-apply its initial hidden state (opacity:0, translateX) on
// re-entry into the viewport — the homepage's hero-content-left and other
// data-aos sections were disappearing on scroll-up after a FR→EN switch
// because the browser restored a non-zero scroll position and AOS scanned
// elements as out-of-viewport at init time.
AOS.init({
  duration: 400,
  once: true,
});

//   =========== CHART JS ========
const period = [];
const dynamicTrendsValue = [];
const btcBase100 = [];
//const currentLang = window.location.pathname.includes('/en/') ? 'en' : 'fr';

async function fetchJsonData() {
  // SparkCore-published JSON (R2, via the Pages Function) — same Dynamic Trends
  // base-100 series the home chart used to read from the public Google Sheet.
  try {
    const response = await fetch("/data/funds/dynamic-trends.json", {
      cache: "no-cache",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const d = await response.json();
    const locale = currentLang === "en" ? "en-US" : "fr-FR";

    (d.chart_base100 || []).forEach((p) => {
      period.push(
        new Date(p.date + "T00:00:00").toLocaleDateString(locale, {
          year: "numeric",
          month: "long",
        })
      );
      dynamicTrendsValue.push(p.fund);
      btcBase100.push(p.benchmark);
    });

    renderChart(period, dynamicTrendsValue, btcBase100);
  } catch (error) {
    console.error("Error fetching data:", error);
    document.getElementById("data-container").textContent =
      "Failed to load data.";
  }
}

function renderChart(dates, dynamicTrends, btcBase) {
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
      height: window.innerWidth <= 768 ? 300 : 538,
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
      labels: {
        colors: "#DBD1BC",
      },
      markers: {
        shape: "square",
        size: window.innerWidth <= 768 ? 10 : 14,
        strokeWidth: 0,
      },
    },
    tooltip: {
      theme: "dark",
    },
  };

  const chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();
}

// Lazy-load: defer apexcharts download + chart render until #chart enters viewport.
// Reason: ApexCharts is ~530 KB uncompressed and accounted for ~351 ms of long-task
// time on mobile; users rarely scroll to the chart, and even when they do, a 300 px
// rootMargin gives enough lead time to fetch + render before it is on-screen.
function loadApexCharts() {
  if (typeof ApexCharts !== "undefined") return Promise.resolve();
  return new Promise(function (resolve, reject) {
    var s = document.createElement("script");
    s.src = "https://cdn.jsdelivr.net/npm/apexcharts";
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });
}

(function () {
  var chartEl = document.querySelector("#chart");
  if (!chartEl) return;
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
          io.disconnect();
          loadApexCharts().then(fetchJsonData).catch(function (err) {
            console.error("Failed to load ApexCharts:", err);
          });
          return;
        }
      }
    }, { rootMargin: "300px" });
    io.observe(chartEl);
  } else {
    loadApexCharts().then(fetchJsonData);
  }
})();