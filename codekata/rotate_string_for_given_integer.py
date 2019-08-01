mk1,mk2=map(str,input().split())
mk3=int(mk2)
m=[]
for i in mk1 :
  m.append(i)
mk4=m[-mk3:]+m[:-mk3]
print(*mk4,sep="")
