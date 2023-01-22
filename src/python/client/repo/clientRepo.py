from src.python.client.domain.client_model import Client
from src.python.shared.infra.database.prisma_handler import prisma


async def create_client(client: Client):
    await prisma.client.create({
        'data': client
    })


async def update_client():
    await prisma.client.update({
        'data': {}
    })


async def get_client():
    await prisma.client.find_unique({
        'where': {

        }
    })
