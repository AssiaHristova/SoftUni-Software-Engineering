month = input()
nights = int(input())

price_s = 0.0
price_a = 0.0

if month == 'May' or \
        month == 'October':
    price_s = 50
    price_a = 65
elif month == 'June' or \
        month == 'September':
    price_s = 75.20
    price_a = 68.70
else:
    price_s = 76
    price_a = 77

if 7 < nights < 14:
    if month == 'May' or \
            month == 'October':
        price_s = price_s * 0.95
elif nights > 14:
    price_a = price_a * 0.90
    if month == 'May' or \
            month == 'October':
        price_s = price_s * 0.70
    elif month == 'June' or \
            month == 'September':
        price_s = price_s * 0.80

total_price_a = nights * price_a
total_price_s = nights * price_s

print(f'Apartment: {total_price_a:.2f} lv.')
print(f'Studio: {total_price_s:.2f} lv.')
