# app.py
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Iris Scatter Plot", layout="wide")
st.title("🌸 Iris Flower Scatter Plot")

# Načtení datasetu Iris
iris_df = px.data.iris()

# Vytvoření interaktivního scatter plotu
fig = px.scatter(
    iris_df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=['petal_width'],
    title="Iris Flower Characteristics"
)

# Zobrazení grafu ve Streamlit
st.plotly_chart(fig, width='stretch')
