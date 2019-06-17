m1=int(input())
m2=input().split()
for i in range(len(m2)-1):
  if(m2[i]>m2[i+1]):
    print(i)
    break
