days = int(input())
room = input()
grade = input()

if room == 'room for one person':
    price_1 = (days - 1) * 18
elif room == 'apartment' and days < 10:
    price_1 = ((days - 1) * 25) * 70/100
elif room == 'apartment' and 10 <= days <= 15:
    price_1 = ((days - 1) * 25) * 65/100
elif room == 'apartment' and days > 15:
    price_1 = ((days - 1) * 25) * 50/100
elif room == 'president apartment' and days < 10:
    price_1 = ((days - 1) * 35) * 90/100
elif room == 'president apartment' and 10 <= days <= 15:
    price_1 = ((days - 1) * 35) * 85/100
elif room == 'president apartment' and days > 15:
    price_1 = ((days - 1) * 35) * 80/100
else:
    price_1 = 0

if grade == 'positive':
    price_total = price_1 + price_1 * 25/100
elif grade == 'negative':
    price_total = price_1 - price_1 * 10/100
else:
    price_total = 0

print(f'{price_total:.2f}')

