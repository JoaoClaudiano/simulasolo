# =====================================================
# visualization/stress_path.py
# =====================================================


import matplotlib.pyplot as plt

class StressPathPlot:

    @staticmethod
    def plot(sig1, sig3):
        fig, ax = plt.subplots()
        ax.plot(sig3, sig1, marker="o")
        ax.set_xlabel("σ3 (MPa)")
        ax.set_ylabel("σ1 (MPa)")
        ax.set_title("Stress Path")
        ax.grid(True)
        plt.show()
