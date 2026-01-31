# =====================================================
# core/reliability/monte_carlo.py
# =====================================================


class MonteCarlo:
@staticmethod
def simulate(function, variables, n=10000):
results = []
for _ in range(n):
sampled = {k: v.sample() for k, v in variables.items()}
results.append(function(**sampled))
return results
