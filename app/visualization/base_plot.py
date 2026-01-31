# =====================================================
# visualization/base_plot.py
# =====================================================
import matplotlib.pyplot as plt


class BasePlot:
@staticmethod
def show():
plt.grid(True)
plt.tight_layout()
plt.show()
