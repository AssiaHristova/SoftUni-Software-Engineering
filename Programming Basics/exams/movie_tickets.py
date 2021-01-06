a1 = int(input())
a2 = int(input())
n = int(input())


for i in range(a1, a2):
    symbol1 = chr(i)
    symbol4 = ord(symbol1)
    for j in range(1, n):
        symbol2 = j
        for k in range(1, int(n / 2)):
            symbol3 = k
            if symbol4 % 2 != 0:
                if (symbol2 + symbol3 + symbol4) % 2 != 0:
                    print(f"{symbol1}-{symbol2}{symbol3}{symbol4}")
