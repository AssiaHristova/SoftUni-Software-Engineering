n = 125
p = 5
mask_0 = ~(1 << p)
mask_1 = 1 << p
result_0 = n & mask_0
result_1 = n | mask_1   
print(result_0)
print(result_1)
