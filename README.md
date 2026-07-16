# WGUPS Delivery Routing System

## Overview

The WGUPS Delivery Routing System is a Python application that simulates package delivery operations for the Western Governors University Parcel Service (WGUPS).

The application loads package and distance data from CSV files, assigns packages to delivery trucks while respecting delivery constraints, calculates delivery routes using a nearest-neighbor routing algorithm, and tracks package and truck status throughout the delivery day. A command-line interface allows users to run the delivery simulation, look up individual packages, view the status of all packages at a specified time, and inspect truck information.

This project was developed as part of the Western Governors University Computer Science curriculum and follows object-oriented design principles, modular architecture, and automated testing practices.


---

## Features

- Loads package and distance data from CSV files
- Custom hash table implementation for efficient package storage and retrieval
- Nearest-neighbor routing algorithm for package delivery
- Simulates deliveries using three trucks and two drivers
- Tracks truck mileage throughout the delivery day
- Calculates travel time using an average speed of 18 MPH
- Supports delayed package arrivals
- Handles package address corrections during the simulation
- Tracks package status as:
  - Delayed
  - At Hub
  - En Route
  - Delivered
- Look up any package at a user-specified time
- View all package statuses at a user-specified time
- View truck status and assigned packages at a user-specified time
- Automated unit testing for core components


---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- CSV Data Processing
- pathlib
- unittest
- Git / GitHub


---

## Project Structure

```text
C950 Project/
│
├── data/
│   ├── distance_file.csv
│   └── package_file.csv
│
├── src/
│   ├── main.py
│   ├── delivery_services.py
│   ├── routing.py
│   ├── truck.py
│   ├── driver.py
│   ├── package.py
│   ├── hash_table.py
│   └── distance_table.py
│
├── tests/
│
└── README.md
```

---

## Routing Algorithm

Package deliveries are performed using a nearest-neighbor routing algorithm.

Each truck repeatedly selects the closest undelivered package from its current location until all assigned packages have been delivered. While this heuristic does not always produce the mathematically optimal route, it provides an efficient solution that satisfies the project requirements while maintaining a total mileage below the required limit.


---

## Delivery Constraints

The simulation accounts for all delivery constraints provided in the project requirements, including:

- Delayed packages that arrive at the hub at **9:05 AM**
- Package 9 address correction available after **10:20 AM**
- Packages that must be delivered together
- Packages that must be assigned to a specific truck
- Three delivery trucks with only two available drivers
- Truck capacity limit of 16 packages


---

## Time Simulation

Truck travel time is calculated using the required average speed of **18 miles per hour**.

Travel time is determined from the distance traveled:

```
Travel Time = Distance ÷ Speed
```

Package and truck statuses are calculated dynamically based on user-selected times, allowing the application to accurately report historical delivery information throughout the day.


---

## Distance Table Design

The provided distance file stores distances in a lower-triangular matrix.

Example:

```
      A     B     C
A    0
B   7.2    0
C   3.8   7.1    0
```

Since only half of the matrix is provided, the application automatically retrieves distances regardless of direction.

For example:

```
Location A → Location B
```

and

```
Location B → Location A
```

both return the same distance.


---

## Running the Application

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd "C950 Project"
```

Run the application:

```bash
python -m src.main
```


---

## Running Tests

The project uses Python's built-in **unittest** framework.

Run all tests:

```bash
python -m unittest discover
```

Example output:

```
......
----------------------------------------------------------------------
Ran 22 tests in 0.04s

OK
```

(The number of tests may vary as additional tests are added.)


---

## Development Practices

This project emphasizes several software engineering principles:

- Object-oriented design
- Separation of responsibilities between classes
- Modular architecture
- Custom hash table implementation
- Automated unit testing
- Type hints
- Meaningful comments and documentation
- Incremental development using Git


---

## Future Improvements

Potential future enhancements include:

- Docker containerization
- PostgreSQL database integration
- REST API for package management
- React-based web interface
- Interactive route visualization
- More advanced route optimization algorithms (2-opt, A*, etc.)
- Persistent package history and reporting


---
