def continue_or_quit():
    while True:
        print("[1] Days of the week in Maori\n"
              "[2] Numbers in Maori\n"
              "[3] Leave the quiz")
        # Ask user if they want to continue or quit
        choice = int(input("What would you like to do"))

        # If input is 1
        if choice == 1:
            print("Goodbye")
            exit()

        # If input is 2
        elif choice == 2:
            print("days_of_the_week()")

        # If input is 3
        elif choice == 3:
            print("maori_numbers")
        # else input is not yes or no print error message
        else:
            print("Error - Please enter a number between 1 and 3")


# Main Routine
continue_or_quit()
