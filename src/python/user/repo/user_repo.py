from src.python.shared.infra.database.prisma_handler import prisma


async def get_user_with_public_id(public_id: str):
    return await get_user({'publicId': public_id})


async def get_user_with_email(email: str):
    return await get_user({'email': email})


async def get_user(where_param: dict):
    return await prisma.user.find_unique(
        where=where_param
    )
