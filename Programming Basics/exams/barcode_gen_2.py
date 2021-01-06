barcode_1 = int(input())
barcode_last = int(input())

n = 0

for i in range(barcode_1, barcode_last + 1):
    count = 0
    for j in str(i):
        n = int(j)
        if n % 2 != 0:
            count += 1
        if count == 4:
            print(i, end=' ')


