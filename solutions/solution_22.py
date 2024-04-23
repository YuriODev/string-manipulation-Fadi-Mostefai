# Prompt the user to enter a string
string = input("Enter a string: ")

# Characters to remove from the string
to_remove = " !@#$%^&*()_+[]{}|;:,.<>?/"

# Remove all the wrong characters in the string
for char in to_remove:
    string = string.replace(char, "")

# Check if the string is a palindrome
if string.lower() == string[::-1].lower():
    print("Yes")
else:
    print("No")
