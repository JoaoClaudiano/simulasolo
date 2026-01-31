class ComplianceReport:
    @staticmethod
    def elu_result(ok, Sd, Rd):
        return {
        "ELU": "OK" if ok else "NÃO ATENDE",
        "Solicitação (Sd)": Sd,
        "Resistência (Rd)": Rd
        }

    @staticmethod
    def els_result(settlement, limit, ok):
        return {
        "ELS": "OK" if ok else "NÃO ATENDE",
        "Recalque": settlement,
        "Limite": limit
        }
