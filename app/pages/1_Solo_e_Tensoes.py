# =====================================================
# app/pages/1_Solo_e_Tensoes.py
# =====================================================

import streamlit as st
from app.ui_utils import UI
from visualization.stress_path import StressPathPlot

st.title("Análise de Solo e Tensões")
UI.section("Entradas")

sig1 = st.text_input("σ1 (lista, MPa)", "100,120,140")
sig3 = st.text_input("σ3 (lista, MPa)", "50,60,70")

if st.button("Gerar Stress Path"):
    try:
        s1 = [float(x.strip()) for x in sig1.split(",")]
        s3 = [float(x.strip()) for x in sig3.split(",")]
        StressPathPlot.plot(s1, s3)
    except Exception as e:
        st.error(f"Erro ao gerar Stress Path: {e}")
