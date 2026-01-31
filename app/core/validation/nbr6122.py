class NBR6122:
    @staticmethod
    def allowable_settlement(foundation_type):
        if foundation_type == "sapata":
            return 25  # mm
            if foundation_type == "estaca":
                return 10  # mm
                return 20

    @staticmethod
    def minimum_dimensions(foundation_type):
        if foundation_type == "sapata":
            return {"B_min": 0.6, "D_min": 0.5}
            if foundation_type == "estaca":
                return {"D_min": 0.25}
                return {}
