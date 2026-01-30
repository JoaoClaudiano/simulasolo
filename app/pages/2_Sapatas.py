# =====================================================
# app/pages/2_Sapatas.py
# =====================================================
import streamlit as st
from app.ui_utils import UI
from core.bearing_capacity import Terzaghi, Meyerhof
from visualization.bearing_capacity import BearingCapacityPlot


st.title("Fundações Superficiais – Sapatas")
UI.section("Parâmetros do Solo")


c = UI.number("Coesão c (kPa)", 20)
phi = UI.number("Ângulo φ (°)", 30)
gamma = UI.number("Peso específico γ (kN/m³)", 18)


if st.button("Comparar Métodos"):
    results = {
    "Terzaghi": Terzaghi.compute_curve(c, phi, gamma),
    "Meyerhof": Meyerhof.compute_curve(c, phi, gamma)
    }
    BearingCapacityPlot.compare(results)
