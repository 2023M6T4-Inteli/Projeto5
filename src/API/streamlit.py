import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("C:\\M6\\modelo_embedding_layer(keras).h5")

# Função para calcular a média dos vetores
def calcular_media(vetores):
    return np.mean(vetores, axis=0)

# Função para realizar a previsão
def fazer_previsao(vetor_medio):
    # Realizar qualquer pré-processamento necessário no vetor médio
    # ...
    # Fazer a previsão usando o modelo carregado
    previsao = model.predict(np.array([vetor_medio]))
    return previsao

# Configuração do aplicativo Streamlit
def main():
    # Título do aplicativo
    st.title('Aplicativo de Previsão')

    # Descrição
    st.write('Faça a previsão usando o modelo carregado')

    # Upload do arquivo CSV
    st.write('Faça o upload do arquivo CSV')
    file = st.file_uploader('Selecione um arquivo CSV', type=['csv'])

    if file is not None:
        # Carregar o arquivo CSV em um DataFrame
        df = pd.read_csv(file)

        # Exibir o DataFrame carregado
        st.write('Dados carregados:')
        st.write(df)

        # Calcular a média dos vetores
        vetor_medio = calcular_media(df.values[:, :50])

        # Botão para realizar a previsão
        if st.button('Prever'):
            # Chamar a função de previsão com o vetor médio
            resultado = fazer_previsao(vetor_medio)

            # Exibir o resultado
            st.write('O resultado da previsão é:')
            st.write(resultado)

# Executar o aplicativo
if __name__ == '__main__':
    main()
