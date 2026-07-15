from datetime import datetime

from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.truck import Truck


class Routing:

    def __init__(
        self,
        package_table: HashTable,
        distance_table: DistanceTable
    ) -> None:

        self.package_table = package_table
        self.distance_table = distance_table


    def deliver_truck(
        self,
        truck: Truck
    ) -> None:

        # Continue delivering packages until the truck is empty.
        while truck.packages:

            next_package_id = self.find_next_package(truck)

            # No packages are currently available.
            if next_package_id is None:

                truck.current_time = datetime(
                    2026,
                    7,
                    10,
                    10,
                    20
                )

                continue

            self.deliver_package(
                truck,
                next_package_id
            )


        # Return truck to hub after deliveries.
        # distance = self.distance_table.get_distance(
        #     truck.current_location,
        #     Truck.HUB_ADDRESS
        # )

        # truck.travel(distance)

        # truck.current_location = Truck.HUB_ADDRESS



    def find_next_package(
        self,
        truck: Truck
    ) -> int | None:

        shortest_distance = float("inf")
        closest_package = None


        for package_id in truck.packages:

            package = self.package_table.search(
                package_id
            )


            if package.delivery_time is not None:
                continue


            # Delayed packages cannot leave before arrival.
            if package.arrival_time is not None:

                if truck.current_time < package.arrival_time:
                    continue


            # Package 9 address is unknown until 10:20 AM.
            # It can be loaded, but cannot be delivered before then.
            if (
                package_id == 9
                and truck.current_time < datetime(
                    2026,
                    7,
                    10,
                    10,
                    20
                )
            ):
                continue


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

        package = self.package_table.search(
            package_id
        )


        # Update package 9 address after the correction time.
        if (
            package_id == 9
            and truck.current_time >= datetime(
                2026,
                7,
                10,
                10,
                20
            )
        ):

            package.update_address(
                "Third District Juvenile Court\n410 S State St",
                "Salt Lake City",
                "UT",
                "84111"
            )


        # Record when the package leaves the hub.
        package.departure_time = truck.current_time


        distance = self.distance_table.get_distance(
            truck.current_location,
            package.address
        )


        truck.travel(distance)

        truck.current_location = package.address


        package.status = "Delivered"

        package.delivery_time = truck.current_time

        package.truck_id = truck.truck_id


        truck.remove_package(
            package_id
        )