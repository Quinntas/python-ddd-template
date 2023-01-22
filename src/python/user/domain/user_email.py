import re

from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.core.value_object.value_object_exception import ValueObjectException

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class UserEmail(ValueObject):
    def __init__(self, email: str):
        self.email: str = self.create(email)

        super().__int__(self.email)

    @staticmethod
    def create(email: str) -> str:
        if not re.fullmatch(regex, email):
            raise ValueObjectException('Email is not valid')
        return email
