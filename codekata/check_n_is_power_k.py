mk1,mk2=map(int,input().split())
f=0
for i in range(0,mk1):
  if(mk2**i==mk1):
    f=f+1
if(f>0):
  print("yes")
else:
  print("no")
