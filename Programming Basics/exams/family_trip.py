budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_expenses = int(input())

total_price = 0

if nights > 7:
    price_per_night = price_per_night * 0.95

price = nights * price_per_night
total_price = price + budget * (extra_expenses / 100)
money_out = budget - total_price

if budget >= total_price:
    print(f"Ivanovi will be left with {money_out:.2f} leva after vacation.")
else:
    print(f"{abs(money_out):.2f} leva needed.")
