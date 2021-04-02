import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_string = ', '.join([str(el) for el in args])
        kwargs_string = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        parameters = args_string + kwargs_string
        result = func(*args, **kwargs)
        return f'you called {func.__name__}({parameters})\nit returned {result}'

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

