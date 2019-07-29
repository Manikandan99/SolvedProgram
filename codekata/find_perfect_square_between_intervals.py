import math
m1,m2=map(int,input().split())
c=0
for i in range(m1,m2+1):
  t1=int(i)
  t2=math.sqrt(i)
  if(t1==t2*t2):
    c=c+1
print(c)
