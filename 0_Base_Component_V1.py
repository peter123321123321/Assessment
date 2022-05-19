""""""

# Functions go here
import random


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
    print("Program continues\n")


def continue_or_quit():
    while True:
        print("[1] Days of the week in Maori\n"
              "[2] Numbers in Maori\n"
              "[3] Leave the quiz")
        # Ask user if they want to continue or quit
        choice = int(input("What would you like to try"))

        # If input is 1
        if choice == 1:
            days_of_week()
        # If input is 2
        elif choice == 2:
            print("maori numbers")

        # If input is 3
        elif choice == 3:
            print("Goodbye")
            exit()

        # else input is not yes or no print error message
        else:
            print("Error - Please enter a number between 1 and 3")


def days_of_week():

    # Puts question and answers in the same list
    days_of_the_week = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                        ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                        ["Sunday", "ratapu"]]

    # Keeps track of player score and total questions
    player_score = 0
    total = 0

    # Shuffles list
    total += 1
    random.shuffle(days_of_the_week)
    for i in days_of_the_week:

        # Asks user for input
        question = input(f"What is the maori name for {i[0]}")

        # If user is correct print 'correct' anything else print 'incorrect'
        if question == i[1]:
            print("correct")
            player_score += 1
        else:
            print("Incorrect")

    # Shows player their final score
    print(f"You got {player_score}/{total}")


# Main routine
played_before = yes_no_checker("Have you played before: \n")

# If users input is no show instructions
if played_before == "No":
    instructions()

quiz_continue = input("Would you like to try a quiz or quit\n"
                      "Enter to continue or 'X' to quit\n").upper()
if quiz_continue == "":
    continue_or_quit()
elif quiz_continue == "X":
    print("Goodbye")
    exit()

play_again = input("Would you like to play again\n"
                   "Enter to continue or 'X' to quit")
if play_again == "":
    continue_or_quit()

print("goodbye")
