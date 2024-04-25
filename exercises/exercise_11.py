# Your solution to Exercise 11
string = str(input())
index_store = 0
for index in range(len(string) - 1, 1, -1):
  if string[index] == " ":
    index_store = index
    break
if index_store == 0:
  print(string[:-1])
else:
  print(string[index_store + 1:])