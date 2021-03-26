class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.Iterator(self)

    def __reversed__(self):
        return self.Iterator(self, is_reversed=True)

    class Iterator:
        def __init__(self, custom_range_obj, is_reversed=False):
            self.custom_range_obj = custom_range_obj
            self.is_reversed = is_reversed
            if is_reversed:
                self.index = custom_range_obj.end
            else:
                self.index = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.index > self.custom_range_obj.end or self.index < self.custom_range_obj.start:
                raise StopIteration
            index = self.index
            if self.is_reversed:
                self.index -= 1
            else:
                self.index += 1
            return index