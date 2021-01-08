sugar_cubes = input().split()
command = input()

sugar_cubes_int = [int(element) for element in sugar_cubes]

while not command == "Mort":
    command_list = command.split()
    if 'Add' in command_list:
        value = int(command_list[1])
        sugar_cubes_int.append(value)
    elif 'Remove' in command_list:
        value = int(command_list[1])
        sugar_cubes_int.remove(value)
    elif 'Replace' in command_list:
        value = int(command_list[1])
        replacement = int(command_list[2])
        count = 0
        if value in sugar_cubes_int:
            for i in range(len(sugar_cubes_int)):
                if sugar_cubes_int[i] == value:
                    count += 1
                    if count == 1:
                        sugar_cubes_int[i] = replacement
    elif 'Collapse' in command_list:
        value = int(command_list[1])
        greater_than_value = []
        for element in sugar_cubes_int:
            if element >= value:
                greater_than_value.append(element)
        sugar_cubes_int.clear()
        sugar_cubes_int = greater_than_value

    command = input()

sugar_cubes_str = [str(element) for element in sugar_cubes_int]
print(' '.join(sugar_cubes_str))



