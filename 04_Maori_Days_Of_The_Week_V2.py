"""04_Maori_Days_Of_The_Week_V2
optimize and simplify 04_Maori_Days_Of_The_Week_V1
e.g. changing it so instead of adding +1 everytime your correct
it adds +1 regardless and -1 if you get it wrong
"""


import random

# Puts question and answers in the same list
days_of_the_week = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                    ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                    ["Sunday", "ratapu"]]

# Keeps track of player score and total questions
total = 0
player_score = 0
# Shuffles list
random.shuffle(days_of_the_week)
for i in days_of_the_week:
    total += 1
    question = input(f"What is the Maori word for {i[0]}").lower()
    if i[0] == "Monday" and question == "rahina":
        print("correct")

    elif i[0] == "Tuesday" and question == "ratu":
        print("correct")

    elif i[0] == "Wednesday" and question == "raapa":
        print("correct")

    elif i[0] == "Thursday" and question == "rapare":
        print("correct")

    elif i[0] == "Friday" and question == "ramere":
        print("correct")

    elif i[0] == "Saturday" and question == "rahoroi":
        print("correct")

    elif i[0] == "Sunday" and question == "ratapu":
        print("correct")

    else:
        print("incorrect")
        player_score -= 1

    player_score += 1

# Shows player their final score
print(f"You got {player_score}/{total}")
