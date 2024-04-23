# Input encrypted text
text = input("Enter encrypted text: ")

# Determine the number of letters 'k' in the longest word
k = 0
current_length = 0
max_length = 0

for char in text:
    if char.isalpha():
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_length = 0

if current_length > max_length:
    max_length = current_length

k = max_length

# Decrypt the text directly in the loop
decrypted_text = ''
for char in text:
    if 'a' <= char <= 'z':  # Lowercase letters
        new_pos = (ord(char) - ord('a') - k) % 26 + ord('a')
        decrypted_text += chr(new_pos)
    elif 'A' <= char <= 'Z':  # Uppercase letters
        new_pos = (ord(char) - ord('A') - k) % 26 + ord('A')
        decrypted_text += chr(new_pos)
    else:
        decrypted_text += char  # Non-alphabet characters remain unchanged

# Output the decrypted text
print(decrypted_text)
