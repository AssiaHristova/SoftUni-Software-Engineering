def abs_values(nums_list):
    return [abs(el) for el in nums]
    #return list(map(abs, nums))


nums = [float(el) for el in input().split()]
#nums = map(float, input().split())

print(abs_values(nums))
