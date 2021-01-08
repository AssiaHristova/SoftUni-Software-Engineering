gifts = input().split()
command = input()

while not command == "No Money":
    command_list = command.split()
    if 'OutOfStock' in command_list:
        gift = command_list[1]
        if gift in gifts:
            for i in range(0, len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = "None"
    elif "Required" in command_list:
        gift = command_list[1]
        index = int(command_list[2])
        if index in range(0, len(gifts)):
            gifts[index] = gift
    elif "JustInCase" in command_list:
        gift = command_list[1]
        gifts[-1] = gift

    command = input()

for gift in gifts:
    if gift == "None":
        gifts.remove(gift)

print(' '.join(gifts))


