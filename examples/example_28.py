# Prompt the user to enter an expression
expression = input("Enter the expression: ")

# Initialize the result variable
result = 0

# Initialize the first number
number = 0

# Initialize the sign to positive
sign = 1

# Iterate through each character in the expression
for char in expression:
    # Check if the character is a digit
    if char.isdigit():
        # If it is a digit, update the number variable
        number = number * 10 + int(char)
    else:
        # If it is not a digit, perform the calculation based on the sign and number
        result += sign * number
        number = 0

        # Update the sign based on the character
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1

# Add the last number to the result
result += sign * number

# Output the result
print(result)
