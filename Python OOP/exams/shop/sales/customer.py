from shop.deliveries.product import Product


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.products = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The customer's name cannot be an empty string.")
        self.__name = value

    def add_product(self, product: Product, quantity):
        if product not in self.products:
            self.products[product.name] = quantity
        else:
            self.products[product.name] += quantity
