fuel = input()
liters = int(input())

if fuel == 'Diesel' or \
        fuel == 'Gasoline' or \
        fuel == 'Gas':
    if liters >= 25:
        print(f'You have enough {fuel}.')
    else:
        print(f'Fill your tank with {fuel}!')
else:
    print(f'Invalid fuel!')
