mk1,mk=map(str,input().split())
mk3=int(mk)
m=[]
for i in mk1:
  m.append(i)
mk5=m[-mk3:]+m[:-mk3]
print(*mk5,sep="")
