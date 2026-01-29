# =====================================================
# visualization/stress_path.py
# =====================================================


class StressPathPlot:
@staticmethod
def plot(sig1, sig3):
plt.figure()
p = [(s1 + s3) / 2 for s1, s3 in zip(sig1, sig3)]
q = [(s1 - s3) / 2 for s1, s3 in zip(sig1, sig3)]
plt.plot(p, q)
plt.xlabel("p (tensão média)")
plt.ylabel("q (tensão desviadora)")
plt.title("Stress Path")
BasePlot.show()
