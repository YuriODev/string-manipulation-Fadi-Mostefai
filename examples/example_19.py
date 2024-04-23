# Take input for the binary string
binary_string = input("Enter the binary string: ")

# Initialize variables to track the longest zero sequence and current zero count
longest_sequence = 0
current_count = 0

# Iterate over each character in the string
for char in binary_string:
    if char == '0':
        current_count += 1
    else:
        if current_count > longest_sequence:
            longest_sequence = current_count
        current_count = 0

# Check the last sequence in case the string ends with '0'
if current_count > longest_sequence:
    longest_sequence = current_count

# Print the longest sequence of zeros
print(longest_sequence)
