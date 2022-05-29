import random


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
        question = input(f"What is the maori word for {i[0]}").lower()

        # If user is correct print 'correct' anything else print 'incorrect'
        if question == i[1]:
            player_score += 1
            print("Well done, you're correct")
        else:
            print(f"Incorrect, the answer was {i[1]}")

    # Shows player their final score
    if player_score != 7:
        print(f"Your final score is {player_score}/7")
    else:
        print(f"CONGRATULATIONS - You got a perfect score")


# Main Routine
days_of_week()
