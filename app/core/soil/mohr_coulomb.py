# =====================================================
# core/soil/mohr_coulomb.py
# =====================================================


@dataclass
class MohrCoulomb:
cohesion: float
friction_angle: float


def shear_strength(self, sigma_n):
return self.cohesion + sigma_n * math.tan(math.radians(self.friction_angle))


def factor_of_safety(self, stress: StressState):
s1, s3 = stress.principal_stresses()
tau = (s1 - s3) / 2
sigma = (s1 + s3) / 2
return self.shear_strength(sigma) / tau if tau != 0 else float('inf')

