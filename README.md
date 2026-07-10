# WGUPS Delivery Routing System

## Overview

The WGUPS Delivery Routing System is a Python application that simulates package delivery operations for the Western Governors University Parcel Service.

The program uses object-oriented design principles to model delivery components including packages, trucks, locations, and routing logic. The goal of the system is to efficiently deliver packages while tracking truck mileage and delivery status.

This project was developed as part of the WGU Computer Science curriculum and expanded with professional software development practices including automated testing and modular design.


## Features

Current features:

- Load delivery location data from CSV files
- Store and retrieve distances between delivery locations
- Handle the provided distance matrix format
- Perform distance lookups between any two locations
- Automated unit tests for core functionality

Planned features:

- Package management system
- Truck simulation
- Package delivery status tracking
- Route optimization
- Delivery time calculation
- User interface for viewing delivery progress


## Technologies Used

- Python 3
- Object-Oriented Programming
- CSV data processing
- Unit Testing (`unittest`)
- Git / GitHub


## Project Structure

C950 Project/
│
├── main.py
│ Application entry point
│
├── distancetable.py
│ Handles loading and retrieving location distances
│
├── Distance_File.csv
│ Distance data between delivery locations
│
├── tests/
│ Automated unit tests
│
│ └── test_distancetable.py
│
└── README.md


## Distance Table Design

The provided distance file stores distances in a lower-triangular matrix format.

Example:

  A   B   C
A 0
B 7.2 0
C 3.8 7.1 0


Because only half of the distance matrix is stored, the application includes logic to retrieve distances regardless of the requested direction.

Example:


Location A → Location B


and


Location B → Location A


both return the same distance.

---

## Running the Application

Clone the repository:

bash
git clone <repository-url>

Navigate into the project directory:

cd "C950 Project"

Run the application:

python main.py

## Running Tests

The project uses Python's built-in unittest framework.

To run all tests:

python -m unittest discover

Example output:

......
----------------------------------------------------------------------
Ran 6 tests in 0.02s

OK

## Development Practices

This project follows several software engineering practices:

Separation of responsibilities between classes
Automated testing for core components
Meaningful comments and documentation
Incremental development using version control
Modular project structure
Future Improvements

## Potential improvements include:

Implementing route optimization algorithms
Adding package tracking history
Adding a graphical user interface
Improving data validation
Adding additional automated tests