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

        # WGUPS has three trucks.
        self.trucks = [
            Truck(1),
            Truck(2),
            Truck(3)
        ]

        # WGUPS only has two drivers.
        self.drivers = [
            Driver(1),
            Driver(2)
        ]

        self.routing = Routing(
            self.package_table,
            self.distance_table
        )


    def assign_packages(self) -> None:

        self.assign_required_packages()

        self.assign_package_groups()

        self.assign_remaining_packages()


    def assign_required_packages(self) -> None:

        # Truck 2 must carry these packages.
        for package_id in TRUCK_TWO_REQUIRED_PACKAGES:

            self.trucks[1].load_package(
                package_id
            )


    def assign_package_groups(self) -> None:

        # These packages must remain together.
        for package_id in GROUPED_PACKAGES:

            self.trucks[0].load_package(
                package_id
            )


    def assign_remaining_packages(self) -> None:

        assigned_packages = set()

        # Track packages already assigned.
        for truck in self.trucks:
            assigned_packages.update(
                truck.packages
            )


        truck_index = 0

        for package_id in range(1, 41):

            if package_id in assigned_packages:
                continue

            # Delayed packages arrive later.
            if package_id in DELAYED_PACKAGES:
                continue


            while (
                len(self.trucks[truck_index].packages)
                >= Truck.CAPACITY
            ):
                truck_index += 1


            self.trucks[truck_index].load_package(
                package_id
            )


    def load_delayed_packages(self) -> None:

        # Delayed packages arrive at 9:05 AM.
        for package_id in DELAYED_PACKAGES:

            self.trucks[2].load_package(
                package_id
            )


    def dispatch_trucks(self) -> None:

        # Only two trucks can operate because there are two drivers.
        for truck in self.trucks:

            # Do not dispatch trucks with no packages.
            if not truck.packages:
                continue

            available_driver = self.get_available_driver()

            if available_driver is None:
                break

            available_driver.assign_truck(truck)

            truck.set_departure_time(
                self.current_time
            )

            self.routing.deliver_truck(truck)

            available_driver.release_truck()

    def get_available_driver(self):

        for driver in self.drivers:
            if driver.available:
                return driver

        return None

    def simulate(self) -> None:

        # Assign morning packages.
        self.assign_packages()


        # Dispatch first two trucks.
        self.dispatch_trucks()


        # Advance time to delayed package arrival.
        self.current_time = datetime(
            2026,
            7,
            10,
            9,
            5
        )


        self.load_delayed_packages()


        # Dispatch remaining deliveries.
        self.dispatch_trucks()


    def total_mileage(self) -> float:

        return sum(
            truck.mileage
            for truck in self.trucks
        )