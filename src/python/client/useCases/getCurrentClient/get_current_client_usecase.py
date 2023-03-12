from src.python.client.domain.client import Client
from src.python.client.mapper.client_mapper import to_dict
from src.python.shared.core.base_usecase import UseCase


class GetCurrentClientUseCase(UseCase):
    async def execute(self, _client: Client):
        return to_dict(_client)
