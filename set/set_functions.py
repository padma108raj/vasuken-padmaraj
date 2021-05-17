# Demo of add() in set
s={10,20,30,40}
s.add(50)
print(s,type(s))

# Demo of update() 

l=[40,50,60,70,80]
s.update(l,range(5))
print(s)

# Demo of Copy()
# Copy is used clone : Return the copy of set

s1=s.copy()
print("Elements in s1",s1)
s1.clear()
print(s1)
