class ValueObjectException(Exception):
    def __init__(self, error_value: str):
        self.error_value: str = error_value
        super().__init__(self.error_value)
