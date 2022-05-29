""" 05_Maori_Numbers_V1
randomly generate shuffled numbers and asks user
the maori word for it until all numbers have been done
"""

import random

# List of numbers
num_list = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# Randomly shuffle questions so its different each time
random.shuffle(num_list)
for i in num_list:
    # Ask user for input, if input is correct print correct
    # else print incorrect
    # repeat for Maori number
    if i[0] == 1:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "tahi":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 2:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "rua":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 3:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "toru":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 4:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "wha":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 5:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "rima":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 6:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "ono":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 7:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "whitu":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 8:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "waru":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 9:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "iwa":
            print("Correct")
        else:
            print("Incorrect")

    if i[0] == 10:
        attempt = input(f"What is the Maori word for {i[0]}")
        if attempt == "tekau":
            print("Correct")
        else:
            print("Incorrect")
