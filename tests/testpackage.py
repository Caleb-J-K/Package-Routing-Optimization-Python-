import unittest
from package import Package


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
        self.assertEqual(self.package.package_id, 1)
        self.assertEqual(self.package.address, "123 Main St")
        self.assertEqual(self.package.city, "Salt Lake City")
        self.assertEqual(self.package.state, "UT")
        self.assertEqual(self.package.zip_code, "84107")

    def test_default_delivery_status(self):
        self.assertEqual(self.package.status, "At Hub")
        self.assertIsNone(self.package.delivery_time)
        self.assertIsNone(self.package.departure_time)
        self.assertIsNone(self.package.truck_id)

    def test_package_string(self):
        package_string = str(self.package)

        self.assertIn("Package 1", package_string)
        self.assertIn("123 Main St", package_string)
        self.assertIn("At Hub", package_string)


if __name__ == "__main__":
    unittest.main()