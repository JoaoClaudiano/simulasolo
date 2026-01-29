# =====================================================
# core/shallow/boussinesq.py
# =====================================================


class Boussinesq:
@staticmethod
def vertical_stress(q, z, r):
return (3 * q * z**3) / (2 * math.pi * (r**2 + z**2)**(5/2))
