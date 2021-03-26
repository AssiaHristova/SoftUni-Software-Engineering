class vowels:   # iterator
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        if char not in self.vowels:
            return self.__next__()
        return char


def vowels_gen(text):   # gen function
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
    for ch in text:
        if ch in vowels:
            yield ch


def vowels_g(text):     # gen comprehension
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
    return (ch for ch in text if ch in vowels)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

my_string_2 = vowels_gen('Abcedifuty0o')
print(list(my_string_2))

my_string_3 = vowels_g('Abcedifuty0o')
print(list(my_string_3))





