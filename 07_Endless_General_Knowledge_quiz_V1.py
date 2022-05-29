import random

general_knowledge = [["Monday", "rahina"], ["Tuesday", "ratu"], ["Wednesday", "raapa"],
                     ["Thursday", "rapare"], ["Friday", "ramere"], ["Saturday", "rahoroi"],
                     ["Sunday", "ratapu"], [1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"],
                     [5, "rima"], [6, "ono"], [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"],
                     ["January", "hanuere"], ["February", "pepuere"], ["March", "maehe"],
                     ["April", "aperira"], ["May", "mei"], ["June", "hune"],
                     ["July", "hurae"], ["August", "akuhata"], ["September", "hepetma"],
                     ["October", "oketopa"], ["November", "noema"], ["December", "tihema"]]
player_score = 0

random.shuffle(general_knowledge)
# Shuffles list
for i in general_knowledge:
    # Asks user for input
    question = input(f"What is the maori word for {i[0]}")

    # If user is correct print 'correct' anything else print 'incorrect'
    if question == i[1]:
        print("correct")
        player_score += 1
    else:
        print(f"Incorrect, the answer was {i[1]}")
        print(f"Well done You answered {player_score} out of {player_score + 1} questions")
