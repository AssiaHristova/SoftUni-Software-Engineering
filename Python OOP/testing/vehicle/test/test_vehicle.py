import unittest
from vehicle.project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_vehicle_init__expect_to_create_it(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_check_if_capacity_change_when_fuel_change(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_vehicle_drive__when_fuel_more_than_needed__expect_fuel_to_decrease_with_amount_needed(self):
        self.vehicle.drive(20)

        self.assertEqual(25, self.vehicle.fuel)

    def test_vehicle_drive__when_fuel_less_than_needed__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(200)

        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_vehicle_refuel__when_fuel_less_than_capacity__expect_fuel_to_increase_with_fuel(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(35, self.vehicle.fuel)

    def test_vehicle_refuel__when_fuel_more_than_capacity__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(100)

        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_vehicle_str__expect_to_return_info(self):
        result = f"The vehicle has 200 " \
                 f"horse power with 50 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, str(self.vehicle))


if __name__ == '__main__':
    unittest.main()