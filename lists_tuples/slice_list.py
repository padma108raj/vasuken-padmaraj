s='padmaraj'
l=list(s)
print("Printing the String List:",l)

print("slicing:",s[::])
print("slicing[1:5]",s[1:5])
print("slicing[8:1:-1]",s[8:1:-1])
print("slicing[::2]",s[::2])
print("slicing to reverse the string",s[::-1])

for char in s:
  print(char,end="$$$")
