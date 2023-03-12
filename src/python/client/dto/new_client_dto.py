from typing import Optional

from pydantic import Field

from src.python.shared.core.base_dto import BaseDTO


class NewClientDTO(BaseDTO):
    email: str
    password: str
    name: str
    phone_number: str
    avatar: Optional[str] = Field(default="http://www.gravatar.com/avatar/3b3be63a4c2a439b013787725dfce802?d=identicon")
