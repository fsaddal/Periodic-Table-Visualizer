import csv
import sys
import re

# Open and read the CSV file
file_path = 'periodictable.csv'

try:
    with open(file_path, encoding='utf-8') as elementsFile:
        elementsCsvReader = csv.reader(elementsFile)
        elements = list(elementsCsvReader)
except FileNotFoundError:
    print(f"File {file_path} not found. Ensure the file is in the correct location.")
    sys.exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    sys.exit()

# Skip irrelevant rows to get to the header
START_ROW = 4  # The actual header is in row 5 (index 4)
elements = elements[START_ROW:]

# Define the column headers
ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 
               'Group', 'Period', 'Atomic weight', 'Density', 
               'Melting point', 'Boiling point', 'Specific heat capacity',
               'Electronegativity', 'Abundance in Earth\'s crust']
LONGEST_COLUMN = max(len(col) for col in ALL_COLUMNS)

# Create a dictionary to store element details
ELEMENTS = {}

for line in elements[1:]:  # Skip the header row
    # Skip empty lines
    if not any(line):
        continue

    # Map the row data to the column headers
    element = {
        'Atomic Number': line[0],
        'Symbol': line[1],
        'Element': line[2],
        'Origin of name': line[3],
        'Group': line[4],
        'Period': line[5],
        'Atomic weight': line[6] + ' u',
        'Density': line[7] + ' g/cm^3',
        'Melting point': line[8] + ' K',
        'Boiling point': line[9] + ' K',
        'Specific heat capacity': line[10] + ' J/(g*K)',
        'Electronegativity': line[11],
        'Abundance in Earth\'s crust': line[12] + ' mg/kg'
    }

    # Remove [roman numeral] text from values
    for key, value in element.items():
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    # Add to ELEMENTS dictionary by both atomic number and symbol
    ELEMENTS[line[0]] = element
    ELEMENTS[line[1]] = element

# Print the periodic table and allow user to query
print('Periodic Table of Elements')
print()

while True:
    print('''           Periodic Table of Elements
          1  2  3  4  5  6  7  8  9  10  11  12 13 14 15 16 17 18
        1 H                                                    He
        2 Li Be                                 B  C  N  O  F  Ne
        3 Na Mg                                 Al Si P  S  Cl Ar
        4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
        5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
        6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
        7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')

    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').strip()

    if response.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        sys.exit()

    # Search for the element
    if response in ELEMENTS:
        print("\nElement Details:")
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(f"{keyJustified}: {ELEMENTS[response][key]}")
        input("\nPress Enter to continue...")
    else:
        print("Invalid input. Please enter a valid symbol or atomic number.\n")
