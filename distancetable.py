"""
The DistanceTable class loads the distance table from a csv file
and provides fast distance lookups between addresses.
"""

import csv


class DistanceTable:
    """
    Stores all delivery addresses and the distances between them.
    """
    
    #stores every address in a list for easy access, in the order it appears in the Distance_File.csv
    def __init__(self):
        #Stores the list of addresses from the CSV file.
        self.addresses = []

        #Stores the distance values between locations.
        self.distance_table = []

    def load_distances(self, filename):
        """
        Reads the distance table from a CSV file and 
        loads the addresses and distances into memory.
        """

        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

            self.addresses = [
                address.strip()
                for address in rows[0][2:]  # Skip the first two columns
            ]

            rows = rows[1:]  # Skip the first row / address list

            #Process each row of distance data.
            for row in rows:
                cleaned_row = [
                    value.strip()
                    for value in row[2:]
                ]

                self.distance_table.append(cleaned_row)


    def get_distance(self, address1, address2):
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