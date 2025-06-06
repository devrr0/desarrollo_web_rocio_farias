Highcharts.chart('stats1', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Cantidad de Actividades por Día'
    },
    xAxis: {
        type: "datetime",
        dateTimeLabelFormats: {
        month: "%b %e, %Y",
        },
        title: {
        text: "Fecha",
        },
    },
    yAxis: {
        title: {
            text: 'Cantidad de Actividades'
        },
        allowDecimals: false
    },
    series: [{
        name: 'Actividades',
        data: [] 
    }]
});

fetch("http://127.0.0.1:5000/get-stats-data")
  .then((response) => response.json())
  .then((data) => {
    let parsedData = data.map((item) => {
      const [year, month, day] = item.date
        .split("-")
        .map((part) => parseInt(part, 10));
      return [
        Date.UTC(year, month - 1, day), // javascript month indices start from 0 !
        item.count,
      ];
    });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "stats1"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));