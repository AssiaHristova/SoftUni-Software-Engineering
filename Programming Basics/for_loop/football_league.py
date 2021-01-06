capacity = int(input())
fans = int(input())

count_A = 0
count_B = 0
count_V = 0
count_G = 0

for fan in range(1, fans + 1):
    sector = input()
    if sector == 'A':
        count_A += 1
    elif sector == 'B':
        count_B += 1
    elif sector == 'V':
        count_V += 1
    else:
        count_G += 1

print(f'{(count_A / fans) * 100:.2f}%')
print(f'{(count_B / fans) * 100:.2f}%')
print(f'{(count_V / fans) * 100:.2f}%')
print(f'{(count_G / fans) * 100:.2f}%')
print(f'{(fans / capacity) * 100:.2f}%')

