# This program is designed to do stoichiometry problems for chemistry class.
# Imports functions from other files for use.
from errors import errorMessage
from element import periodicTable
from element import whatsyourElement
from chemcalc import stoichCalc
from chemcalc import moleBridge
from chemcalc import calcProgram
from spooky import skeleton
# Sets this variable to 1.  It's just a constant.
calculator = 1

# Loops the calculator so that you can just keep using it.
while calculator == 1:
  def startUp():
    print('''
    -----------------------------------
    --  Super Easy Chemistry Program --
    -----------------------------------
    ---      Accepted Inputs        ---
    -----------------------------------                    
    ---        stoich calc          ---
    --- calculator (for two numbers)---
    ---         element             ---
    ---     mole bridge (WIP)       ---
    ---                             ---
    -----------------------------------
    - Note: These are case sensitive. -
    -----------------------------------
    ''')
    # Adds a new line.
    print(" ")
  startUp()
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
      periodicTable()
      whatsyourElement()
    elif option== "mole bridge":
      print('''e
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
    elif option == "spook":
      skeleton()
      print("Spooky")
    else:
      print("You did not enter an accepted value.")
   
  # Asks the user what they want to use.
  option = input("What do you want to do? ")
  calcOptions()

  # This program was made to complete chemistry and other mathematical problems with ease.
