N = int(input())

for i in range(1111, 10000):
    count = 0
    symbol = str(i)
    for j, digit in enumerate(symbol):
        special = int(digit)
        if special != 0:
            if N % special == 0:
                count += 1
        if count == 4:
            print(i, end=' ')
            break



