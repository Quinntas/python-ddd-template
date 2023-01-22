from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.domain.shared_datetime import SharedDatetime
from src.python.shared.domain.shared_uuid import SharedUUID
from src.python.user.domain.user_email import UserEmail
from src.python.user.domain.user_model import User
from src.python.user.domain.user_name import UserName
from src.python.user.domain.user_password import UserPassword
from src.python.user.domain.user_role import UserRole


def to_model(user) -> User:
    user_loaded = {
        'id': user.id,
        'publicId': SharedUUID(user.publicId),
        'name': UserName(user.name),
        'email': UserEmail(user.email),
        'email_verified': user.email_verified,
        'password': UserPassword(user.password, True),
        'role': UserRole(user.role),
        'created_at': SharedDatetime(user.createdAt),
        'updated_at': SharedDatetime(user.updatedAt)
    }
    return User(**user_loaded)


def to_dict(_user: User) -> dict:
    return_value = {}
    user_dict = _user.dict()
    for key in user_dict.keys():
        if ValueObject in user_dict[key].__class__.__mro__:
            return_value[key] = user_dict[key].get_value()
            continue
        return_value[key] = user_dict[key]
    return return_value
