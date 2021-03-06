from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing Circle')


class Rectangle(Shape):
    def draw(self):
        print('Drawing Rectangle')


Circle().draw()
Rectangle().draw()