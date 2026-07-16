import unittest
from datetime import datetime

from src.truck import Truck


class TestTruck(unittest.TestCase):

    def setUp(self):

        self.truck = Truck(1)

    def test_truck_initialization(self):

        self.assertEqual(
            self.truck.truck_id,
            1
        )

        self.assertEqual(
            self.truck.packages,
            []
        )

        self.assertEqual(
            self.truck.mileage,
            0.0
        )

        self.assertIsNone(
            self.truck.departure_time
        )

        self.assertIsNone(
            self.truck.current_time
        )

        self.assertEqual(
            self.truck.current_location,
            Truck.HUB_ADDRESS
        )

    def test_load_package(self):

        self.truck.load_package(
            1
        )

        self.assertIn(
            1,
            self.truck.packages
        )

    def test_remove_package(self):

        self.truck.load_package(
            5
        )

        self.truck.remove_package(
            5
        )

        self.assertNotIn(
            5,
            self.truck.packages
        )

    def test_remove_missing_package(self):

        with self.assertRaises(ValueError) as context:

            self.truck.remove_package(
                99
            )

        self.assertIn(
            "not found",
            str(context.exception).lower()
        )

    def test_truck_capacity(self):

        for package_id in range(
            Truck.CAPACITY
        ):

            self.truck.load_package(
                package_id
            )

        with self.assertRaises(ValueError) as context:

            self.truck.load_package(
                17
            )

        self.assertIn(
            "capacity",
            str(context.exception).lower()
        )

    def test_departure_time(self):

        departure = datetime(
            2026,
            7,
            10,
            8,
            0
        )

        self.truck.set_departure_time(
            departure
        )

        self.assertEqual(
            self.truck.departure_time,
            departure
        )

        self.assertEqual(
            self.truck.current_time,
            departure
        )

    def test_travel_updates_mileage(self):

        self.truck.set_departure_time(
            datetime(
                2026,
                7,
                10,
                8,
                0
            )
        )

        self.truck.travel(
            18
        )

        self.assertEqual(
            self.truck.mileage,
            18
        )

        self.assertEqual(
            self.truck.current_time.hour,
            9
        )

    def test_travel_updates_fractional_time(self):

        self.truck.set_departure_time(
            datetime(
                2026,
                7,
                10,
                8,
                0
            )
        )

        self.truck.travel(
            9
        )

        self.assertEqual(
            self.truck.mileage,
            9
        )

        self.assertEqual(
            self.truck.current_time.hour,
            8
        )

        self.assertEqual(
            self.truck.current_time.minute,
            30
        )


if __name__ == "__main__":
    unittest.main()