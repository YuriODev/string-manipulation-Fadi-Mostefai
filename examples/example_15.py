# Get input from the user
n = int(input("Enter the number: "))

# Initialize the total variable
total = 0
# Initialize the output string
output = ""

# Check if the input is valid
if n >= 2:
    # Iterate from 1 to n-1
    for i in range(1, n):
        # Calculate the sum of i*(i+1) and add it to the total
        total += i * (i + 1)
        # Build the output string
        output += f"{i}*{i + 1}+"

    # Remove the last '+' from the output string
    output = output[:-1]
    # Add the total to the output string
    output += f"={total}"
    # Print the final output
    print(output)
else:
    # Print an error message if the input is invalid
    print("Invalid input")
