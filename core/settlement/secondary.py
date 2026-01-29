# =====================================================
# core/settlement/secondary.py
# =====================================================


@dataclass
class SecondarySoil:
C_alpha: float
H: float
t1: float
t2: float


class SecondarySettlement:
@staticmethod
def creep(soil: SecondarySoil):
return soil.C_alpha * soil.H * math.log10(soil.t2 / soil.t1)
