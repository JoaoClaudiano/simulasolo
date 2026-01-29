# =====================================================
# service/base.py
# =====================================================


class ServiceResult(dict):
"""Resultado padronizado para consumo pela UI"""
def ok(self):
return self.get("status") == "ok"
