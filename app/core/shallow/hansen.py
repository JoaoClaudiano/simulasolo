# =====================================================
# core/shallow/hansen.py
# =====================================================


class Hansen:
    @staticmethod
    def factors(phi):
        phi = math.radians(phi)
        Nq = math.exp(math.pi * math.tan(phi)) * math.tan(math.pi/4 + phi/2)**2
        Nc = (Nq - 1) / math.tan(phi)
        Ng = 1.5 * (Nq - 1) * math.tan(phi)
        return Nc, Nq, Ng


    @staticmethod
    def ultimate_capacity(c, gamma, B, D, phi):
        Nc, Nq, Ng = Hansen.factors(phi)
        return c * Nc + gamma * D * Nq + 0.5 * gamma * B * Ng
