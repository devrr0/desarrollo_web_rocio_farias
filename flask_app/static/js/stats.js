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
          day: "%e %b %Y",
          month: "%b %Y",
          year: "%Y"
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

Highcharts.chart('stats2', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Total de Actividades por Tipo'
    },
    series: [{
        name: 'Actividades',
        colorByPoint: true,
        data: [],
        showInLegend: true,
        dataLabels: {
            enabled: true,
            format: '{point.name}: {point.percentage:.1f} %'
        }
    }]
});


fetch("http://127.0.0.1:5000/get-stats-data")
  .then((response) => response.json())
  .then((data) => {
    let parsedData = data.per_day.map((item) => {
      const [year, month, day] = item.date
        .split("-")
        .map((part) => parseInt(part, 10));
      return [
        Date.UTC(year, month - 1, day), // javascript month indices start from 0 !
        item.count
      ];
    });
    let parsedData2 = data.per_theme.map((item) => ({
      name: item.theme, 
      y: item.count,
    }));

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "stats1"
    );
    const chart2 = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "stats2"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
    chart2.update({
      series: [
        {
          data: parsedData2,
        },
      ],
    });
    Highcharts.chart('stats3', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Actividades Iniciadas por Mes'
    },
    xAxis: {
        categories: data.per_time.xAxis
    },
    yAxis: {
        title: {
            text: 'Cantidad de Actividades'
        }
    },
    series: data.per_time.series
});

  })
  .catch((error) => console.error("Error:", error));