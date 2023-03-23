from abc import abstractmethod

from pydantic import BaseModel


class BaseDomain(BaseModel):
    class Config:
        arbitrary_types_allowed = True

        @abstractmethod
        def get_private_attributes(self) -> list:
            pass
