budget = float(input())
n = int(input())

total_price = 0

for i in range(1, n + 1):
    series = input()
    price = float(input())
    if series == 'Thrones':
        total_price += price / 2
    elif series == 'Lucifer':
        total_price += price * 0.60
    elif series == 'Protector':
        total_price += price * 0.70
    elif series == 'TotalDrama':
        total_price += price * 0.80
    elif series == 'Area':
        total_price += price * 0.90
    else:
        total_price += price

money_out = budget - total_price

if budget >= total_price:
    print(f"You bought all the series and left with {money_out:.2f} lv.")
else:
    print(f"You need {abs(money_out):.2f} lv. more to buy the series!")


