# Creating the dictionary

d={100:"Apple", 200:"Banana",300:"Grapes"}
d1=dict()
print("Dictionary with elements",d)
print("Dictionary without elements",d1)
d[400]="Pineapple"
print("Dictionary with elements",d)

# Access the Dictionary

print("I want value of key 100 d[key]:",d[100])

for k,v in d.items():
   print(k,":",v)

# Deleting the Element from Dictionary

del d[400]
print("Dictionary with elements",d)

