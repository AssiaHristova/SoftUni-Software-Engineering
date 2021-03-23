class Person:
    counter = -1

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Person.counter += 1
        self.counter = Person.counter

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'Person {self.counter}: {self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        people_names = [p.name for p in self.people]
        people_surnames = [p.surname for p in self.people]
        full_names = [people_names[i] + ' ' + people_surnames[i] for i in range(len(people_names))]
        return f"Group {self.name} with members {', '.join(full_names)}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
