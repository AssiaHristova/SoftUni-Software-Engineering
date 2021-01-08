array = input().split()
command = input()

array_nums = [int(num) for num in array]

while not command == 'end':
    command_list = command.split()
    if 'swap' in command_list:
        index_1 = int(command_list[1])
        index_2 = int(command_list[2])
        array_nums[index_1], array_nums[index_2] = array_nums[index_2], array_nums[index_1]
    elif 'multiply' in command:
        index_1 = int(command_list[1])
        index_2 = int(command_list[2])
        array_nums[index_1] *= array_nums[index_2]
    elif 'decrease' in command_list:
        for i in range(len(array_nums)):
            array_nums[i] -= 1

    command = input()

array_str = [str(num) for num in array_nums]
print(', '.join(array_str))

