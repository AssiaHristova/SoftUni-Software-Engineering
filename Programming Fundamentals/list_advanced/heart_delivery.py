houses = input().split('@')
command = input()

hearts = [int(house) for house in houses]
house_failed = len(hearts)
last_position = 0

while not command == "Love!":
    length = int(command[-1])
    if (last_position + length) > (len(hearts) + 1):
        length = 0
    else:
        length += last_position
    if hearts[length] > 0:
        hearts[length] -= 2
        if hearts[length] == 0:
            house_failed -= 1
            print(f"Place {length} has Valentine's day.")
    else:
        print(f"Place {length} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_position}.")

if house_failed > 0:
    print(f"Cupid has failed {house_failed} places.")
else:
    print("Mission was successful.")

