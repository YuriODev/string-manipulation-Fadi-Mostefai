# Input string
input_string = input("Enter a string: ")

# Variable to store the encoded result
encoded_string = ""

# Initialize count and previous character
count = 1
previous_char = input_string[0]

# Iterate over the string starting from the second character
for char in input_string[1:]:
    if char == previous_char:
        count += 1
    else:
        # Append the count and character to the result string if count is more than 1
        if count > 1:
            encoded_string += str(count)
        encoded_string += previous_char
        # Reset the count and update previous character
        previous_char = char
        count = 1

# Handle the last run
if count > 1:
    encoded_string += str(count)
encoded_string += previous_char

# Print the encoded string
print(encoded_string)
