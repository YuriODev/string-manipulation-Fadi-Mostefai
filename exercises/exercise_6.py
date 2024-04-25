# Your solution to Exercise 6

string = str(input())
num = False
str = False
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = lowerletters.upper()
count = 0
while count < len(string):
  try:
    if 0 <= int(string[count]) <= 9:
      num = True
  except:
    if string[count] in lowerletters or string[count] in upperletters:
      str = True
    pass
  count += 1

if num:
  if str:
    print("Your message includes numbers and letters.")
  else:
    print("Your message includes numbers only.")
else:
  print("Your message includes letters only.")
