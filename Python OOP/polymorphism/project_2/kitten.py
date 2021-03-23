from project_2.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super(Cat, self).__init__(name, age, gender)

    def make_sound(self):
        return "Meow"

    def repr(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


kitten = Kitten('Kitty', 2)
print(kitten.make_sound())
print(kitten.repr())