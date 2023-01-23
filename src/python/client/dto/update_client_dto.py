from pydantic import BaseModel


class UpdateClientDTO(BaseModel):
    phone_number: str
    avatar: str
