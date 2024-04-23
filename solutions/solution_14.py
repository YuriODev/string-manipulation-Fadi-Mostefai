text = input("Enter a string: ")

text = text.strip()

# Initialize variables
result = ""  # Start with an empty result string
punctuation = '.!,;:.-?'

# Iterate through the string but stop before the last character to handle the next character logic
for i in range(len(text) - 1):
    current_char = text[i]
    next_char = text[i + 1]

    # Append current character if:
    # 1. It's not a space, or
    # 2. It's a space and the next character is neither a space nor a punctuation
    if current_char != ' ' or (next_char not in punctuation and next_char != ' '):
        result += current_char

# Always append the last character if the text is not empty
if len(text) > 0:
    result += text[-1]

# Print result
print(result)
