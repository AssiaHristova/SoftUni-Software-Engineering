a = int(input())
bin_a = ''
while a > 0:
    d = a % 2
    a = a // 2
    bin_a += str(d)

bin_a = bin_a[::-1]
print(bin_a)


