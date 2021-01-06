joyneries = int(input())
type = input()
delivery = input()

price_1 = 0
price_total = 0

if type == '90X130':
    price_1 = 110
    if joyneries < 30:
        price_total = joyneries * price_1
    elif 30 <= joyneries < 60:
        price_total = (joyneries * price_1) * 0.95
    elif joyneries >= 60:
        price_total = (joyneries * price_1) * 0.92
elif type == '100X150':
    price_1 = 140
    if joyneries < 40:
        price_total = joyneries * price_1
    elif 40 <= joyneries < 80:
        price_total = (joyneries * price_1) * 0.95
    elif joyneries >= 80:
        price_total = (joyneries * price_1) * 0.90
elif type == '130X180':
    price_1 = 190
    if joyneries < 20:
        price_total = joyneries * price_1
    elif 20 <= joyneries < 50:
        price_total = (joyneries * price_1) * 0.93
    elif joyneries >= 50:
        price_total = (joyneries * price_1) * 0.88
elif type == '200X300':
    price_1 = 250
    if joyneries < 25:
        price_total = joyneries * price_1
    elif 25 <= joyneries < 50:
        price_total = (joyneries * price_1) * 0.91
    elif joyneries >= 50:
        price_total = (joyneries * price_1) * 0.86

if delivery == 'With delivery':
    price_total += 60

if joyneries > 99:
    price_total = price_total * 0.96

if joyneries < 10:
    print("Invalid order")
else:
    print(f"{price_total:.2f} BGN")

