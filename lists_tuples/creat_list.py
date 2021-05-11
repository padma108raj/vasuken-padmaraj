# Creating the Empty List

elist=[]
print("Type of list",type(elist))
print("Printing Empty List:",elist)

# Creating the list Dynamically 

elist=list(range(0,10,2))
print("Dynamic list is printing:",elist)

s='padmaraj'
l=list(s)
print("Printing the String List:",l)

list=eval(input("Enter list:"))
print("The values of inputList:",list)

# Types of the all the above lists

print("Type of elist:",type(elist))
print("Type of s list:",type(s))
print("Type if the inputList:",type(list))
