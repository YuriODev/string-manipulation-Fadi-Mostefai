# Take input for word A
word_a = input("Enter word A: ")
# Take input for word B
word_b = input("Enter word B: ")

# Check if word B can be constructed from word A
can_construct = True

for char_b in word_b:
    char_b_count = 0
    char_a_count = 0
    for char in word_b:
        if char == char_b:
            char_b_count += 1
    for char in word_a:
        if char == char_b:
            char_a_count += 1
    if char_b_count > char_a_count:
        can_construct = False
        break

# Output result
print("Yes" if can_construct else "No")
