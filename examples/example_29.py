# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize a string to store the most frequent letters
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Initialize a string to store the count of each letter
letter_count = ""

# Count the frequency of each letter in the input string
# Iterate through each letter in the 'letters' string
for letter in letters:
    # Initialize a counter for the current letter
    current_letter_counter = 0

    # Iterate through each character in the input string, converted to uppercase
    for char in input_string.upper():
        # Check if the character matches the current letter
        if char.upper() == letter:
            # Increment the counter for the current letter
            current_letter_counter += 1

    # Append the count of the current letter to the 'letter_count' string
    letter_count += str(current_letter_counter)

# Find the maximum frequency of any letter
max_frequency = 0
# Iterate through each count in the 'letter_count' string
for count in letter_count:
    # Check if the current count is greater than the current maximum frequency
    if int(count) > max_frequency:
        # Update the maximum frequency
        max_frequency = int(count)

# Print the letters with the maximum frequency
# Iterate through each index in the 'letters' string
for i in range(len(letters)):
    # Check if the count at the current index is equal to the maximum frequency
    if int(letter_count[i]) == max_frequency:
        # Print the letter at the current index, without a newline character
        print(letters[i], end='')

print()

# Print the maximum frequency
print(max_frequency)
