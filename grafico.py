import pandas as pd
import streamlit as st

try:
  tot_registros = df.count()['total']
except:
  df = pd.read_csv('https://perfil-i.ibict.br/media/uploads/user_sum.csv')

meses = df.groupby(df['month'].str[0:4]).count()
lista = []
for item in meses['month'].index:
    lista.append(item)
  
option = st.selectbox(
    "Escolha o ano", lista
)

if option:
    data = df[df['month'].str.startswith('2024', na=False)]
else:
    data = df

st.bar_chart(data, x='month', y='total')
