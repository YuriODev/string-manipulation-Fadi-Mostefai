# Prompt user to enter an IP address
ip = input("Enter an IP address: ")

# Initialise 
part = ''  # Variable to store each part of the IP address
dot_count = 0  # Counter for the number of dots in the IP address
valid = True  # Flag to indicate if the IP address is valid
part_count = 0  # Counter for the number of parts in the IP address

# Iterate over each character in the IP address
for i in range(len(ip)):
    char = ip[i]
    if char.isdigit():
        # Build the part string
        part += char
    elif char == '.':
        if part == '' or int(part) > 255 or i == 0 or (i > 0 and not ip[i-1].isdigit()):
            # If the part is empty, greater than 255, or not preceded by a digit, the IP address is invalid
            valid = False
            break
        part_count += 1
        # Reset part on dot
        part = ''
        dot_count += 1
    else:
        # If a non-digit character is encountered, the IP address is invalid
        valid = False
        break

# Check the last part after the last dot or if no dots were found
if valid and part != '' and int(part) <= 255:
    part_count += 1
else:
    valid = False

# Must have exactly four parts and three dots to be valid
if part_count != 4 or dot_count != 3:
    valid = False

# Print the result for each IP
print("Yes" if valid else "No")