import pandas as pd
import streamlit as st
import plotly.express as px
import json

st.set_page_config(layout='wide')

st.title('Data Application')

df_base = pd.read_parquet('data/p48_2015_2022_EN.parquet')

with open('src/options.json', 'r') as f:
    options = json.load(f)
    
with st.sidebar:
    year = st.selectbox('Year', options['year'])
    granularity = st.selectbox('Granularity', options['granularity'])
    columns = st.multiselect('Columns', options['columns'], default=options['columns'][:3], max_selections=5)
    aggfunc = st.selectbox('Aggregation Function', options['aggfunc'])
    
    
df = df_base.loc[year, columns]
df = df.groupby(level=granularity).agg(aggfunc)
dfm = df.melt(ignore_index=False).reset_index()

st.write('## Plot')

fig = px.bar(
    dfm,
    x=granularity,
    y='value',
    color='variable',
    facet_row='variable',
    title=f'Energy generation during {year}, in MWh'
)

fig.update_yaxes(matches=None)
st.plotly_chart(fig)


st.write('## Table')

dfs = df.T.style.background_gradient(axis=1).format(precision=0)
st.write(dfs)