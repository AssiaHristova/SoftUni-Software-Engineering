number = int(input())


def sum_odd_even(num):
    sum_even = 0
    sum_odd = 0
    for symbol in str(num):
        if int(symbol) % 2 == 0:
           sum_even += int(symbol)
        else:
            sum_odd += int(symbol)
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


print(sum_odd_even(number))

