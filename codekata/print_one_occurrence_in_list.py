n=int(input())
m=[]
mk=list(map(int,input().split()))
for i in mk:
  if(mk.count(i)==1):
    m.append(mk[i])
print(*m,sep=" ")
