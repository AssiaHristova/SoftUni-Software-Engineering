class Catalogue:
    def __init__(self, name):
        self.name = name

    products = []

    def add_product(self, product):
        Catalogue.products.append(product)

    def get_by_letter(self, first_letter):
        products_first_letter = [product for product in Catalogue.products if product[0] == first_letter]
        return products_first_letter

    def __repr__(self):
        sorted_products = sorted(Catalogue.products)
        result = '\n'.join(sorted_products)
        return f"Items in the {self.name} catalogue:\n{result}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
