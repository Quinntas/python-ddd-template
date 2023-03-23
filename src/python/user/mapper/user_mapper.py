from src.python.shared.core.base_mapper import BaseMapper
from src.python.shared.utils.model_loader import dict_to_domain_loader, domain_to_dict_loader
from src.python.user.domain.user import User


class UserMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    @staticmethod
    def to_domain(raw_user_repo_result: dict) -> User:
        return dict_to_domain_loader(User, raw_user_repo_result.__dict__)

    @staticmethod
    def to_dict(_user: User) -> dict:
        return domain_to_dict_loader(_user, User)
