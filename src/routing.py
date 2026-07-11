"""
Contains routing logic for the WGUPS delivery simulation.

Uses a nearest-neighbor approach to determine the next delivery
location for each truck.
"""

from src.truck import Truck
from src.hash_table import HashTable
from src.distance_table import DistanceTable


class Routing:
    """
    Handles package delivery routing.

    Determines delivery order, calculates travel distances,
    and updates package and truck information.
    """

    def __init__(
        self,
        package_table: HashTable,
        distance_table: DistanceTable
    ) -> None:
        """
        Initializes the routing system.

        Args:
            package_table: Stores package objects.
            distance_table: Provides distance lookups.
        """

        self.package_table = package_table
        self.distance_table = distance_table


    def deliver_truck(self, truck: Truck) -> None:
        """
        Delivers all packages assigned to a truck.

        Uses a nearest-neighbor routing strategy.
        """

        while truck.packages:

            next_package_id = self.find_next_package(truck)

            self.deliver_package(
                truck,
                next_package_id
            )

        # Return truck to hub after deliveries.
        distance = self.distance_table.get_distance(
            truck.current_location,
            Truck.HUB_ADDRESS
        )

        truck.travel(distance)

        truck.current_location = Truck.HUB_ADDRESS


    def find_next_package(
        self,
        truck: Truck
    ) -> int:
        """
        Finds the closest package destination
        from the truck's current location.
        """

        shortest_distance = float("inf")
        closest_package = None


        for package_id in truck.packages:

            package = self.package_table.search(
                package_id
            )

            distance = self.distance_table.get_distance(
                truck.current_location,
                package.address
            )


            if distance < shortest_distance:
                shortest_distance = distance
                closest_package = package_id


        return closest_package


    def deliver_package(
        self,
        truck: Truck,
        package_id: int
    ) -> None:
        """
        Delivers a package and updates simulation data.
        """

        package = self.package_table.search(
            package_id
        )


        distance = self.distance_table.get_distance(
            truck.current_location,
            package.address
        )


        truck.travel(distance)


        truck.current_location = package.address


        package.status = "Delivered"

        package.delivery_time = truck.current_time

        package.truck_id = truck.truck_id


        truck.remove_package(package_id)