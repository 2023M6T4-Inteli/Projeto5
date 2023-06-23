fetch('http://127.0.0.1:5000/quantidadecomentarios', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data); // Verifique o objeto retornado no console

    // Ajuste para acessar o valor correto
    document.getElementById('quantComentarios').innerHTML = data.quantidade_comentarios;
  })
  .catch(error => {
    // Em caso de erro na chamada GET
    console.error('Erro:', error);
  });

  // Chamada GET para obter os dados relacionados
fetch('http://127.0.0.1:5000/dados-relacionados', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    // Aqui você pode manipular os dados retornados pela chamada GET

    // Atualize o gráfico de rosca com os novos dados
    criarGraficoRosca(data);

  })
  .catch(error => {
    // Em caso de erro na chamada GET
    console.error('Erro:', error);
  });


  fetch('http://127.0.0.1:5000/palavras', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data); // Verifique o objeto retornado no console

    // Atualizar o conteúdo dos elementos HTML
    for (let i = 0; i < data.length; i++) {
      document.getElementById(`palavras${i + 1}`).innerHTML = data[i][0];
    }
  })
  .catch(error => {
    // Em caso de erro na chamada GET
    console.error('Erro:', error);
  });


  
  fetch('http://127.0.0.1:5000/sentimentoPalavra', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data);

    // Iterar sobre as palavras e aplicar as cores correspondentes
    let i = 1;
    for (const palavra in data) {
      const sentimento = data[palavra];

      // Obter a categoria com o maior valor
      let maxCategoria = '';
      let maxValor = 0;
      for (const categoria in sentimento) {
        if (categoria !== 'palavra' && categoria !== 'aparicoes') {
          if (sentimento[categoria] > maxValor) {
            maxCategoria = categoria;
            maxValor = sentimento[categoria];
          }
        }
      }

      const corSentimento = document.getElementById('corSentimento' + i);

      if (maxCategoria === 'POSITIVE') {
        corSentimento.style.backgroundColor = 'green';
      } else if (maxCategoria === 'NEGATIVE') {
        corSentimento.style.backgroundColor = 'red';
      } else if (maxCategoria === 'NEUTRAL') {
        corSentimento.style.backgroundColor = 'gray';
      }

      i++;
    }
  })
  .catch(error => {
    // Em caso de erro na chamada GET
    console.error('Erro:', error);
  });



  fetch('http://127.0.0.1:5000/sentimento-mes', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data);

    // Defina a ordem desejada dos meses
    var ordemMeses = [
      'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];

    // Crie um objeto vazio para armazenar os sentimentos por mês na ordem correta
    var sentimentosPorMesOrdenados = {};

    // Preencha o objeto com os sentimentos por mês na ordem correta
    ordemMeses.forEach(mes => {
      sentimentosPorMesOrdenados[mes] = data[mes] || {};
    });

    // Extrair os meses e os dados para cada categoria do objeto ordenado
    const months = Object.keys(sentimentosPorMesOrdenados);
    const positiveData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_positivo);
    const negativeData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_negativo);
    const neutralData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_neutro);

    // Atualizar os valores da variável dataLinha com os dados extraídos
    dataLinha.labels = months;
    dataLinha.datasets[0].data = positiveData;
    dataLinha.datasets[1].data = negativeData;
    dataLinha.datasets[2].data = neutralData;

    // Verificar se um gráfico já existe e destruí-lo
    const chartElement = document.getElementById('g5Linha');
    if (chartElement) {
      Chart.getChart(chartElement).destroy();
    }

    // Criar o gráfico de linhas usando a biblioteca Chart.js
    const ctx = chartElement.getContext('2d');
    const options = {
      responsive: true,
      maintainAspectRatio: false,
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
      },
      scales: {
        x: {
          grid: {
            display: false
          },
          ticks: {
            font: {
              size: 8 // Reduza o tamanho da fonte dos meses
            }
          }
        },
        y: {
          beginAtZero: true,
          grid: {
            color: 'rgba(0, 0, 0, 0.1)'
          },
          ticks: {
            font: {
              size: 8 // Reduza o tamanho da fonte do eixo Y
            },
            precision: 0,
            min: 0,
            maxTicksLimit: 4
          }
        }
      }
    };

    // Criar o gráfico de linhas usando a biblioteca Chart.js com as opções de configuração
    new Chart(ctx, {
      type: 'line',
      data: dataLinha,
      options: options
    });
  })
  .catch(error => {
    console.error('Erro:', error);
  });







  fetch('http://127.0.0.1:5000/sentimento-mes', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data);

    // Defina a ordem desejada dos meses
    var ordemMeses = [
      'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];

    // Crie um objeto vazio para armazenar os sentimentos por mês na ordem correta
    var sentimentosPorMesOrdenados = {};

    // Preencha o objeto com os sentimentos por mês na ordem correta
    ordemMeses.forEach(mes => {
      sentimentosPorMesOrdenados[mes] = data[mes] || {};
    });

    // Extrair os meses e os dados para cada categoria do objeto ordenado
    const months = Object.keys(sentimentosPorMesOrdenados);
    const positiveData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_positivo);
    const negativeData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_negativo);
    const neutralData = months.map(month => sentimentosPorMesOrdenados[month].quantidade_neutro);

    // Atualizar os valores da variável dataLinha com os dados extraídos
    dataLinha.labels = months;
    dataLinha.datasets[0].data = positiveData;
    dataLinha.datasets[1].data = negativeData;
    dataLinha.datasets[2].data = neutralData;

    // Verificar se um gráfico já existe e destruí-lo
    const chartElement = document.getElementById('g5Linha');
    if (chartElement) {
      Chart.getChart(chartElement).destroy();
    }

    // Criar o gráfico de linhas usando a biblioteca Chart.js
    const ctx = chartElement.getContext('2d');
    const options = {
      responsive: true,
      maintainAspectRatio: false,
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
      },
      scales: {
        x: {
          grid: {
            display: false
          },
          ticks: {
            font: {
              size: 8 // Reduza o tamanho da fonte dos meses
            }
          }
        },
        y: {
          beginAtZero: true,
          grid: {
            color: 'rgba(0, 0, 0, 0.1)'
          },
          ticks: {
            font: {
              size: 8 // Reduza o tamanho da fonte do eixo Y
            },
            precision: 0,
            min: 0,
            maxTicksLimit: 4
          }
        }
      }
    };

    // Criar o gráfico de linhas usando a biblioteca Chart.js com as opções de configuração
    new Chart(ctx, {
      type: 'line',
      data: dataLinha,
      options: options
    });

    // Adicione a lógica para selecionar um mês
    const selectMonth = document.getElementById('selectMesesG6');
    selectMonth.addEventListener('change', () => {
      const selectedMonth = selectMonth.value;
      const selectedData = sentimentosPorMesOrdenados[selectedMonth];

      // Verificar os valores de positivo, negativo e neutro para o mês selecionado
      const quantidadePositivo = selectedData ? selectedData.quantidade_positivo : 0;
      const quantidadeNegativo = selectedData ? selectedData.quantidade_negativo : 0;
      const quantidadeNeutro = selectedData ? selectedData.quantidade_neutro : 0;

      // Atualizar os valores do gráfico de barras com os dados extraídos
      dataBarras.datasets[0].data = [quantidadeNegativo, quantidadePositivo, quantidadeNeutro];

      // Atualizar o rótulo do gráfico de barras com o mês selecionado
      dataBarras.datasets[0].label = selectedMonth;

      // Atualizar o gráfico de barras usando a biblioteca Chart.js
      myChartBarras.update();
    });
  });


