# =====================================================
# core/deep/block_failure.py
# =====================================================


class BlockFailure:
@staticmethod
def capacity(cu, gamma, B, L, D):
return cu * B * L + gamma * D * B * L
