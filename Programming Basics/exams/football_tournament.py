team = input()
matches = int(input())

points = 0
count_w = 0
count_d = 0
count_l = 0

for match in range(1, matches + 1):
    result = input()
    if result == 'W':
        points += 3
        count_w += 1
    elif result == 'D':
        points += 1
        count_d += 1
    else:
        count_l += 1


if matches == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {count_w}")
    print(f"## D: {count_d}")
    print(f"## L: {count_l}")
    print(f"Win rate: {((count_w / matches) * 100):.2f}%")

