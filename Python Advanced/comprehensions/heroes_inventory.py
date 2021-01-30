heroes = input().split(', ')
command = input()

heroes_inventory = {hero: [] for hero in heroes}

while not command == "End":
    data = command.split('-')
    name, item, cost = data
    if name in heroes_inventory:
        if heroes_inventory[name]:
            if item not in heroes_inventory[name][0]:
                heroes_inventory[name][0].append(item)
                heroes_inventory[name][1].append(int(cost))
        else:
            heroes_inventory[name] = [[item], [int(cost)]]
    command = input()


for name, [item, cost] in heroes_inventory.items():
    print(f"{name} -> Items: {len(item)}, Cost: {sum(cost)}")


