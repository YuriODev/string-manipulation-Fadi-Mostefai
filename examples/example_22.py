# Take input for the expression
expression = input("Enter the expression: ")

# Initialize the result with the first number (assumes expression starts with a number)
result = int(expression[0])

# Loop through the expression starting from the first operator
i = 1
while i < len(expression):
    operator = expression[i]
    digit = int(expression[i+1])

    if operator == '+':
        result += digit
    elif operator == '-':
        result -= digit

    i += 2  # Move to the next operator

# Print the final result
print(result)
