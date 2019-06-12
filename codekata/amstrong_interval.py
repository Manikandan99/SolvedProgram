a,c=map(int,input().split())
for b in range(a,c):
  m=b
  sum1=0
  while(b!=0):
    r=b%10
    sum1=sum1+(r**3)
    b=b//10
  if(sum1==m):
    print(m,end=' ')
