def plunder(towns, town, people, gold):
    if town in towns:
        if towns[town][0] > people:
            towns[town][0] -= people
        else:
            people = towns[town][0]
            towns[town][0] = 0
        if towns[town][1] > gold:
            towns[town][1] -= gold
        else:
            gold = towns[town][1]
            towns[town][1] = 0
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if towns[town][0] == 0 or towns[town][1] == 0:
            towns.pop(town)
            print(f"{town} has been wiped off the map!")
        return towns


def prosper(towns, town, gold):
    if town in towns:
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.")
    return towns


line = input()

towns = {}

while not line == "Sail":
    data = line.split("||")
    town = data[0]
    population = int(data[1])
    gold = int(data[2])
    if town in towns:
        towns[town][0] += population
        towns[town][1] += gold
    else:
        towns[town] = [population, gold]
    line = input()

command = input()

while not command == "End":
    events = command.split('=>')
    if events[0] == 'Plunder':
        town = events[1]
        population = int(events[2])
        gold = int(events[3])
        towns = plunder(towns, town, population, gold)
    elif events[0] == 'Prosper':
        town = events[1]
        gold = int(events[2])
        towns = prosper(towns, town, gold)
    command = input()

sorted_towns = sorted(towns.items(), key=lambda x: (-x[1][1], x[0]))

print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')

if len(towns) > 0:
    for town in sorted_towns:
        print(f'{town[0]} -> Population: {town[1][0]} citizens, Gold: {town[1][1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


