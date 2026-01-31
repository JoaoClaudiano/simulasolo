# =====================================================
# core/deep/pile_settlement.py
# =====================================================


class PileSettlement:
    @staticmethod
    def elastic_load(P, L, A, Ep):
        return (P * L) / (A * Ep)
