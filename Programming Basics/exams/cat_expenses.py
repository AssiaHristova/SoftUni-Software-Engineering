bed_price = float(input())
toilet_per_month = float(input())

food_price = toilet_per_month * 1.25
toys_price = food_price / 2
vet_price = toys_price * 1.10
monthly_expenses = toilet_per_month + food_price + toys_price + vet_price
other_expenses = monthly_expenses * 0.05

yearly_expenses = bed_price + (monthly_expenses + other_expenses) * 12

print(f'{yearly_expenses:.2f} lv.')

