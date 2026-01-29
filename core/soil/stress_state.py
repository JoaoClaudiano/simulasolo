# core/soil/stress_state.py

import math

def principal_stresses(sigma_x, sigma_y, tau_xy):
    avg = (sigma_x + sigma_y) / 2
    radius = math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)

    sigma_1 = avg + radius
    sigma_3 = avg - radius

    return sigma_1, sigma_3
