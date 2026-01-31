# =====================================================
# core/reliability/probability.py
# =====================================================


class Probability:
    @staticmethod
    def failure_probability(results, limit):
        failures = [r for r in results if r < limit]
        return len(failures) / len(results)


    @staticmethod
    def reliability_index(pf):
        if pf <= 0:
            return float('inf')
            return -math.erfcinv(2 * pf) * math.sqrt(2)
