from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)

# Carregar os DataFrames
dados_preprocessados = pd.read_csv('dados_preprocessados.csv')
remocao_autor = pd.read_csv('remocaoautor.csv')

#ROTAS

# Rota principal para verificar se a API está conectada
@app.route('/', methods=['GET'])
def api_status():
    return jsonify({'status': 'API conectada'})





# Rota para contar a quantidade de comentários no DataFrame dados_preprocessados
@app.route('/quantidade-comentarios', methods=['GET'])
def quantidade_comentarios():
    quantidade = len(dados_preprocessados)
    return jsonify({'quantidade_comentarios': quantidade})

# Rota para obter o principal sentimento da base
import numpy as np

# Rota para obter dados relacionando quantidade de comentários e principal sentimento
@app.route('/dados-relacionados', methods=['GET'])
def dados_relacionados():
    sentimentos = dados_preprocessados['sentimento'].value_counts()
    dados = []
    for sentimento, quantidade in sentimentos.items():
        dados.append({'sentimento': sentimento, 'quantidade_comentarios': quantidade})
    return jsonify({'dados_relacionados': dados})

@app.route('/detalhamento-mensal', methods=['GET'])
def detalhamento_mensal():
    mes = request.args.get('mes')  # Parâmetro para alternar entre os meses
    data_selecionada = dados_preprocessados[dados_preprocessados['data'].dt.month == int(mes)]
    
    sentimentos_mensais = data_selecionada['sentimento'].value_counts()
    quantidade_negativo = sentimentos_mensais.get('NEGATIVO', 0)
    quantidade_positivo = sentimentos_mensais.get('POSITIVO', 0)
    quantidade_neutro = sentimentos_mensais.get('NEUTRO', 0)
    
    return jsonify({
        'mes': mes,
        'quantidade_negativo': quantidade_negativo,
        'quantidade_positivo': quantidade_positivo,
        'quantidade_neutro': quantidade_neutro
    })

@app.route('/analise-sentimento-mensal', methods=['GET'])
def analise_sentimento_mensal():
    comentarios_por_mes = dados_preprocessados['data'].dt.to_period('M').value_counts().sort_index()
    
    return jsonify(comentarios_por_mes.to_dict())

@app.route('/interacoes', methods=['GET'])
def interacoes():
    comentarios_por_mes = dados_preprocessados['data'].dt.to_period('M').value_counts().sort_index()
    sentimentos = dados_preprocessados['sentimento'].value_counts()
    
    return jsonify({
        'comentarios_por_mes': comentarios_por_mes.to_dict(),
        'sentimentos': sentimentos.to_dict()
    })

# Rota para gerar um gráfico de rosca com a quantidade de cada sentimento
@app.route('/grafico-rosca', methods=['GET'])
def grafico_rosca():
    sentimentos = dados_preprocessados['sentimento'].value_counts()

    # Configuração do gráfico
    plt.figure(figsize=(6, 6))
    plt.pie(sentimentos.values, labels=sentimentos.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Distribuição de Sentimentos')
    
    # Salvar o gráfico em um arquivo temporário
    chart_file = 'grafico_rosca.png'
    plt.savefig(chart_file)
    plt.close()
    
    return render_template('grafico.html', chart_file=chart_file)

@app.route('/principal-sentimento', methods=['GET'])
def principal_sentimento():
    sentimentos = dados_preprocessados['sentimento'].value_counts()
    principal = sentimentos.idxmax()
    quantidade = sentimentos[principal]
    
    try:
        principal_int = int(principal)
    except ValueError:
        principal_int = None

    # Converter para int se for um valor numpy.int64
    if isinstance(principal_int, np.int64):
        principal_int = int(principal_int)
    
    return jsonify({'principal_sentimento': principal_int, 'quantidade': quantidade})

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

@app.route('/principal-palavras', methods=['GET'])
def principal_palavras():
    stop_words = set(stopwords.words('portuguese'))  # Definindo as stopwords em português
    palavras_indesejadas = ['não', 'btgpactual', 'btg', 'voce', 'sobre', 'dia', 'pactual','nao',
                            'banco', 'ja', 'ja', 'sao', 'são', 'link', 'só', 'so', 'melhor','hoje',
                            'hj', 'todos','pra','tambem','todos','r','maior', 'evento', 'tudo', 'ter',
                            'ainda', 'fazer', 'ter','bio','investimento', 'voces', 'vocês','aqui','ano',
                            'time','sempre','obrigado','pode','agora', 'ate','até','semana','investir']
    textos = dados_preprocessados['texto']
    
    # Remoção de stopwords e contagem de palavras
    palavras = {}
    for texto in textos:
        if isinstance(texto, str):  # Verifica se o valor é uma string
            tokens = word_tokenize(texto.lower())  # Tokenização e conversão para minúsculas
            palavras_filtradas = [palavra for palavra in tokens if palavra.isalpha() and palavra not in stop_words and palavra not in palavras_indesejadas]
            
            for palavra in palavras_filtradas:
                if palavra in palavras:
                    palavras[palavra] += 1
                else:
                    palavras[palavra] = 1
    
    # Ordenando as palavras por frequência
    palavras_principais = sorted(palavras.items(), key=lambda x: x[1], reverse=True)[:10]  # Selecionando as 10 palavras mais frequentes
    
    return jsonify(palavras_principais)


if __name__ == '__main__':
    app.run()
