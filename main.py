#studentID: 012582173

import csv

from hashtable import HashTable
from package import Package

#Create the package hash table
package_table = HashTable()

def load_packages(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            print(row)
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            # Create a Package object
            package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)

            # Insert the package into the hash table
            package_table.insert(package_id, package)

# Load all package data
load_packages("Package_File.csv")


# Test the hash table
print(package_table.search(1))
print(package_table.search(15))
print(package_table.search(40))