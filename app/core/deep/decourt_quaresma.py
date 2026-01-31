# =====================================================
# core/deep/decourt_quaresma.py
# =====================================================


class DecourtQuaresma:
@staticmethod
def capacity(spt, pile):
qb = 0.12 * spt
qs = 0.015 * spt
base = math.pi * (pile.diameter/2)**2 * qb
side = math.pi * pile.diameter * pile.length * qs
return base + side
