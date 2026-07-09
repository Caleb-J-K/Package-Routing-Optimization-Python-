
class Package:
    #constructor for the package class
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes):
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
        self.status = "At the hub"
        self.delivery_time = None
        self.departure_time = None

    #formats the package information into a string for easy printing
    def __str__(self):
        return (
    f"Package {self.package_id} | "
    f"{self.address}, {self.city}, {self.state}, {self.zip_code} | "
    f"Deadline: {self.deadline} | "
    f"Weight: {self.weight} | "
    f"Status: {self.status}"
    )