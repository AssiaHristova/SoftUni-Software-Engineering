b = input()
dec_b = 0

for i in range(len(b)):
    magnitude = 2 ** ((len(b) - 1) - i)
    dec_b += (int(b[i]) * magnitude)

print(dec_b)

