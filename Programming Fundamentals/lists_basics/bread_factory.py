string = input()

energy = 100
coins = 100

events_list = string.split('|')
Flag = True

for element in events_list:
    elements_list = element.split('-')
    event = elements_list[0]
    num = int(elements_list[1])
    if event == "rest":
        if (energy + num) <= 100:
            energy += num
            print(f"You gained {num} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {0} energy.")
            print(f"Current energy: {energy}.")
    elif event == "order":
        if (energy - 30) >= 0:
            energy -= 30
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if (coins - num) > 0:
            coins -= num
            print(f"You bought {event}.")
        else:
            Flag = False
            print(f"Closed! Cannot afford {event}.")
            break

if Flag is True:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



