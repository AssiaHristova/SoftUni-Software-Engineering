n = int(input())

count1 = 0
count2 = 0
count3 = 0
p1 = 0.0
p2 = 0.0
p3 = 0.0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        count1 += 1
        p1 = (count1 / n) * 100
    if number % 3 == 0:
        count2 += 1
        p2 = (count2 / n) * 100
    if number % 4 == 0:
        count3 += 1
        p3 = (count3 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
