data = input()

products = {}

while not data == "buy":
    data_list = data.split()
    name = data_list[0]
    price = float(data_list[1])
    quantity = int(data_list[2])
    if name in products:
        products[name][0] = price
        products[name][1] += quantity
    else:
        products[name] = [price, quantity]

    data = input()

for name, value in products.items():
    print(f"{name} -> {(value[0] * value[1]):.2f}")