//   // Faz a requisição fetch para obter os dados de comentários por dia
// fetch('http://127.0.0.1:5000/comentarios-dia')
// .then(response => response.json())
// .then(data => {
//   console.log(data);

//   // Extrair os dados de quantidade de comentários e sentimentos para cada tipo de interação
//   const comentariosPositivos = data.map(item => item.comentario_positivo);
//   const comentariosNegativos = data.map(item => item.comentario_negativo);
//   const comentariosNeutros = data.map(item => item.comentario_neutro);
//   const marcacoesPositivas = data.map(item => item.marcacao_positivo);
//   const marcacoesNegativas = data.map(item => item.marcacao_negativo);
//   const marcacoesNeutras = data.map(item => item.marcacao_neutro);
//   const respostasPositivas = data.map(item => item.resposta_positivo);
//   const respostasNegativas = data.map(item => item.resposta_negativo);
//   const respostasNeutras = data.map(item => item.resposta_neutro);

//   // Atualizar os valores do gráfico de barras com os dados extraídos
//   dataBarras.datasets[0].data = [
//     comentariosPositivos.reduce((a, b) => a + b, 0),
//     comentariosNegativos.reduce((a, b) => a + b, 0),
//     comentariosNeutros.reduce((a, b) => a + b, 0)
//   ];
//   dataBarras.datasets[1].data = [
//     marcacoesPositivas.reduce((a, b) => a + b, 0),
//     marcacoesNegativas.reduce((a, b) => a + b, 0),
//     marcacoesNeutras.reduce((a, b) => a + b, 0)
//   ];
//   dataBarras.datasets[2].data = [
//     respostasPositivas.reduce((a, b) => a + b, 0),
//     respostasNegativas.reduce((a, b) => a + b, 0),
//     respostasNeutras.reduce((a, b) => a + b, 0)
//   ];

//   // Verificar se um gráfico já existe e destruí-lo
//   const chartElement = document.getElementById('graficoBarras');
//   if (chartElement) {
//     Chart.getChart(chartElement).destroy();
//   }

//   // Criar o gráfico de barras usando a biblioteca Chart.js
//   const ctx = chartElement.getContext('2d');
//   const options = {
//     responsive: true,
//     maintainAspectRatio: false,
//     plugins: {
//       legend: {
//         display: true,
//         position: 'bottom',
//         labels: {
//           usePointStyle: true,
//           boxWidth: 8,
//           font: {
//             size: 8
//           }
//         }
//       }
//     },
//     scales: {
//       x: {
//         grid: {
//           display: false
//         },
//         ticks: {
//           font: {
//             size: 8 // Reduza o tamanho da fonte dos meses
//           }
//         }
//       },
//       y: {
//         beginAtZero: true,
//         grid: {
//           color: 'rgba(0, 0, 0, 0.1)'
//         },
//         ticks: {
//           font: {
//             size: 8 // Reduza o tamanho da fonte do eixo Y
//           },
//           precision: 0,
//           min: 0,
//           maxTicksLimit: 4
//         }
//       }
//     }
//   };

//   // Criar o gráfico de barras usando a biblioteca Chart.js com as opções de configuração
//   new Chart(ctx, {
//     type: 'bar',
//     data: dataBarras,
//     options: options
//   });
// });

