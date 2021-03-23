import math
import json
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        if type(self) == Shape:
            raise TypeError('Shape is abstract')

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * math.pi

    def area(self):
        return self.radius ** 2 * math.pi


class Serializer(ABC):
    def __init__(self, print_func):
        self.print_func = print_func

    @abstractmethod # the child class needs to implement the abstract method, otherwise it will brake
    def serialize(self, obj):
        pass

    def print(self, obj):
        return self.print_func(self.serialize(obj))


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj.__dict__)


class TextSerializer(Serializer):
    def serialize(self, obj):
        return '; '.join(f'{key}={value}' for key, value in obj.__dict__.items())


circle = Circle(5)
print(circle.area())
JsonSerializer(print)\
    .print(circle)