num = int(input())

for i in range(1, num + 1):
    symbol = '*'
    print(f'{symbol * i}')
for i in range(num - 1, 0, -1):
    symbol = '*'
    print(f'{symbol * i}')

