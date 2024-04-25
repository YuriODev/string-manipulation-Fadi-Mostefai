# Your solution to Exercise 9
string = str(input())
firstletter = string[0]
lastletter = string[-1]
if string[1] == firstletter:
  newstring = string.lstrip(firstletter)
  newstring_reversed = newstring[::1]
  newstring_reversed += firstletter
  newstring = newstring_reversed[::-1]
else:
  newstring = string.lstrip(firstletter)
if string[-2] == lastletter:
  newstring = newstring.rstrip(lastletter)
  newstring += lastletter
else:
  newstring = newstring.rstrip(lastletter)
newstring += firstletter
newstring_reversed = newstring[::-1]
newstring_reversed += lastletter
newstring = newstring_reversed[::-1]
print(newstring)