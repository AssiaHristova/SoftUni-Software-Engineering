def round_elements(list_nums):
    return list(map(abs, nums))


nums = map(float, input().split())

print(round_elements(nums))