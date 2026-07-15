# StudentID: 012582173

import csv
from pathlib import Path
from datetime import datetime

from src.delivery_services import DeliveryService
from src.distance_table import DistanceTable
from src.hash_table import HashTable
from src.package import Package
from src.delivery_services import DELAYED_PACKAGES


# Project file locations.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

PACKAGE_FILE = DATA_DIR / "package_file.csv"
DISTANCE_FILE = DATA_DIR / "distance_file.csv"


def load_packages(
    filename: str | Path,
    distance_table: DistanceTable
) -> HashTable:

    package_table = HashTable()

    with open(filename, "r", newline="") as file:

        reader = csv.reader(file)

        # Skip CSV header.
        next(reader)

        for row in reader:

            package_id = int(row[0])

            address = distance_table.find_full_address(
                row[1]
            )

            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            arrival_time = None

            # Delayed packages arrive at the hub at 9:05 AM.
            if package_id in [DELAYED_PACKAGES]:

                arrival_time = datetime(
                    2026,
                    7,
                    10,
                    9,
                    5
                )


            package = Package(
                package_id,
                address,
                city,
                state,
                zip_code,
                deadline,
                weight,
                special_notes,
                arrival_time
            )


            # Store package by ID for fast lookup.
            package_table.insert(
                package_id,
                package
            )

    return package_table



def initialize_system():

    distance_table = DistanceTable()

    distance_table.load_distances(
        DISTANCE_FILE
    )

    package_table = load_packages(
        PACKAGE_FILE,
        distance_table
    )


    delivery_service = DeliveryService(
        package_table,
        distance_table
    )


    return package_table, delivery_service



def display_menu():

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
        ).replace(
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

City:
{package.city}

State:
{package.state}

ZIP Code:
{package.zip_code}

Deadline:
{package.deadline}

Weight:
{package.weight}

Status:
{status}
"""
    )


    if (
        package.departure_time is None
        or check_time < package.departure_time
    ):

        print(
            "Truck:\nN/A"
        )

    else:

        print(
            f"Truck:\n{package.truck_id}"
        )


    if status == "Delivered":

        print(
            f"\nDelivery Time:\n{package.delivery_time}"
        )


    print(
        "------------------------------"
    )



def display_packages(package_table):

    # Display all packages currently in the system.
    for package_id in range(1, 41):

        package = package_table.search(
            package_id
        )

        if package:

            print(package)



def display_trucks(delivery_service):

    # Display current truck information.
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

    simulation_complete = False


    while True:

        display_menu()

        choice = input(
            "Enter selection: "
        )


        if choice == "1":

            if simulation_complete:

                print(
                    "\nSimulation has already been completed."
                )

                continue


            delivery_service.simulate()

            simulation_complete = True

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