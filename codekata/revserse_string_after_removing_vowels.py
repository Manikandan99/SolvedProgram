m1=int(input())
mk=input()
l=[]
for i in mk:
  if(i not in "aeiou"):
    l.append(i)
print(*l[::-1],sep="")
