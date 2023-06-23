from flask import Flask, jsonify
from flask_cors import CORS
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
from collections import OrderedDict
from operator import itemgetter
import re
from collections import Counter
import numpy as np
import calendar
import locale

matplotlib.use('Agg')

app = Flask(__name__)
CORS(app)

# Carregar os DataFrames
dados_preprocessados = pd.read_csv('dados_preprocessados.csv')
remocao_autor = pd.read_csv('base_tratada.csv')

# #ROTAS

# Rota principal para verificar se a API está conectada
@app.route('/', methods=['GET'])
def api_status():
    return jsonify({'status': 'API conectada'})



# Rota para contar a quantidade de comentários no DataFrame dados_preprocessados
@app.route('/quantidadecomentarios', methods=['GET'])
def quantidade_comentarios():
    quantidade = len(dados_preprocessados)
    return jsonify({'quantidade_comentarios': quantidade})

# # Rota para obter o principal sentimento da base
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




@app.route('/sentimento-mes', methods=['GET'])
def sentimento_por_mes():
    sentimentos_por_mes = {}

    # Definir o locale para o idioma português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    # Converter a coluna 'data' para o formato correto de data
    remocao_autor['data'] = pd.to_datetime(remocao_autor['data'], format='%d-%m-%Y', errors='coerce')

    # Criar um DataFrame com todos os meses do ano
    todos_meses = pd.DataFrame({'mes': range(1, 13)})

    # Merge dos dados com todos os meses para garantir que todos os meses sejam incluídos
    data_agrupada = todos_meses.merge(remocao_autor, left_on='mes', right_on=remocao_autor['data'].dt.month, how='left')

    for mes, data_selecionada in data_agrupada.groupby('mes'):
        nome_mes = calendar.month_name[int(mes)].capitalize()

        # Contar os sentimentos mensais
        sentimentos_mensais = data_selecionada['sentimento'].value_counts()
        quantidade_positivo = int(sentimentos_mensais.get('POSITIVE', 0))
        quantidade_negativo = int(sentimentos_mensais.get('NEGATIVE', 0))
        quantidade_neutro = int(sentimentos_mensais.get('NEUTRAL', 0))

        sentimentos_por_mes[nome_mes] = {
            'quantidade_positivo': quantidade_positivo,
            'quantidade_negativo': quantidade_negativo,
            'quantidade_neutro': quantidade_neutro
        }

    # Ordenar os meses em português
    meses_ordenados = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    # Reordenar os meses no JSON
    sentimentos_por_mes_ordenados = {mes: sentimentos_por_mes.get(mes, {}) for mes in meses_ordenados}

    return jsonify(sentimentos_por_mes_ordenados)


@app.route('/categorias-por-mes', methods=['GET'])
def categorias_por_mes():
    categorias_por_mes = {}

    # Converter a coluna 'data' para o formato correto de data
    remocao_autor['data'] = pd.to_datetime(remocao_autor['data'], format='%d-%m-%Y', errors='coerce')

    # Criar um DataFrame com todos os meses do ano
    todos_meses = pd.DataFrame({'mes': range(1, 13)})

    # Merge dos dados com todos os meses para garantir que todos os meses sejam incluídos
    data_agrupada = todos_meses.merge(remocao_autor, left_on='mes', right_on=remocao_autor['data'].dt.month, how='left')

    for mes, data_selecionada in data_agrupada.groupby('mes'):
        nome_mes = calendar.month_name[int(mes)].capitalize()

        # Contar as categorias mensais
        categorias_mensais = data_selecionada['sentimento'].value_counts()
        quantidade_positive = int(categorias_mensais.get('POSITIVE', 0))
        quantidade_negative = int(categorias_mensais.get('NEGATIVE', 0))
        quantidade_neutral = int(categorias_mensais.get('NEUTRAL', 0))

        categorias_por_mes[nome_mes] = {
            'POSITIVE': quantidade_positive,
            'NEGATIVE': quantidade_negative,
            'NEUTRAL': quantidade_neutral
        }

    # Ordenar os meses em português
    meses_ordenados = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    # Reordenar as categorias por mês no JSON
    categorias_por_mes_ordenadas = {mes: categorias_por_mes.get(mes, {}) for mes in meses_ordenados}

    return jsonify(categorias_por_mes_ordenadas)


if __name__ == '__main__':
    app.run()