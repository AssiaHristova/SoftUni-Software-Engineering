def age_assignment(*args, **kwargs):
    persons = {}
    names = list(filter(lambda x: isinstance(x, str), args))
    for letter, age in kwargs.items():
        for name in names:
            if name.startswith(letter):
                persons[name] = age
    return persons


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))




