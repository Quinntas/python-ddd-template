from src.python.shared.core.value_object.value_object import ValueObject

pattern: str = "^https:\/\/[0-9A-z.]+.[0-9A-z.]+.[a-z]+$"


class ClientAvatar(ValueObject):
    def __init__(self, avatar: str):
        self.avatar: str = self.create(avatar)

        super().__int__(self.avatar)

    @staticmethod
    def create(avatar: str) -> str:
        # if not re.match(pattern, avatar):
        #    raise ValueObjectException('avatar link is not correct')
        return avatar
