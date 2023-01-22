from pydantic import BaseModel

from src.python.shared.domain.shared_datetime import SharedDatetime
from src.python.shared.domain.shared_uuid import SharedUUID
from src.python.user.domain.user_email import UserEmail
from src.python.user.domain.user_name import UserName
from src.python.user.domain.user_password import UserPassword
from src.python.user.domain.user_role import UserRole


class User(BaseModel):
    id: int
    publicId: SharedUUID
    name: UserName
    email: UserEmail
    email_verified: bool
    password: UserPassword
    role: UserRole
    created_at: SharedDatetime
    updated_at: SharedDatetime

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
