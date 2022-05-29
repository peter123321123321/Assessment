"""Final Version Maori Quiz
This is the final version of my quiz including all finished components
"""

# Functions go here
import random


def yes_no_checker(question_text):
    # Loops question
    while True:

        # Ask user if they've played before and converts to lowercase
        answer = input(question_text).lower()

        # If user inputs 'yes' or 'y' return Yes
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If user inputs 'no' or 'n' Return No
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If anything else is input show error message
        else:
            print("Error - Please enter Yes or No")


def instructions():
    print()
    print(formatter("=", "How to play"))
    print("_" * 75)
    print("You will be offered a choice between two quizzes:")
    print("\t[1] Maori days of the week quiz")
    print("\t[2] Maori numbers quiz")
    print()
    print("You will then be asked a series of questions about the chosen topic")
    print("At the end of the game you will be shown your score")
    print("Good luck and happy learning!")
    print("_" * 75)


def continue_or_quit(continue_text):
    # Loop question
    while True:
        # Show user options
        print()
        print("[1] Redirects to Maori days of the week quiz\n"
              "[2] Redirects to Maori numbers quiz\n"
              "[3] Quit the quiz")
        try:
            # Ask user if they want to continue or quit
            choice = int(input(continue_text))

            # If input is 1 return 1
            if choice == 1:
                return 1

            # If input is 2 return 2
            elif choice == 2:
                return 2

            # If input is 3 print goodbye message and exit
            elif choice == 3:
                print()
                print(formatter("=", "Thanks for learning with us. We hope To see you next time"))
                exit()

            # If anything else print error message
            else:
                print("Error - Please enter a number between 1 and 3")
        # If error print error message
        except ValueError:
            print("Error - Please enter a number between 1 and 3")


def days_of_week():

    # Puts question and answers in the same list
    days_of_the_week = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                        ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                        ["Sunday", "ratapu"]]

    # Keeps track of player score
    player_score = 0
    # Shuffles list
    random.shuffle(days_of_the_week)

    for i in days_of_the_week:
        # Ask user for input
        print()
        question = input(f"What is the Maori word for {i[0]} ").lower()

        # If user is correct print 'correct' +1 player score anything else print 'incorrect'
        if question == i[1]:
            print(formatter("!", "Well done, you're correct"))
            player_score += 1
        else:
            print(formatter("!", f"Incorrect, the answer is {i[1]}"))

    # If below 7 Shows player their final score else print perfect score message
    print()
    if player_score != 7:
        print(f"Your final score is {player_score}/7")
    else:
        print(formatter("!", f"CONGRATULATIONS - You got a perfect score"))


def maori_numbers():
    # Puts question and answers in the same list
    num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
                [8, "waru"], [9, "iwa"], [10, "tekau"]]

    # Keeps track of player score
    player_score = 0

    # Shuffle list
    random.shuffle(num_list)
    for i in num_list:
        # Ask user for input
        print()
        attempt = input(f"What is the Maori word for {i[0]} ").lower()

        if attempt == i[1]:
            # If user is correct print 'correct' +1 player score anything else print 'incorrect'
            player_score += 1
            print(formatter("!", "Well done, you're correct"))
        else:
            print(formatter("!", f"Incorrect, the answer was {i[1]}"))

    # If below 7 Shows player their final score else print perfect score message
    print()
    if player_score != 10:
        print(f"Your final score is {player_score}/10")
    else:
        print(formatter("!", f"CONGRATULATIONS - You got a perfect score"))


def formatter(symbol, text):
    # Formats text
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("=", "Welcome to the Maori quizzes"))
# Ask user if they've played before
played_before = yes_no_checker("Have you played before: ")

# If users input is No show instructions
if played_before == "No":
    instructions()

# :oop question
while True:
    # If input 1 redirect to days of week if input 2 redirect to maori numbers
    quiz_continue = continue_or_quit("Please choose one of the above options and press Enter ")
    if quiz_continue == 1:
        days_of_week()
    elif quiz_continue == 2:
        maori_numbers()
