# =====================================================
# app/ui_utils.py
# =====================================================

import streamlit as st


class UI:
    @staticmethod
    def section(title: str):
        st.markdown(f"### {title}")

    @staticmethod
    def number(label: str, default=0.0):
        return st.number_input(label, value=float(default))

    @staticmethod
    def text(label: str, default=""):
        return st.text_input(label, value=default)
