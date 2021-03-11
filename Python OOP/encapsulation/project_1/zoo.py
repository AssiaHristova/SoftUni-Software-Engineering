from project_1.lion import Lion
from project_1.tiger import Tiger
from project_1.cheetah import Cheetah
from project_1.keeper import Keeper
from project_1.vet import Vet
from project_1.caretaker import Caretaker


class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker_names = [w for w in self.workers if w.name == worker_name]
        if not worker_names:
            return f"There is no {worker_name} in the zoo"
        worker = worker_names[0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salaries = [w.salary for w in self.workers]
        if self.__budget < sum(workers_salaries):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum(workers_salaries)
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_costs = [a.get_needs() for a in self.animals]
        if self.__budget < sum(animal_costs):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum(animal_costs)
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if type(a) == Lion]
        tigers = [a for a in self.animals if type(a) == Tiger]
        cheetahs = [a for a in self.animals if type(a) == Cheetah]
        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join([str(lion) for lion in lions])
        result += '\n'
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join([str(tiger) for tiger in tigers])
        result += '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join([str(cheetah) for cheetah in cheetahs])
        return result

    def workers_status(self):
        keepers = [w for w in self.workers if type(w) == Keeper]
        vets = [w for w in self.workers if type(w) == Vet]
        caretakers = [w for w in self.workers if type(w) == Caretaker]
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join([str(keeper) for keeper in keepers])
        result += '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join([str(caretaker) for caretaker in caretakers])
        result += '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join([str(vet) for vet in vets])
        return result