from collections import deque

cups_capacity = input().split()
bottles = input().split()

bottles = [int(el) for el in bottles]
wasted_water = 0
cups = deque()

for el in cups_capacity:
    cups.append(int(el))


while cups:
    cup = cups[0]
    while bottles:
        bottle = bottles.pop()
        if cup > bottle:
            cup -= bottle
        else:
            bottle -= cup
            cups.popleft()
            wasted_water += bottle
            break

    if not bottles:
        print(f"Cups: ", end='')
        while cups:
            print(cups.popleft(), end=' ')

    elif not cups:
        print(f"Bottles: ", end='')
        while bottles:
            print(bottles.pop(), end=' ')

print()
print(f"Wasted litters of water: {wasted_water}")



