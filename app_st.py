
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('PAE_unified_data.csv')

# Sidebar
st.sidebar.header('Parâmetros')
options = st.sidebar.multiselect('Escolha as colunas para filtrar', df.columns)

# Filters
for option in options:
    values = df[option].unique()
    selected_values = st.sidebar.multiselect(f'Escolha os valores para {option}', values)
    df = df[df[option].isin(selected_values)]

# Hue parameter
hue_option = st.sidebar.selectbox('Escolha o atributo para o hue (opcional)', ['Nenhum'] + df.columns.tolist())

# Button
if st.sidebar.button('Visualizar'):
    # Display a bar plot
    st.header('Gráfico de Barras')
    plt.figure(figsize=(10,5))
    if hue_option != 'Nenhum':
        sns.countplot(data=df, x=options[0], hue=hue_option)
    else:
        sns.countplot(data=df, x=options[0])
    plt.xticks(rotation=90)
    st.pyplot()

    # Display a line plot with the mean
    st.header('Linha da Média')
    plt.figure(figsize=(10,5))
    df.groupby(options[0]).size().plot()
    plt.axhline(df.groupby(options[0]).size().mean(), color='red', linestyle='--')
    st.pyplot()
