from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Dados iniciais
books = [
    {"id": 1, "title": "Livro 1", "author": "Autor 1", "sentiment": "positivo"},
    {"id": 2, "title": "Livro 2", "author": "Autor 2", "sentiment": "negativo"},
    {"id": 3, "title": "Livro 3", "author": "Autor 3", "sentiment": "neutro"}
]

# Rota para obter todos os livros
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Rota para obter um livro por ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Livro não encontrado'}), 404

# Rota para criar um novo livro
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Rota para atualizar um livro existente
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json['title']
        book['author'] = request.json['author']
        return jsonify(book)
    return jsonify({'message': 'Livro não encontrado'}), 404

# Rota para excluir um livro
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Livro removido'})
    return jsonify({'message': 'Livro não encontrado'}), 404

# Rota para exibir o gráfico de sentimento
@app.route('/chart')
def show_sentiment_chart():
    sentiment_count = {
        "positivo": 0,
        "negativo": 0,
        "neutro": 0
    }
    for book in books:
        sentiment = book.get("sentiment")
        if sentiment in sentiment_count:
            sentiment_count[sentiment] += 1

    total_books = len(books)
    sentiment_percentages = {
        "positivo": (sentiment_count["positivo"] / total_books) * 100,
        "negativo": (sentiment_count["negativo"] / total_books) * 100,
        "neutro": (sentiment_count["neutro"] / total_books) * 100
    }

    return render_template('chart.html', sentiment_percentages=sentiment_percentages)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run()
