n = input("Enter the number: ")

# Check if the number has more than one digit
if len(n) > 1:
    # Swap the first and last digits
    reversed_number = n[-1] + n[1:-1] + n[0]
else:
    # If the number has only one digit, the reversed number is the same
    reversed_number = n

# Print the reversed number
print(reversed_number)
