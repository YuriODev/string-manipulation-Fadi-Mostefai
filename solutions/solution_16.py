# ## Exercise 16: ASCII Range Printer - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

# **Problem:** Given two characters, print all ASCII characters that lie between them inclusively.

# ### Input:
# - Two characters, each on a separate line.

# ### Output:
# - A string starting with the first and ending with the second input character, including all characters in between.

# ### Examples:

# | No. | Inputs | Outputs    |
# | --- | ------ | ---------- |
# | 1   | A<br>F | ABCDEF     |
# | 2   | 0<br>9 | 0123456789 |

# Prompt the user to enter two characters.
first_char = input("Enter the first character: ")
second_char = input("Enter the second character: ")

# Define the variable to store the ASCII characters.
ascii_characters = ""

# Iterate through the ASCII range of the characters.
for char in range(ord(first_char), ord(second_char) + 1):
    ascii_characters += chr(char)

# Print the ASCII characters.
print(ascii_characters)
