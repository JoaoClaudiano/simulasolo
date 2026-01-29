# =====================================================
# core/reliability/random_variables.py
# =====================================================
import random
from dataclasses import dataclass


@dataclass
class RandomVariable:
mean: float
std: float


def sample(self):
return random.gauss(self.mean, self.std)
