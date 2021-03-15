class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_topping_capacity):
        self.__toppings_capacity = new_topping_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, new_toppings):
        self.__toppings = new_toppings

    def add_topping(self, topping):
        if self.__toppings_capacity <= len(self.__toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        toppings_weight = self.__toppings.values()
        dough_weight = self.__dough.weight
        return dough_weight + sum(toppings_weight)