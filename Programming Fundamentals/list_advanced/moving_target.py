targets = input().split()
command = input()

targets_list = [int(target) for target in targets]

while not command == 'End':
    index = 0
    power = 0
    command_list = command.split()
    if 'Shoot' in command_list:
        index = int(command_list[1])
        power = int(command_list[2])
        if index in range (len(targets_list)):
            targets_list[index] -= power
            if targets_list[index] <= 0:
                targets_list.remove(targets_list[index])
    elif 'Add' in command_list:
        index = int(command_list[1])
        value = int(command_list[2])
        if index in range(len(targets_list)):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif 'Strike' in command_list:
        index = int(command_list[1])
        radius = int(command_list[2])
        target_radius = targets_list[index]
        if index in range(len(targets_list)) and index + radius in range(len(targets_list)) and index - radius in range(len(targets_list)):
            result_1 = targets_list[:index - radius]
            result_2 = targets_list[index + radius + 1:]
            targets_list = result_1 + result_2
        else:
            print("Strike missed!")

    command = input()

targets_list_str = list(map(lambda target: str(target), targets_list))
result = '|'.join(targets_list_str)
print(result)
