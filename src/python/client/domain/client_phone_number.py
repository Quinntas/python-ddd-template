from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject

_minimum_phone_number_length: int = 6


class ClientPhoneNumber(ValueObject):
    def __init__(self, phone_number: str):
        super().set_multi_guard()
        self.phone_number: str = self.create(phone_number)

    def create(self, phone_number: str) -> str:
        self.multi_guard.add_result(Guard.against_at_least("Phone Number", _minimum_phone_number_length, phone_number))
        self.multi_guard.add_result(Guard.against_none("Phone Number", phone_number))
        self.multi_guard.check()
        return self.set_value(phone_number)
