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
    while True:
        print()
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
                print()
                print(formatter("=", "Thanks for learning with us. We hope To see you next time"))
                exit()

            # else input is not yes or no print error message
            else:
                print("Error - Please enter a number between 1 and 3")
        except ValueError:
            print("Error - Please enter a number between 1 and 3")


def days_of_week():

    # Puts question and answers in the same list
    days_of_the_week = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                        ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                        ["Sunday", "ratapu"]]

    # Keeps track of player score and total questions
    player_score = 0
    # Shuffles list
    random.shuffle(days_of_the_week)

    for i in days_of_the_week:
        # Asks user for input
        print()
        question = input(f"What is the maori name for {i[0]}")

        # If user is correct print 'correct' anything else print 'incorrect'
        if question == i[1]:
            print(formatter("!", "correct"))
            player_score += 1
        else:
            print(formatter("!", f"Incorrect, the answer was {i[1]}"))

    # Shows player their final score
    print()
    if player_score != 7:
        print(f"Your final score is {player_score}/7")
    else:
        print(formatter("!", f"CONGRATULATIONS - You got a perfect score"))


def maori_numbers():
    num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
                [8, "waru"], [9, "iwa"], [10, "tekau"]]

    player_score = 0
    random.shuffle(num_list)
    for i in num_list:
        print()
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == i[1]:
            player_score += 1
            print(formatter("!", "Well done, your correct"))
        else:
            print(formatter("!", f"Incorrect, the answer was {i[1]}"))

    print()
    if player_score != 10:
        print(f"Your final score is {player_score}/10")
    else:
        print(formatter("!", f"CONGRATULATIONS - You got a perfect score"))


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("=", "Welcome to the Maori quizzes"))
played_before = yes_no_checker("Have you played before: ")

# If users input is no show instructions
if played_before == "No":
    instructions()

while True:
    quiz_continue = continue_or_quit("Please choose on of the above options and press Enter")
    if quiz_continue == 1:
        days_of_week()
    elif quiz_continue == 2:
        maori_numbers()
