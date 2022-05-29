"""component 5 - statement formatter v3
"""


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
print(formatter("-", "Welcome to Maori quizzes"))
print()
print(formatter("!", "You are correct"))
print()
print(formatter("=", "Goodbye, thanks for learning with us"))
