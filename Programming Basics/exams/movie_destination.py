budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000 * 0.70
    elif destination == "Sofia":
        price_per_day = 17000 * 1.25
    else:
        price_per_day = 24000
else:
    if destination == "Dubai":
        price_per_day = 40000 * 0.70
    elif destination == "Sofia":
        price_per_day = 12500 * 1.25
    else:
        price_per_day = 20250

price = days * price_per_day
money_out = budget - price

if budget >= price:
    print(f"The budget for the movie is enough! We have {money_out:.2f} leva left!")
else:
    print(f"The director needs {abs(money_out):.2f} leva more!")