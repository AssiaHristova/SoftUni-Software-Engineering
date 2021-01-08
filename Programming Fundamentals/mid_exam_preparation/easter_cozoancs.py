budget = float(input())
flour_price = float(input())

price_cozonac = flour_price + (flour_price * 0.75) + ((flour_price * 1.25) / 4)
cozonacs = 0
colored_eggs = 0

while budget > 0:
    if budget - price_cozonac > 0:
        budget -= price_cozonac
    else:
        break
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= (cozonacs - 2)

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

