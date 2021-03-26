class take_skip:
    start_count = 0

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_count >= self.count:
            raise StopIteration
        index = self.index
        self.start_count += 1
        self.index += self.step
        return index


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

