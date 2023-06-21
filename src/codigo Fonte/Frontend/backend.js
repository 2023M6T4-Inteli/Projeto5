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
