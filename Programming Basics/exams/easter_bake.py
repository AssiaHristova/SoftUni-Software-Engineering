import sys
import math
breads = int(input())

sugar_packets = 0
flour_packets = 0
sugar = 0
flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for bread in range(1, breads + 1):
    sugar_per_bread = int(input())
    flour_per_bread = int(input())
    sugar += sugar_per_bread
    flour += flour_per_bread
    if sugar_per_bread > max_sugar:
        max_sugar = sugar_per_bread
    if flour_per_bread > max_flour:
        max_flour = flour_per_bread

sugar_packets = math.ceil(sugar / 950)
flour_packets = math.ceil(flour / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

