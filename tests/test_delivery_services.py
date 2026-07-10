"""
Unit tests for the DeliveryService class.
"""

import unittest

from src.delivery_services import DeliveryService
from src.hash_table import HashTable
from src.distance_table import DistanceTable
from src.package import Package
from src.truck import Truck


class TestDeliveryService(unittest.TestCase):

    def setUp(self):
        """
        Creates a DeliveryService with test package data.

        A small mock package table is used instead of loading the
        full CSV because these tests focus on package assignment logic.
        """

        self.package_table = HashTable()

        # Create mock packages 1-40.
        for package_id in range(1, 41):

            package = Package(
                package_id,
                "Test Address",
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

        self.distance_table = DistanceTable()

        self.delivery_service = DeliveryService(
            self.package_table,
            self.distance_table
        )


    def test_service_initialization(self):
        """
        Verify DeliveryService creates three trucks
        and initializes the simulation time.
        """

        self.assertEqual(
            len(self.delivery_service.trucks),
            3
        )

        self.assertEqual(
            self.delivery_service.current_time.hour,
            8
        )


    def test_assign_required_packages_to_truck_two(self):
        """
        Verify truck-restricted packages are assigned
        to truck 2.
        """

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
        """
        Verify packages that must travel together
        are assigned to the same truck.
        """

        self.delivery_service.assign_packages()

        trucks = self.delivery_service.trucks

        group = [
            13,
            14,
            15,
            16,
            19,
            20
        ]

        assigned_truck = None

        for truck in trucks:
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
        """
        Verify delayed packages are not assigned
        before arriving at the hub.
        """

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
        """
        Verify a package cannot appear on multiple trucks.
        """

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
        """
        Verify no truck exceeds its package capacity.
        """

        self.delivery_service.assign_packages()

        for truck in self.delivery_service.trucks:

            self.assertLessEqual(
                len(truck.packages),
                Truck.CAPACITY
            )


if __name__ == "__main__":
    unittest.main()