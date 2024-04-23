# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize the counters for lowercase and uppercase letters
lowercase_count = 0
uppercase_count = 0
total_char_count = 0

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a letter
    if char.isalpha():
        total_char_count += 1
        # Check if the character is lowercase
        if char.lower() == char:
            lowercase_count += 1
        # Check if the character is uppercase
        elif char.upper() == char:
            uppercase_count += 1

# Check if there are no letters in the input string
if total_char_count == 0:
    print("0.00\n0.00")
else:
    # Calculate the percentage of lowercase and uppercase letters
    lowercase_percentage = (lowercase_count / total_char_count) * 100
    uppercase_percentage = (uppercase_count / total_char_count) * 100

    # Print the percentages of lowercase and uppercase letters
    print(f"{lowercase_percentage:.2f}\n{uppercase_percentage:.2f}")
