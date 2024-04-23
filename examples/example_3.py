# Take input for the string and the prefix to check
input_string = input("Enter the string: ")
prefix = input("Enter the prefix: ")

# Check if the string starts with the given prefix
starts_with_prefix = input_string.startswith(prefix)

# Print the result
print(starts_with_prefix)
