import random


def maori_numbers():
    num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
                [8, "waru"], [9, "iwa"], [10, "tekau"]]

    player_score = 0
    random.shuffle(num_list)
    for i in num_list:
        attempt = input(f"What is the Maori word for {i[0]}").lower()
        if attempt == i[1]:
            player_score += 1
            print(f"Correct")
        else:
            print(f"Incorrect, the answer was {i[1]}")

    if player_score != 10:
        print(f"Your final score is {player_score}/10")
    else:
        print(f"CONGRATULATIONS - You got a perfect score")


# Main routine
maori_numbers()
