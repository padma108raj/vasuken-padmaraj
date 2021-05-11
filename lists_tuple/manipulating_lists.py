list=[]
list.append("Apple")
list.append("Banana")
list.append("Grapes")

print("Items in the list",list)
list.insert(1,"Dragon Fruit")
print(list)
list.insert(10,"Peanuts")
print(list)
print("="*60)
print("Extend Function")

food_items=["Burger","Chicken","Sandwitch"]

list.extend(food_items)
#list.extend("Mushroom")
print(list)

print("="*60)
print("Remove Functions")
print("="*60)

list.remove("Sandwitch")
print(list)
print("="*60)
print("POP Functions")
print("="*60)
list.pop()
list.pop(0)
print(list)

print("="*60)
print("Aliasing")
print("="*60)

a=[1,2,3,4]
b=a

print("Memory Location of the a list:",id(a))
print("Memory Location of the b list:",id(b)) 
print("list a:",a)
a.append(5)
print("list a:",a)
print("list b:",b) 
print("="*60)
print("Cloning using the Copy()")
print("="*60)

b=a.copy()
a.append(7)
b.append(6)

print("list a:",a)
print("list b:",b) 

