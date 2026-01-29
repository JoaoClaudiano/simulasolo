# =====================================================
# service/reliability_service.py
# =====================================================


from core.reliability.monte_carlo import MonteCarlo
from core.reliability.probability import Probability


class ReliabilityService:
@staticmethod
def monte_carlo_check(function, variables, limit, n=10000):
results = MonteCarlo.simulate(function, variables, n)
pf = Probability.failure_probability(results, limit)
beta = Probability.reliability_index(pf)


return {
"status": "ok",
"pf": pf,
"beta": beta
}
