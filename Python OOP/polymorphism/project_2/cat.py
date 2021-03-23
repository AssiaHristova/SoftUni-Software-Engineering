from project_2.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super(Cat, self).__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"

    def repr(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"