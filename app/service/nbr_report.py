# =====================================================
# service/nbr_report.py
# =====================================================


class NormativeReport:
@staticmethod
def summary(results: dict):
ok = all(r["status"] == "OK" for r in results.values())
return {
"conclusao": "ATENDE À NORMA" if ok else "NÃO ATENDE À NORMA",
"detalhes": results
}
