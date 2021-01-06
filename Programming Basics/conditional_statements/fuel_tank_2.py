fuel = input()
liters = float(input())
card = input()

price = 0
discount_price = 0

if fuel == 'Gasoline':
    if card == 'Yes':
        price = liters * (2.22 - 0.18)
    else:
        price = liters * 2.22
elif fuel == 'Diesel':
    if card == 'Yes':
        price = liters * (2.33 - 0.12)
    else:
        price = liters * 2.33
elif fuel == 'Gas':
    if card == 'Yes':
        price = liters * (0.93 - 0.08)
    else:
        price = liters * 0.93

if 20 <= liters <= 25:
    discount_price = price * 92 / 100
elif liters > 25:
    discount_price = price * 90 / 100
else:
    discount_price = price

print(f'{discount_price:.2f} lv.')

