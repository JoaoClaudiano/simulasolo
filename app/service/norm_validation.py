# =====================================================
# service/norm_validation.py
# =====================================================

"""
Valida fundações conforme NBR 6122:2019
"""

class NBR6122Validator:

    @staticmethod
    def bearing_capacity(q_adm, q_solic):
        return q_solic <= q_adm

    @staticmethod
    def settlement(sett, sett_lim):
        return sett <= sett_lim

    @staticmethod
    def dimensions(B):
        return B >= 0.6
