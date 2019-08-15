n=int(input())
mk=list(map(int,input().split()))
for i in range(0,len(mk)):
  if(mk[i]==i):
    print(mk[i],end=" ")
