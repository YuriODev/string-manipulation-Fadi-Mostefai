# Take input for the expression
expression = input("Enter the expression: ")

# Initialize counter for open parentheses
balance = 0
is_balanced = True

# Iterate through each character in the expression
for char in expression:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
    # If at any point there are more closing parentheses, it's unbalanced
    if balance < 0:
        is_balanced = False
        break

# If there are open parentheses left unmatched, it's unbalanced
if balance != 0:
    is_balanced = False

# Output result
print("True" if is_balanced else "False")
