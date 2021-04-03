import unittest
from unittest import mock
from utils import Utils


class SampleTest(unittest.TestCase):
    def setUp(self):
        self.utils = Utils()      # before each test

    @mock.patch('validators.TypeValidator')
    def test_utils_sum_when_ints_expect_correct(self, validator_mock):
        # Arrange(prepare)
        validator = validator_mock.return_value
        validator.validate.return_value = None
        numbers = [1, 2, 3, 4, 5]
        # Act
        actual_result = self.utils.my_sum(numbers)
        # Assert
        expected_result = 15

        self.assertEqual(expected_result, actual_result, 'Actual result not equal to expected result')

    def test_my_sum_when_floats_expect_correct(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        actual_result = self.utils.my_sum(numbers)
        expected_result = 15.0

        self.assertEqual(expected_result, actual_result)

    def my_sum_when_numbers_are_string(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            self.utils.my_sum(numbers)

        actual_message = context.exception.args[0]
        expected_message = 'numbers should be numbers.'
        self.assertEqual(actual_message, expected_message)





