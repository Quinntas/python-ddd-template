from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.shared.infra.database.prisma_handler import prisma


async def create_client(new_client: NewClientDTO):
    return await prisma.client.create(
        data={
            'phone_number': new_client.phone_number,
            'avatar': new_client.avatar,
            'user': {
                'create': {
                    'name': new_client.name,
                    'email': new_client.email,
                    'password': new_client.password, }
            },
        })


async def verify_email(public_id: str):
    return await update_client({'email_verified': True}, {'publicId': public_id})


async def put_client(_client: UpdateClientDTO, public_id: str):
    return await update_client({
        'avatar': _client.avatar,
        'phone_number': _client.phone_number
    }, {
        'publicId': public_id
    })


async def update_client(data_param: dict, where_param: dict):
    return await prisma.client.update(
        data=data_param,
        where=where_param
    )


async def get_client_with_public_id(public_id: str):
    return await get_client({'publicId': public_id})


async def get_client_with_user_id(user_id: int):
    return await get_client({'userId': user_id})


async def get_client(where_param: dict):
    return await prisma.client.find_unique(
        where=where_param
    )
