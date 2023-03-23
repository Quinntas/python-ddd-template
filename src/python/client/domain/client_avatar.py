
from src.python.shared.core.value_object.value_object import ValueObject


class ClientAvatar(ValueObject):
    def __init__(self, avatar: str):
        super().set_multi_guard()
        self.avatar: str = self.create(avatar)

    def create(self, avatar: str) -> str:
        return self.set_value(avatar)
