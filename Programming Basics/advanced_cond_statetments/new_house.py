flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0.0

if flowers == 'Roses':
    price = 5
elif flowers == 'Dahlias':
    price = 3.80
elif flowers == 'Tulips':
    price = 2.80
elif flowers == 'Narcissus':
    price = 3
elif flowers == 'Gladiolus':
    price = 2.50

if flowers_count > 80 and flowers == 'Roses':
    price = price * 0.9
elif flowers_count > 90 and flowers == 'Dahlias':
    price = price * 0.85
elif flowers_count > 80 and flowers == 'Tulips':
    price = price * 0.85
elif flowers_count < 120 and flowers == 'Narcissus':
    price = price * 1.15
elif flowers_count < 80 and flowers == 'Gladiolus':
    price = price * 1.20

total_price = flowers_count * price
money_out = abs(budget - total_price)


if budget >= total_price:
    print(f'Hey, you have a great garden with {flowers_count} {flowers} and {money_out:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_out:.2f} leva more.')
