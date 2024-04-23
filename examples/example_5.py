input_string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase
input_string = input_string.replace(" ", "").lower()

# Check if the string is a palindrome
is_palindrome = input_string == input_string[::-1]

# Print the result
print(is_palindrome)
