games = int(input())

count_1 = 0
count_2 = 0
count_3 = 0
count_others = 0

for game in range(1, games + 1):
    name = input()
    if name == 'Hearthstone':
        count_1 += 1
    elif name == 'Fornite':
        count_2 += 1
    elif name == 'Overwatch':
        count_3 += 1
    else:
        count_others += 1

print(f"Hearthstone - {((count_1 / games) * 100):.2f}%")
print(f"Fornite - {((count_2 / games) * 100):.2f}%")
print(f"Overwatch - {((count_3 / games) * 100):.2f}%")
print(f"Others - {((count_others / games) * 100):.2f}%")

