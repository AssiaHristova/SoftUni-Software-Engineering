n = int(input())

number = 0
avg_num = 0

for i in range(1, n + 1):
    number = int(input())
    avg_num += number / n

print(f'{avg_num:.2f}')

