# Prompt user to enter a string
input_string = input("Enter a string: ")

# Initialize counters for uppercase, lowercase, and whitespace characters
upper_count = 0
lower_count = 0
space_count = 0

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is uppercase
    if char.isupper():
        upper_count += 1
    # Check if the character is lowercase
    elif char.islower():
        lower_count += 1
    # Check if the character is whitespace
    elif char.isspace():
        space_count += 1

# Print the counts of uppercase characters
print(f"Upper {upper_count}")
