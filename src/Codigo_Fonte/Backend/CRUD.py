from flask import Flask, jsonify, request, render_template
from collections import Counter
import matplotlib.pyplot as plt

app = Flask(__name__)

# Dados iniciais (exemplo)
financial_product_comments = [
    {"id": 1, "comment": "Esse produto financeiro é incrível!", "sentiment": "positivo"},
    {"id": 2, "comment": "Não estou satisfeito com os retornos desse produto.", "sentiment": "negativo"},
    {"id": 3, "comment": "A taxa de juros desse produto é muito alta.", "sentiment": "negativo"}
]

# Rota principal para verificar se a API está rodando
@app.route('/', methods=['GET'])
def api_status():
    return jsonify({'status': 'API está em execução'})

# Rota para pegar todos os comentários
@app.route('/comments', methods=['GET'])
def get_all_comments():
    return jsonify(financial_product_comments)

# Rota para pegar um comentário específico pelo ID
@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = next((c for c in financial_product_comments if c['id'] == comment_id), None)
    if comment:
        return jsonify(comment)
    return jsonify({'message': 'Comentário não encontrado'}), 404

# Rota para análise de sentimento de palavras específicas
@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    words = request.json['words']
    sentiment_scores = []

    for word in words:
        sentiment_scores.append(get_sentiment_score(word))

    return jsonify(sentiment_scores)

# Rota para criar um gráfico das palavras mais procuradas nos comentários
@app.route('/chart', methods=['GET'])
def create_word_frequency_chart():
    words = [word.lower() for comment in financial_product_comments for word in comment['comment'].split()]
    word_counts = Counter(words).most_common(10)
    top_words = [word[0] for word in word_counts]
    word_frequencies = [word[1] for word in word_counts]

    plt.bar(top_words, word_frequencies)
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.title('Palavras Mais Procuradas nos Comentários')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvar o gráfico em um arquivo temporário
    chart_file = 'word_frequency_chart.png'
    plt.savefig(chart_file)
    plt.close()

    return render_template('chart.html', chart_file=chart_file)

# Função auxiliar para obter o sentimento de uma palavra
def get_sentiment_score(word):
    # Lógica para obter o sentimento da palavra
    # Substitua este trecho com a sua própria implementação de análise de sentimento

    # Exemplo simples: atribuir positivo a palavras com mais de 3 letras, negativo caso contrário e neutro caso seja uma palavra vazia
    if len(word) > 3:
        return 'positivo'
    elif len(word) > 0:
        return 'negativo'
    else:
        return 'neutro'

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run()
