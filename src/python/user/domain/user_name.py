from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.core.value_object.value_object_exception import ValueObjectException

_minimum_name_length: int = 3


class UserName(ValueObject):
    def __init__(self, name: str):
        self.name: str = self.create(name)

        super().__int__(self.name)

    @staticmethod
    def create(name: str) -> str:
        minimum_value_result = Guard.against_at_least(_minimum_name_length, name)
        if minimum_value_result.is_failure:
            raise ValueObjectException(minimum_value_result.get_error_value())
        return name
