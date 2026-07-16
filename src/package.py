from datetime import datetime


class Package:
    
    # Initializes package object
    def __init__(
        self, 
        package_id: int, 
        address: str, 
        city: str, 
        state: str, 
        zip_code: str, 
        deadline: str, 
        weight: str, 
        special_notes: str,
        arrival_time: datetime | None = None
    ) -> None:
        
        # Package and delivery information
        self.package_id: int= package_id
        self.original_address: str = address
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
        self.deadline: str = deadline
        self.weight: str = weight
        self.special_notes: str = special_notes
        
        # Delivery tracking information
        self.status: str = "At Hub"
        self.arrival_time: datetime | None = arrival_time
        self.delivery_time: datetime | None = None
        self.departure_time: datetime | None = None
        self.truck_id: int | None = None

    # Formats package information for CLI display.
    def __str__(self):

        delivery_info = ""

        if self.delivery_time is not None:
            delivery_info = (
                f" | Delivered: "
                f"{self.delivery_time.strftime('%I:%M %p')}"
            )

        return (
            f"Package {self.package_id} | "
            f"{self.address}, {self.city}, {self.state}, {self.zip_code} | "
            f"Deadline: {self.deadline} | "
            f"Weight: {self.weight} | "
            f"Status: {self.status}"
            f"{delivery_info}"
        )
    
    def get_status_at_time(self, check_time: datetime) -> str:

        if self.arrival_time is not None and check_time < self.arrival_time:
            return "Delayed"

        if self.delivery_time is not None and check_time >= self.delivery_time:
            return "Delivered"

        if self.departure_time is not None and check_time >= self.departure_time:
            return "En Route"

        return "At Hub"
    
    def update_address(
            self, 
            address: str, 
            city: str, 
            state: str, 
            zip_code: str
            ) -> None:

        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code