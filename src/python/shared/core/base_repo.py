from abc import ABC

from src.python.shared.infra.database.prisma_handler import prisma


class BaseRepo(ABC):
    @staticmethod
    async def get_unique(prisma_model: str, where: dict, include: dict = None):
        return await getattr(prisma, prisma_model).find_unique(
            where=where,
            include=include
        )

    @staticmethod
    async def create(prisma_model: str, data: dict):
        return await getattr(prisma, prisma_model).create(
            data=data,
        )

    @staticmethod
    async def update(prisma_model: str, data: dict, where: dict, include: dict = None):
        return await getattr(prisma, prisma_model).update(
            data=data,
            where=where,
            include=include
        )
