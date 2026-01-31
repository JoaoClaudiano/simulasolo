import math
from dataclasses import dataclass

@dataclass
class ConsolidationSoil:
    Cc: float
    e0: float
    H: float
    sigma_0: float

class ConsolidationSettlement:
    @staticmethod
    def primary(q, soil: ConsolidationSoil):
        return (
            (soil.Cc / (1 + soil.e0)) *
            soil.H *
            math.log10((soil.sigma_0 + q) / soil.sigma_0)
        )
