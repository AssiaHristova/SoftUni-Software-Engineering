class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if self.status():
            self.quantity += milliliters
        return self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
