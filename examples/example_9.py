# Take input for the string
input_string = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""

# Iterate through the characters of the input string
for char in input_string:
    # Check if the character is a digit and greater than 5
    if char.isdigit() and int(char) > 5:
        # Divide the digit by 2 and append it to the result
        result += str(int(char) // 2)
    # Check if the character is a digit and odd
    elif char.isdigit() and int(char) % 2 != 0:
        # Append the digit to the result
        result += char

# Print the result
print(result)
