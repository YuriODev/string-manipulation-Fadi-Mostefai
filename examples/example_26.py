# Input a sentence from the user
sentence = input("Enter a sentence ending with a period: ")

# Remove the trailing period for ease of processing
sentence = sentence[:-1]

# Initialize variables to find the shortest word and its length
shortest_word = ''
min_length = len(sentence)
current_word = ''

# Traverse each character in the sentence
for char in sentence:
    # Build a word while iterating through alphabetical characters
    if char.isalpha():
        current_word += char
    else:
        # Check if a word was built and is shorter than the known shortest word
        if current_word and (len(current_word) < min_length):
            shortest_word = current_word
            min_length = len(current_word)
        # Reset current word after saving
        current_word = ''

# Final check for the last word in case the sentence ends directly after it
if current_word and (len(current_word) < min_length):
    shortest_word = current_word
    min_length = len(current_word)

# Output the shortest word and its length
print(f'{shortest_word} {min_length}')
