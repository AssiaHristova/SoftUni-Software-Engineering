shops = input().split()
n = int(input())

for i in range(1, n + 1):
    command = input().split()
    if 'Include' in command:
        shop = command[1]
        shops.append(shop)
    elif 'Visit' in command:
        number_of_shops = int(command[2])
        if number_of_shops in range(0, len(shops)):
            if "first" in command:
                shops = shops[number_of_shops:]
            elif "last" in command:
                shops.reverse()
                shops = shops[number_of_shops:]
                shops.reverse()
    elif 'Prefer' in command:
        index_1 = int(command[1])
        index_2 = int(command[2])
        if index_1 in range(0, len(shops)) and index_2 in range(0, len(shops)):
            shops[index_1], shops[index_2] = shops[index_2], shops[index_1]
    elif 'Place' in command:
        shop = command[1]
        index = int(command[2])
        if index in range(0, len(shops)):
            shops.insert(index + 1, shop)

print("Shops left:")
print(' '.join(shops))


