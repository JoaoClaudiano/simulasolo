from dataclasses import dataclass

@dataclass
class ELUFactors:
    gamma_g: float = 1.4   # ações permanentes
    gamma_q: float = 1.4   # ações variáveis
    gamma_r: float = 1.0   # resistência

class ELU:
    @staticmethod
    def design_load(G, Q, factors: ELUFactors):
        return factors.gamma_g * G + factors.gamma_q * Q

    @staticmethod
    def design_resistance(R, factors: ELUFactors):
        return R / factors.gamma_r

    @staticmethod
    def check(G, Q, R, factors: ELUFactors):
        Sd = ELU.design_load(G, Q, factors)
        Rd = ELU.design_resistance(R, factors)
        return Sd <= Rd, Sd, Rd
