"""
Defines the DeliveryService class used to manage the WGUPS delivery simulation.

The DeliveryService coordinates trucks, packages, and distance data.
It serves as the main layer between the data structures and the delivery logic.
"""

from datetime import datetime

from src.truck import Truck
from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.routing import Routing
from src.driver import Driver


TRUCK_TWO_REQUIRED_PACKAGES = [
    3,
    18,
    36,
    38
]

GROUPED_PACKAGES = [
    13,
    14,
    15,
    16,
    19,
    20
]

DELAYED_PACKAGES = [
    6,
    25,
    28,
    32
]


class DeliveryService:

    def __init__(
            self,
            package_table: HashTable,
            distance_table: DistanceTable
    ) -> None:
        
        self.package_table = package_table
        self.distance_table = distance_table
        self.current_time = datetime(2026, 7, 10, 8, 0)

        # Initialize three trucks for the delivery service.
        self.trucks = [
            Truck(1),
            Truck(2),
            Truck(3)
        ]

        # WGUPS has three trucks but only two drivers.
        self.drivers = [
            Driver(1),
            Driver(2)
        ]

        # Handles route planning and deliveries.
        self.routing = Routing(
            self.package_table,
            self.distance_table
        )

    def assign_packages(self) -> None:
        """
        Assigns packages to trucks based on delivery constraints.

        Packages are assigned in the following order:
        1. Packages restricted to specific trucks.
        2. Packages that must travel together.
        3. Remaining available packages.
        """

        self.assign_required_packages()
            
        self.assign_package_groups()

        self.assign_remaining_packages()


    def assign_required_packages(self) -> None:
        """
        Assigns packages that have specific truck requirements.

        Truck 2 must contain packages:
        3, 18, 36, and 38.
        """

        truck_2 = self.trucks[1]

        for package_id in TRUCK_TWO_REQUIRED_PACKAGES:
            truck_2.load_package(package_id)


    def assign_package_groups(self) -> None:
        """
        Assigns packages that must be delivered together.

        Packages 13, 14, 15, 16, 19, and 20
        must travel together.
        """

        truck_1 = self.trucks[0]

        for package_id in GROUPED_PACKAGES:
            truck_1.load_package(package_id)

            
    def assign_remaining_packages(self) -> None:
        """
        Assigns remaining available packages to trucks.

        Delayed packages are skipped because they are not
        available at the beginning of the simulation.

        Packages already assigned due to constraints are skipped.
        """

        assigned_packages = set()


        # Track packages already assigned to trucks.
        for truck in self.trucks:
            assigned_packages.update(truck.packages)


        truck_index = 0

        for package_id in range(1, 41):

            # Skip packages already assigned.
            if package_id in assigned_packages:
                continue

            # Skip delayed packages.
            if package_id in DELAYED_PACKAGES:
                continue

            # Find the next available truck.
            while (
                len(self.trucks[truck_index].packages)
                >= Truck.CAPACITY
            ):
                truck_index += 1

            self.trucks[truck_index].load_package(package_id)

    def dispatch_trucks(self) -> None:
        """
        Dispatches each truck to complete its assigned deliveries.
        """

        for truck in self.trucks:

            truck.set_departure_time(
                self.current_time
            )

            self.routing.deliver_truck(truck)

    def simulate(self) -> None:
        """
        Runs the complete delivery simulation.

        The current implementation:
            1. Assigns packages.
            2. Dispatches all trucks.

        Time-based delivery events will be incorporated as the
        simulation is expanded.
        """

        self.assign_packages()

        print("After assignment:")
        for truck in self.trucks:
            print(f"Truck {truck.truck_id}: {truck.packages}")

        self.dispatch_trucks()

    def total_mileage(self) -> float:
        """
        Returns the total mileage driven by all trucks.
        """

        return sum(
            truck.mileage
            for truck in self.trucks
        )