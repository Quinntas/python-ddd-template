from src.python.shared.core.guard import Guard
from src.python.shared.core.regex_list.regex_list import email_regex
from src.python.shared.core.value_object.value_object import ValueObject


class UserEmail(ValueObject):
    def __init__(self, email: str):
        super().set_multi_guard()
        self.email: str = self.create(email)

    def create(self, email: str) -> str:
        self.multi_guard.add_result(Guard.against_none("email", email))
        self.multi_guard.add_result(Guard.against_regex("email", email, email_regex))
        self.multi_guard.check()
        return self.set_value(email)
