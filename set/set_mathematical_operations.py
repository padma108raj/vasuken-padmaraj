""" 
This is to Demo Union , intersection & Difference

"""
x={10,20,30,40}
y={30,40,50,60}

print("Union:",x.union(y))

print("Intersection",x.intersection(y))

print("Difference:",x.difference(y))

print("Symmetric Difference:",x.symmetric_difference(y))

print(x^y)
