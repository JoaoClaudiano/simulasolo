from dataclasses import dataclass

@dataclass
class LoadCombination:
    G: float
    Q: float

class LoadCombinations:
    @staticmethod
    def fundamental(G, Q):
        return LoadCombination(G=G, Q=Q)

    @staticmethod
    def service(G, Q, psi=0.3):
        return LoadCombination(G=G, Q=psi * Q)
