import sys

divisor = int(input())
bound = int(input())

max_n = -sys.maxsize

for n in range(1, bound + 1):
    if n % divisor == 0:
        if n > maxN:
            maxN = n

print(max_n)

