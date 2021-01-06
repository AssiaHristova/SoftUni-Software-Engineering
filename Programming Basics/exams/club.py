revenue = float(input())
cocktail = input()

price = 0
order_price = 0
total_price = 0

while cocktail != "Party!":
    count = int(input())
    for i, value in enumerate(cocktail, 1):
        if i > 0:
            price = i
    order_price = price * count
    if order_price % 2 != 0:
        order_price = order_price * 0.75
    total_price += order_price
    if total_price >= revenue:
        break

    cocktail = input()

if cocktail == "Party!":
    print(f"We need {(revenue - total_price):.2f} leva more.")
else:
    print("Target acquired.")

print(f"Club income - {total_price:.2f} leva.")

