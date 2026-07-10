# StudentID: 012582173

"""
Loads package data from a CSV file and stores it in a custome hash table,
also serves as the main entry point for the routing program.
"""

import csv
from pathlib import Path

from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.package import Package


# Resolve the base directory and data directory paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

PACKAGE_FILE = DATA_DIR / "package_file.csv"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


def load_packages(filename: str | Path) -> HashTable:
    """
    Reads package data from a CSV file, 
    creates Package objects, 
    and inserts them into the hash table.
    """

    package_table = HashTable()

    with open(filename, 'r', newline='') as file:

        reader = csv.reader(file)

        # Skip the header row
        next(reader)  

        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            # Create a Package object using CSV data
            package = Package(
                package_id, 
                address, 
                city, 
                state, 
                zip_code, 
                deadline, 
                weight, 
                special_notes
                )

            # Insert the package into the hash table
            package_table.insert(package_id, package)

    return package_table

def main():
    
    # Load all package data into the hash table
    package_table = load_packages(PACKAGE_FILE)

    # Create a DistanceTable object
    distance_table = DistanceTable()

    # Load the CSV data
    distance_table.load_distances(DISTANCE_FILE)

    print(package_table)

if __name__ == "__main__":
    main()