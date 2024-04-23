# Prompt the user for a character
character = input("Enter a character: ")

# Prompt the user for a string
string = input("Enter a string: ")

# Change the specified character to uppercase
output = string.replace(character, character.upper())

# Output the modified string
print(output)
