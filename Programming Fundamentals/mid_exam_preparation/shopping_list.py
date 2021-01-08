groceries = input().split("!")
command = input()

while not command == "Go Shopping!":
    command_list = command.split()

    if 'Urgent' in command_list:
        if command_list[1] not in groceries:
            groceries.insert(0, command_list[1])
    elif 'Unnecessary' in command_list:
        if command_list[1] in groceries:
            groceries.remove(command_list[1])
    elif 'Correct' in command_list:
        if command_list[1] in groceries:
            for i in range(len(groceries)):
                if groceries[i] == command_list[1]:
                    groceries[i] = command_list[2]
    elif 'Rearrange' in command_list:
        if command_list[1] in groceries:
            groceries.remove(command_list[1])
            groceries.append(command_list[1])

    command = input()

print(', '.join(groceries))
