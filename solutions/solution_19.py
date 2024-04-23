# Prompt the user to enter a number
number = input("Enter a number: ")

# Declare a variable to store the first decimal digit
first_decimal_digit = None

# Iterate through the number
for i in range(len(number)):
    # Check if the current character is a decimal point
    if number[i] == ".":
        # Get the first decimal digit
        first_decimal_digit = number[i + 1]
        break

# Print the first decimal digit
if first_decimal_digit:
    print(first_decimal_digit)
else:
    print("0")
