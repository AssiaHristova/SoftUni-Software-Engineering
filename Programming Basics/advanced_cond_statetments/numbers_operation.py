N1 = int(input())
N2 = int(input())
operation = input()


if operation == '+' or \
        operation == '-' or \
        operation == '*':
    result = 0
    if operation == '+':
        result = N1 + N2
    elif operation == '-':
        result = N1 - N2
    else:
        result = N1 * N2
    if result % 2 == 0:
        print(f'{N1} {operation} {N2} = {result} - even')
    else:
        print(f'{N1} {operation} {N2} = {result} - odd')

if N2 != 0 and operation == '/':
    result = N1 / N2
    print(f'{N1} / {N2} = {result:.2f}')
elif N2 != 0 and operation == '%':
    result = N1 % N2
    print(f'{N1} % {N2} = {result}')
elif N2 == 0:
    print(f'Cannot divide {N1} by zero')
