number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def sum_numbers(num_1, num_2):
    result_add = num_1 + num_2
    return result_add


def subtract_numbers(sum_1, num_3):
    result_subtract = sum_1 - num_3
    return result_subtract


def add_and_subtract(num_1, num_2, num_3):
    result = subtract_numbers(sum_numbers(num_1, num_2), num_3)
    return result


print(add_and_subtract(number_1, number_2, number_3))

