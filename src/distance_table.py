"""
Provides the DistanceTable class used to load and retrieve delivery distances.

The distance data is stored as a lower triangular matrix, where each address
has a corresponding index used to efficiently retrieve the distance between
two locations.
"""

import csv
from pathlib import Path


class DistanceTable:
    """
    Stores delivery addresses and the distances between locations.

    The distance file contains a list of addresses and a lower triangular
    distance matrix. Addresses are stored separately so that lookups can
    convert addresses into matrix indexes.
    """
    
    # Initializes an empty distance table.
    def __init__(self) -> None: 
        self.addresses: list[str] = [] # Stores addresses in the order they appear in the distance file.
        self.distance_table: list[list[str]] = [] # Stores the lower triangular distance matrix as a list of lists.


    def load_distances(self, filename: str | Path) -> None:
        """
        Loads address and distance data from a CSV file.
        """

        # Clears any existing data to prevent duplicate entries if this method is called more than once.
        self.addresses.clear()
        self.distance_table.clear()

        with open(filename, 'r', newline='') as file:

            reader = csv.reader(file)
            rows = list(reader)

            # The first row contains the addresses, the first two columns are not addresses, so we skip them.
            self.addresses = [
                address.strip()
                for address in rows[0][2:]  # Skip the first two columns
            ]

            # The remaining rows after the first 2 contain the distance data.
            for row in rows[1:]:  # Skip the first row which contains addresses
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
        """
        Returns the distance between two addresses.
        """

        #distance from an address to itself is always 0.0
        if address1 == address2:
            return 0.0

        try:
            #find the position of each address in the list.
            index1 = self.addresses.index(address1)
            index2 = self.addresses.index(address2)
        except ValueError:
            raise ValueError(
                f"One or both addresses not found: {address1}, {address2}"
            )

        #The distance table is a lower triangular matrix, 
        # so we need to check which index is larger.
        if index2 < index1:
            distance = self.distance_table[index1][index2]
        else:
            distance = self.distance_table[index2][index1]

        #convert the distance to a float and return it.
        return float(distance)
    
    def find_full_address(self, street_address: str) -> str:
        """
        Finds the distance table address matching a package address.

        Handles minor formatting differences between CSV files.
        """

        clean_package_address = (
            street_address
            .strip()
            .lower()
        )

        for address in self.addresses:

            clean_distance_address = (
                address
                .strip()
                .lower()
            )

            # Direct match
            if clean_package_address in clean_distance_address:
                return address

            # Handle common abbreviation differences
            normalized_package = (
                clean_package_address
                .replace("station", "sta")
            )

            normalized_distance = (
                clean_distance_address
                .replace("station", "sta")
            )

            if normalized_package in normalized_distance:
                return address

        raise ValueError(
            f"Address not found in distance table: {street_address}"
        )