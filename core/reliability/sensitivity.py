# =====================================================
# core/reliability/sensitivity.py
# =====================================================


class Sensitivity:
@staticmethod
def finite_difference(function, base_params, delta=1e-3):
sensitivities = {}
base_value = function(**base_params)


for key in base_params:
params = base_params.copy()
params[key] += delta
sensitivities[key] = (function(**params) - base_value) / delta


return sensitivities
