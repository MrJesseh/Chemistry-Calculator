# This program is designed to do stoichiometry problems for chemistry class.


# Sets this variable to 1.  It's just a constant.
calculator = 1

# Loops the calculator so that you can just keep using it.
while calculator == 1:
  def startUp():
    print('''
    ---------------------------------
      Super Easy Chemistry Program
    ---------------------------------
    Accepted Inputs:

    stoich calc
    calculator (for two numbers)
    element
    mole bridge (WIP)

    --------------------------------
    Note: These are case sensitive.
    --------------------------------
    ''')
    # Adds a new line.
    print(" ")
  startUp()
  def whatsyourelement():
    element = input("What is your element? ")
    if element in chemName:
      # Stores value of index number of chemName of the element entered
      indexnumelement = chemName.index(element)
      # Uses indexnumelement above to find the Chemical Symbol of the same index in the list
      symbol = chemSymb[indexnumelement]
      # Uses indexnumelement to display list molarMass at the index
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
  def stoichCalc(problemType):
    if problemType == "moles to moles":
      # Gets the numbers from the user.
      moles = input("Enter moles of substance A: ")
      coEffA = input("Enter the coefficient of substance A: ")
      coEffB = input("Enter the coefficient of substance B: ")
      # Calculates conversion factor based on Coefficients.
      conversionFactor = float(coEffB) / float(coEffA)
      # Calculates the output moles.
      output = float(moles) * float(conversionFactor)
      print("The amount of moles of substance B is: ", str(output))
      print("The equation would be: ", str(moles), " moles A", "x", "(", str(coEffB), "moles B", "/", str(coEffA), "moles A",")", "=", str(output))
    elif problemType == "moles to mass":
      # Gets the numbers from the user.
      moles = input("Enter moles of the substance: ")
      molarMassA = input("Enter the molar mass of the substance: ")
      # Calculates molar Molar Mass.
      output = float(moles) * float(molarMassA)
      print("The molar mass is: ", str(output))
      if molarMassA in molarMass:
        findMass = molarMass.index(molarMassA)
        giveName = chemName[findMass]
        print("")
        print("It looks like your element is "+giveName )
    elif problemType == "mass to moles":
      # Gets user inputs about the problem.
      massA = input("Enter the mass of the substance: ")
      molarMassA = input("Enter the molar mass of the substance: ")
      # Calculates the mass.
      moles = float(massA) / float(molarMassA)
      print("The amount of moles of the substance is: ", str(moles))
    elif problemType == "mass to mass":
      # Gets user inputs about the problem.
      massA = input("Enter the mass of the substance: ")
      molarMassA = input("Enter the molar mass of the substance: ")
      # Calculates the mass.
      molesA = float(massA) / float(molarMassA)
      # Gets more inputs.
      coEffA = input("Enter the coefficient of substance A: ")
      coEffB = input("Enter the coefficient of substance B: ")
      conversionFactor = float(coEffB) / float(coEffA)
      # Calculates the output moles.
      molesB = float(molesA) * float(conversionFactor)
      # More inputs
      molarMassB = input("Enter the molar mass of substance B: ")
      # Calculates mass.
      massB = float(molesB) * float(molarMassB)
      print("The mass of substance B is: ", str(massB))
      if molarMassA in molarMass:
        findMassA = molarMass.index(molarMassA)
        findMassB = molarMass.index(molarMassB)
        giveNameA = chemName[findMassA]
        giveNameB = chemName[findMassB]
        print("")
        print("It looks like your first mass is the element "+giveNameA)
        print("It looks like your second element is "+giveNameB)
          
    elif problemType == "dihydrogen monoxide":
      print("water")
    else:
      print("You did not enter an accepted value, press 'Run' to try again.")
  def calcProgram(calcType):
    if calcType == "add":
      number1 = input("Enter the first number: ")
      number2 = input("Enter the second number: ")
      sumnum = float(number1) + float(number2)
      print("The sum is: ", str(sumnum))
    elif calcType == "subtract":
      number1 = input("Enter the first number: ")
      number2 = input("Enter the second number: ")
      difnum = float(number1) - float(number2)
      print("The difference is: ", str(difnum))
    elif calcType == "multiply":
      number1 = input("Enter the first number: ")
      number2 = input("Enter the second number: ")
      prodnum = float(number1) * float(number2)
      print("The product is: ", str(prodnum))
    elif calcType == "divide":
      number1 = input("Enter the first number: ")
      number2 = input("Enter the second number: ")
      # handles divide by zero error.
      if int(number2) == 0:
        print("Cannot divide by zero.")
        pass
      else:
        quotnum = float(number1) / float(number2)
        print("The quotient is: ", str(quotnum))
    else:
      print("You did not enter an accepted value.")
  def moleBridge(calcType):
    if calcType == "moles to atoms":
      # Asks user to input the number of moles.
      moles = input("Enter the number of moles: ")
      # Calculates amount of atoms.
      atoms = float(moles) * (6.022 * 10**23)
      print("The amount of atoms is: ", str(atoms))
    elif calcType == "atoms to moles":
      # Asks user for the number of atoms.
      atoms = input("Enter the number of atoms: ")
      # Calculates moles
      moles = float(atoms) / (6.022 * 10**23)
      print("The amount of moles is: ", str(moles))
    elif calcType == "atoms to mass":
      # Asks for the amount of atoms
      atoms = input("Enter the amount of atoms: ")
      # Calculate moles
      moles = float(atoms) / float((6.022 * 10**23))
      # Asks for molar mass.
      molarMass = input("Enter the molar mass: ")
      mass = float(moles) * float(molarMass)
      print("The mass is", str(mass))
    elif calcType == "mass to atoms":
         # Asks for the amount of atoms
      mass = input("Enter the mass: ")
      molarMass = input("Enter the molar mass: ")
      # Calculates moles
      moles = float(mass) / float(molarMass)
      # Calculates atoms
      atoms = float(moles) * float((6.022 * 10**23))
      print("The amount of atoms is: ", str(atoms)) 
  def calcOptions():
    if option == "stoich calc":
      print('''
      -------------
      Problem Types:
      -------------
      moles to moles
      moles to mass
      mass to moles
      mass to mass

      ''')
      problemType = input("What type of problem do you want to do? ")
      stoichCalc(problemType)
    elif option == "calculator":
      print('''
      -----------
      Calculations
      -----------

      add
      subtract
      multiply
      divide

      NOTE: Only works for two numbers as of right now.

      ''')
      calcType = input("What calculation do you want to do? ")
      calcProgram(calcType)
    elif option == "element":
      print('''
      -----------
      Element Information
      -----------
      ''')
      whatsyourelement()
    elif option == "mole bridge":
      print('''
      ---------------
      Conversions
      ---------------
      moles to atoms
      atoms to moles
      atoms to mass
      mass to atoms
      
      ''')
      calcType = input("Which calculation do you want to do? ")
      moleBridge(calcType)
    else:
      print("You did not enter an accepted value.")

  # List of Chemical Symbols, corresponds with list of element names
  chemSymb = ['Jc`  ', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk','Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Jw']

  # List of Element names, corresponds with list of Chemical Symbols
  chemName = ['Josh Conklin','Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum','Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium','Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roetgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine','Oganessan','Jesse Wright']

  # List of Molar Masses, corresponds with both Chemical Symbols and Chemical names
  molarMass = ['Co-Creator', '1.008', '4.002602', '6.94', '9.0121', '10.81', '12.011', '14.007', '15.999', '18.9984', '20.1797', '22.989769', '24.305', '26.9815', '28.085', '30.973761', '32.06', '35.45', '39.95', '39.0983', '40.078', '44.956', '47.867', '50.942', '51.9961', '54.938', '55.845', '58.933', '58.6934', '63.546', '65.38', '69.723', '72.630', '74.92', '78.971', '79.904', '83.798', '85.4678', '87.62', '88.91', '91.22', '92.91', '95.95', '98', '101.07', '102.91', '106.42', '107.868', '112.414', '114.82', '118.710', '121.760', '127.6', '126.90', '131.293', '132.91', '137.327', '138.905', '140.116', '140.91', '144.242', '145', '150.36', '151.964', '157.25', '158.93', '162.50', '164.930328', '167.259', '168.934', '172.05', '174.967', '178.49', '180.94788', '183.84', '186.207', '190.23', '192.217', '195.084', '196.967', '200.592', '204.38', '207.2', '208.980', '209', '210', '222', '223', '226', '227', '232.0377', '231.03588', '238.02891', '237', '244', '243', '247', '247', '251', '252', '257', '258', '259', '266', '267', '268', '269','270', '270', '278', '281', '282', '285', '286', '289', '290', '293', '294', '294','Creator']

  # Asks the user what they want to use.
  option = input("What do you want to do? ")
  calcOptions()

  # This program was made to complete chemistry and other mathematical problems with ease.
