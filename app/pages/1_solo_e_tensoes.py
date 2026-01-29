# app/pages/1_solo_e_tensoes.py

import streamlit as st
from services.soil_service import analyze_stress
from visualization.mohr_plot import plot_mohr

st.title("Análise de Tensões no Solo")

sigma_x = st.number_input("σx (kPa)")
sigma_y = st.number_input("σy (kPa)")
tau_xy = st.number_input("τxy (kPa)")

if st.button("Analisar"):
    result = analyze_stress({
        "sigma_x": sigma_x,
        "sigma_y": sigma_y,
        "tau_xy": tau_xy
    })

    st.metric("σ₁", f"{result['sigma_1']:.2f} kPa")
    st.metric("σ₃", f"{result['sigma_3']:.2f} kPa")

    plot_mohr(sigma_x, sigma_y, tau_xy)
