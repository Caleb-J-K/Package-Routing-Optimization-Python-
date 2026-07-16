import unittest

from src.driver import Driver
from src.truck import Truck


class TestDriver(unittest.TestCase):

    def test_driver_initialization(self):

        driver = Driver(1)

        self.assertEqual(
            driver.driver_id,
            1
        )

        self.assertTrue(
            driver.available
        )

        self.assertIsNone(
            driver.current_truck
        )

        self.assertIsNone(
            driver.available_time
        )

    def test_driver_assignment(self):

        driver = Driver(1)
        truck = Truck(1)

        driver.assign_truck(
            truck
        )

        self.assertEqual(
            driver.current_truck,
            truck
        )

        self.assertFalse(
            driver.available
        )

    def test_driver_release(self):

        driver = Driver(1)
        truck = Truck(1)

        driver.assign_truck(
            truck
        )

        driver.release_truck()

        self.assertTrue(
            driver.available
        )

        self.assertIsNone(
            driver.current_truck
        )


if __name__ == "__main__":
    unittest.main()