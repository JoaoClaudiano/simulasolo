# =====================================================
# core/soil/stress.py
# =====================================================
import math
from dataclasses import dataclass


@dataclass
class StressState:
    sigma_x: float
    sigma_y: float
    tau_xy: float


    def principal_stresses(self):
        avg = (self.sigma_x + self.sigma_y) / 2
        r = math.sqrt(((self.sigma_x - self.sigma_y) / 2)**2 + self.tau_xy**2)
        return avg + r, avg - r


    def stress_path(self, increments):
        path = []
        sx, sy, t = self.sigma_x, self.sigma_y, self.tau_xy
        for dsx, dsy, dt in increments:
            sx += dsx
            sy += dsy
            t += dt
            path.append(StressState(sx, sy, t))
            return path

