# =====================================================
# visualization/bearing_capacity.py
# =====================================================


class BearingCapacityPlot:
    @staticmethod
    def compare(methods_results):
        plt.figure()
        for method, values in methods_results.items():
            plt.plot(values, label=method)
            plt.legend()
            plt.title("Comparação de Métodos de Capacidade de Carga")
            BasePlot.show()
