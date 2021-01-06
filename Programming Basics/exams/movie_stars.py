budget = float(input())
actor = input()

budget_left = 0
commission_all = 0

while actor != "ACTION":
    commission = 0
    if len(actor) > 15:
        commission = budget_left * 0.20
    else:
        commission = float(input())
    commission_all += commission
    budget_left = budget - commission_all
    if budget_left < 0:
        break

    actor = input()

if budget_left >= 0:
    print(f"We are left with {budget_left:.2f} leva.")
else:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")

