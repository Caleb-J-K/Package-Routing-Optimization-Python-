from datetime import datetime

from src.truck import Truck


class Driver:

    def __init__(self, driver_id: int) -> None:

        self.driver_id: int = driver_id

        # Tracks whether this driver can operate a truck.
        self.available: bool = True

        # Stores the truck currently assigned to this driver.
        self.current_truck: Truck | None = None

        self.available_time: datetime | None = None

    def assign_truck(self, truck: Truck) -> None:

        # Assign a truck and mark driver as unavailable.
        self.current_truck = truck
        self.available = False

    def release_truck(self) -> None:

        # Free the driver after completing a route.
        self.current_truck = None
        self.available = True