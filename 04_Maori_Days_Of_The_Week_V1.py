"""04_Maori_Days_Of_The_Week_V1
randomly shuffles a list of questions and asks the user them one at a time
print if they're correct or incorrect and tracks there score
"""


import random

# Puts question and answers in the same list
days_of_the_week = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                    ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                    ["Sunday", "ratapu"]]

# Keeps track of player score and total questions
player_score = 0
total = 0

# Shuffles list
random.shuffle(days_of_the_week)
for i in days_of_the_week:
    total += 1
    if i[1] == "rahina":

        # Ask user for input, if input is correct print correct
        # else print incorrect
        # repeat for each day of the week
        question = input(f"What is the Maori word for {i[0]}")
        if question == "rahina":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "ratu":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "ratu":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "raapa":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "raapa":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "rapare":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "rapare":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "ramere":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "ramere":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "rahoroi":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "rahoroi":
            print("correct")
            player_score += 1
        else:
            print("incorrect")
    if i[1] == "ratapu":
        question = input(f"What is the Maori word for {i[0]}")
        if question == "ratapu":
            print("correct")
            player_score += 1
        else:
            print("incorrect")


# Shows player their final score
print(f"You got {player_score}/{total}")
