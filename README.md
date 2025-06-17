# Package Sorter

A simple Python function that simulates a robotic arm's logic for dispatching packages based on their size and weight.

## Objective

Sort packages into the correct stack:

- STANDARD: Not bulky and not heavy.
- SPECIAL: Bulky or heavy, but not both.
- REJECTED: Both bulky and heavy.

## Rules

- A package is bulky if:
  - Volume (width * height * length) >= 1,000,000 cm³, or
  - Any single dimension >= 150 cm
- A package is heavy if:
  - Mass >= 20 kg

## Project Structure

.
├── sort.py         # Main sorting logic
├── test_sort.py    # Unit tests using unittest
└── README.md                 # This file

## Usage

Import and use the sort function:

    from sort.py import sort

    stack = sort(width=120, height=100, length=80, mass=15)
    print(stack)  # "SPECIAL"

## Running Tests

Run all tests:

    python test_package_sorter.py

Or using discovery:

    python -m unittest discover


## Author

Carlos Mario Araujo
carlosm.araujob@gmail.com