operator = (input())
number_1 = int(input())
number_2 = int(input())


def calculator(oper, num_1, num_2):
    result = None
    if oper == 'multiply':
        result = num_1 * num_2
    elif oper == 'divide':
        result = num_1 // num_2
    elif oper == 'add':
        result = num_1 + num_2
    elif oper == 'subtract':
        result = num_1 - num_2
    return result


print(calculator(operator, number_1, number_2))
