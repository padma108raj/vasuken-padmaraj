"""
Approach1

"""

l=eval(input("Enter list of value:"))
s=set(l)
print(s)

""" 
Approcah 2

"""

l=eval(input("Enter list of values:"))
l1=[]
for x in l:
  if x not in l1:
    l1.append(x)

print(l1)


