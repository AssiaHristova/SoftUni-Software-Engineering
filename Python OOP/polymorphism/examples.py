import math
import json


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * math.pi

    def area(self):
        return self.radius ** 2 * math.pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)

    def __add__(self, other):
        return Square(self.width + other.width)


class Serializer:
    def serialize(self, obj):
        pass


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj.__dict__)


class TextSerializer(Serializer):
    def serialize(self, obj):
        return '; '.join(f'{key}={value}' for key, value in obj.__dict__.items())


def get_serializer(type):
    if type == 'json':
        return JsonSerializer()
    elif type == 'text':
        return TextSerializer()


type = 'json'
type_2 = 'text'
serializer = get_serializer(type)
serializer_2 = get_serializer(type_2)
print(serializer.serialize(Square(3)))
print(serializer_2.serialize(Circle(4)))

circle = Circle(6)
print(isinstance(circle, Circle))
print(isinstance(circle, Shape))
print(isinstance(circle, object))
rectangle = Rectangle(10, 5)


def print_shape(s: Shape):
    print(f'Perimeter: {s.perimeter()}')
    print(f'Area: {s.area()}')


def print_shapes(shapes: [Shape]):
    for s in shapes:
        print_shape(s)


print_shape(circle)
print_shape(rectangle)
print_shapes([circle, rectangle, Square(4), Shape()])

print(dir(circle))

square_1 = Square(3)
square_2 = Square(4)
print(serializer.serialize(square_1 + square_2))








