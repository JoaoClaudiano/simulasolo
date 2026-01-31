# =====================================================
# core/shallow/terzaghi.py
# =====================================================


@dataclass
class Soil:
    gamma: float
    cohesion: float
    friction_angle: float


class Terzaghi:
    @staticmethod
    def factors(phi):
        phi = math.radians(phi)
        Nq = math.exp(math.pi * math.tan(phi)) * math.tan(math.pi/4 + phi/2)**2
        Nc = (Nq - 1) / math.tan(phi) if phi > 0 else 5.7
        Ng = 2 * (Nq + 1) * math.tan(phi)
        return Nc, Nq, Ng


    @staticmethod
    def ultimate_capacity(soil: Soil, B, D):
        Nc, Nq, Ng = Terzaghi.factors(soil.friction_angle)
        return soil.cohesion * Nc + soil.gamma * D * Nq + 0.5 * soil.gamma * B * Ng
