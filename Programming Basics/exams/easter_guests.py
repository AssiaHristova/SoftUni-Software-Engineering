import math

guests = int(input())
budget = int(input())

eggs = guests * 2
breads = math.ceil(guests / 3)
price = breads * 4 + eggs * 0.45

if budget >= price:
    print(f"Lyubo bought {breads} Easter bread and {eggs} eggs.")
    print(f"He has {(budget - price):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {(price - budget):.2f} lv. more.")


