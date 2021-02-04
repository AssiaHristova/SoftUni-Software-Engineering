nums = [int(el) for el in input().split()]

filtered_nums = list(filter(lambda x: x % 2 == 0, nums))
print(filtered_nums)



