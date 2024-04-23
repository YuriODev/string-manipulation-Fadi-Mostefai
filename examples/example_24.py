# Input string of digits
number = input("Enter a string of digits: ")

# Start from the end and insert commas every three digits
formatted_number = ''
count = 0

# Reverse iterate over the number string
for i in range(len(number) - 1, -1, -1):
    formatted_number = number[i] + formatted_number
    count += 1
    if count == 3 and i != 0:  # Avoid adding a comma at the start
        formatted_number = ',' + formatted_number
        count = 0

# Print the formatted number
print(formatted_number)
