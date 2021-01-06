n = int(input())
time = input()

price_min = 0

if n >= 100:
    price_min = n * 0.06
elif n >= 20:
    price_min = n * 0.09
else:
    if time == 'day':
        price_min = n * 0.79 + 0.70
    else:
        price_min = n * 0.90 + 0.70

print(f'{price_min:.2f}')