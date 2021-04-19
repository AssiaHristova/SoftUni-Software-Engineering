from shop.sales.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        self.customers.append(customer)

    def remove(self, customer_name: str):
        searched_customers = [c for c in self.customers if c.name == customer_name]
        if not searched_customers:
            raise ValueError(f"Customer {customer_name} does not exist.")
        self.customers.remove(searched_customers[0])
        return f"Removed customer: {customer_name}"

    def find(self, customer_name: str):
        found_customers = [c for c in self.customers if c.name == customer_name]
        if not found_customers:
            return None
        return found_customers[0]