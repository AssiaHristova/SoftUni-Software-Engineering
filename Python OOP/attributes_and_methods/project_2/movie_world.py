class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        filtered_customers = [c for c in self.customers if c.id == customer_id]
        if filtered_customers:
            customer = filtered_customers[0]
            filtered_dvds = [d for d in self.dvds if d.id == dvd_id]
            if filtered_dvds:
                dvd = filtered_dvds[0]
                if dvd.is_rented:
                    if dvd in customer.rented_dvds:
                        return f"{customer.name} has already rented {dvd.name}"
                    return "DVD is already rented"
                if dvd.age_restriction > customer.age:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        filtered_customers = [c for c in self.customers if c.id == customer_id]
        if filtered_customers:
            customer = filtered_customers[0]
            filtered_dvds = [d for d in self.dvds if d.id == dvd_id]
            if filtered_dvds:
                dvd = filtered_dvds[0]
                if dvd not in customer.rented_dvds:
                    return f"{customer.name} does not have that DVD"
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += (str(customer) + '\n')
        for dvd in self.dvds:
            result += (str(dvd) + '\n')
        return result



