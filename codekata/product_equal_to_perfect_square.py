
import math
m1,m2=map(int,input().split())
m3=int(m1*m2)
t=math.sqrt(m3)
if(m3==t*t):
  print("yes")
else:
  print("no")
