def first_function():
    print('from first')


def second_function():
    first_function()
    print('from second')


second_function()


