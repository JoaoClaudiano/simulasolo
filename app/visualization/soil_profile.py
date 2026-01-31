# =====================================================
# visualization/soil_profile.py
# =====================================================


class SoilProfilePlot:
@staticmethod
def plot(layers, depths):
plt.figure()
plt.step(layers, depths)
plt.gca().invert_yaxis()
plt.xlabel("Camadas")
plt.ylabel("Profundidade")
plt.title("Perfil Estratigráfico do Solo")
BasePlot.show()
