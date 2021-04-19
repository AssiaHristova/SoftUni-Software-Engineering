from unittest import TestCase, main
from test_survivor.project.survivor import Survivor


class SurvivorTests(TestCase):
    def setUp(self):
        self.survivor = Survivor('Assia', 34)

    def test_init_if_all_valid(self):
        self.assertEqual('Assia', self.survivor.name)
        self.assertEqual(34, self.survivor.age)
        self.assertEqual(100, self.survivor.health)
        self.assertEqual(100, self.survivor.needs)

    def test_init_if_no_name__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('', 34)

        self.assertEqual("Name not valid!", str(ex.exception))

    def test_init_if_age_is_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('Assia', -3)

        self.assertEqual("Age not valid!", str(ex.exception))

    def test_init_if_health_is_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.health = -4

        self.assertEqual("Health not valid!", str(ex.exception))

    def test_init_if_needs_is_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.needs = -4

        self.assertEqual("Needs not valid!", str(ex.exception))

    def test_needs_sustenance_if_needs_is_more_than_100__expect_False(self):
        self.survivor.needs = 130

        self.assertEqual(False, self.survivor.needs_sustenance)

    def test_needs_sustenance_if_needs_is_less_than_100__expect_True(self):
        self.survivor.needs = 30

        self.assertEqual(True, self.survivor.needs_sustenance)

    def test_needs_healing_if_health_is_more_than_100__expect_False(self):
        self.survivor.health = 120

        self.assertEqual(False, self.survivor.needs_healing)

    def test_needs_healing_if_health_is_less_than_100__expect_True(self):
        self.survivor.health = 20

        self.assertEqual(True, self.survivor.needs_healing)


if __name__ == '__main__':
    main()

