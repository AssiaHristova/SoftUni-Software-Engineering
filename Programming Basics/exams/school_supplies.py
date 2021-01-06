pensils = int(input())
markers = int(input())
board_cleaner = float(input())
discount = int(input())

price = pensils * 5.80 + markers * 7.20 + board_cleaner * 1.20
total_price = price - price * (discount / 100)

print(f'{total_price:.3f}')
