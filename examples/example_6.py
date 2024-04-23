# Take input for the symbol
symbol = input("Enter a symbol: ")

# Solution 1

# Check if the symbol is a digit
if "0" <= symbol <= "9":
    print("Yes")
else:
    print("No")

# Solution 2

digits = "0123456789"

# Check if the symbol is a digit
if symbol in digits:
    print("Yes")
else:
    print("No")
