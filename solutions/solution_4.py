# Prompt the user to enter the first word
first_word = input("Enter the first word: ")

# Prompt the user to enter the second word
second_word = input("Enter the second word: ")

# Check if the first word starts with the same letter the second word does
output = first_word[0] == second_word[0]

# Output the result
print(output)
