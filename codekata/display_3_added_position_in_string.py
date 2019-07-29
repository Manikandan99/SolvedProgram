mk=input()
l=[]
for i in mk:
  l.append(i)
t=0
for x in range(0,len(mk)):
  if(x==t):
    print(l[x],end="")
    t=t+3
