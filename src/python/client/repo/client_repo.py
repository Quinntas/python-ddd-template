from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.shared.core.base_repo import BaseRepo


class ClientRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    async def create_client(self, new_client: NewClientDTO):
        return await self.create("client", data={
            'phone_number': new_client.phone_number,
            'avatar': new_client.avatar,
            'addressHistory': {
                'create': {}
            },
            'orderHistory': {
                'create': {}
            },
            'user': {
                'create': {
                    'name': new_client.name,
                    'email': new_client.email,
                    'password': new_client.password
                }
            },
        })

    async def put_client(self, _client: UpdateClientDTO, public_id: str):
        return await self.update("client", {
            'avatar': _client.avatar,
            'phone_number': _client.phone_number
        }, {'publicId': public_id})

    async def get_client_with_public_id(self, public_id: str):
        return await self.get_unique("client", {'publicId': public_id})

    async def get_client_with_user_id(self, user_id: int):
        return await self.get_unique("client", {'userId': user_id})
