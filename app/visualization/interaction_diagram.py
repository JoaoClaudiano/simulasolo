# =====================================================
# visualization/interaction_diagram.py
# =====================================================


class InteractionDiagram:
    @staticmethod
    def plot(N, M):
        plt.figure()
        plt.plot(N, M)
        plt.xlabel("Força Normal")
        plt.ylabel("Momento")
        plt.title("Diagrama de Interação N–M")
        BasePlot.show()
