from src.python.shared.core.guard import Guard
from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.encryption.encryption import gen_pbkdf2_sha256, verify_encryption

_minimum_password_length: int = 6


class UserPassword(ValueObject):
    def __init__(self, password: str, is_hashed: bool = True):
        super().set_multi_guard()
        self.password: str = self.create(password, is_hashed)

    def create(self, password: str, is_hashed: bool) -> str:
        if not is_hashed:
            self.multi_guard.add_result(Guard.against_at_least("Password", _minimum_password_length, password))
            self.multi_guard.check()
            return self.set_value(gen_pbkdf2_sha256(password))
        return self.set_value(password)

    def compare(self, context: str) -> bool:
        return verify_encryption(context, self.password)
