import sys

def errorMessage(errorType):
  if errorType == "divzero":
    sys.stderr.write("Error: cannot divide by zero.\n")
  elif errorType == "notacc":
    sys.stderr.write("Error: You did not enter an accepted value.\n")

    