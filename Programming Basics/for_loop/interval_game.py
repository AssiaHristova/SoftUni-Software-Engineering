moves = int(input())

result = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for move in range(1, moves + 1):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.2
        count1 += 1
    elif 10 <= number <= 19:
        result += number * 0.3
        count2 += 1
    elif 20 <= number <= 29:
        result += number * 0.4
        count3 += 1
    elif 30 <= number <= 39:
        result += 50
        count4 += 1
    elif 40 <= number <= 50:
        result += 100
        count5 += 1
    else:
        result -= result / 2
        count6 += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {(count1 / moves) * 100:.2f}%")
print(f"From 10 to 19: {(count2 / moves) * 100:.2f}%")
print(f"From 20 to 29: {(count3 / moves) * 100:.2f}%")
print(f"From 30 to 39: {(count4 / moves) * 100:.2f}%")
print(f"From 40 to 50: {(count5 / moves) * 100:.2f}%")
print(f"Invalid numbers: {(count6 / moves) * 100:.2f}%")

