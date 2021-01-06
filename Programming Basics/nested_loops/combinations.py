n = int(input())
x1 = 0
x2 = 0
x3 = 0
count = 0

for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            if x1 + x2 + x3 == n:
                count += 1
print(count)
