from shop.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        if product in self.products:
            raise ValueError(f"Product {product.name} already exists.")
        self.products.append(product)
        return f"Product {product.name} successfully added to inventory."

    def decrease(self, product: Product, quantity: int):
        if product in self.products:
            if product.quantity > quantity:
                product.quantity -= quantity
        return f"Left quantity of {product.name}: {product.quantity}"

    def find(self, product_name: str):
        found_products = [p for p in self.products if p.name == product_name]
        if not found_products:
            return None
        return found_products[0]

