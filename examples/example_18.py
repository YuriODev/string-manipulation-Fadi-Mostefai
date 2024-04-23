# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Prompt the user to enter the substring to replace
substring = input("Enter the substring to replace: ")

# Prompt the user to enter the new substring
new_substring = input("Enter the new substring: ")

# Solution 1: Replace substring without using replace function
# Check if the substring is present in the input string
if substring in input_string:
    result = ""  # Initialize an empty string to store the modified string
    i = 0  # Initialize a counter variable to keep track of the current position in the input string

    # Iterate through the input string until the end of the string with room for the substring
    while i < len(input_string) - len(substring) + 1:
        # Check if the current substring matches the substring to be replaced
        if input_string[i:i + len(substring)] == substring:
            result += new_substring  # Append the new substring to the result string
            i += len(substring)  # Move the counter past the matched substring
        else:
            result += input_string[i]  # Append the current character to the result string
            i += 1  # Move the counter to the next character

    print(result)  # Print the modified string
else:
    print("is impossible")  # Print a message indicating that the substring was not found in the input string

# Solution 2: Replace substring using replace function
if substring in input_string:
    result = input_string.replace(substring, new_substring)
    print(result)
else:
    print("is impossible")
