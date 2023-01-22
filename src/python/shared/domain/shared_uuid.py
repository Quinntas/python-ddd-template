from uuid import uuid4

from src.python.shared.core.value_object.value_object import ValueObject


class SharedUUID(ValueObject):
    def __init__(self, uuid: str = None):
        if uuid is None or uuid == '':
            self.user_uuid: str = self.generate_uuid()
        else:
            self.user_uuid: str = uuid

        super().__int__(self.user_uuid)

    @staticmethod
    def generate_uuid() -> str:
        return uuid4().__str__()
