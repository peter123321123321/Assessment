"""03_Continue_or_quit_V1
Give the user the choice between quizzes or quiting"""

# Ask user if they want to continue or quit
choice = int(input("Which quiz would you like to try\n"
                   "[1] Days of the week in Maori\n"
                   "[2] Maori numbers\n"
                   "[3] Quit\n"))

# If input is 1
if choice == 1:
    print("Maori days of the week")

# If input is 2
elif choice == 2:
    print("Maori numbers")

# If input is 3
elif choice == 3:
    print("quit")

# Else print error message
else:
    print("Please enter a number between 1 and 3")

# Show user input
print(f"You entered {choice}")


# doesnt loop value errors
