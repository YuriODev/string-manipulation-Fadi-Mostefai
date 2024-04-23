input_string = input("Enter a string: ")

# Ensure the input string has at least 2 characters
if len(input_string) >= 2:
    # Extract the last two characters
    last_two = input_string[-2:]
    # Print the last two characters repeated 5 times
    print(last_two * 5)
