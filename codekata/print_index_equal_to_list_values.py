n=int(input())
m=[]
mk=list(map(int,input().split()))
for i in range(0,len(mk)):
  if(mk[i]==i):
    m.append(mk[i])
if(len(m)!=0):
  print(*m,sep=" ")
else:
  print("-1")
