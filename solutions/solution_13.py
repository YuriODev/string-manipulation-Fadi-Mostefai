# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize an empty string to store the digits
digits = ""

# Iterate through the characters in the input string
for char in string:
    # Check if the character is a digit
    if char.isdigit():
        # Append the digit to the 'digits' string
        digits += char

# Print the extracted digits
print(digits)
