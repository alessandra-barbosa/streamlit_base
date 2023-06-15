import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Expectativa de Vida')

df=pd.read_csv('df_complete.csv')
df['year']=df['year'].astype(str)

select=st.multiselect('country', df['country'].unique(), 'Brazil')
filtro=df[df['country'].isin(select)]

st.dataframe(filtro)

st.subheader('Grafico expecitativa de vida')
sns.barplot(x='country', y='expectancy', data=filtro);
st.pyplot(plt)


filtro.to_csv('dados.csv')

with open('dados.csv', 'rb') as file:
    btn=st.download_button(label='Download',data=file, file_name='dados.csv',
                           mime='application/octet-stream' )