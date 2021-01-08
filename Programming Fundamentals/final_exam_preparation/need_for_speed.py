def drive(cars, car, distance, fuel):
    if car in cars:
        if cars[car][1] > fuel:
            cars[car][1] -= fuel
            cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")
    return cars


def refuel(cars, car, fuel):
    if car in cars:
        if cars[car][1] + fuel > 75:
            fuel = 75 - cars[car][1]
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    return cars


def revert(cars, car, km):
    if car in cars:
       if cars[car][0] - km > 10000:
            cars[car][0] -= km
            print(f"{car} mileage decreased by {km} kilometers")
       else:
           cars[car][0] = 10000
    return cars

n = int(input())

cars = {}

for i in range(n):
    cars_info = input().split("|")
    car = cars_info[0]
    mileage = int(cars_info[1])
    fuel = int(cars_info[2])
    cars[car] = [mileage, fuel]

line = input()

while not line == "Stop":
    command = line.split(" : ")
    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        cars = drive(cars, car, distance, fuel)
    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        cars = refuel(cars, car, fuel)
    elif command[0] == 'Revert':
        car = command[1]
        km = int(command[2])
        cars = revert(cars, car, km)

    line = input()

cars_sorted = sorted(cars.items(), key=lambda x: (-x[1][0], x[0]))

for car in cars_sorted:
    print(f"{car[0]} -> Mileage: {car[1][0]} kms, Fuel in the tank: {car[1][1]} lt.")

