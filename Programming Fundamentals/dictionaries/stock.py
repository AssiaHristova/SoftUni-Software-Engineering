string = input().split()
search_products = input().split()

products = {}

for index in range(0, len(string), 2):
    key = string[index]
    value = int(string[index + 1])
    products[key] = value

for product in search_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")