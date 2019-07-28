a=input()
l=[]
t=0
for i in a:
  l.append(i)
for i in range(0,len(a)):
  if(i%2!=0):
    l[i-1],l[i]=l[i],l[i-1]
print(*l,sep="")
