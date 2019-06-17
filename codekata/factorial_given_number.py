mk1=int(input())
if(mk1==0 or mk1==1):
  print(1)
else:
  mk2=1
  for i in range(1,mk1+1):
   mk2=mk2*i
  print(mk2)
