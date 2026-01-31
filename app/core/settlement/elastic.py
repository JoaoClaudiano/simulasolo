import math
from dataclasses import dataclass

@dataclass
class ElasticSoil:
    E: float        # Módulo de elasticidade (kPa)
    nu: float       # Coeficiente de Poisson

class ElasticSettlement:
    @staticmethod
    def immediate(q, B, soil: ElasticSoil, shape_factor=1.0):
        """
        q = pressão aplicada (kPa)
        B = menor dimensão da fundação (m)
        """
        return (q * B * (1 - soil.nu**2)) / soil.E * shape_factor
