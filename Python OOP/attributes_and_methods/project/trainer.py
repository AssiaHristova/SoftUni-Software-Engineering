from project.gym import Gym


class Trainer:
    id = 0

    def __init__(self, name):
        self.name = name
        self.id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return len(Gym.trainers) + 1
