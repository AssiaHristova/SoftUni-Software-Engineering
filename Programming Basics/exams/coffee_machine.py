drinks = input()
sugar = input()
drink_count = int(input())

price = 0

if sugar == "Without":
    if drinks == "Espresso":
        if drink_count >= 5:
            price = ((drink_count * 0.90) * 0.65) * 0.75
        else:
            price = (drink_count * 0.90) * 0.65
    elif drinks == "Cappuccino":
        price = drink_count
    else:
        price = drink_count * 0.50
elif sugar == "Normal":
    if drinks == "Espresso":
        if drink_count >= 5:
            price = drink_count * 0.75
        else:
            price = drink_count
    elif drinks == "Cappuccino":
        price = drink_count * 1.20
    else:
        price = drink_count * 0.60
else:
    if drinks == "Espresso":
        if drink_count >= 5:
            price = (drink_count * 1.20) * 0.75
        else:
            price = drink_count * 1.20
    elif drinks == "Cappuccino":
        price = drink_count * 1.60
    else:
        price = drink_count * 0.70

if price > 15:
    price = price * 0.8

print(f"You bought {drink_count} cups of {drinks} for {price:.2f} lv.")

