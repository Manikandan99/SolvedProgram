b=int(input())
c=b
sum=0
while(b!=0):
  r=b%10
  sum=sum+(r**3)
  b=b//10
if(sum==c):
  print("yes")
else:
  print("no")
