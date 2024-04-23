# Prompt the user to enter a string.
user_input = input("Enter a string: ")

# Check length of the string
if len(user_input) == 1:
    # Output the string as it is
    output = user_input
elif len(user_input) == 2:
    # Swap the two characters
    output = user_input[::-1]
else:
    # Swap the first and last characters of the string
    output = user_input[-1] + user_input[1:-1] + user_input[0]

# Output the modified string
print(output)
