""" 05_Maori_Numbers_V3
converts 05_Maori_Numbers_V2 into a function
and adds small changes that make it easier for user to play quiz
"""
import random


def maori_numbers():
    # puts question and answer in same list
    num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
                [8, "waru"], [9, "iwa"], [10, "tekau"]]

    # players score
    player_score = 0
    # Shuffles list
    random.shuffle(num_list)
    for i in num_list:
        # ask user for input
        attempt = input(f"What is the Maori word for {i[0]}").lower()
        if attempt == i[1]:
            # if users correct +1 to score then print correct
            player_score += 1
            print(f"Correct")
        else:
            # else print incorrect
            print(f"Incorrect, the answer was {i[1]}")

    # ifp player score below 10 print there score else print congratulations message
    if player_score != 10:
        print(f"Your final score is {player_score}/10")
    else:
        print(f"CONGRATULATIONS - You got a perfect score")


# Main routine
maori_numbers()
