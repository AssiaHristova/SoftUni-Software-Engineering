import math
targets = input().split('|')
command = input()

targets_nums = [int(num) for num in targets]
points = 0
target = 0

while not command == "Game over":
    command_list = command.split()
    if 'Shoot' in command_list:
        aim = command_list[1].split('@')
        start_index = int(aim[1])
        length = int(aim[2])
        if length > len(targets_nums):
            n = math.floor(length / len(targets_nums))
        else:
            n = 1
        if start_index in range(0, len(targets_nums)):
            if 'Left' in aim:
                target = start_index - length
                if target < 0:
                    target = start_index - length + (len(targets_nums) * n)
                targets_nums[target] -= 5
                points += 5
                if targets_nums[target] < 5:
                    points += targets_nums[target]
                    targets_nums[target] = 0

            elif 'Right' in aim:
                target = start_index + length
                if target > len(targets_nums) - 1:
                    target = start_index + length - (len(targets_nums) * n)
                targets_nums[target] -= 5
                points += 5
                if targets_nums[target] < 5:
                    points += targets_nums[target]
                    targets_nums[target] = 0

    elif 'Reverse' in command_list:
        targets_nums.reverse()

    command = input()

targets_str = [str(num) for num in targets_nums]
print(' - '.join(targets_str))
print(f"Iskren finished the archery tournament with {points} points!")
