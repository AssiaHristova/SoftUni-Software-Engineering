sleeve_dimension = float(input())
front_side_dimension = float(input())
cloth = input()
tie = input()

shirt_dimension = (sleeve_dimension + front_side_dimension) * 2
shirt_total = (shirt_dimension * 1.10) / 100
price = 0

if cloth == "Linen":
    if tie == "Yes":
        price = (shirt_total * 15 + 10) * 1.20
    else:
        price = shirt_total * 15 + 10
elif cloth == "Cotton":
    if tie == "Yes":
        price = (shirt_total * 12 + 10) * 1.20
    else:
        price = shirt_total * 12 + 10
elif cloth == "Denim":
    if tie == "Yes":
        price = (shirt_total * 20 + 10) * 1.20
    else:
        price = shirt_total * 20 + 10
elif cloth == "Twill":
    if tie == "Yes":
        price = (shirt_total * 16 + 10) * 1.20
    else:
        price = shirt_total * 16 + 10
else:
    if tie == "Yes":
        price = (shirt_total * 11 + 10) * 1.20
    else:
        price = shirt_total * 11 + 10

print(f"The price of the shirt is: {price:.2f}lv.")
