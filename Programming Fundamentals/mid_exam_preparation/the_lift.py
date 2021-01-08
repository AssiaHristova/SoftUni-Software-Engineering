people = int(input())
lift = input().split()

wagons = [int(wagon) for wagon in lift]
count_full = 0
index = 0

while people > 0:
    for wagon in wagons:
        if wagon == 4:
            count_full += 1
            index += 1
        if wagon < 4:
            people -= (4 - wagon)
            if people >= 0:
                wagons[index] += (4 - wagon)
                count_full += 1
                index += 1
            else:
                wagons[index] = (4 + people)
                break

    if count_full == len(wagons):
        break

lift = [str(wagon) for wagon in wagons]

if people <= 0:
    if count_full == len(wagons):
        print(f"{' '.join(lift)}")
    else:
        print("The lift has empty spots!")
        print(f"{' '.join(lift)}")
else:
    if count_full == len(wagons):
        print(f"There isn't enough space! {people} people in a queue!")
        print(f"{' '.join(lift)}")


