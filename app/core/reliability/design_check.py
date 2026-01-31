# =====================================================
# core/reliability/design_check.py
# =====================================================


class ReliabilityCheck:
@staticmethod
def check(results, characteristic):
mean = sum(results) / len(results)
std = (sum((r - mean)**2 for r in results) / len(results))**0.5
return {
"mean": mean,
"std": std,
"characteristic": characteristic
}
