"""06_Statement_formatter_v1
formats text
"""

# symbol around text
symbol = "*"
# text
text = "hello world"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

# output
print(top_bottom)
print(formatted_text)
print(top_bottom)
