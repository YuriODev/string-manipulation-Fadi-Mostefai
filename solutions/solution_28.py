# Prompt the user to enter a string
string = input("Enter a string: ")

# Count the number of spaces in the string
count = 0

for char in string:
    if char == " ":
        count += 1

# Check the number of spaces in the string
if count == 0:
    word_count = 1
else:
    word_count = count + 1

# Print the number of words in the string
print(word_count)
