# =====================================================
# core/shallow/interaction.py
# =====================================================


class InteractionDiagram:
@staticmethod
def pressure_vs_fs(q_values, q_ult):
return [(q, q_ult / q) for q in q_values if q != 0]
