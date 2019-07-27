a=int(input())
l=list(map(int,input().split()))
for i in range(0,a,2):
  for j in range(i+2,a,2):
    if(l[i]>l[j]):
      l[j],l[i]=l[i],l[j]

for i in range(1,a,2):
  for j in range(i+2,a,2):
    if(l[i]>l[j]):
      l[j],l[i]=l[i],l[j]

print(*l,sep=" ")

#input:6
8 5 6 1 3 4
#output: 3 1 6 4 8 5
