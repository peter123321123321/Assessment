"""01_Yes_No_Checker_V1
"""

# Ask user if they've played before
played_before = input("Have you played before")

# If user inputs 'yes' continue with program
if played_before == "yes":
    print("Continue program")

# If user inputs 'no' show instructions
elif played_before == "no":
    print("Show instructions")

# If anything else is input show error message
else:
    print("Error - Please enter yes or no")
