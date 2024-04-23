# Prompt the user to enter a string
string = input("Enter a string: ")

# Iterate through the string and multiply the digits
result = 1

for char in string:
    if char.isdigit():
        result *= int(char)

# Print the result
print(result)
