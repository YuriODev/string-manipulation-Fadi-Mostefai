# Prompt the user to enter a simple arithmetic expression.
expression = input("Enter a simple arithmetic expression: ")

# Define the variables to store the numbers and the operator.
number1 = operator = number2 = ""

# Iterate through the expression.
for char in expression:
    # If the character is a digit, append it to the first number.
    if char.isdigit():
        if operator == "":
            number1 += char
        else:
            number2 += char
    # If the character is an operator, store it.
    else:
        operator = char

# Convert the numbers to integers.
number1 = int(number1)
number2 = int(number2)

# Perform the operation based on the operator.
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
else:
    result = number1 * number2

# Print the result.
print(result)
