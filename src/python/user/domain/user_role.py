from enum import Enum

from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject


class Role(Enum):
    CLIENT = 'CLIENT'
    STORE = 'STORE'


class UserRole(ValueObject):
    def __init__(self, role: Role | str):
        super().set_multi_guard()
        self.role: str = self.create(role)

    def create(self, role: Role | str) -> str:
        if type(role) is Role:
            return self.set_value(role)
        self.multi_guard.add_result(Guard.against_wrong_enum("role", role, Role))
        self.multi_guard.check()
        return self.set_value(role)
