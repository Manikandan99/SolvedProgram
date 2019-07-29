mk=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,mk):
  l1.append(l[i])
  l2.append(l.count(l[i]))
m1=min(l2)
m2=l2.index(m1)
print(l1[m2])
