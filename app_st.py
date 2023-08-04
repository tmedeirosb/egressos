
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
    fig, ax = plt.subplots(figsize=(10,5))
    if hue_option != 'Nenhum':
        sns.countplot(data=df, x=options[0], hue=hue_option, ax=ax)
    else:
        sns.countplot(data=df, x=options[0], ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
