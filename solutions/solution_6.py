# Prompt the user to enter a message.
message = input("Enter a message: ")

# Check if the message contains only letters.
if message.isalpha():
    print("Your message includes letters only.")
# Check if the message contains only digits.
elif message.isdigit():
    print("Your message includes numbers only.")
# Check if the message contains both letters and digits.
else:
    print("Your message includes numbers and letters.")
