mk1,mk2=input().split()
c=0
for i in range(0,len(mk1)):
  if(mk1[i]!=mk2[i]):
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
