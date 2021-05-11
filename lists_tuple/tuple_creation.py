"""
 Creating the Tuples

"""

t=10,20,30,40
print(t)
print(type(t))

t2=10
t3=10,

print("t2 type:",type(t2))
print("t3 type:",type(t3))
"""
1. t=()- yes 2. t=10,20,30,40 - yes  3. t=10 - No  4. t=10, - yes 5. t=(10) - No 6. t=(10,) -yes  7.t=(10,20,30,40) -yes
"""

t=tuple(range(1,200,7))
print(t)
