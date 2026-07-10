from datetime import timedelta

class Truck:
    """
    A class representing a delivery truck.
    """

    Speed = 18  # miles per hour
    Capacity = 16  # packages
    HubAddress = (
        "Western Governors University\n"
        "4001 South 700 East,\n"
        "Salt Lake City, UT 84107"
    )

    def __init__(self, truck_id):
        """
        Initializes a Truck object with the given truck ID.
        """
        self.truck_id = truck_id
        self.packages = []  # List to hold packages assigned to the truck
        self.mileage = 0.0  # Total mileage for the truck
        self.departure_time = None  # Time when the truck departs for deliveries
        self.current_time = None  # Start time at 8:00 AM
        self.current_location = self.HubAddress  # Start at the hub address


    def load_packages(self, package_id):
        """
        Loads a package onto the truck if it has not reached its capacity.
        """
        if len(self.packages) < self.Capacity:
            self.packages.append(package_id)
        else:
            raise Exception("Truck capacity reached. Cannot load more packages.")
        

    def remove_package(self,package_id):
        """
        Removes a package from the truck if it is present.
        """
        if package_id in self.packages:
            self.packages.remove(package_id)
        else:
            raise Exception("Package not found on the truck.")
        

    def set_departure_time(self, departure_time):
        """
        Sets the departure time for the truck.
        """
        self.departure_time = departure_time
        self.current_time = departure_time  # Initialize current time to departure time


    def travel(self, distance):
        """
        Simulates the truck traveling a certain distance and updates the current time.
        """
        self.mileage += distance

        if self.current_time is not None:

            hours = distance / self.Speed

            self.current_time += timedelta(hours=hours)


    def __str__(self):
        """
        Returns a string representation of the Truck object.
        """
        return (
            f"Truck: {self.truck_id}\n"
            f"Packages: {self.packages}\n"
            f"Mileage: {self.mileage:.2f} miles\n"
            f"Location: {self.current_location}"
        )