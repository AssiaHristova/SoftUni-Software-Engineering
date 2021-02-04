def odd_or_even(nums, command):
    if command == "Odd":
        print(f'{sum([num for num in nums if not num % 2 == 0]) * len(nums)}')
    elif command == "Even":
        print(f'{sum([num for num in nums if num % 2 == 0]) * len(nums)}')


command = input()
nums = [int(el) for el in input().split()]

odd_or_even(nums, command)




