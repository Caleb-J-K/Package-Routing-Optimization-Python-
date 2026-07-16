import unittest
from pathlib import Path

from src.delivery_services import DeliveryService
from src.hash_table import HashTable
from src.distance_table import DistanceTable
from src.package import Package
from src.truck import Truck


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


class TestDeliveryService(unittest.TestCase):

    def setUp(self):

        self.distance_table = DistanceTable()
        self.distance_table.load_distances(DISTANCE_FILE)

        self.package_table = HashTable()

        # Create mock packages using real delivery addresses.
        for package_id in range(1, 41):

            address = self.distance_table.addresses[
                package_id % len(self.distance_table.addresses)
            ]

            package = Package(
                package_id,
                address,
                "Salt Lake City",
                "UT",
                "84107",
                "EOD",
                "1",
                ""
            )

            self.package_table.insert(
                package_id,
                package
            )

        self.delivery_service = DeliveryService(
            self.package_table,
            self.distance_table
        )

    def test_service_initialization(self):

        self.assertEqual(
            len(self.delivery_service.trucks),
            3
        )

        self.assertEqual(
            self.delivery_service.current_time.hour,
            8
        )

    def test_assign_required_packages_to_truck_two(self):

        self.delivery_service.assign_packages()

        truck_two = self.delivery_service.trucks[1]

        required_packages = [
            3,
            18,
            36,
            38
        ]

        for package_id in required_packages:

            self.assertIn(
                package_id,
                truck_two.packages
            )

    def test_package_group_stays_together(self):

        self.delivery_service.assign_packages()

        group = [
            13,
            14,
            15,
            16,
            19,
            20
        ]

        assigned_truck = None

        for truck in self.delivery_service.trucks:

            if group[0] in truck.packages:

                assigned_truck = truck
                break

        self.assertIsNotNone(
            assigned_truck
        )

        for package_id in group:

            self.assertIn(
                package_id,
                assigned_truck.packages
            )

    def test_delayed_packages_not_loaded_initially(self):

        self.delivery_service.assign_packages()

        delayed_packages = [
            6,
            25,
            28,
            32
        ]

        assigned_packages = []

        for truck in self.delivery_service.trucks:

            assigned_packages.extend(
                truck.packages
            )

        for package_id in delayed_packages:

            self.assertNotIn(
                package_id,
                assigned_packages
            )

    def test_no_package_assigned_twice(self):

        self.delivery_service.assign_packages()

        all_packages = []

        for truck in self.delivery_service.trucks:

            all_packages.extend(
                truck.packages
            )

        self.assertEqual(
            len(all_packages),
            len(set(all_packages))
        )

    def test_truck_capacity_not_exceeded(self):

        self.delivery_service.assign_packages()

        for truck in self.delivery_service.trucks:

            self.assertLessEqual(
                len(truck.packages),
                Truck.CAPACITY
            )

    def test_dispatched_packages_have_truck_id(self):

        self.delivery_service.assign_packages()

        self.delivery_service.dispatch_trucks(self.delivery_service.trucks[:2])

        for package_id in range(1, 41):

            package = self.package_table.search(
                package_id
            )

            if package.truck_id is not None:

                self.assertIsNotNone(
                    package.truck_id
                )

    def test_dispatch_first_two_trucks(self):

        self.delivery_service.assign_packages()

        self.delivery_service.dispatch_trucks(
            self.delivery_service.trucks[:2]
        )

        self.assertEqual(
            len(self.delivery_service.trucks[0].packages),
            0
        )

        self.assertEqual(
            len(self.delivery_service.trucks[1].packages),
            0
        )

    def test_simulate(self):

        self.delivery_service.simulate()

        for truck in self.delivery_service.trucks:

            self.assertEqual(
                len(truck.packages),
                0
            )

        for package_id in range(1, 41):

            package = self.package_table.search(
                package_id
            )

            self.assertEqual(
                package.status,
                "Delivered"
            )

    def test_total_mileage(self):

        self.delivery_service.simulate()

        mileage = self.delivery_service.total_mileage()

        self.assertGreater(
            mileage,
            0
        )

        self.assertLess(
            mileage,
            140
        )

    def test_package_status_updated(self):

        self.delivery_service.simulate()

        package = self.package_table.search(
            1
        )

        self.assertEqual(
            package.status,
            "Delivered"
        )

        self.assertIsNotNone(
            package.delivery_time
        )

    def test_packages_receive_delivery_time(self):

        self.delivery_service.simulate()

        package = self.package_table.search(
            10
        )

        self.assertIsNotNone(
            package.delivery_time
        )


if __name__ == "__main__":
    unittest.main()