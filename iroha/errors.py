class IrohaError(Exception):
    def __init__(self, message):
        super().__init__(f"誤り: {message}")
    
class IrohaWarning(Warning):
    def __init__(self, message):
        super().__init__(f"警告: {message}")