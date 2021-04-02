import functools


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key_tuple = args + tuple(kwargs.values())
        cache_key = cache_key_tuple[0]
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func(*args, **kwargs)
        return wrapper.log[cache_key]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

