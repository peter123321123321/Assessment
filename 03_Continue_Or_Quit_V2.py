# Ask user if they want to continue or quit
choice = input("Would you like to try a quiz or quit\n"
               "<Enter> to continue or 'X' to quit").lower()

# If input is X quit program
if choice == "X":
    print("quit program")

# If input is yes continue program
elif choice == "yes" or choice == "y":
    print("continue program")

else:
    print("Please enter yes or X")

# Show user input
print(f"You entered {choice}")

# doesnt loop
