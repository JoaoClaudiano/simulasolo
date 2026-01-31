# =====================================================
# app/pages/4_Validacao_Normativa.py
# =====================================================

import streamlit as st
from app.service.norm_validation import NBR6122Validator
from app.service.nbr_report import NormativeReport

st.title("Validação Normativa – NBR 6122")

q_adm = st.number_input("Capacidade admissível (kPa)", 200.0)
q_solic = st.number_input("Tensão solicitante (kPa)", 150.0)

sett = st.number_input("Recalque calculado (mm)", 18.0)
sett_lim = st.number_input("Recalque admissível (mm)", 25.0)

B = st.number_input("Largura da fundação (m)", 0.8)

if st.button("Validar Projeto"):
    try:
        results = {
            "Capacidade": NBR6122Validator.bearing_capacity(q_adm, q_solic),
            "Recalque": NBR6122Validator.settlement(sett, sett_lim),
            "Dimensão": NBR6122Validator.dimensions(B),
        }

        report = NormativeReport.summary(results)

        st.subheader(report["conclusao"])
        st.json(report["detalhes"])
    except Exception as e:
        st.error(f"Erro na validação normativa: {e}")
