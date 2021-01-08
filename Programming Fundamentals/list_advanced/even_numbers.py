string = [int(el) for el in input().split(', ')]

even_nums = [index for index in range(len(string)) if string[index] % 2 == 0]

print(even_nums)

nums = list(map(int, input().split(', ')))
even_numbers = list(filter(lambda index: nums[index] % 2 == 0, range(len(nums))))
print(even_numbers)





