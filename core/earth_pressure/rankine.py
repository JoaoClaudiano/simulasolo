import math

class Rankine:
    @staticmethod
    def coefficients(phi):
        phi = math.radians(phi)
        Ka = math.tan(math.pi/4 - phi/2)**2
        Kp = math.tan(math.pi/4 + phi/2)**2
        return Ka, Kp

    @staticmethod
    def active_pressure(gamma, H, Ka):
        return 0.5 * gamma * H**2 * Ka

    @staticmethod
    def passive_pressure(gamma, H, Kp):
        return 0.5 * gamma * H**2 * Kp
