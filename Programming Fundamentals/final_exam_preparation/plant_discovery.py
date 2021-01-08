def rate(plants, plant, rating):
    if plant in plants:
        plants[plant][1].append(rating)
    else:
        print('error')
    return plants


def update(plants, plant, rarity):
    if plant in plants:
        plants[plant][0] = rarity
    else:
        print('error')
    return plants


def reset(plants, plant):
    if plant in plants:
        plants[plant][1] = [0]
    else:
        print('error')
    return plants


n = int(input())

plants = {}

for i in range(n):
    data = input().split('<->')
    plant = data[0]
    rarity = int(data[1])
    plants[plant] = [rarity, [0]]

line = input()

while not line == "Exhibition":
    command = line.split(': ')
    info = command[1].split(' - ')
    if command[0] == 'Rate':
        if len(info) == 2:
            plant = info[0]
            rating = float(info[1])
            plants = rate(plants, plant, rating)
        else:
            print('error')
    elif command[0] == 'Update':
        if len(info) == 2:
            plant = info[0]
            rarity = int(info[1])
            plants = update(plants, plant, rarity)
        else:
            print('error')
    elif command[0] == 'Reset':
        if len(info) == 1:
            plant = info[0]
            plants = reset(plants, plant)
        else:
            print('error')
    else:
        print('error')

    line = input()


plants_sorted = sorted(plants.items(), key=lambda x: (-x[1][0], -sum(x[1][1]) / len(x[1][1])))

print('Plants for the exhibition:')
for el in plants_sorted:
    if el[1][1][0] == 0 and len(el[1][1]) > 1:
        el[1][1] = el[1][1][1:]
    print(f'- {el[0]}; Rarity: {el[1][0]}; Rating: {(sum(el[1][1]) / len(el[1][1])):.2f}')

