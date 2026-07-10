"""
Defines the Package class used throughout the routing program.

Each Package object contains information about a specific package, 
including its ID, address, delivery deadline, weight, and any special notes. 
The class also tracks the package's delivery status and times.
"""
class Package:
    """
    Represents a package to be delivered.
    Stores package information from the package csv file and tracks delivery status and times.
    """
    
    #constructor for the package class
    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, deadline: str, weight: str, special_notes: str):
        
        #Basic package information
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        
        #Delivery information
        self.status = "At Hub"
        self.delivery_time = None
        self.departure_time = None
        self.truck_id = None

    #formats the package information into a string for easy printing
    def __str__(self):
        return (
    f"Package {self.package_id} | "
    f"{self.address}, {self.city}, {self.state}, {self.zip_code} | "
    f"Deadline: {self.deadline} | "
    f"Weight: {self.weight} | "
    f"Status: {self.status}"
    )