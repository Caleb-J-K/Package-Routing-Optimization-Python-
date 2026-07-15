from datetime import datetime

from src.truck import Truck
from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.routing import Routing
from src.driver import Driver


DELAYED_PACKAGES = [
    6,
    25,
    28,
    32
]

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

class DeliveryService:

    def __init__(
        self,
        package_table: HashTable,
        distance_table: DistanceTable
    ) -> None:

        self.package_table = package_table
        self.distance_table = distance_table

        # Simulation begins at 8:00 AM.
        self.current_time = datetime(
            2026,
            7,
            10,
            8,
            0
        )

        # Available trucks in the WGUPS fleet.
        self.trucks = [
            Truck(1),
            Truck(2),
            Truck(3)
        ]

        # Only two drivers are available.
        self.drivers = [
            Driver(1),
            Driver(2)
        ]

        # Handles package routing and delivery.
        self.routing = Routing(
            self.package_table,
            self.distance_table
        )

    def assign_packages(self) -> None:

        self.assign_required_packages()

        self.assign_package_groups()

        self.assign_remaining_packages()

    def assign_required_packages(self) -> None:

        # Truck 2 has packages with specific requirements.
        truck_2 = self.trucks[1]

        for package_id in TRUCK_TWO_REQUIRED_PACKAGES:
            truck_2.load_package(package_id)

    def assign_package_groups(self) -> None:

        # These packages must travel together.
        truck_1 = self.trucks[0]

        for package_id in GROUPED_PACKAGES:
            truck_1.load_package(package_id)

    def assign_remaining_packages(self) -> None:

        assigned_packages = set()

        # Track packages already assigned.
        for truck in self.trucks:
            assigned_packages.update(truck.packages)

        truck_index = 0

        for package_id in range(1, 41):

            # Skip packages already assigned.
            if package_id in assigned_packages:
                continue

            # Delayed packages are loaded after arrival.
            if package_id in DELAYED_PACKAGES:
                continue

            # Move to the next truck when capacity is reached.
            while (
                len(self.trucks[truck_index].packages)
                >= Truck.CAPACITY
            ):
                truck_index += 1

            self.trucks[truck_index].load_package(
                package_id
            )

    def load_delayed_packages(self) -> None:

        # Delayed packages arrive at the hub at 9:05 AM.
        arrival_time = datetime(
            2026,
            7,
            10,
            9,
            5
        )

        if self.current_time < arrival_time:
            return

        truck_index = 0

        for package_id in DELAYED_PACKAGES:

            # Avoid loading duplicate packages.
            already_loaded = any(
                package_id in truck.packages
                for truck in self.trucks
            )

            if already_loaded:
                continue

            while (
                len(self.trucks[truck_index].packages)
                >= Truck.CAPACITY
            ):
                truck_index += 1

            self.trucks[truck_index].load_package(
                package_id
            )

    def dispatch_trucks(self) -> None:

        # Dispatch trucks currently assigned packages.
        for truck in self.trucks:

            if not truck.packages:
                continue

            truck.set_departure_time(
                self.current_time
            )

            self.routing.deliver_truck(
                truck
            )

    def simulate(self) -> None:

        self.assign_packages()

        self.dispatch_trucks()

        # Advance time when delayed packages arrive.
        self.current_time = datetime(
            2026,
            7,
            10,
            9,
            5
        )

        self.load_delayed_packages()

        self.dispatch_trucks()

    def total_mileage(self) -> float:

        return sum(
            truck.mileage
            for truck in self.trucks
        )