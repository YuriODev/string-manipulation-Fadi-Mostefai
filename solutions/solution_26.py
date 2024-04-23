# Prompt the user to enter four integers separated by a space.
print("Enter four integers: a, b, c, and d")

a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
c = int(input("Enter 'c': "))
d = int(input("Enter 'd': "))

# Print the multiplication table.
print("\t", end="")
for i in range(c, d + 1):
    print(i, end="\t")
print()

for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()