# =====================================================
# app/app.py
# =====================================================

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))


import streamlit as st


st.set_page_config(page_title="SimulaSolo", layout="wide")
st.title("SimulaSolo – Plataforma Geotécnica")


st.markdown("""
Escolha uma análise no menu lateral.
- Solo e Tensões
- Fundações Superficiais (Sapatas)
- Fundações Profundas (Estacas)
""")
