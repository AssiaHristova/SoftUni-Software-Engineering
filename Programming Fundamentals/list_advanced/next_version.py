first_version = input().split('.')

first_version_nums = list(map(lambda x: int(x), first_version))
next_version = [num for num in first_version_nums]

if (first_version_nums[2] + 1) < 9:
    next_version[2] += 1
else:
    next_version[2] = 0
    next_version[1] += 1
    if next_version[1] > 9:
        next_version[1] = 0
        next_version[0] += 1

result = [str(el) for el in next_version]
print('.'.join(result))




