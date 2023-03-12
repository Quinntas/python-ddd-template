from pydantic import BaseModel

from src.python.client.domain.client_avatar import ClientAvatar
from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.shared.domain.shared_datetime import SharedDatetime
from src.python.shared.domain.shared_uuid import SharedUUID


class Client(BaseModel):
    id: int
    publicId: SharedUUID
    phone_number: ClientPhoneNumber
    userId: int
    avatar: ClientAvatar
    createdAt: SharedDatetime
    updatedAt: SharedDatetime

    class Config:
        arbitrary_types_allowed = True

    @staticmethod
    def get_private_attributes() -> list:
        return ['id', 'userId']
