#studentID: 012582173
"""
Loads package data from a CSV file and stores it in a custome hash table,
also serves as the main entry point for the routing program.
"""
import csv

from hashtable import HashTable
from package import Package

PACKAGE_FILE = "Package_File.csv"

def load_packages(filename):
    """
    Reads package data from a CSV file, 
    creates Package objects, 
    and inserts them into the hash table.
    """

    # Create a hash table to store the packages
    package_table = HashTable()

    with open(filename, 'r', newline='') as file:

        reader = csv.reader(file)

        next(reader)  # Skip the header row

        # Read each row in the CSV file and create Package objects
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
                address, city, 
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
    
    # Test the hash table
    print(package_table.search(1))
    print(package_table.search(15))
    print(package_table.search(40))

if __name__ == "__main__":
    main()