# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize an empty string to store unique characters
unique_chars = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is not already in the unique_chars string and is not a whitespace character
    if char not in unique_chars and not char.isspace():
        # If the character is unique and not a whitespace character, add it to the unique_chars string
        unique_chars += char

# Print the resulting unique_chars string
print(unique_chars)
