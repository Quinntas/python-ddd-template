class ValueObjectException(Exception):
    def __init__(self, error_value: str | list):
        self.error_value: str | list = error_value
        super().__init__(self.error_value)
