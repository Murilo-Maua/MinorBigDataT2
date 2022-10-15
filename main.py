import streamlit as st
import pandas as pd

#Carrega o arquivo de dados
dataset = pd.read_csv("./data/netflix movie.csv", names=["Name", "Type","Classification", "Number", "Release_Year", "Duration", "Score"])

st.title("Meu Dashboard🤞")
st.write("Dashboard para iniciarmos a exploração do Streamlit")
st.dataframe(dataset)
selecionados = st.multiselect("Ano de Lançamento:", dataset.Release_Year.unique())
filtrados = dataset.query('Release_Year in @selecionados')
st.subheader("Dados Filtrados:")
st.dataframe(filtrados)
