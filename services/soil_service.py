# services/soil_service.py

from core.soil.stress_state import principal_stresses

def analyze_stress(data):
    sigma_1, sigma_3 = principal_stresses(
        data["sigma_x"],
        data["sigma_y"],
        data["tau_xy"]
    )

    return {
        "sigma_1": sigma_1,
        "sigma_3": sigma_3,
        "fs": sigma_1 / sigma_3
    }
