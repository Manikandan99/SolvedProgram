mk1,mk2=map(int,input().split())
m3=list(map(int,input().split()))
m4=[]
for i in range(len(m3)):
  if(m3[i]%2!=0):
    m4.append(m3[i])
print(m4[mk2-1])
