from src.python.shared.infra.database.prisma_handler import prisma


async def shutdown():
    print('[DATABASE] Disconnecting to the database')
    await prisma.disconnect()
    print('[APP] App is shut down')