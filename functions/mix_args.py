special_variable=100

def f1(*s):
  f1_variable=300
  print(special_variable)
  for s1 in s:
    print(s1)

def f2():
  print(special_variable)

f1(10)
f1(10,20,40,30)
f1(10,"A",30,"B")
f1()
f2()
