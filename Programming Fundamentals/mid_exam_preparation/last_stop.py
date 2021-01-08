paintings = input().split()
command = input()

paintings_nums = [int(painting) for painting in paintings]

while not command == "END":
    command_list = command.split()
    if 'Change' in command_list:
        painting_1 = int(command_list[1])
        painting_2 = int(command_list[2])
        if painting_1 in paintings_nums:
            for i in range(0, len(paintings_nums)):
                if paintings_nums[i] == painting_1:
                    paintings_nums[i] = painting_2
    elif 'Hide' in command_list:
        painting = int(command_list[1])
        if painting in paintings_nums:
            paintings_nums.remove(painting)
    elif 'Switch' in command_list:
        painting_1 = int(command_list[1])
        painting_2 = int(command_list[2])
        index_1 = 0
        index_2 = 0
        if painting_1 in paintings_nums and painting_2 in paintings_nums:
            for i in range(0, len(paintings_nums)):
                if paintings_nums[i] == painting_1:
                    index_1 = i
            for j in range(0, len(paintings_nums)):
                if paintings_nums[j] == painting_2:
                    index_2 = j
            paintings_nums[index_1], paintings_nums[index_2] = paintings_nums[index_2], paintings_nums[index_1]
    elif 'Insert' in command_list:
        index = int(command_list[1])
        painting = int(command_list[2])
        if index in range(0, len(paintings_nums)):
            paintings_nums.insert(index + 1, painting)
    elif 'Reverse' in command_list:
        paintings_nums.reverse()

    command = input()

paintings_str = [str(painting) for painting in paintings_nums]
print(' '.join(paintings_str))



