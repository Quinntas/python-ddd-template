from src.python.shared.core.guard import MultiGuard


class ValueObject(object):
    def __int__(self, value: any = None):
        self.multi_guard: MultiGuard = MultiGuard()
        self.value = value

    def set_multi_guard(self):
        self.multi_guard: MultiGuard = MultiGuard()
        return self.multi_guard

    def get_value(self):
        return self.value

    def set_value(self, value: any):
        self.value = value
        return self.value
