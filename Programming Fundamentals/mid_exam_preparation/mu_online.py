rooms = input().split('|')

health = 100
bitcoins = 0
count = 0

for room in rooms:
    command = room.split()
    count += 1
    if "potion" in command:
        if health + int(command[-1]) < 100:
            health += int(command[-1])
            print(f"You healed for {command[-1]} hp.")
        else:
            print(f"You healed for {(100 - health)} hp.")
            health = 100
        print(f"Current health: {health} hp.")
    elif "chest" in command:
        bitcoins += int(command[-1])
        print(f"You found {command[-1]} bitcoins.")
    else:
        health -= int(command[-1])
        if health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {count}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
