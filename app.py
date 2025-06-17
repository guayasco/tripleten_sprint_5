# Importando bibliotecas utilizadas no projeto
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo arquivo CSV escopo do projeto em um DataFrame
car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma') # Criar botão de histograma
scatter_button = st.button('Criar gráfico de dispersão') # Criar botão de gráfico de dispersão
        
if hist_button: # Se o botão for clicado
    # Escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
           
    # Criar um histograma
    fig = px.histogram(car_data, x="odometer")
       
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # Se o botão for clicado
    # Escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
           
    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
       
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
