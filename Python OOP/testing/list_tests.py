class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        integer_list = IntegerList()

    def test_int_list_add__when_int__expect_to_add_it(self):
    #   add operation, should add an element and returns the list. If the element is not an integer, a ValueError is thrown
        integer_list = IntegerList()
        internal_list = integer_list.add(1)

        self.assertEqual([1], internal_list)

    def test_int_list_add__when_str__expect_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add('string')

    def test_int_list_remove_if_index_in_range__expect_return_index(self):
    #    remove_index operation removes the element on that index and returns it. If the index is out of range, an IndexError is thrown
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, value_to_be_removed, 4)
        result = integer_list.remove_index(2)

        self.assertEqual(value_to_be_removed, result)
        self.assertListEqual([1, 2, 4], integer_list.get_data())

    def test_int_list_remove_if_index_not_in_range__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 4

        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_init__when_integers__expect_to_create_it(self):
    #    __init__should only take integers, and store them
        IntegerList(1, 2, 3)

    def test_init__when_not_only_integers__expect_to_exception(self):
        with self.assertRaises(Exception):
            IntegerList(1, 2, 'string')

    def test_int_list_get_if_index_in_range__expect_return_element(self):
    #    getshould r eturn the specific element If the index is out of range, an IndexError is thrown
        value_to_get = 3
        integer_list = IntegerList(1, 2, value_to_get, 4)
        result = integer_list.get(2)

        self.assertEqual(value_to_get, result)

    def test_int_list_get_if_index_not_in_range__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 4

        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_int_list_insert_if_index_in_range__expect_to_insert_it(self):
    #    insert If the index is out of range, IndexError is thrown If the element is not an integer, ValueError is thrown
        integer_list = IntegerList(1, 2, 3)
        integer_list.insert(0, 0)

        self.assertEqual([0, 1, 2, 3], integer_list.get_data())

    def test_int_list_insert_if_index_not_in_range__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 4

        with self.assertRaises(IndexError):
            integer_list.insert(index, 4)

    def test_int_list_insert__when_str__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        string = 'string'

        with self.assertRaises(ValueError):
            integer_list.insert(0, string)

    def test_list_int_get_biggest__expect_to_return_the_biggest_int(self):
    #    get_biggest
        biggest = 17
        integer_list = IntegerList(1, 2, biggest, 3)
        actual = integer_list.get_biggest()

        self.assertEqual(biggest, actual)

    def test_list_int_get_index__when_index_is_valid__expect_to_return_the_element(self):
    #    get_index
        index_to_get = 2
        value_to_get = 3
        integer_list = IntegerList(1, 2, value_to_get, 4)
        result = integer_list.get_index(value_to_get)

        self.assertEqual(index_to_get, result)



if __name__ == '__main__':
    unittest.main()

