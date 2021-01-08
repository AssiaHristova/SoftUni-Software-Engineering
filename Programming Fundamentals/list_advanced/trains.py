wagons = int(input())

train = [0 for _ in range(wagons)]

command = input()

while not command == 'End':
    command_list = command.split()
    if 'add' in command_list:
        people = int(command_list[1])
        train[-1] += people
    elif 'insert' in command_list:
        index = int(command_list[1])
        people = int(command_list[2])
        train[index] += people
    elif 'leave' in command_list:
        index = int(command_list[1])
        people = int(command_list[2])
        train[index] -= people

    command = input()

print(train)
