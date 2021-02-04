def func_executor(*args):
    result_list = []
    for el in args:
        function_name = el[0]
        arguments = el[1]
        result = function_name(*arguments)
        result_list.append(result)
    return result_list


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
