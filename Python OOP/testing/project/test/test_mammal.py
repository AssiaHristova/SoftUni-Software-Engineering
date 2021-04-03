import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    name = 'Puhi'
    type = 'Cat'
    sound = 'Meow'
    mammal = Mammal(name, type, sound)

    def test_mammal_init__expect_to_create_it(self):
        self.assertEqual('Puhi', self.name)
        self.assertEqual('Cat', self.type)
        self.assertEqual('Meow', self.sound)

    def test_mammal_make_sound__expect_to_make_sound(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = f"{self.name} makes {self.sound}"

        self.assertEqual(result, mammal.make_sound())

    def test_mammal_get_kingdom__expect_to_return_kingdom(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = "animals"

        self.assertEqual(result, mammal.get_kingdom())

    def test_mammal_info__expect_to_return_info(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = f"{self.name} is of type {self.type}"

        self.assertEqual(result, mammal.info())



if __name__ == '__main__':
    unittest.main()