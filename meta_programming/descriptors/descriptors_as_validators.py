import abc
from numbers import Number

class Validated(abc.ABC):

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        instance.__dict__[self.storage_name] = self.validate(value)

    def __get__(self, instance, owner):
        return instance.__dict__[self.storage_name]

    @abc.abstractmethod
    def validate(self, value):
        pass


class ValidateIsNumber(Validated):

    def validate(self, value):
        if not isinstance(value, Number):
            raise TypeError
        return value

class ValidateIsNotBlack(Validated):

    def validate(self, value):
        value = value.strip()
        if not value:
            raise TypeError
        return value
