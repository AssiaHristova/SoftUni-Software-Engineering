from project_3.hardware.hardware import Hardware
from unittest import TestCase, main

from project_3.software.software import Software


class HardwareTests(TestCase):
    def setUp(self):
        self.hardware = Hardware("HDD", 'Heavy', 200, 200)

    def test_init__expect_all_attributes(self):
        self.assertEqual(self.hardware.name, 'HDD')
        self.assertEqual(self.hardware.type, 'Heavy')
        self.assertEqual(self.hardware.capacity, 200)
        self.assertEqual(self.hardware.memory, 200)
        self.assertEqual(self.hardware.software_components, [])

    def test_available_memory__if_nothing_installed__expect_to_be_full(self):
        self.assertEqual(self.hardware.available_memory, 200)

    def test_available_capacity__if_nothing_installed__expect_to_be_full(self):
        self.assertEqual(self.hardware.available_capacity, 200)

    def test_install__expect_to_add_in_software_components(self):
        software = Software("SSD", "Linux", 50, 100)
        self.hardware.install(software)

        self.assertEqual(self.hardware.software_components, [software])

    def test_install__when_not_enough_memory__expect__exception(self):
        software = Software("SSD", "Linux", 50, 300)

        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual(self.hardware.software_components, [])

    def test_install__when_not_enough_capacity__expect__exception(self):
        software = Software("SSD", "Linux", 300, 100)

        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual(self.hardware.software_components, [])

    def test_available_memory__if_software_installed__expect_to_decrease(self):
        software = Software("SSD", "Linux", 50, 100)
        self.hardware.install(software)

        self.assertEqual(self.hardware.available_memory, 100)

    def test_available_capacity__if_software_installed__expect_to_decrease(self):
        software = Software("SSD", "Linux", 50, 100)
        self.hardware.install(software)

        self.assertEqual(self.hardware.available_capacity, 150)

    def test_uninstall__expect_to_remove_from_software_components(self):
        software = Software("SSD", "Linux", 50, 100)
        self.hardware.install(software)
        self.hardware.uninstall(software)

        self.assertEqual(self.hardware.software_components, [])

    def test_uninstall_if_software_not_installed__expect_software_components_to_remain(self):
        software = Software("SSD", "Linux", 50, 100)
        software_2 = Software("HHD", "Windows", 50, 100)
        self.hardware.install(software)
        self.hardware.uninstall(software_2)

        self.assertEqual(self.hardware.software_components, [software])


if __name__ == '__main__':
    main()








