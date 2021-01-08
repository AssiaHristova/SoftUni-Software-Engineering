string = input().split()

products = {}

for index in range(0, len(string), 2):
    key = string[index]
    value = int(string[index + 1])
    products[key] = value

print(products)
