# Prompt the user to enter the shift amount
shift = int(input("Enter the shift amount: "))

# Prompt the user to enter the string to encrypt
string = input("Enter the string to encrypt: ")

# Initialize the encrypted string
encrypted_string = ""

# Iterate through the string
for char in string:
    # Check if the character is a letter
    if char.isalpha():
        # Get the ASCII value of the character
        ascii_value = ord(char)
        # Check if the character is uppercase
        if char.isupper():
            # Encrypt the character
            encrypted_char = chr((ascii_value - 65 + shift) % 26 + 65)
        else:
            # Encrypt the character
            encrypted_char = chr((ascii_value - 97 + shift) % 26 + 97)
    else:
        # If the character is not a letter, keep it as it is
        encrypted_char = char
    # Append the encrypted character to the encrypted string
    encrypted_string += encrypted_char

# Print the encrypted string
print(encrypted_string)
