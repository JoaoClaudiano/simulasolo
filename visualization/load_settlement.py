# =====================================================
# visualization/load_settlement.py
# =====================================================


class LoadSettlementPlot:
@staticmethod
def plot(loads, settlements):
plt.figure()
plt.plot(loads, settlements)
plt.xlabel("Carga")
plt.ylabel("Recalque")
plt.title("Curva Carga × Recalque")
BasePlot.show()
