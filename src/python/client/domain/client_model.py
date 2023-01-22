from pydantic import BaseModel

from src.python.client.domain.client_avatar import ClientAvatar
from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.shared.domain.shared_uuid import SharedUUID


class Client(BaseModel):
    id: int
    uuid: SharedUUID
    phone_number: ClientPhoneNumber
    avatar_number: ClientAvatar
    userId: int
    created_at: str
    updated_at: str

    class Config:
        arbitrary_types_allowed = True
