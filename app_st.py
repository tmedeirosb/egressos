
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
        plot = sns.countplot(data=df, x=options[0], hue=hue_option, ax=ax)
    else:
        plot = sns.countplot(data=df, x=options[0], ax=ax)
    plot.set_xticklabels(plot.get_xticklabels(), rotation=90)

    # Add the values on top of each bar
    for p in plot.patches:
        plot.annotate(format(p.get_height(), '.0f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha = 'center', 
                      va = 'center', 
                      xytext = (0, 10), 
                      textcoords = 'offset points')

    st.pyplot(fig)
