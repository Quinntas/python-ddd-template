class ValueObject(object):
    def __int__(self, value):
        self.value = value

    def get_value(self):
        return self.value
