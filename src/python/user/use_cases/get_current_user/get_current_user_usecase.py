from src.python.shared.core.base_usecase import UseCase
from src.python.user.domain.user import User
from src.python.user.mapper.index import user_mapper


class GetCurrentUserUseCase(UseCase):
    async def execute(self, user: User):
        return user_mapper.to_dict(user)
