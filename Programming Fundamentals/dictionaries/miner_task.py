command = input()
resources = {}
n = 1
resource = ''
quantity = 0

while not command == 'stop':
    if n % 2 == 0:
        quantity = int(command)
        if resource in resources:
            resources[resource] += quantity
        else:
            resources[resource] = 0
    else:
        resource = command
        if resource in resources:
            resources[resource] += 0
        else:
            resources[resource] = 0

    n += 1
    command = input()

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')



