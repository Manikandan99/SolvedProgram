l=['a','e','i','o','u']
m=input()
p=0
for i in range(len(m)):
  if(l.count(m[i])!=0):
    print("yes")
    p=1
    break
if(p!=1):
  print("no")
