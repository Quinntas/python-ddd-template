from abc import ABC, abstractmethod


class BaseMapper(ABC):
    @abstractmethod
    def to_domain(self, *args, **kwargs):
        pass

    @abstractmethod
    def to_dict(self, *args, **kwargs):
        pass
