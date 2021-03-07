from project.gym import Gym



class Equipment:
    id = 0

    def __init__(self, name):
        self.name = name
        self.id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return len(Gym.equipment) + 1