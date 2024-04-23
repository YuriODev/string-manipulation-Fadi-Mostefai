# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterate over each character in the input string
for char in input_string:
    # Check if the character is a letter
    if char.isalpha():
        letter_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1

# Print the count of letters and digits
print(f"Letters {letter_count}")
print(f"Digits {digit_count}")
