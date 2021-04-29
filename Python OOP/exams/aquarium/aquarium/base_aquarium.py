from abc import ABC, abstractmethod
from typing import Union
from project_4.fish.saltwater_fish import SaltwaterFish
from project_4.fish.freshwater_fish import FreshwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def available_capacity(self):
        result = self.capacity - len(self.fish)
        return result > 0

    def add_fish(self, fish: Union[SaltwaterFish, FreshwaterFish]):
        if not self.available_capacity():
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        if not self.fish:
            fish_result = f"Fish: none\n"
        else:
            fish_result = [f.name for f in self.fish]
        result = f"{self.name}:\n"
        result += f"Fish: {' '.join(fish_result)}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result


