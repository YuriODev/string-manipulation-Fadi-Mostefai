# Take input for the string
input_string = input("Enter a string: ")

# Find the index of the first space character
first_space_index = input_string.find(" ")

# Check if there is a space in the string
if first_space_index != -1:
    # Extract the first word from the string
    first_word = input_string[:first_space_index]
else:
    # If there is no space, the first word is the whole string
    first_word = input_string

# Print the first word
print(first_word)
