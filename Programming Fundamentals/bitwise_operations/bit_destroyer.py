n = int(input())
p = int(input())
bin_n = bin(n)
mask = ~(1 << p)
result = mask & n
print(result)
