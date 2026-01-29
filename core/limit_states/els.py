class ELS:
    @staticmethod
    def settlement_ok(settlement, limit):
        return settlement <= limit

    @staticmethod
    def rotation_ok(rotation, limit):
        return rotation <= limit

    @staticmethod
    def stress_ok(stress, allowable):
        return stress <= allowable
