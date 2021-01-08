gifts = input()

command = ''
gifts_list = gifts.split(' ')

while not command == "No Money":
    command = input()
    command_list = command.split(' ')
    for word in command_list:
        if word == "OutOfStock":
            command_list.remove("OutOfStock")
            gift = str(command_list[0])
            for i in gifts_list:
                if i == gift:
                    index = gifts_list.index(gift)
                    gifts_list[index] = "None"
        elif word == "Required":
            command_list.remove("Required")
            gift = command_list[0]
            index = int(command_list[1])
            if index in range(len(gifts_list)):
                gifts_list[index] = gift
        elif word == "JustInCase":
            command_list.remove("JustInCase")
            gift = str(command_list[0])
            gifts_list[-1] = gift

for j in gifts_list:
    if not j == 'None':
        print(j, end=' ')




