


class Worker:

  def __init__(self, name, salary, energy):
    self.name = name
    self.salary = salary
    self.energy = energy
    self.money = 0

  def work(self):
    if self.energy <= 0:
        raise Exception('Not enough energy.')

    self.money += self.salary
    self.energy -= 1

  def rest(self):
    self.energy += 1

  def get_info(self):
    return (f'{self.name} has saved {self.money} money.')


import unittest


class WorkerTests(unittest.TestCase):
    name = 'Test Worker'
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init_expected_to_be_initialised(self):
    # Test if the worker is initialized with correct name, salary and energy
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_rest__expect_energy_to_be_incremented(self):
    # Test if the worker's energy is incremented after the rest method is called
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work_when_energy_is_0_or_negative__expect_exception(self):
    # Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

        self.worker.energy = -5
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__expect_money_to_be_increased_by_salary(self):
    # Test if the worker's money is increased by his salary correctly after the work method is called
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_worker_work__expect_energy_to_be_decresed(self):
    # Test if the worker's energy is decreased after the work method is called
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_values(self):
    # Test if the get_info method returns the proper string with correct values
        expected_info = f'{self.name} has saved 0 money.'
        actual_info = self.worker.get_info()

        self.assertEqual(expected_info, actual_info)



if __name__ == '__main__':
    unittest.main()

