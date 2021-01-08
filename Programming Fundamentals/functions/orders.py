order = input()
quantity = int(input())


def order_price(product, count):
    price = 0
    if product == 'coffee':
        price = count * 1.50
    elif product == 'coke':
        price = count * 1.40
    elif product == 'water':
        price = count * 1.00
    elif product == 'snacks':
        price = count * 2.00
    return price


print(f'{order_price(order, quantity):.2f}')


