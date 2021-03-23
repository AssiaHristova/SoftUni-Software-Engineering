from project_2.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super(Cat, self).__init__(name, age, gender)

    def make_sound(self):
        return "Hiss"

    def repr(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


tom = Tomcat('Tom', 3)
print(tom.make_sound())
print(tom.repr())


