"""02_instructions_V1
instructions function
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
            print("Error - Please enter yes or no")


def instructions():
    print("=== How to play ===")
    print()
    print("Instructions go here")
    print()
    print("Program continues")
    print()


# Main routine
played_before = yes_no_checker("Have you played before: ")

# If users input is no show instructions
if played_before == "No":
    instructions()
else:
    print("Program continues")
