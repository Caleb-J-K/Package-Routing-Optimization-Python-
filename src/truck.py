from datetime import datetime, timedelta


class Truck:

    SPEED = 18  # Truck speed in miles per hour.
    CAPACITY = 16  # Maximum number of packages per truck.

    HUB_ADDRESS = (
        "Western Governors University\n"
        "4001 South 700 East, \n"
        "Salt Lake City, UT 84107"
    )

    def __init__(self, truck_id: int) -> None:

        self.truck_id: int = truck_id

        # Package IDs currently loaded on the truck.
        self.packages: list[int] = []

        # Tracks total distance traveled.
        self.mileage: float = 0.0

        # Tracks when the truck leaves the hub.
        self.departure_time: datetime | None = None

        # Tracks the truck's current simulation time.
        self.current_time: datetime | None = None

        # Trucks begin at the WGUPS hub.
        self.current_location: str = self.HUB_ADDRESS

    def load_package(self, package_id: int) -> None:

        # Prevent trucks from exceeding their maximum capacity.
        if len(self.packages) < self.CAPACITY:
            self.packages.append(package_id)

        else:
            raise ValueError(
                "Truck capacity reached. Cannot load more packages."
            )

    def remove_package(self, package_id: int) -> None:

        # Remove a package after it has been delivered.
        if package_id in self.packages:
            self.packages.remove(package_id)

        else:
            raise ValueError(
                "Package not found on the truck."
            )

    def set_departure_time(self, departure_time: datetime) -> None:

        # Initialize the truck clock when it leaves the hub.
        self.departure_time = departure_time
        self.current_time = departure_time

    def travel(self, distance: float) -> None:

        # Add mileage and advance the truck's clock based on travel distance.
        self.mileage += distance

        if self.current_time is not None:

            travel_hours = distance / self.SPEED

            self.current_time += timedelta(
                hours=travel_hours
            )

    def __str__(self) -> str:

        return (
            f"Truck: {self.truck_id}\n"
            f"Packages: {self.packages}\n"
            f"Mileage: {self.mileage:.2f} miles\n"
            f"Location: {self.current_location}"
        )