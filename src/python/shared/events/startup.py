from src.python.shared.infra.database.prisma_handler import prisma


async def startup():
    print('[DATABASE] Connecting to the database')
    await prisma.connect()
    print('[APP] App is running')
