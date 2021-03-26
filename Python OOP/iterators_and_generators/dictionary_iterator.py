class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if  not self.dictionary:
            raise StopIteration
        for key, value in self.dictionary.items():
            result = key, value
            self.dictionary.pop(key)
            self.index += 1
            return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
