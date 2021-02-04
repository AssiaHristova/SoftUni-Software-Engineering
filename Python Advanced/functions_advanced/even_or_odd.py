def even_odd(*args):
    command = list(filter(lambda x: isinstance(x, str), args))[0]
    nums = list(filter(lambda x: isinstance(x, int), args))
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, nums))
    elif command == "odd":
        return list(filter(lambda x: x % 2 != 0, nums))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))