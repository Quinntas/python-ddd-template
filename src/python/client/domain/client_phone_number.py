from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.core.value_object.value_object_exception import ValueObjectException

_minimum_phone_number_length: int = 6


class ClientPhoneNumber(ValueObject):
    def __init__(self, phone_number: str):
        self.phone_number: str = self.create(phone_number)

        super().__int__(self.phone_number)

    @staticmethod
    def create(phone_number: str) -> str:
        minimum_value_result = Guard.against_at_least(_minimum_phone_number_length, phone_number)
        if minimum_value_result.is_failure:
            raise ValueObjectException(minimum_value_result.get_error_value())
        return phone_number
