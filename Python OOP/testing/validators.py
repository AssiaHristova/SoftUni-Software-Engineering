from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, *args, **kwargs):
        pass


class TypeValidator(Validator):
    def validate(self, value, types):
        if type(value) not in types:
            raise ValueError('numbers should be numbers.')

