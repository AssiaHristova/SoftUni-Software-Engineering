import sys

n = int(input())

sum_even = 0
sum_odd = 0
max_odd = -sys.maxsize
min_odd = sys.maxsize
max_even = -sys.maxsize
min_even = sys.maxsize

for i in range(1, n+1):
    number = float(input())
    if i % 2 == 0:
        sum_even += number
        if number > max_even:
            max_even = number
        if number < min_even:
            min_even = number
    else:
        sum_odd += number
        if number > max_odd:
            max_odd = number
        if number < min_odd:
            min_odd = number

print(f'OddSum={sum_odd:.2f},')
if not min_odd == sys.maxsize:
    print(f'OddMin={min_odd:.2f},')
else:
    print('OddMin=No,')
if not max_odd == -sys.maxsize:
    print(f'OddMax={max_odd:.2f},')
else:
    print('OddMax=No,')
print(f'EvenSum={sum_even:.2f},')
if not min_even == sys.maxsize:
    print(f'EvenMin={min_even:.2f},')
else:
    print('EvenMin=No,')
if not max_even == -sys.maxsize:
    print(f'EvenMax={max_even:.2f}')
else:
    print('EvenMax=No')
