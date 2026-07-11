import unittest
from datetime import datetime
from pathlib import Path

from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.package import Package
from src.routing import Routing
from src.truck import Truck


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


class TestRouting(unittest.TestCase):
    """
    Tests the routing logic used to deliver packages.
    """

    def setUp(self):
        """
        Creates a routing system using the real distance table
        and a small package table.
        """

        self.distance_table = DistanceTable()
        self.distance_table.load_distances(DISTANCE_FILE)

        self.package_table = HashTable()

        # Use real addresses from the distance table.
        address1 = self.distance_table.addresses[1]
        address2 = self.distance_table.addresses[2]

        package1 = Package(
            1,
            address1,
            "Salt Lake City",
            "UT",
            "84107",
            "EOD",
            "5",
            ""
        )

        package2 = Package(
            2,
            address2,
            "Salt Lake City",
            "UT",
            "84107",
            "EOD",
            "5",
            ""
        )

        self.package_table.insert(1, package1)
        self.package_table.insert(2, package2)

        self.routing = Routing(
            self.package_table,
            self.distance_table
        )

        self.truck = Truck(1)
        self.truck.set_departure_time(
            datetime(2026, 7, 10, 8, 0)
        )

        self.truck.load_package(1)
        self.truck.load_package(2)


    def test_find_next_package(self):
        """
        Verify the routing algorithm returns one of the
        packages currently on the truck.
        """

        package_id = self.routing.find_next_package(
            self.truck
        )

        self.assertIn(
            package_id,
            self.truck.packages
        )


    def test_deliver_package(self):
        """
        Verify delivering a package updates all
        package and truck information.
        """

        self.routing.deliver_package(
            self.truck,
            1
        )

        package = self.package_table.search(1)

        self.assertEqual(
            package.status,
            "Delivered"
        )

        self.assertIsNotNone(
            package.delivery_time
        )

        self.assertNotIn(
            1,
            self.truck.packages
        )

        self.assertGreater(
            self.truck.mileage,
            0
        )


    def test_deliver_truck(self):
        """
        Verify all packages are delivered and
        the truck returns to the hub.
        """

        self.routing.deliver_truck(
            self.truck
        )

        self.assertEqual(
            len(self.truck.packages),
            0
        )

        self.assertEqual(
            self.truck.current_location,
            Truck.HUB_ADDRESS
        )

        self.assertGreater(
            self.truck.mileage,
            0
        )


if __name__ == "__main__":
    unittest.main()