n = int(input())
m = int(input())

for number in range(n, m + 1):
    num_in_str = str(number)
    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(num_in_str):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_even == sum_odd:
        print(number, end=' ')



