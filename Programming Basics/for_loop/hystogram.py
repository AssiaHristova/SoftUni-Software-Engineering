n = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0
p5 = 0.0

for i in range(n):
    number = int(input())
    if 1 <= number < 200:
        count1 += 1
        p1 = (count1 / n) * 100
    elif 200 <= number < 400:
        count2 += 1
        p2 = (count2 / n) * 100
    elif 400 <= number < 600:
        count3 += 1
        p3 = (count3 / n) * 100
    elif 600 <= number < 800:
        count4 += 1
        p4 = (count4 / n) * 100
    elif 800 <= number <= 1000:
        count5 += 1
        p5 = (count5 / n) * 100


print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
