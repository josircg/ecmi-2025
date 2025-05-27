import pandas as pd
import matplotlib.pyplot as plt

try:
  tot_registros = df.count()['total']
except:
  df = pd.read_csv('https://perfil-i.ibict.br/media/uploads/user_sum.csv')

st.bar_chart(df, x='month', y='total')
