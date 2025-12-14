import streamlit as st

st.title("📊 Streamlit demo z Colabu přes LocalTunnel")
st.write("Ahoj z Colabu! 😊")

x = st.slider("Vyber číslo:", 0, 100, 25)
st.write(f"Vybral jsi: {x}")
