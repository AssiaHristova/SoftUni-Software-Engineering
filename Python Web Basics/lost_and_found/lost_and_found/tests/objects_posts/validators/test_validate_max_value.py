from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.validators import validate_max_value


class ValidateMaxValueTests(TestCase):
    def test__when_value_is_less_than_max_value__expect_to_work(self):
        value = 5
        validate_func = validate_max_value(value + 1)
        validate_func(value)

    def test__when_value_is_equal_to_max_value__expect_to_work(self):
        value = 5
        validate_func = validate_max_value(value)
        validate_func(value)

    def test__when_value_is_more_than_max_value__expect_to_raise_error(self):
        value = 5
        validate_func = validate_max_value(value - 1)
        with self.assertRaises(ValidationError) as ex:
            validate_func(value)
        self.assertIsNotNone(ex.exception)


