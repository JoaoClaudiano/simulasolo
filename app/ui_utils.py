# =====================================================
# app/ui_utils.py
# =====================================================
import streamlit as st


class UI:
@staticmethod
def section(title):
st.markdown(f"## {title}")


@staticmethod
def number(label, value, min=0.0):
return st.number_input(label, value=value, min_value=min)
