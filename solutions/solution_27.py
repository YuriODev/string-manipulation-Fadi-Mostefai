# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize the encoded string
encoded_string = ""

# Initialize the count of the current character
count = 1

# Iterate through the string
for i in range(1, len(string)):
    # If the current character is the same as the previous character
    if string[i] == string[i - 1]:
        # Increment the count
        count += 1
    else:
        # Append the character and its count to the encoded string
        encoded_string += string[i - 1] + str(count)
        # Reset the count
        count = 1

# Append the last character and its count to the encoded string
encoded_string += string[-1] + str(count)

# Print the encoded string
print(encoded_string)