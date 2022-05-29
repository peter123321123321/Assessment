"""01_Yes_No_Checker_V3
convert version 3 into a function
based off 01_Yes_No_Checker_V2
"""


def yes_no_checker(question_text):
    while True:

        # Ask user if they've played before and converts to lowercase
        answer = input(question_text).lower()

        # If user inputs 'yes' or 'y' continue with program
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If user inputs 'no' or 'n' show instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If anything else is input show error message
        else:
            print("Error - Please enter Yes or No")


# Main routine
played_before = yes_no_checker("Have you played before: ")

# If users input is no show instructions
if played_before == "No":
    print("Instructions")
