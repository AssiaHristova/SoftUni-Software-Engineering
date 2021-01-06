import math
import sys
airlines = int(input())

max_passengers = -sys.maxsize
max_airline = ''

for airline in range(1, airlines + 1):
    count = 0
    passengers_per_airline = 0
    name = input()
    command = input()
    while command != "Finish":
        passengers_per_flight = int(command)
        count += 1
        passengers_per_airline += passengers_per_flight

        command = input()

    avg_passengers = passengers_per_airline / count
    if avg_passengers > max_passengers:
        max_passengers = avg_passengers
        max_airline = name
    print(f"{name}: {math.floor(avg_passengers)} passengers.")

print(f"{max_airline} has most passengers per flight: {math.floor(max_passengers)}")
