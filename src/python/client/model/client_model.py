from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class Client(BaseModel):
    id: Optional[int]
    uuid: Optional[str] = Field(default=uuid4().__str__())
    name: str
    email: EmailStr
    email_verified_at: Optional[str] = Field(default="")
    password: str
    phone_number: str
    avatar: str
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        validate_assignment = True

    def get_dict(self) -> dict:
        result = self.dict()
        result.pop('id', None)
        return result

    def default_response(self) -> dict:
        response = self.get_dict()
        response.pop('password', None)
        response.pop('email_verified_at', None)
        return response

    def put_response(self) -> dict:
        response = self.default_response()
        response.pop('created_at', None)
        response.pop('updated_at', None)
        response.pop('uuid', None)
        return response
