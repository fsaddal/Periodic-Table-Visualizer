This program is designed to provide detailed information about elements in the periodic table. Users can look up any element by entering its atomic number or symbol, and the program will display relevant data such as atomic weight, density, boiling point, and more. It uses a CSV file (periodictable.csv) as the source for element data.

Features

Display Periodic Table: A simple visualization of the periodic table for easy reference.
Element Lookup: Users can input an element's atomic number or symbol to get detailed information.
User-Friendly Interface: Clear prompts and error handling to guide users throughout the program.
Data Cleaning: Automatically removes unnecessary formatting (e.g., [roman numerals]) from the data.
How to Use

Prepare the CSV File:
Ensure the file periodictable.csv is in the same directory as the program.
The file should contain element data with proper formatting.
Run the Program:
Use Python to execute the script: python periodic_table.py.
Follow the on-screen instructions.
Lookup Options:
Enter an atomic number (e.g., 1 for Hydrogen).
Enter an element symbol (e.g., H for Hydrogen).
Type QUIT to exit the program.
Requirements

Python 3.x
periodictable.csv file with element data.
Modules:
csv
sys
re
Error Handling

If the file periodictable.csv is not found, the program will display an error message and exit.
If an invalid input is entered, the program will prompt the user to try again.
Example

Periodic Table of Elements

Enter a symbol or atomic number to examine, or QUIT to quit.
> H

Element Details:
     Atomic Number: 1
            Symbol: H
           Element: Hydrogen
    Origin of name: Greek: "hydro" and "genes" meaning water-forming
             Group: 1
            Period: 1
     Atomic weight: 1.008 u
           Density: 0.08988 g/cm^3
     Melting point: 14.01 K
     Boiling point: 20.28 K
Specific heat capacity: 14.304 J/(g*K)
  Electronegativity: 2.20
Abundance in Earth's crust: 1400 mg/kg
Notes

The program assumes the CSV file's data starts from the fifth row (header row index: 4). Adjust START_ROW if needed for different file structures.
Data values are processed to ensure readability (e.g., appending units to values like atomic weight and density).
This program is a helpful tool for anyone interested in exploring the periodic table in a quick and interactive way
