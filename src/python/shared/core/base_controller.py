from abc import ABC, abstractmethod


class BaseController(ABC):
    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass
