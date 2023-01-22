from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.encryption.encryption import gen_pbkdf2_sha256, verify_encryption

_minimum_password_length: int = 6


class UserPassword(ValueObject):
    def __init__(self, password: str, is_hashed: bool):
        self.password: str = self.create(password, is_hashed)

        super().__int__(self.password)

    @staticmethod
    def create(password: str, is_hashed: bool) -> str:
        minimum_value_result = Guard.against_at_least(_minimum_password_length, password)
        if minimum_value_result.is_failure:
            raise ValueObjectException(minimum_value_result.get_error_value())
        if not is_hashed:
            return gen_pbkdf2_sha256(password)
        return password

    def compare(self, context: str) -> bool:
        return verify_encryption(context, self.password)
