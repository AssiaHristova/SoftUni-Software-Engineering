fruit = input()
type = input()
boosters = int(input())

price = 0

if type == 'small':
    if fruit == 'Watermelon':
        price = (boosters * 2) * 56
    elif fruit == 'Mango':
        price = (boosters * 2) * 36.66
    elif fruit == 'Pineapple':
        price = (boosters * 2) * 42.10
    else:
        price = (boosters * 2) * 20
else:
    if fruit == 'Watermelon':
        price = (boosters * 5) * 28.70
    elif fruit == 'Mango':
        price = (boosters * 5) * 19.60
    elif fruit == 'Pineapple':
        price = (boosters * 5) * 24.80
    else:
        price = (boosters * 5) * 15.20

if 400 <= price <= 1000:
    price = price * 0.85
elif price > 1000:
    price = price * 0.5

print(f"{price:.2f} lv.")
