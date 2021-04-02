from dataclasses import dataclass


class singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


def singleton_2(func):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = func(*args, **kwargs)
        return instance

    return wrapper


@singleton_2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@dataclass
class Person_2:
    name: str
    age: int


gosho = Person('Gosho', 17)
pesho = Person('Pesho', 16)
print(id(pesho))
print(id(gosho))
print(pesho == gosho)
maria = Person_2('Maria', 11)
print(maria)

