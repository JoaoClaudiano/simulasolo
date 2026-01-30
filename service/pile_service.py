# =====================================================
# service/pile_service.py
# =====================================================


from core.deep.aoki_velloso import AokiVelloso
from core.deep.decourt_quaresma import DecourtQuaresma
from core.deep.group import PileGroup


class PileService:
    @staticmethod
    def single_pile(method, spt, pile):
        if method == "aoki":
        capacity = AokiVelloso.capacity(spt, pile)
        elif method == "decourt":
        capacity = DecourtQuaresma.capacity(spt, pile)
        else:
        return {"status": "error", "message": "Método inválido"}
    
    
    return {
        "status": "ok",
        "method": method,
        "capacity": capacity
        }
    

@staticmethod
    def pile_group(single_capacity, n, spacing, diameter):
        eff = PileGroup.efficiency(n, spacing, diameter)
        total = PileGroup.group_capacity(single_capacity, n, eff)
    
    
    return {
        "status": "ok",
        "efficiency": eff,
        "group_capacity": total
        }
