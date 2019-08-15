n=int(input())
mk=list(map(int,input().split()))
m=[]
for i in mk:
  if(mk.count(i)>1):
    m.append(i)
l=len(m)
if(l>0):
  print(*set(m),sep=" ")
else:
  print("unique")
