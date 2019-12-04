# Allows for the functionality of the stoichiometric calculator.
from errors import errorMessage
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
    elif problemType == "dihydrogen monoxide":
      print("water")
    else:
      print("You did not enter an accepted value, press 'Run' to try again.")
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
        errorType = "divzero"
        errorMessage(errorType)  
      
      else:
        quotnum = float(number1) / float(number2)
        print("The quotient is: ", str(quotnum))
    else:
      print("You did not enter an accepted value.")

