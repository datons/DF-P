import pandas as pd
import streamlit as st
import plotly.express as px
import os

file_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(file_directory, 'data/gapminder.csv')

df_base = pd.read_csv(path)

st.set_page_config(layout='wide')

st.title('Data Application')

options_year = df_base['year'].unique()
value_year = st.selectbox('Year', options_year)
mask_year = df_base['year'] == value_year

df = df_base[mask_year]
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country', log_x=True)


st.write('## Plot')
st.plotly_chart(fig)

st.write('## Table')
st.write(df)