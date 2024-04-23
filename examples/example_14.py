# Prompt the user to enter a letter
letter = input("Enter a letter: ")

# Check if the letter is a vowel
if letter.lower() in "aeiou":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
