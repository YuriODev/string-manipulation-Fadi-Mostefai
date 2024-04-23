# Prompt the user to enter a Windows file path.
path = input("Enter a Windows file path: ")

letter = path[0]

print(letter + ":")

for char in path[3:]:
    # If the character is a backslash, print a newline character.
    output = "\n" if char == "\\" else char

    print(output, end="")

print()
