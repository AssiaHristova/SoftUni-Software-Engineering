class Singleton(type):      # rewrite the class behaviour
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class PersonFactory(metaclass=Singleton):
    pass


p = PersonFactory()
print(type(p))
print(type(PersonFactory))
print(PersonFactory() == PersonFactory())
