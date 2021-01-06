budget = float(input())
count_extras = int(input())
price_costumes_per_extra = float(input())

decor = budget * 10/100
price_costumes = count_extras * price_costumes_per_extra

if count_extras > 150:
    price_costumes = price_costumes * 90/100

my_budget = decor + price_costumes
money_out = abs(budget - my_budget)

if my_budget > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_out:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_out:.2f} leva left.')





