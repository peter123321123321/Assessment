def continue_or_quit(continue_text):
    while True:
        print("[1] Redirects to Maori days of the week quiz\n"
              "[2] Redirects to Maori numbers quiz\n"
              "[3] Quit the quiz")
        # Ask user if they want to continue or quit
        try:
            choice = int(input(continue_text))

            # If input is 1
            if choice == 1:
                return 1

            # If input is 2
            elif choice == 2:
                return 2

            # If input is 3
            elif choice == 3:
                print("Thanks for learning with us. We hope To see you next time")
                exit()

            # else input is not yes or no print error message
            else:
                print("Error - Please enter a number between 1 and 3")
        except ValueError:
            print("Error - Please enter a number between 1 and 3")


# Main Routine
choose_quiz = continue_or_quit("Please choose from on of the above options")
if choose_quiz == 1:
    print("Redirect to Maori days of the week quiz")
elif choose_quiz == 1:
    print("Redirect to Maori numbers quiz")
