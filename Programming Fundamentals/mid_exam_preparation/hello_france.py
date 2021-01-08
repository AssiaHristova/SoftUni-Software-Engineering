items_price = input().split('|')
budget = float(input())

new_prices = []
profit = 0

for element in items_price:
    element_list = element.split('->')
    item = element_list[0]
    price = float(element_list[1])
    new_price = 0
    if item == 'Clothes':
        if price <= 50:
            if budget >= price:
                budget -= price
                new_price = price * 1.4
                profit += (new_price - price)
                new_prices.append(new_price)
    elif item == 'Shoes':
        if price <= 35:
            if budget >= price:
                budget -= price
                new_price = price * 1.4
                profit += (new_price - price)
                new_prices.append(new_price)
    elif item == 'Accessories':
        if price <= 20.50:
            if budget >= price:
                budget -= price
                new_price = price * 1.4
                profit += (new_price - price)
                new_prices.append(new_price)

for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print()
print(f"Profit: {profit:.2f}")
budget += sum(new_prices)
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

