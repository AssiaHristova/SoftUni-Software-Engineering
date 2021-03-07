class Store:
    items = {}

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    @classmethod
    def from_size(cls, name, type, size):
        capacity = int(size / 2)
        return cls(name, type, capacity)

    @staticmethod
    def can_add_item(items, capacity):
        total_items_quantity = 0
        for item, quantity in items.items():
            total_items_quantity += quantity
        if total_items_quantity >= capacity:
            return False
        return True

    def add_item(self, item_name):
        if not self.can_add_item(self.items, self.capacity):
            return "Not enough capacity in  the store"
        if item_name not in self.items:
            self.items[item_name] = 1
        else:
            self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))


