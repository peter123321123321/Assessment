def continue_or_quit(query):
    while True:
        # Ask user if they want to continue or quit
        choice = int(input(query))

        # If input is 1
        if choice == 1:
            return 1

        # If input is 2
        elif choice == 2:
            return 2

        # If input is 3
        elif choice == 3:
            return 3
        # else input is not yes or no print error message
        else:
            print("Error - Please enter a number between 1 and 3")
            print()


# Main Routine
quiz_continue = continue_or_quit("Which quiz would you like to try\n"
                                 "[1] Days of the week in Maori\n"
                                 "[2] Maori numbers\n"
                                 "[3] Quit\n")
if quiz_continue == 1:
    print("Days of the week in Maori")
elif quiz_continue == 2:
    print("Maori numbers")
elif quiz_continue == 3:
    print("Exit program")
