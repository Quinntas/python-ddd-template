import datetime

from src.python.shared.core.value_object.value_object import ValueObject


class SharedDatetime(ValueObject):
    def __init__(self, dt: datetime.datetime = None):
        self.dt: datetime.datetime = dt

        super().__int__(self.dt)

    def get_value(self) -> str:
        return self.dt.strftime("%d/%m/%Y-%H:%M:%S")
