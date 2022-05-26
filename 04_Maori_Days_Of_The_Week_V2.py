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

    # Asks user for input
    question = input(f"What is the maori word for {i[0]}")

    # If user is correct print 'correct' anything else print 'incorrect'
    if question == i[1]:
        print("correct")
        player_score += 1
    else:
        print("Incorrect")

# Shows player their final score
print(f"You got {player_score}/{total}")
