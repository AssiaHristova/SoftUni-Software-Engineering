import math


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        value = math.floor(value)
        return cls(value)

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value):
        if not type(value) == str:
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        if not type(integer) == Integer:
            return "number should be an Integer instance"
        return self.value + integer.value

    def __repr__(self):
        return f'{self.value}'


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(first_num)
print(second_num)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(Integer.from_string(2))
integer = Integer.from_string("10")
print(first_num.add(second_num))

import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")

    def test_add_success(self):
        first_integer = Integer(10)
        second_integer = Integer(12)
        result = first_integer.add(second_integer)
        self.assertEqual(result, 22)

    def test_add_error(self):
        first_integer = Integer(10)
        second_integer = 12
        result = first_integer.add(second_integer)
        self.assertEqual(result, "number should be an Integer instance")


if __name__ == "__main__":
    unittest.main()


