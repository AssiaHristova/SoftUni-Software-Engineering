n = int(input())
p = int(input())
mask = n >> p
bit = mask & 1
print(bit)


