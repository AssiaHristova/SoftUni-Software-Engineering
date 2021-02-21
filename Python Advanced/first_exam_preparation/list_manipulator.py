from collections import deque


def list_manipulator(numbers, *args):
    commands = deque()
    nums = []

    for el in args:
        if isinstance(el, str):
            commands.append(el)
        else:
            nums.append(el)

    while commands:
        first_command = commands.popleft()
        second_command = commands.popleft()
        if first_command == "add":
            if second_command == "beginning":
                for i in range(len(nums)):
                    numbers.insert(i, nums[i])
                return numbers
            elif second_command == "end":
                for num in nums:
                    numbers.append(num)
                return numbers
        elif first_command == "remove":
            if second_command == "beginning":
                if nums:
                    for i in range(nums[0]):
                        numbers.pop(0)
                else:
                    numbers.pop(0)
                return numbers
            elif second_command == "end":
                if nums:
                    for i in range(nums[0]):
                        numbers.pop()
                else:
                    numbers.pop()
                return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
