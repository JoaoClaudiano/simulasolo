# =====================================================
# core/deep/group.py
# =====================================================


class PileGroup:
    @staticmethod
    def efficiency(n, spacing, diameter):
        return min(1.0, 1 - 0.1 * (diameter / spacing) * (n - 1))


    @staticmethod
    def group_capacity(single_capacity, n, efficiency):
        return single_capacity * n * efficiency
