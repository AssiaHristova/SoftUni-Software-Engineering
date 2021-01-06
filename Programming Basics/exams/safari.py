budget = float(input())
fuel = float(input())
day = input()

cost = fuel * 2.10 + 100
total_cost = 0
money_out = 0

if day == 'Saturday':
    total_cost = cost * 0.9
else:
    total_cost = cost * 0.8

money_out = budget - total_cost

if money_out >= 0:
    print(f'Safari time! Money left: {money_out:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(money_out):.2f} lv.')

