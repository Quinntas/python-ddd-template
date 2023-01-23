from typing import Optional

from pydantic import BaseModel, Field


class NewClientDTO(BaseModel):
    email: str
    password: str
    name: str
    phone_number: str
    avatar: Optional[str] = Field(default='https://open.spotify.com/playlist/5MEtslGRV8YZdXO3a1sBJ4')
