# =====================================================
# app/pages/3_Estacas.py
# =====================================================

import streamlit as st
from app.ui_utils import UI
from core.piles import AokiVelloso
from visualization.load_settlement import LoadSettlementPlot

st.title("Fundações Profundas – Estacas")
UI.section("Dados SPT")

Nspt = UI.number("NSPT médio", 10)

if st.button("Carga × Recalque"):
    try:
        load, settlement = AokiVelloso.load_settlement_curve(Nspt)
        LoadSettlementPlot.plot(load, settlement)
    except Exception as e:
        st.error(f"Erro na análise de estacas: {e}")
