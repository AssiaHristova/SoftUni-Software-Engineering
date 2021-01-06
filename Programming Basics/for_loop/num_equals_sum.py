import sys

n = int(input())

sum_numbers = 0
number_max = -sys.maxsize

for i in range(n):
    number = int(input())
    sum_numbers += number
    if number > number_max:
        number_max = number


if sum_numbers - number_max == number_max:
    print('Yes')
    print(f'Sum = {number_max}')
else:
    print('No')
    print(f'Diff = {abs(number_max - (sum_numbers - number_max))}')

