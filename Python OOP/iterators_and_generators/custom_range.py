class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.index = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.index > self.custom_range_obj.end:
                raise StopIteration
            index = self.index
            self.index += 1
            return index


for x in CustomRange(1, 10):
    print(x)

cr = CustomRange(1, 10)
iter1 = iter(cr)
iter2 = iter(cr)

for x in iter1:
    print(x)

for x in iter2:
    print(x)

for x in reversed(cr):
    print(x)