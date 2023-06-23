from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
CORS(app)

# Carregar os DataFrames
dados_preprocessados = pd.read_csv('dados_preprocessados.csv')
remocao_autor = pd.read_csv('remocaoautor.csv')

#ROTAS

# Rota principal para verificar se a API está conectada
@app.route('/', methods=['GET'])
def api_status():
    return jsonify({'status': 'API conectada'})



# Rota para contar a quantidade de comentários no DataFrame dados_preprocessados
@app.route('/quantidadecomentarios', methods=['GET'])
def quantidade_comentarios():
    quantidade = len(dados_preprocessados)
    return jsonify({'quantidade_comentarios': quantidade})

# Rota para obter o principal sentimento da base
import numpy as np
sentimentos = dados_preprocessados['sentimento'].value_counts()


# Rota para obter dados relacionando quantidade de comentários e principal sentimento
@app.route('/dados-relacionados', methods=['GET'])
def dados_relacionados():
    sentimentos = dados_preprocessados['sentimento'].value_counts()
    dados = []
    for sentimento, quantidade in sentimentos.items():
        dados.append({'sentimento': sentimento, 'quantidade_comentarios': quantidade})
    return jsonify({'dados_relacionados': dados})


@app.route('/palavras', methods=['GET'])
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

import requests




from collections import OrderedDict

from operator import itemgetter

@app.route('/sentimentoPalavra', methods=['GET'])
def comentarios_por_palavra():
    # Obtém as 10 palavras principais da rota '/palavras'
    response = requests.get('http://127.0.0.1:5000/palavras')
    palavras_principais = response.json()

    # Cria um dicionário para mapear cada palavra ao seu sentimento
    sentimento_palavras = {}

    for palavra, _ in palavras_principais:
        sentimento_palavras[palavra] = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}

    for i, comentario in enumerate(dados_preprocessados['texto']):
        if isinstance(comentario, str):
            tokens = word_tokenize(comentario.lower())
            for palavra in sentimento_palavras:
                if palavra in tokens:
                    sentimento = dados_preprocessados.loc[i, 'sentimento'].upper()
                    sentimento_palavras[palavra][sentimento] += 1

    # Cria uma lista de palavras ordenadas em ordem decrescente com base nas aparições
    palavras_ordenadas = sorted(palavras_principais, key=itemgetter(1), reverse=True)

    # Adiciona a contagem de aparições de cada palavra em cada categoria de sentimento
    resultado_simplificado = []

    for palavra, aparicoes in palavras_ordenadas:
        resultado_simplificado.append({
            'palavra': palavra,
            'POSITIVE': sentimento_palavras[palavra]['POSITIVE'],
            'NEGATIVE': sentimento_palavras[palavra]['NEGATIVE'],
            'NEUTRAL': sentimento_palavras[palavra]['NEUTRAL'],
            'aparicoes': aparicoes
        })

    return jsonify(resultado_simplificado)


















# @app.route('/detalhamento-mensal', methods=['GET'])
# def detalhamento_mensal():
#     mes = request.args.get('mes')  # Parâmetro para alternar entre os meses
#     data_selecionada = dados_preprocessados[dados_preprocessados['data'].dt.month == int(mes)]
    
#     sentimentos_mensais = data_selecionada['sentimento'].value_counts()
#     quantidade_negativo = sentimentos_mensais.get('NEGATIVO', 0)
#     quantidade_positivo = sentimentos_mensais.get('POSITIVO', 0)
#     quantidade_neutro = sentimentos_mensais.get('NEUTRO', 0)
    
#     return jsonify({
#         'mes': mes,
#         'quantidade_negativo': quantidade_negativo,
#         'quantidade_positivo': quantidade_positivo,
#         'quantidade_neutro': quantidade_neutro
#     })

# @app.route('/analise-sentimento-mensal', methods=['GET'])
# def analise_sentimento_mensal():
#     comentarios_por_mes = dados_preprocessados['data'].dt.to_period('M').value_counts().sort_index()
    
#     return jsonify(comentarios_por_mes.to_dict())

# @app.route('/interacoes', methods=['GET'])
# def interacoes():
#     comentarios_por_mes = dados_preprocessados['data'].dt.to_period('M').value_counts().sort_index()
#     sentimentos = dados_preprocessados['sentimento'].value_counts()
    
#     return jsonify({
#         'comentarios_por_mes': comentarios_por_mes.to_dict(),
#         'sentimentos': sentimentos.to_dict()
#     })

# Rota para gerar um gráfico de rosca com a quantidade de cada sentimento
# @app.route('/grafico-rosca', methods=['GET'])
# def grafico_rosca():
#     sentimentos = dados_preprocessados['sentimento'].value_counts()

#     # Configuração do gráfico
#     plt.figure(figsize=(6, 6))
#     plt.pie(sentimentos.values, labels=sentimentos.index, autopct='%1.1f%%', startangle=90)
#     plt.axis('equal')
#     plt.title('Distribuição de Sentimentos')
    
#     # Salvar o gráfico em um arquivo temporário
#     chart_file = 'grafico_rosca.png'
#     plt.savefig(chart_file)
#     plt.close()
    
    # return render_template('grafico.html', chart_file=chart_file)




from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize




if __name__ == '__main__':
    app.run()
