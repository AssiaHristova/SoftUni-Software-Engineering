from shop.deliveries.drink import Drink
from shop.deliveries.food import Food
from shop.deliveries.product import Product
from shop.deliveries.product_repository import ProductRepository
from shop.sales.customer import Customer
from shop.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        product = None
        if product_type == 'Food':
            product = Food(name)
        elif product_type == 'Drink':
            product = Drink(name)

        self.product_repository.add(product)

    def create_customer(self, customer_name):
        customer = self.customer_repository.find(customer_name)
        if not customer:
            customer = Customer(customer_name)
            self.customer_repository.add(customer)
        return customer

    def product_sell(self, product: Product, needed_quantity, available_quantity, customer: Customer):
        result = ''
        if needed_quantity <= available_quantity:
            customer.add_product(product, needed_quantity)
            left = self.product_repository.decrease(product, needed_quantity)
            if left:
                result += left + '\n'
        else:
            customer.add_product(product, available_quantity)
            result += f"Left quantity of {product.name}: {0}" + '\n'
            self.product_repository.products.remove(product)

        return result

    def sell(self, customer_name: str, **shopping_list):
        result = ''
        customer = self.create_customer(customer_name)

        for key, value in shopping_list.items():
            needed_product = key
            needed_quantity = value

            product = self.product_repository.find(needed_product)
            available_quantity = 0
            if product:
                available_quantity = product.quantity

            result += self.product_sell(product, needed_quantity, available_quantity, customer)

        return result


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















