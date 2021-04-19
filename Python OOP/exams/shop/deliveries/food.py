from shop.deliveries.product import Product


class Food(Product):
    quantity = 15

    def __init__(self, name):
        super(Food, self).__init__(name, Food.quantity)