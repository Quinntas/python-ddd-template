from enum import Enum

from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.core.value_object.value_object_exception import ValueObjectException


class Role(Enum):
    ADMIN = 'ADMIN'
    CLIENT = 'CLIENT'


class UserRole(ValueObject):
    def __init__(self, role: Role | str):
        self.role: str = self.create(role)

        super().__int__(self.role)

    @staticmethod
    def create(role: Role | str) -> str:
        if type(role) == str:
            for _role in Role:
                if _role.value == role:
                    return role
            raise ValueObjectException('Role is not correct')
        return role.value
