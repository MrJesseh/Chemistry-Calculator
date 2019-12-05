import time
import sys
def periodicTable():
  print('''
  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  -------------
              -------------------------------------------------------------
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------
  ''')
  # List of Chemical Symbols, corresponds with list of element names
chemSymb = ['Jc`  ', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk','Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Jw']
chemName = ['Josh Conklin','Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum','Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium','Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roetgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine','Oganessan','Jesse Wright']

  # List of Molar Masses, corresponds with both Chemical Symbols and Chemical names
molarMass = ['Co-Creator', '1.008', '4.002602', '6.94', '9.0121', '10.81', '12.011', '14.007', '15.999', '18.9984', '20.1797', '22.989769', '24.305', '26.9815', '28.085', '30.973761', '32.06', '35.45', '39.95', '39.0983', '40.078', '44.956', '47.867', '50.942', '51.9961', '54.938', '55.845', '58.933', '58.6934', '63.546', '65.38', '69.723', '72.630', '74.92', '78.971', '79.904', '83.798', '85.4678', '87.62', '88.91', '91.22', '92.91', '95.95', '98', '101.07', '102.91', '106.42', '107.868', '112.414', '114.82', '118.710', '121.760', '127.6', '126.90', '131.293', '132.91', '137.327', '138.905', '140.116', '140.91', '144.242', '145', '150.36', '151.964', '157.25', '158.93', '162.50', '164.930328', '167.259', '168.934', '172.05', '174.967', '178.49', '180.94788', '183.84', '186.207', '190.23', '192.217', '195.084', '196.967', '200.592', '204.38', '207.2', '208.980', '209', '210', '222', '223', '226', '227', '232.0377', '231.03588', '238.02891', '237', '244', '243', '247', '247', '251', '252', '257', '258', '259', '266', '267', '268', '269','270', '270', '278', '281', '282', '285', '286', '289', '290', '293', '294', '294','Creator']

def whatsyourElement():
  element = input("What is your element? ")
  if element in chemName:
    # Stores value of index number of chemName of the element entered
    indexnumelement = chemName.index(element)
    # Uses indexnumelement above to find the Chemical Symbol of the same index in the list
    symbol = chemSymb[indexnumelement]
    # Uses indexnumelement to display list molarMass at the index777777777
    molprint = molarMass[indexnumelement]
    print('''
    
    ''')
    print("Here is the information that we found on "+element)
    print("Name ---------------------------------------------- "+ element)
    print("Chemical Symbol ----------------------------------- "+ symbol)
    # Uses string because it is a number value
    print("Atomic Number ------------------------------------- "+ str(indexnumelement))
    print("Molar Mass ---------------------------------------- "+ molprint)
    print('''
    
    ''')
  elif element in chemSymb:
    # indexnumelement variable if user inputs a symbol instead of a name
    indexnumelement = chemSymb.index(element)
    name = chemName[indexnumelement]
    molprint = molarMass[indexnumelement]
    print('''
    
    ''')
    print("Information about "+element)
    print("Name ---------------------------------------------- "+ name)
    print("Chemical Symbol ----------------------------------- "+ element)
    print("Atomic Number ------------------------------------- "+ str(indexnumelement))
    print("Molar Mass ---------------------------------------- "+ molprint)
    print('''
    
    ''')
    helpful = input("Did you find what you needed? ")
  if helpful == "no":
    periodicTable()
    whatsyourElement()
  else:
    load = 1
#here is the animation
    while load < 5:
      sys.stdout.write('\rloading |')
      time.sleep(0.1)
      sys.stdout.write('\rloading /')
      time.sleep(0.1)
      sys.stdout.write('\rloading -')
      time.sleep(0.1)
      sys.stdout.write('\rloading \\')
      time.sleep(0.1)
      load = load + 1
    sys.stdout.write('\rDone!     ')
      
      
# List of Element names, corresponds with list of Chemical Symbols
  