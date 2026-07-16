import unittest
from datetime import datetime

from src.package import Package


class TestPackage(unittest.TestCase):

    def setUp(self):

        self.package = Package(
            1,
            "123 Main St",
            "Salt Lake City",
            "UT",
            "84107",
            "10:30 AM",
            "5",
            "None"
        )

    def test_package_creation(self):

        self.assertEqual(
            self.package.package_id,
            1
        )

        self.assertEqual(
            self.package.address,
            "123 Main St"
        )

        self.assertEqual(
            self.package.city,
            "Salt Lake City"
        )

        self.assertEqual(
            self.package.state,
            "UT"
        )

        self.assertEqual(
            self.package.zip_code,
            "84107"
        )

    def test_default_delivery_status(self):

        self.assertEqual(
            self.package.status,
            "At Hub"
        )

        self.assertIsNone(
            self.package.departure_time
        )

        self.assertIsNone(
            self.package.delivery_time
        )

        self.assertIsNone(
            self.package.truck_id
        )

    def test_package_string(self):

        package_string = str(
            self.package
        )

        self.assertIn(
            "Package 1",
            package_string
        )

        self.assertIn(
            "123 Main St",
            package_string
        )

        self.assertIn(
            "At Hub",
            package_string
        )

    def test_status_at_hub(self):

        check_time = datetime(
            2026,
            7,
            10,
            8,
            0
        )

        self.assertEqual(
            self.package.get_status_at_time(check_time),
            "At Hub"
        )

    def test_status_en_route(self):

        self.package.departure_time = datetime(
            2026,
            7,
            10,
            8,
            0
        )

        check_time = datetime(
            2026,
            7,
            10,
            8,
            30
        )

        self.assertEqual(
            self.package.get_status_at_time(check_time),
            "En Route"
        )

    def test_status_delivered(self):

        self.package.departure_time = datetime(
            2026,
            7,
            10,
            8,
            0
        )

        self.package.delivery_time = datetime(
            2026,
            7,
            10,
            9,
            15
        )

        check_time = datetime(
            2026,
            7,
            10,
            10,
            0
        )

        self.assertEqual(
            self.package.get_status_at_time(check_time),
            "Delivered"
        )

    def test_status_delayed(self):

        self.package.arrival_time = datetime(
            2026,
            7,
            10,
            9,
            5
        )

        check_time = datetime(
            2026,
            7,
            10,
            8,
            30
        )

        self.assertEqual(
            self.package.get_status_at_time(check_time),
            "Delayed"
        )


if __name__ == "__main__":
    unittest.main()