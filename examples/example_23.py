# Input string A
a = input("Enter string A: ")
# Input string B
b = input("Enter string B: ")

count = 0
# Use a loop to manually check for occurrences
for i in range(len(a) - len(b) + 1):  # Only go up to where B can fully fit in A
    if a[i:i+len(b)] == b:  # Check if the substring of A equals B
        count += 1

# Print the number of occurrences
print(count)
