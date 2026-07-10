"""
Defines the Truck class used to simulate package deliveries.

Each truck tracks its assigned packages, current location, mileage,
Departure time, and current simulation time as it completes deliveries.
"""

from datetime import datetime, timedelta


class Truck:
    """
    Represents a delivery truck used by the WGUPS routing system.

    A truck is responsible for transporting packages, tracking its
    current location, mileage, and simulation time throughout the
    delivery process.
    """

    SPEED = 18  # miles per hour
    CAPACITY = 16  # max # of packages
    HUB_ADDRESS = (
        "Western Governors University\n"
        "4001 South 700 East,\n"
        "Salt Lake City, UT 84107"
    )

    def __init__(self, truck_id: int) -> None:
        """
        Initializes a Truck object with the given truck ID.
        """
        self.truck_id: int = truck_id
        self.packages: list[int] = []  # List to hold packages assigned to the truck
        self.mileage: float = 0.0  # Total mileage for the truck
        self.departure_time: datetime | None = None  # Time when the truck departs for deliveries
        self.current_time: datetime | None = None  # Start time at 8:00 AM
        self.current_location: str = self.HUB_ADDRESS  # Start at the hub address


    def load_package(self, package_id: int) -> None:
        """
        Loads a package onto the truck if it has not reached its capacity.
        """
        if len(self.packages) < self.CAPACITY:
            self.packages.append(package_id)
        else:
            raise ValueError("Truck capacity reached. Cannot load more packages.")
        

    def remove_package(self,package_id: int) -> None:
        """
        Removes a package from the truck if it is present.
        """
        if package_id in self.packages:
            self.packages.remove(package_id)
        else:
            raise ValueError("Package not found on the truck.")
        

    def set_departure_time(self, departure_time: datetime) -> None:
        """
        Sets the departure time for the truck.
        """
        self.departure_time = departure_time
        self.current_time = departure_time  # Initialize current time to departure time


    def travel(self, distance: float) -> None:
        """
        Simulates the truck traveling a certain distance and updates the current time.
        """
        self.mileage += distance

        if self.current_time is not None:

            hours = distance / self.SPEED

            self.current_time += timedelta(hours=hours)


    def __str__(self) -> str:
        """
        Returns a string summary of the Truck object.
        """
        return (
            f"Truck: {self.truck_id}\n"
            f"Packages: {self.packages}\n"
            f"Mileage: {self.mileage:.2f} miles\n"
            f"Location: {self.current_location}"
        )