class GuardResult:
    def __init__(self, is_failure: bool, error_value: str = None):
        self.is_failure: bool = is_failure
        if is_failure is True:
            self.error_value: str = error_value

    def get_error_value(self) -> str:
        return self.error_value


class Guard:
    @staticmethod
    def against_at_least(minimum_value: int, value: str) -> GuardResult:
        if minimum_value >= len(value):
            return GuardResult(True, f'Text is not at least {minimum_value} chars')
        return GuardResult(False)
