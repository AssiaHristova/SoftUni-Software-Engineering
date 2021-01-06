budget = float(input())
extras = int(input())
costumes = float(input())

decor = budget * 0.10

if extras > 150:
    costumes = costumes * 0.90

cost = decor + extras * costumes
money_out = budget - cost

if cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_out):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_out:.2f} leva left.")
