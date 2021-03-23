import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * self.__radius * math.pi

    def calculate_area(self):
        return self.__radius ** 2 * math.pi


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_perimeter(self):
        return (self.__width + self.__height) * 2

    def calculate_area(self):
        return self.__width * self.__height


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

