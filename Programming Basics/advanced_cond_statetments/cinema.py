movie = input()
rows = int(input())
columns = int(input())

price = 0.0

if movie == 'Premiere':
    price = 12
elif movie == 'Normal':
    price = 7.50
elif movie == 'Discount':
    price = 5

revenue = rows * columns * price

print(f'{revenue:.2f} leva')

