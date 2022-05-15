import random

days_of_the_week = [["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"], ["Friday"], ["Saturday"], ["Sunday"]]
player_score = 0
total = 0

# Shuffles list
random.shuffle(days_of_the_week)
while total < 7:

    # Ask user day of the week
    # If user is correct print correct and add 1 to their score and total

    question = input(f"What is the maori name for {days_of_the_week[0][0]}")
    if question == "rahina":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

    question = input(f"What is the maori name for {days_of_the_week[1][0]}")
    if question == "ratu":
        print("correct")
        player_score += 1
        total += 1

    else:
        print("Incorrect")
        total += 1
    question = input(f"What is the maori name for {days_of_the_week[2][0]}")
    if question == "raapa":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

    question = input(f"What is the maori name for {days_of_the_week[3][0]}")
    if question == "rapare":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

    question = input(f"What is the maori name for {days_of_the_week[4][0]}")
    if question == "ramere":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

    question = input(f"What is the maori name for {days_of_the_week[5][0]}")
    if question == "rahoroi":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

    question = input(f"What is the maori name for {days_of_the_week[6][0]}")
    if question == "ratapu":
        print("correct")
        player_score += 1
        total += 1
    else:
        print("Incorrect")
        total += 1

# Shows player their final score
print(f"You got {player_score}/{total}")
