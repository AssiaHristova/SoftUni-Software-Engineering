
from aquarium.aquarium.freshwater_aquarium import FreshwaterAquarium
from aquarium.aquarium.saltwater_aquarium import SaltwaterAquarium
from aquarium.decoration.decoration_repository import DecorationRepository
from aquarium.decoration.ornament import Ornament
from aquarium.decoration.plant import Plant
from aquarium.fish.freshwater_fish import FreshwaterFish
from aquarium.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def find_aquarium(self, aquarium_name):
        aquarium = None
        aquariums = [a for a in self.aquariums if a.name == aquarium_name]
        if aquariums:
            aquarium = aquariums[0]
        return aquarium

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration:
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        else:
            return f"There isn't a decoration of type {decoration_type}."

    @staticmethod
    def is_water_suitable(fish, fish_type):
        return fish.__class__.__name__ == fish_type

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)

        if not fish:
            return f"There isn't a fish of type {fish_type}."

        if not self.is_water_suitable(fish, fish_type):
            return "Water not suitable."

        aquarium = self.find_aquarium(aquarium_name)
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        fish_value = sum([f.price for f in aquarium.fish])
        decorations_value = sum([d.price for d in aquarium.decorations])
        value = fish_value + decorations_value
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result



controller = Controller()
print(controller.add_aquarium('SaltwaterAquarium', 'salt'))
print(controller.add_decoration('Plant'))
print(controller.insert_decoration('salt', 'Plant'))
print(controller.add_fish('salt', 'SaltwaterFish', 'dorry', 'saltfish', 20))
print(controller.feed_fish('salt'))
print(controller.calculate_value('salt'))
print(controller.report())









