barcode_1 = int(input())
barcode_last = int(input())

for barcode in range(barcode_1, barcode_last + 1):
    count_odd = 0
    symbol = str(barcode)
    for j, digit in enumerate(symbol):
        n = int(digit)
        if n % 2 != 0:
            count_odd += 1
        if count_odd == 4:
            print(barcode, end=' ')
            break

