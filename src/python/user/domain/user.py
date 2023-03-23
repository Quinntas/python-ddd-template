from src.python.shared.core.base_domain import BaseDomain
from src.python.shared.domain.shared_datetime import SharedDatetime
from src.python.shared.domain.shared_uuid import SharedUUID
from src.python.user.domain.user_email import UserEmail
from src.python.user.domain.user_name import UserName
from src.python.user.domain.user_password import UserPassword
from src.python.user.domain.user_role import UserRole


class User(BaseDomain):
    id: int
    publicId: SharedUUID
    name: UserName
    email: UserEmail
    email_verified: bool
    password: UserPassword
    role: UserRole
    createdAt: SharedDatetime
    updatedAt: SharedDatetime

    @staticmethod
    def get_private_attributes() -> list:
        return ['id', 'password', 'role']
