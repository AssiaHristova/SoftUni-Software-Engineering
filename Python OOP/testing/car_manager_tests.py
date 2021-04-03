class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest

class CarManagerTests(unittest.TestCase):
    make = 'Subaru'
    model = 'Forester'
    fuel_consumption = 10
    fuel_capacity = 100

    def test_make_setter_when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_model_setter_when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = None

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_fuel_consumption_setter_when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = -5

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_consumption_setter_when_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity_setter_when_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity_setter_when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = -5

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_amount_setter_when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_car_refuel__when_fuel_is_zero_expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(0)

    def test_car_refuel__when_fuel_is_negative_expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_car_refuel__when_fuel_is_positive_expect_to_increase_fuel_amount_by_provided_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_fuel_is_more_than_fuel_capacity_expect_to_increase_fuel_amount_up_to_fuel_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_car_drive__when_fuel_is_more_than_needed_expect_to_decrease_fuel_amount_by_needed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 50
        needed = (100 / 100) * car.fuel_consumption
        car.drive(100)

        self.assertEqual(40, car.fuel_amount)

    def test_car_drive__when_fuel_is_less_than_needed_expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 10
        needed = (200 / 100) * car.fuel_consumption

        with self.assertRaises(Exception) as context:
            car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == '__main__':
    unittest.main()