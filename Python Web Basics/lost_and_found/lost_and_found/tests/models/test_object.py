from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class TestObject(TestCase):
    valid_name = 'object1'
    valid_image = 'http://image.com'
    valid_height = 2
    valid_weight = 1

    def test__when_width_is_less_than_max__expect_to_work(self):
        width = 5
        object_1 = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )
        object_1.full_clean()
        object_1.save()

    def test__when_width_is_equal_to_max__expect_to_work(self):
        width = 600
        object_1 = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )
        object_1.full_clean()
        object_1.save()

    def test__when_width_is_more_than_max__expect_to_raise_error(self):
        width = 605
        object_1 = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight
        )

        with self.assertRaises(ValidationError) as ex:
            object_1.full_clean()
            object_1.save()
        self.assertIsNotNone(ex.exception)
