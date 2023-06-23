// Gráfico de Barras

const dataBarras = {
  labels: ['Negativo', 'Positivo', 'Neutro'],
  datasets: [
    {
      label:  '',
      data: [192, 140, 48],
      backgroundColor: ['#FF3333', '#0DBC53', '#B5B5B5']
    }
  ]
};

const optionsBarras = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      beginAtZero: true
    },
    y: {
      beginAtZero: true
    }
  },
  plugins: {
    legend: {
      display: true,
      labels: {
        boxWidth: 0 // Definir a largura da caixa de cor como 0 para removê-la
      }
    }
  }
};

const ctxBarras = document.getElementById('g6Barras').getContext('2d');
const myChartBarras = new Chart(ctxBarras, {
  type: 'bar',
  data: dataBarras,
  options: optionsBarras
});
