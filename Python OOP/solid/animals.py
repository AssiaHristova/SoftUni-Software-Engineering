from abc import ABC, abstractmethod


class SoundMaker(ABC):
    @abstractmethod
    def make_sound(self, sound):
        pass


class Flier(ABC):
    @abstractmethod
    def fly(self):
        pass


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Cat(Animal, SoundMaker):
    sound = 'mow'

    def make_sound(self, sound):
        return self.sound

    def eat(self):
        pass


class Dog(Animal, SoundMaker):
    sound = 'bau'

    def make_sound(self, sound):
        return self.sound

    def eat(self):
        pass


class Mole(Animal):
    def eat(self):
        pass


class Dragon(Animal, Flier):
    def eat(self):
        pass

    def fly(self):
        pass


def animal_sound(animals):
    for animal in animals:
        sound = animal.sound
        print(animal.make_sound(sound))


animals = [Cat(), Dog()]
animal_sound(animals)
