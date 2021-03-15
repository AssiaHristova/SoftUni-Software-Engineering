from project_2.person import Person
from project_2.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."