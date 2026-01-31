import math

class Coulomb:
    @staticmethod
    def active_coefficient(phi, delta, beta=0):
        phi = math.radians(phi)
        delta = math.radians(delta)
        beta = math.radians(beta)

        numerator = math.sin(phi + delta) * math.sin(phi - beta)
        denominator = math.cos(delta + beta) * math.cos(beta)
        return (numerator / denominator) / (
        math.cos(beta) * (1 + math.sqrt(numerator / denominator))**2
        )
