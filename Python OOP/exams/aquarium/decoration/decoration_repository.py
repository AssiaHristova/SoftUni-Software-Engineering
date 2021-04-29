from aquarium.decoration.ornament import Ornament
from aquarium.decoration.plant import Plant
from typing import Union


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: Union[Ornament, Plant]):
        self.decorations.append(decoration)

    def remove(self, decoration: Union[Ornament, Plant]):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        decorations = [d for d in self.decorations if d.__class__.__name__ == decoration_type]
        if decorations:
            decoration = decorations[0]
            return decoration
        return "None"

