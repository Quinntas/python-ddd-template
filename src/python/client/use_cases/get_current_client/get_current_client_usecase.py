from src.python.client.mapper.index import client_mapper
from src.python.client.repo.index import client_repo
from src.python.shared.core.base_usecase import UseCase
from src.python.user.domain.user import User


class GetCurrentClientUseCase(UseCase):
    async def execute(self, _user: User):
        _client = await client_repo.get_client_with_user_id(_user.id)
        return client_mapper.to_dict(client_mapper.to_domain(_client))
