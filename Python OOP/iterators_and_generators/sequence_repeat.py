class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        index = self.index
        while index > len(self.sequence) - 1:
            index -= len(self.sequence)
        ele = self.sequence[index]
        self.index += 1
        return ele


result = sequence_repeat('abc', 8)
for item in result:
    print(item, end ='')
