class Dog:
    def sound(self):
        print('Bau')


class Car:
    def sound(self):
        print('Brum')


def make_sound(obj):
    obj.sound()


make_sound(Dog())
make_sound(Car())

