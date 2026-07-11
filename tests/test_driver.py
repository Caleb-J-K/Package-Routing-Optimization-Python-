import unittest

from src.driver import Driver
from src.truck import Truck


class TestDriver(unittest.TestCase):

    def test_driver_initialization(self):
        """
        Verify drivers start available.
        """

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

    def test_driver_assignment(self):
        driver = Driver(1)
        truck = Truck(1)

        driver.assign_truck(truck)

        self.assertEqual(driver.current_truck, truck)
        self.assertFalse(driver.available)


if __name__ == "__main__":
    unittest.main()