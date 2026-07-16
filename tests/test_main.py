import unittest
from datetime import datetime

from src.main import (
    initialize_system,
    load_packages,
    PACKAGE_FILE,
    DISTANCE_FILE
)

from src.distance_table import DistanceTable


class TestMain(unittest.TestCase):

    def test_load_packages(self):

        distance_table = DistanceTable()

        distance_table.load_distances(
            DISTANCE_FILE
        )

        package_table = load_packages(
            PACKAGE_FILE,
            distance_table
        )

        for package_id in range(1, 41):

            package = package_table.search(
                package_id
            )

            self.assertIsNotNone(
                package
            )

    def test_initialize_system(self):

        package_table, delivery_service = initialize_system()

        self.assertIsNotNone(
            package_table
        )

        self.assertIsNotNone(
            delivery_service
        )

        self.assertEqual(
            len(delivery_service.trucks),
            3
        )

    def test_delayed_packages_have_arrival_time(self):

        package_table, _ = initialize_system()

        delayed_packages = [
            6,
            25,
            28,
            32
        ]

        for package_id in delayed_packages:

            package = package_table.search(
                package_id
            )

            self.assertIsNotNone(
                package.arrival_time
            )

            self.assertEqual(
                package.arrival_time,
                datetime(
                    2026,
                    7,
                    10,
                    9,
                    5
                )
            )

    def test_package_nine_loaded(self):

        package_table, _ = initialize_system()

        package = package_table.search(
            9
        )

        self.assertIsNotNone(
            package
        )

        self.assertEqual(
            package.package_id,
            9
        )


if __name__ == "__main__":
    unittest.main()