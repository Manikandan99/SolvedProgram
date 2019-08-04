mk1,mk2=input().split()
k=0
f=0
for i in range(0,len(mk1)):
    if(mk1.count(mk1[i])==mk2.count(mk2[i])):
      f=1
    else:
      k=1
if(f==1 and k==0):
  print("yes")
else:
  print("no")
