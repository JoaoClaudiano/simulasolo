# =====================================================
# service/shallow_service.py
# =====================================================


from app.core.shallow.terzaghi import Terzaghi
from app.core.shallow.meyerhof import Meyerhof
from app.core.shallow.hansen import Hansen
from app.core.shallow.vesic import Vesic
from app.core.limit_states.elu import ELU, ELUFactors


class ShallowFoundationService:
    @staticmethod
    def bearing_capacity(method, soil, B, D, G, Q):
        methods = {
        "terzaghi": Terzaghi.ultimate_capacity,
        "meyerhof": Meyerhof.ultimate_capacity,
        "hansen": Hansen.ultimate_capacity,
        "vesic": Vesic.ultimate_capacity
        }


        if method not in methods:
            return {"status": "error", "message": "Método inválido"}


            q_ult = methods[method](
            soil.cohesion,
            soil.gamma,
            B,
            D,
            soil.friction_angle
            )


            ok, Sd, Rd = ELU.check(G, Q, q_ult, ELUFactors())


            return {
            "status": "ok",
            "method": method,
            "q_ult": q_ult,
            "ELU": ok,
            "Sd": Sd,
            "Rd": Rd
            }
