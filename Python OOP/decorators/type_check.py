import functools


def is_type_valid(parameter_type, parameter):
    return parameter_type == type(parameter)


def type_check(parameter_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(parameter):
            nonlocal parameter_type
            if is_type_valid(parameter_type, parameter):
                return func(parameter)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
