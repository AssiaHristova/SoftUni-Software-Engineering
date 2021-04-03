class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    name = 'Kitty'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat__expect_size_increse_by_1(self):
    # Cat's size is increased after eating
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat_expect_fed_to_be_true(self):
    # Cat is fed after eating
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat_when_fed__expect_exception(self):
    #Cat cannot eat if already fed, raises an error
        self.cat.eat()

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep_if_not_fed__expect_exception(self):
    #Cat cannot fall asleep if not fed, raises an error
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_sleep_when_fed_expect_not_to_be_sleepy(self):
    # Cat is not sleepy after sleeping
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)



if __name__ == '__main__':
    unittest.main()
