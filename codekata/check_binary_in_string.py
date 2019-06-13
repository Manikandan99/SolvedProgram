m1=input()
t=0
for i in range(len(m1)):
  if(m1[i]!='0' and m1[i]!='1'):
    t=1
if(t!=1):
  print("yes")
else:
  print("no")
