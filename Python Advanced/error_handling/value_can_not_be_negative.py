class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f'{value} is negative')


def validate_positive_num(number):
    if number < 0:
        raise ValueCannotBeNegativeError(number)


while True:
    number = int(input())
    validate_positive_num(number)
    print('All numbers are positive')
