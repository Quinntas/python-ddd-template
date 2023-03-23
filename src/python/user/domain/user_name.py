from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject

_minimum_name_length: int = 3


class UserName(ValueObject):
    def __init__(self, name: str):
        super().set_multi_guard()
        self.name: str = self.create(name)

    def create(self, name: str) -> str:
        self.multi_guard.add_result(Guard.against_none("Name", name))
        self.multi_guard.add_result(Guard.against_at_least("Name", _minimum_name_length, name))
        self.multi_guard.check()
        return self.set_value(name)
