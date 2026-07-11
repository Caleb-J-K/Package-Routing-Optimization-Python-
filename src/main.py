# StudentID: 012582173

"""
Loads package data from a CSV file and stores it in a custome hash table,
also serves as the main entry point for the routing program.
"""

import csv
from pathlib import Path
from datetime import datetime

from src.delivery_services import DeliveryService
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

def initialize_system():
    """
    Loads all required data and creates the delivery system.
    """

    package_table = load_packages(PACKAGE_FILE)

    distance_table = DistanceTable()
    distance_table.load_distances(DISTANCE_FILE)

    return package_table, distance_table

# def main():

#     package_table, distance_table = initialize_system()

#     delivery_service = DeliveryService(
#         package_table,
#         distance_table
#     )

#     delivery_service.assign_packages()

#     delivery_service.simulate()


def display_menu():
    """
    Displays the main menu options.
    """

    print(
        """
===================================
        WGUPS Delivery System
===================================

1. Run delivery simulation
2. Lookup package
3. View all packages
4. View truck status
5. Exit
"""
    )



def lookup_package(package_table):
    """
    Looks up a package and displays its status
    at a user-provided time.
    """

    try:

        package_id = int(
            input("\nEnter package ID: ")
        )

        time_input = input(
            "Enter time (HH:MM AM/PM): "
        )

        check_time = datetime.strptime(
            time_input,
            "%I:%M %p"
        )

        check_time = check_time.replace(
            year=2026,
            month=7,
            day=10
        )

    except ValueError:

        print(
            "Invalid input."
        )

        return


    package = package_table.search(
        package_id
    )


    if package is None:

        print(
            "Package not found."
        )

        return


    status = package.get_status_at_time(
        check_time
    )


    print(
        f"""
------------------------------
Package ID: {package.package_id}

Address:
{package.address}

Deadline:
{package.deadline}

Status:
{status}

Truck:
{package.truck_id}

Delivery Time:
{package.delivery_time}
------------------------------
"""
    )



def display_packages(package_table):
    """
    Displays all packages.
    """

    for package_id in range(1, 41):

        package = package_table.search(
            package_id
        )

        if package:
            print(package)



def display_trucks(delivery_service):
    """
    Displays truck information.
    """

    for truck in delivery_service.trucks:

        print(
            f"""
Truck {truck.truck_id}
Packages: {truck.packages}
Mileage: {truck.mileage:.2f}
Location:
{truck.current_location}
"""
        )



def run_application():

    package_table, delivery_service = initialize_system()


    while True:

        display_menu()

        choice = input(
            "Enter selection: "
        )


        if choice == "1":

            delivery_service.assign_packages()

            delivery_service.simulate()

            print(
                "\nSimulation complete."
            )


        elif choice == "2":

            lookup_package(
                package_table
            )


        elif choice == "3":

            display_packages(
                package_table
            )


        elif choice == "4":

            display_trucks(
                delivery_service
            )


        elif choice == "5":

            print(
                "\nClosing WGUPS system."
            )

            break


        else:

            print(
                "\nInvalid option."
            )



if __name__ == "__main__":
    run_application()