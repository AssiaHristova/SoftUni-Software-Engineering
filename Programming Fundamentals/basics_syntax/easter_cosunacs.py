import math

budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
counter = 0
colored_eggs = 0

price_cosonac = price_eggs + price_flour + price_milk / 4

cosonacs = math.floor(budget / price_cosonac)
budget_left = budget - (cosonacs * price_cosonac)


for cosonac in range(1, cosonacs + 1):
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)

print(f"You made {cosonacs} cozonacs! Now you have {colored_eggs} eggs and {budget_left:.2f}BGN left.")


