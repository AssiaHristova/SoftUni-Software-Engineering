import math

people = int(input())
fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

umbrellas = math.ceil(people / 2)
sunbeds = math.ceil(people * 0.75)
total_price = people * fee + sunbeds * sunbed_price + umbrellas * umbrella_price

print(f"{total_price:.2f} lv.")



