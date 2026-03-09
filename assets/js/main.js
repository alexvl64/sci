// AOS
AOS.init({
  duration: 400,
});

//   =========== CHART JS ========
const period = [];
const dynamicTrendsValue = [];
const btcBase100 = [];
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
      if (match) {
        const year = match[1];
        const month = match[2] - 1;
        const day = match[3];

        const parsedDate = new Date(year, month, day);

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

      dynamicTrendsValue.push(parseFloat(dynamic_trends_base100) || 0);
      btcBase100.push(parseFloat(btc_base100) || 0);
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
fetchJsonData();