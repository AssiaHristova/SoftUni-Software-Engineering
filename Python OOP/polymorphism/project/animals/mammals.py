from project.animals.animal import Animal
from abc import abstractmethod
from project.food import Meat, Vegetable, Fruit


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super(Mammal, self).__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ != 'Vegetable' and food.__class__.__name__ != 'Fruit':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(food, 0.10)


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(food, 0.40)


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ != 'Meat' and food.__class__.__name__ != 'Vegetable':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(food, 0.30)


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(food, 1)


owl = Cat("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
fruit = Fruit(5)
owl.feed(fruit)
print(owl)

hen = Mouse("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

