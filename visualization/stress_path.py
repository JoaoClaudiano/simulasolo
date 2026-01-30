# =====================================================
# visualization/stress_path.py
# =====================================================


import matplotlib.pyplot as plt
import streamlit as st

class StressPathPlot:

    @staticmethod
    def plot(sig1, sig3):
        fig, ax = plt.subplots()
        ax.plot(sig3, sig1, marker="o")
        ax.set_xlabel("σ3")
        ax.set_ylabel("σ1")
        ax.set_title("Stress Path")
        st.pyplot(fig)
