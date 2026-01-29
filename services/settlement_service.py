# =====================================================
# service/settlement_service.py
# =====================================================


from core.settlement.elastic import ElasticSettlement
from core.settlement.consolidation import ConsolidationSettlement
from core.settlement.secondary import SecondarySettlement
from core.limit_states.els import ELS
from core.validation.nbr6122 import NBR6122


class SettlementService:
@staticmethod
def total_settlement(elastic, primary, secondary, foundation_type):
total = elastic + primary + secondary
limit = NBR6122.allowable_settlement(foundation_type)
ok = ELS.settlement_ok(total, limit)


return {
"status": "ok",
"elastic": elastic,
"primary": primary,
"secondary": secondary,
"total": total,
"limit": limit,
"ELS": ok
}
