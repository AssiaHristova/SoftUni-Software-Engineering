sequence = input().split()

nums = [int(num) for num in sequence]
average = sum(nums) / len(nums)

greater_nums = []
for num in nums:
    if num > average:
        greater_nums.append(num)

greater_nums.sort(reverse=True)

if len(greater_nums) == 0:
    print('No')
elif len(greater_nums) > 5:
    top_5 = greater_nums[:5]
    top_5_str = [str(num) for num in top_5]
    print(' '.join(top_5_str))
else:
    greater_nums_str = [str(num) for num in greater_nums]
    print(' '.join(greater_nums_str))



