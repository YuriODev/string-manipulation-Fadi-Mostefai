# Prompt the user to enter a string of digits
number = input("Enter a string of digits: ")

# Declare a variable to store the sum of the digits
sum_of_digits = 0

# Iterate through the number
for char in number:
    # Convert the current character to an integer and add it to the sum
    if char.isdigit():
        sum_of_digits += int(char)

# Print the sum of the digits
print(sum_of_digits)
