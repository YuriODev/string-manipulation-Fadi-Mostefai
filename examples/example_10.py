# Prompt the user to enter the first number
start = int(input("Enter the first number: (> 32)"))

# Prompt the user to enter the second number
end = int(input("Enter the second number: (< 127)"))

# Iterate over the range from start to end (inclusive)
for i in range(start, end + 1):
    # Print the character representation of i and its corresponding integer value
    print(chr(i), i)
