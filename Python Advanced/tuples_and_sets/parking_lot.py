n = int(input())

cars = set()

for _ in range(n):
    line = input().split(', ')
    direction = line[0]
    car = line[1]
    if direction == 'IN':
        cars.add(car)
    elif direction == 'OUT':
        cars.remove(car)

if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')

