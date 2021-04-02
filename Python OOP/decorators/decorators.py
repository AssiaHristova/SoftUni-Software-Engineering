import functools
from time import time


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed for {end - start} seconds.')
        return result

    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_string = ', '.join(args)
        kwargs_string = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args_string}, {kwargs_string}) returned {result}')
        return result

    return wrapper

@uppercase
@debug
def get_hello(name):
    return f'Hello, I am {name}'


@uppercase
def get_temperature():
    return '3 degrees celsius'


@measure_time
def big_loop():
    x = 0
    for _ in range(100000):
        x += 1
    return x


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(4)
def print_text():
    print('Hello from me')


temp = uppercase(get_temperature)
print(get_hello('Pesho'))
print(get_temperature())
big_loop()
print_text()





