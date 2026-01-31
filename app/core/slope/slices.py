import math
from dataclasses import dataclass

@dataclass
class Slice:
    weight: float
    alpha: float
    cohesion: float
    phi: float
    width: float

class Bishop:
    @staticmethod
    def factor_of_safety(slices, tol=1e-4, max_iter=100):
        FS = 1.0

        for _ in range(max_iter):
            num, den = 0, 0
            for s in slices:
                phi = math.radians(s.phi)
                alpha = math.radians(s.alpha)

                num += (
                    s.cohesion * s.width +
                    (s.weight * math.cos(alpha)) * math.tan(phi)
                )
                den += s.weight * math.sin(alpha)

            FS_new = num / den if den != 0 else float("inf")

            if abs(FS_new - FS) < tol:
                return FS_new

            FS = FS_new

        return FS
