def keywordargs(**kwargs):
  for k,v in kwargs.items():
    print(k,"=",v)

keywordargs(n1=10,n2=20,n3=30,n4=40)
keywordargs(rno=100,name="pavan",marks=70,subject="python")
