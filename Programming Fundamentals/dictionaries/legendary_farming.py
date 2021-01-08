data = input().split()

materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junks = {}
legendary_item = None
quantity = 0

while legendary_item is None:
    for i in range(len(data)):
        if legendary_item is not None:
            break
        if i % 2 == 0:
            quantity = int(data[i])
        else:
            material = data[i].lower()
            if material == 'shards' or material == 'fragments' or material == 'motes':
                materials[material] += quantity
                for material, count in materials.items():
                    if count >= 250:
                        materials[material] -= 250
                        if material == 'shards':
                            legendary_item = 'Shadowmourne'
                        elif material == 'fragments':
                            legendary_item = 'Valanyr'
                        elif material == 'motes':
                            legendary_item = 'Dragonwrath'
                        print(f'{legendary_item} obtained!')
            else:
                if material in junks:
                    junks[material] += quantity
                else:
                    junks[material] = quantity

    if legendary_item is not None:
        break
    data = input().split()

sorted_materials = dict(sorted(materials.items(), key=lambda x: (-x[1], x[0])))

sorted_junks = dict(sorted(junks.items(), key=lambda x:x[0]))


for material, quantity in sorted_materials.items():
    print(f'{material}: {quantity}')

for junk, quantity in sorted_junks.items():
    print(f'{junk}: {quantity}')