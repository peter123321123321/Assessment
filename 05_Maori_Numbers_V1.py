import random

number = random.randint(1, 11)
for i in range(number):
    attempt = input(f"What is the Maori word for {i}")
    if i == 1:
        if attempt == "tahi":
            print("Correct")
        else:
            print("Incorrect")

    if i == 2:
        if attempt == "rua":
            print("Correct")
        else:
            print("Incorrect")

    if i == 3:
        if attempt == "toro":
            print("Correct")
        else:
            print("Incorrect")

    if i == 4:
        if attempt == "wha":
            print("Correct")
        else:
            print("Incorrect")

    if i == 5:
        if attempt == "rima":
            print("Correct")
        else:
            print("Incorrect")

    if i == 6:
        if attempt == "ono":
            print("Correct")
        else:
            print("Incorrect")

    if i == 7:
        if attempt == "whitu":
            print("Correct")
        else:
            print("Incorrect")

    if i == 8:
        if attempt == "waru":
            print("Correct")
        else:
            print("Incorrect")

    if i == 9:
        if attempt == "iwa":
            print("Correct")
        else:
            print("Incorrect")

    if i == 10:
        if attempt == "tekau":
            print("Correct")
        else:
            print("Incorrect")
