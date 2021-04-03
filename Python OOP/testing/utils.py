from validators import TypeValidator


class Utils:
    def __init__(self):
        self.validator = TypeValidator()

    def my_sum(self, numbers):
        [self.validator.validate(x, [int, float]) for x in numbers]
        return sum(numbers)
