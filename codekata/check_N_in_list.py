m1,m2=map(int,input().split())
uv=list(map(int,input().split()))
k=0
for i in range(len(uv)):
  if(m2==uv[i]):
    k=0
    print("yes")
    break
  else:
    k=1
    continue
if(k==1):
  print("no")
