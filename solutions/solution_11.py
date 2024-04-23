# Prompt the user to enter a string.
input_string = input("Enter a string: ")

# Count the number of words in the string.
number_of_words = input_string.count(" ") + 1

# Find the last word in the string depending on the number of words.
if number_of_words == 1:
    last_word = input_string
else:
    last_word = ""
    position = -1
    space_found = False

    while not space_found:
        if input_string[position] == " ":
            space_found = True
        else:
            last_word = input_string[position] + last_word
            position -= 1

# Output the last word in the string.
print(last_word)
