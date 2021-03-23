from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = 'mow'

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = 'bau'

    def get_sound(self):
        return self.sound


class Mole(Animal):
    def get_sound(self):    # DON'T DO THAT
        raise TypeError("Moles don't make sounds")


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())





animals = [Cat(), Dog()]
animal_sound(animals)
