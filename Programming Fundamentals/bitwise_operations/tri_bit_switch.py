n = int(input())
p = int(input())
bin_n = bin(n)
mask = n << p
result = n ^ mask
print(result)












