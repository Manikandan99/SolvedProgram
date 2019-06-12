a=int(input())
if(a==0 or a==1):
  print(1)
else:
  m=1
  for i in range(1,a+1):
   m=m*i
  print(m)
