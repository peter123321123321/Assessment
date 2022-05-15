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


# Main Routine
quiz_continue = continue_or_quit("Which quiz would you like to try\n"
                                 "[1] "
                                 "[2]")
if quiz_continue == "Yes":
    print("program continues")
