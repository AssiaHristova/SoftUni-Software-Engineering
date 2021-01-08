houses = input().split('@')
command = input()

hearts = [int(house) for house in houses]
house_failed = len(hearts)
last_position = 0

while not command == "Love!":
    command_list = command.split()
    jump = int(command_list[1])
    if (last_position + jump) > (len(hearts) - 1):
        jump = 0
    else:
        jump += last_position
    if hearts[jump] > 0:
        hearts[jump] -= 2
        if hearts[jump] == 0:
            house_failed -= 1
            print(f"Place {jump} has Valentine's day.")
    elif hearts[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
    last_position = jump

    command = input()

print(f"Cupid's last position was {last_position}.")

if not house_failed == 0:
    print(f"Cupid has failed {house_failed} places.")
else:
    print("Mission was successful.")