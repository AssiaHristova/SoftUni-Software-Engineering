import random


class RandomList(list):
    def get_random_element(self):
        ele = random.choice(self)
        self.remove(ele)
        return ele


# test first zero
import unittest
from unittest import mock


class RandomListTests(unittest.TestCase):
    def test_zero_first(self):
        mocked_choice = lambda x: 5
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(4)
            li.append(3)
            li.append(5)
            self.assertEqual(li.get_random_element(), 5)

if __name__ == '__main__':
    unittest.main()


rl = RandomList([1, 2, 3, 4, 5])
print(rl)
rl.append(-1)
print(rl)
while rl:
    print(rl.get_random_element())



