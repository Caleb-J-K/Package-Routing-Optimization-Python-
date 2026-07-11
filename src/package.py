"""
Defines the Package class used throughout the WGUPS routing application.

Each Package object represents a delivery item and stores its identifying
information, destination details, delivery requirements, and current status.
"""


from datetime import datetime


class Package:
    """
    Represents a package that must be delivered.

    Package objects are created from package CSV data and are stored in the
    package hash table using their package ID as the lookup key.
    """
    
    def __init__(
        self, 
        package_id: int, 
        address: str, 
        city: str, 
        state: str, 
        zip_code: str, 
        deadline: str, 
        weight: str, 
        special_notes: str
    ) -> None:
        
        # Package and delivery information
        self.package_id: int= package_id
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
        self.deadline: str = deadline
        self.weight: str = weight
        self.special_notes: str = special_notes
        
        # Delivery tracking information
        self.status: str = "At Hub"
        self.delivery_time: datetime | None = None
        self.departure_time: datetime | None = None
        self.truck_id: int | None = None

    # Formats the package information into a string for easy printing
    def __str__(self):
        return (
            f"Package {self.package_id} | "
            f"{self.address}, {self.city}, {self.state}, {self.zip_code} | "
            f"Deadline: {self.deadline} | "
            f"Weight: {self.weight} | "
            f"Status: {self.status}"
         )
    
    def get_status_at_time(self, check_time: datetime) -> str:
        """
        Determines package status at a specific time.
        """

        if self.delivery_time is not None and check_time >= self.delivery_time:
            return "Delivered"


        if self.departure_time is not None and check_time >= self.departure_time:
            return "En Route"


        return "At Hub"