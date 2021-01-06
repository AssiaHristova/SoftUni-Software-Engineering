budget = float(input())
product = input()

equipment = 0
count = 0

while product != 'Stop':
    price = float(input())
    count += 1
    if count % 3 == 0:
        equipment += price / 2
    else:
        equipment += price
    if equipment > budget:
        break

    product = input()

if equipment > budget:
    print("You don't have enough money!")
    print(f"You need {(equipment - budget):.2f} leva!")
else:
    print(f"You bought {count} products for {equipment:.2f} leva.")

