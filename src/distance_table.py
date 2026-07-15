import csv
from pathlib import Path


class DistanceTable:
    
    # Initializes an empty distance table that stores addresses and their corresponding distance values.
    def __init__(self) -> None: 
        self.addresses: list[str] = []
        self.distance_table: list[list[str]] = []

    def normalize_address(self, address: str) -> str:
        # Standardizes addresses so small formatting differences do not break lookups.
        return (
            " ".join(address.split())
            .lower()
            .replace("station", "sta")
        )

    def load_distances(self, filename: str | Path) -> None:

        # Clears any existing data in case the table is loaded again.
        self.addresses.clear()
        self.distance_table.clear()

        with open(filename, 'r', newline='') as file:

            reader = csv.reader(file)
            rows = list(reader)

            # Store addresses from first row of the CSV.
            self.addresses = [
                " ".join(address.split())
                for address in rows[0][2:]
            ]

            # Stores the lower triangular distance matrix.
            for row in rows[1:]:
                cleaned_row = [
                value.strip()
                for value in row[2:]
            ]

                self.distance_table.append(cleaned_row)


    def get_distance(
            self,
            address1: str,
            address2: str
        ) -> float:

        clean_address1 = self.normalize_address(address1)
        clean_address2 = self.normalize_address(address2)

        index1 = None
        index2 = None

        # Find the row indices for both addresses.
        for i, address in enumerate(self.addresses):

            clean_address = self.normalize_address(address)

            if clean_address == clean_address1:
                index1 = i

            if clean_address == clean_address2:
                index2 = i

        if index1 is None or index2 is None:
            raise ValueError(
                f"One or both addresses not found: {address1}, {address2}"
            )

        distance = self.distance_table[index1][index2]

        # The CSV only stores half of the distance matrix, if the value is blank, use the reverse direction.
        if distance == "":
            distance = self.distance_table[index2][index1]

        return float(distance)
    
    def find_full_address(self, street_address: str) -> str:

        clean_package_address = self.normalize_address(street_address)
        
        # Match the package CSV address to the full address from the distance table.
        for address in self.addresses:

            clean_distance_address = self.normalize_address(address)

            if clean_package_address in clean_distance_address:
                return address

        raise ValueError(
            f"Address not found in distance table: {street_address}"
        )