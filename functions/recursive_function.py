def fact(n):
  if n==0: 
    result=1
  else:
    result=n*fact(n-1)
  return result

print("Factorial:",fact(7))
print("Factorial of 100:",fact(100))

