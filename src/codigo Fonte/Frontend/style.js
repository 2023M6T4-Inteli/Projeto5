// Gráfico Rosca
var posicaoMaior = 0;

// Função para criar/atualizar o gráfico de rosca
function criarGraficoRosca(data) {
  var ctxRosca = document.getElementById('g4Rosca').getContext('2d');

  // Extrair os valores de quantidade_comentarios do objeto retornado
  var valoresComentarios = data.dados_relacionados.map(item => item.quantidade_comentarios);

  console.log(valoresComentarios);

  var myChartRosca = new Chart(ctxRosca, {
    type: 'doughnut',
    data: {
      labels: ['Negativo', 'Positivo', 'Neutro'],
      datasets: [{
        data: valoresComentarios, // Atualize os dados com os valores de quantidade_comentarios
        backgroundColor: ['#FF3333', '#0DBC53', '#B5B5B5']
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            usePointStyle: true,
            boxWidth: 8,
            font: {
              size: 8
            }
          }
        }
      }
    }
  });

  var maiorValor = valoresComentarios[0];

  for (var i = 1; i < valoresComentarios.length; i++) {
    if (valoresComentarios[i] > maiorValor) {
      maiorValor = valoresComentarios[i];
      posicaoMaior = i;
    }
  }

  console.log("A posição do maior valor é:", posicaoMaior);

  categoria(posicaoMaior); // Chamar a função categoria dentro de criarGraficoRosca

  return posicaoMaior;
}

function categoria(posicaoMaior) {
  if (posicaoMaior == 0) {
    return "Negativo";
  } else if (posicaoMaior == 1) {
    return "Positivo";
  } else if (posicaoMaior == 2) {
    return "Neutro";
  }
}

// var posicaoMaior = criarGraficoRosca(data);
var resultadoCategoria = categoria(posicaoMaior);
console.log(resultadoCategoria);

document.getElementById('principalSentimento').innerHTML = resultadoCategoria;

// Gráfico Linha

const dataLinha = {
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [
      {
        label: 'Positivo',
        data: [15, 12, 20, 18, 25, 22, 28, 30, 32, 28, 20, 18],
        borderColor: '#0DBC53',
        backgroundColor: '#0DBC53'
      },
      {
        label: 'Negativo',
        data: [8, 10, 6, 12, 9, 15, 11, 13, 10, 14, 9, 7],
        borderColor: '#FF3333',
        backgroundColor: '#FF3333'
      },
      {
        label: 'Neutro',
        data: [5, 3, 4, 6, 8, 7, 4, 6, 3, 5, 4, 6],
        borderColor: '#B5B5B5',
        backgroundColor: '#B5B5B5'
      }
    ]
  };
  
  const optionsLinha = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'bottom',
        labels: {
          usePointStyle: true,
          boxWidth: 8,
          generateLabels: function (chart) {
            const originalLabels = Chart.defaults.plugins.legend.labels.generateLabels(chart);
            originalLabels.forEach(label => {
              label.pointStyle = 'circle'; // Define o estilo do ponto como círculo
              label.padding = 8; // Espaçamento entre as bolinhas
            });
            return originalLabels;
          },
          font: {
            size: 8
          }
        }
      }
    }
  };
  
  const ctxLinha = document.getElementById('g5Linha').getContext('2d');
  const myChartLinha = new Chart(ctxLinha, {
    type: 'line',
    data: dataLinha,
    options: optionsLinha
  });
  
  
// Gráfico de Barras

const dataBarras = {
    labels: ['Negativo', 'Positivo', 'Neutro'],
    datasets: [
      {
        label:  '',
        data: [10, 15, 5],
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
  
// Gráfico de Dispersão  

  document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('g7Dispersao').getContext('2d');
  
    var negativo = [
        
        { x: 2, y: 5 }, 
        { x: 2.5, y: 7 }, 
        { x: 4, y: 8 }, 
        { x: 1, y: 3 }, 
        { x: 5, y: 9 },
        { x: 1, y: 3.09 },
        { x: 12, y: 27.78},
        { x: 7, y: 5.51 },
        { x: 6, y: 9.14 },
        { x: 11, y: 22.47},
        { x: 3, y: 18.07 },
        { x: 5, y: 29.84 },
        { x: 9, y: 8.89 },
        { x: 4, y: 26.31 },
        { x: 8, y: 13.46 },
    
    ];

    var neutro = [
        
        { x: 6, y: 7 }, 
        { x: 3, y: 2 }, 
        { x: 8, y: 4 },
        { x: 9.4, y: 13.27 },
        { x: 3.2, y: 28.19 },
        { x: 11.7, y: 0.46 },
        { x: 7.1, y: 22.91 },
        { x: 6.4, y: 27.33 },
        { x: 10.5, y: 16.65 },
        { x: 5.9, y: 24.01 },
        { x: 12, y: 10.12 },
        { x: 9.5, y: 12.56 },
        { x: 2.2, y: 21.74 },
    
    ];
    var positivo = [

        { x: 9, y: 1 }, 
        { x: 7, y: 6 }, 
        { x: 10, y: 3 }, 
        { x: 5.3, y: 3 },
        { x: 4, y: 11.89 },
        { x: 7, y: 23.04 },
        { x: 10, y: 15.28 },
        { x: 3, y: 2.34 },
        { x: 8, y: 14.93 },
        { x: 6, y: 7.61 },
        { x: 2, y: 25.57 },
        { x: 11, y: 6.79 },
        { x: 9, y: 19.12 },
        { x: 5, y: 28.76 },
    
    ];
  
    var scatterChart = new Chart(ctx, {
      type: 'scatter',
      data: {
        datasets: [
          {
            label: 'Negativo',
            data: negativo,
            backgroundColor: '#FF3333'
          },
          {
            label: 'Neutro',
            data: neutro,
            backgroundColor: '#B5B5B5'
          },
          {
            label: 'Positivo',
            data: positivo,
            backgroundColor: '#0DBC53'
          }
        ]
      },
      options: {
        scales: {
          x: {
            type: 'linear',
            position: 'bottom',
            ticks: {
              stepSize: 1,
              min: 1,
              max: 12
            }
          },
          y: {
            type: 'linear',
            position: 'left'
          }
        },
        plugins: {
          legend: {
            display: true,
            position: 'bottom',
            labels: {
              usePointStyle: true,
              boxWidth: 6,
              font: {
                size: 6
              }
            }
          }
        }
      }
    });
  });
  
