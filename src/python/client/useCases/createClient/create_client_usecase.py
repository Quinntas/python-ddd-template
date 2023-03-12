from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.repo.client_repo import create_client
from src.python.shared.core.base_usecase import UseCase
from src.python.shared.encryption.encryption import gen_pbkdf2_sha256


class CreateClientUseCase(UseCase):
    async def execute(self, new_client: NewClientDTO):
        new_client.password = gen_pbkdf2_sha256(new_client.password)
        await create_client(new_client)
