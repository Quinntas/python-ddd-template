from src.python.client.domain.client import Client
from src.python.client.domain.client_avatar import ClientAvatar
from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.client.repo.client_repo import put_client
from src.python.shared.core.base_usecase import UseCase


class UpdateClientUseCase(UseCase):
    async def execute(self, __client: UpdateClientDTO, _client: Client):
        __client.avatar = ClientAvatar(__client.avatar).get_value()
        __client.phone_number = ClientPhoneNumber(__client.phone_number).get_value()
        await put_client(__client, _client.publicId.get_value())
