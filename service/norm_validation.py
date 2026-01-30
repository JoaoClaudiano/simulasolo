# =====================================================
# service/norm_validation.py
# =====================================================

"""
Valida fundações conforme NBR 6122:2019
"""

class NBR6122Validator:

  @staticmethod
  def bearing_capacity(q_adm, q_solic):
      return {
      "status": "OK" if q_solic <= q_adm else "NÃO CONFORME",
      "q_adm": q_adm,
      "q_solic": q_solic,
      "fs_implícito": q_adm / q_solic if q_solic > 0 else None
      }
  
  
  @staticmethod
  def settlement(settlement_calc, settlement_limit):
      return {
      "status": "OK" if settlement_calc <= settlement_limit else "NÃO CONFORME",
      "recalque": settlement_calc,
      "limite": settlement_limit
      }
  
  
  @staticmethod
  def dimensions(B, B_min=0.6):
      return {
      "status": "OK" if B >= B_min else "NÃO CONFORME",
      "B": B,
      "B_min": B_min
      }
