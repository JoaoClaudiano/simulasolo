# =====================================================
# app/app.py
# =====================================================
import streamlit as st


st.set_page_config(page_title="SimulaSolo", layout="wide")
st.title("SimulaSolo – Plataforma Geotécnica")


st.markdown("""
Escolha uma análise no menu lateral.
- Solo e Tensões
- Fundações Superficiais (Sapatas)
- Fundações Profundas (Estacas)
""")
