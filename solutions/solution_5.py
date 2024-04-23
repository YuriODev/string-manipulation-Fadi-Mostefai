# Prompt the user to enter the first string
first_word = input("Enter the first string: ")

# Prompt the user to enter the second string
second_word = input("Enter the second string: ")

# Check if the first string is a substring of the second string
output = first_word in second_word

# Output the result
print("Yes" if output else "No")
