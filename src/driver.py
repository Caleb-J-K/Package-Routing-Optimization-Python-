"""
Defines the Driver class used in the WGUPS delivery simulation.

Drivers control truck availability. Since WGUPS only has two drivers,
a maximum of two trucks can be active at any given time.
"""


from src.truck import Truck


class Driver:
    """
    Represents a delivery driver.

    Tracks whether the driver is currently assigned to a truck.
    """

    def __init__(self, driver_id: int) -> None:
        """
        Initializes a driver.

        Args:
            driver_id: Unique identifier for the driver.
        """

        self.driver_id: int = driver_id
        self.available: bool = True
        self.current_truck: Truck | None = None

    def assign_truck(self, truck: "Truck") -> None:
        """
        Assigns a truck to the driver.

        Args:
            truck:
                Truck assigned to this driver.
        """

        self.current_truck = truck
        self.available = False


    def release_truck(self) -> None:
        """
        Removes the driver's current truck assignment
        and makes the driver available again.
        """

        self.current_truck = None
        self.available = True