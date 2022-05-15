""""""

# Functions go here


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


def instructions():
    print("=== How to play ===")
    print()
    print("Instructions go here")
    print()
    print("Program continues")
    print()


def continue_or_quit(query):
    while True:
        # Ask user if they want to continue or quit
        choice = input(query).lower()

        # If input is X quit program
        if choice == "x":
            return "X"

        # If input is yes continue program
        elif choice == "yes" or choice == "y":
            return "Yes"
        # else input is not yes or no print error message
        else:
            print("Error - Please enter Yes or X")
            print()


# Main routine
played_before = yes_no_checker("Have you played before: ")
print()

# If users input is no show instructions
if played_before == "No":
    print("Instructions")

quiz_continue = continue_or_quit("Would you like to try the quiz or quit\n"
                                 "Yes to continue or 'X' to quit")
print()

if quiz_continue == "Yes":
    print("program continues")
