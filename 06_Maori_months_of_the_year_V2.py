import random


def months_of_year():

    # Puts question and answers in the same list
    months_of_the_year = [["January", "hanuere"], ["February", "pepuere"], ["March", "maehe"],
                          ["April", "aperira"], ["May", "mei"], ["June", "hune"],
                          ["July", "hurae"], ["August", "akuhata"], ["September", "hepetma"],
                          ["October", "oketopa"], ["November", "noema"], ["December", "tihema"]]

    player_score = 0
    random.shuffle(months_of_the_year)
    for i in months_of_the_year:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == i[1]:
            player_score += 1
            print("Well done, your correct")
        else:
            print(f"Incorrect, the answer was {i[1]}")

    print()
    if player_score != 12:
        print(f"Your final score is {player_score}/12")
    else:
        print(f"CONGRATULATIONS - You got a perfect score")


# Main Routine
months_of_year()
