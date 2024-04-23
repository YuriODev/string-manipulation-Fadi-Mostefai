# Take input for the string
input_string = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""

# Iterate through the characters of the input string
for char in input_string:
    # Check if the character is not a digit
    if not char.isdigit():
        # Append the character to the result
        result += char

# Print the result
print(result)
