from project_2.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super(Dog, self).__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"

    def repr(self):
        f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"