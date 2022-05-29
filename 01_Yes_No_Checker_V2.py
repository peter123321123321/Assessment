"""01_Yes_No_Checker_V2
simplifies input by converting it to lowercase.
also allows for y or n input
based off 01_Yes_No_Checker_V1
"""

# Ask user if they've played before and converts to lowercase
played_before = input("Have you played before").lower()

# If user inputs 'yes' or 'y' continue with program
if played_before == "yes" or played_before == "y":
    print("Continue program")

# If user inputs 'no' or 'n' show instructions
elif played_before == "no" or played_before == "n":
    print("Show instructions")

# If anything else is input show error message
else:
    print("Error - Please enter yes or no")
