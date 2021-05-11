# Two numbers as input
# Check the Biggest Number and give the result

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Second Number:"))

if n1 > n2 and n1 > n3:
  print("Biggest Number is:",n1)
elif n2 > n3:
  print("Biggent Number is:",n2)
else:
  print("Biggest Number is:",n3) 
