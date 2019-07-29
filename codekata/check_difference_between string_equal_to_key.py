m,n,d=map(str,input().split())
t=0
r=int(d)
for i in range(0,len(m)):
  if(m[i]!=n[i]):
    t=t+1
if(t==r):
  print("yes")
else:
  print("no")
