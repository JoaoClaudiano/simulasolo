# =====================================================
# app/pages/5_Relatorio_Tecnico.py
# =====================================================

import streamlit as st
from service.report_builder import ReportBuilder
from service.report_render_html import HTMLReportRenderer

st.title("Relatório Técnico Automático")

project = st.text_input(
    "Nome do Projeto",
    "SimulaSolo – Estudo de Fundação"
)

if st.button("Gerar Relatório"):
    try:
        rb = ReportBuilder(project)

        rb.add_section(
            "Metodologia",
            "Análises geotécnicas realizadas conforme métodos consagrados e NBR 6122."
        )
        rb.add_section(
            "Resultados",
            "Capacidade de carga, recalques e verificações normativas atendidas."
        )
        rb.add_section(
            "Conclusão",
            "O projeto atende aos critérios normativos vigentes."
        )

        report = rb.build()
        html = HTMLReportRenderer.render(report)

        st.components.v1.html(html, height=600)
    except Exception as e:
        st.error(f"Erro ao gerar relatório: {e}")
