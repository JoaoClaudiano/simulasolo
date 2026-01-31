# =====================================================
# visualization/pile_group.py
# =====================================================


class PileGroupPlot:
    @staticmethod
    def efficiency(n_piles, efficiency):
        plt.figure()
        plt.bar(n_piles, efficiency)
        plt.xlabel("Número de Estacas")
        plt.ylabel("Eficiência do Grupo")
        plt.title("Eficiência de Grupo de Estacas")
        BasePlot.show()
