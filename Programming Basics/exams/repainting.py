nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

materials_price = (nylon + 2) * 1.5 + (paint * 1.10) * 14.50 + diluent * 5 + 0.40
work_price = (materials_price * 0.30) * hours
total_price = materials_price + work_price

print(f"Total expenses: {total_price:.2f} lv.")
