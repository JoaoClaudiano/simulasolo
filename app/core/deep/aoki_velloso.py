# =====================================================
# core/deep/aoki_velloso.py
# =====================================================


class AokiVelloso:
    @staticmethod
    def capacity(spt, pile: Pile):
        qs = 0.02 * spt
        qb = 0.1 * spt
        side = math.pi * pile.diameter * pile.length * qs
        base = math.pi * (pile.diameter/2)**2 * qb
        return side + base
