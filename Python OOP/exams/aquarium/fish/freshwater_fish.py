from aquarium.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    initial_size = 3

    def __init__(self, name: str, species: str, price: float):
        super(FreshwaterFish, self).__init__(name, species, self.initial_size, price)

    def eat(self):
        self.size += 3

