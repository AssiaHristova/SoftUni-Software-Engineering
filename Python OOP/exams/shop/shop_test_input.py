from shop.shop import Shop
from shop.sales.customer import Customer


shop = Shop()
shop.deliver('Food', 'bread')
shop.deliver('Food', 'eggs')
shop.deliver('Food', 'milk')
shop.deliver('Drink', 'water')
shop.deliver('Drink', 'beer')
customer = Customer('Raya')
shop.customer_repository.add(customer)
print(len(shop.product_repository.products))
print(len(shop.customer_repository.customers))
shopping_list = {'bread': 3, 'eggs': 10, 'milk': 1, 'beer': 20}
print(shop.sell('Assia', **shopping_list))
print(len(shop.product_repository.products))
print(len(shop.customer_repository.customers))