collection = input()
budget = float(input())

clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50

new_prices = []
profit = 0
collection_list = collection.split('|')

for element in collection_list:
    elements_list = element.split('->')
    item = elements_list[0]
    price = float(elements_list[1])
    increased_price = 0
    if item == 'Clothes':
        if price <= 50:
            if budget - price >= 0:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
                profit += (increased_price - price)
    elif item == 'Shoes':
        if price <= 35:
            if budget - price >= 0:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
                profit += (increased_price - price)
    elif item == 'Accessories':
        if price <= 20.50:
            if budget - price >= 0:
                budget -= price
                increased_price = price * 1.4
                new_prices.append(increased_price)
                profit += (increased_price - price)

budget_after_selling = budget + sum(new_prices)

for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print()
print(f"Profit: {profit:.2f}")

if budget_after_selling >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


