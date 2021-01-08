n = int(input())
b = int(input())
bin_n = str(bin(n))
count = 0
result = ''

for i in range(len(bin_n)):
    if bin_n[i] == '1':
        result = bin_n[i:]
        break

for char in result:
    if char == str(b):
        count += 1

print(count)
