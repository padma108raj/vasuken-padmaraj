d=dict({100:"apple",200:"Grapes",300:"Oranges"})
print("Lets print the d.key()",d.keys()) #([list of keys])
print("Lets print the d.value()",d.values()) #([List of Values])

# d.items() - output [(k,v),(k,v),(k,v)]

print("Lets print the d.items()",d.items())

for k,v in d.items():
  print(k,":",v)

# Cloning Dictionary

d1=d.copy()
print(d1)

# Dictionary Comprehensions

squares={x:x*x for x in range(1,11)}
print(squares)
