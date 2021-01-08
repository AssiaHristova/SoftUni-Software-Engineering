n = int(input())

for i in range(1, n + 1):
    sum_digits = 0
    num_str = str(i)
    for digit in num_str:
        sum_digits += int(digit)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')


