// Função para exibir a lista de livros
function showBookList() {
    fetch('/books')
        .then(response => response.json())
        .then(data => {
            const bookList = document.getElementById('bookList');
            bookList.innerHTML = '';

            data.forEach(book => {
                const listItem = document.createElement('li');
                listItem.textContent = `Livro: ${book.title}, Autor: ${book.author}`;
                bookList.appendChild(listItem);
            });
        });
}

// Função para exibir o gráfico de sentimento
function showSentimentChart() {
    window.location.href = '/chart';
}

// Adicionar evento de clique para o botão "Imprimir Lista de Livros"
document.getElementById('showBooksBtn').addEventListener('click', showBookList);

// Adicionar evento de clique para o botão "Gerar Gráfico de Sentimentos"
document.getElementById('showSentimentChartBtn').addEventListener('click', showSentimentChart);
