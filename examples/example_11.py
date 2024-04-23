# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Check if the input string is empty
if len(input_string) == 0:
    print(0)  # If the string is empty, print 0
else:
    # Initialize the word count to 1 since the first word is not preceded by a space
    word_count = 1 
    # Iterate over each character in the input string, stripping any leading or trailing whitespace
    for char in input_string.strip():
        if char == " ":
            # Increment the word count for each space character
            word_count += 1

    print(word_count)  # Print the final word count
