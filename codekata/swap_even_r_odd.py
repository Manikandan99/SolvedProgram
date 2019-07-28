m1=input()
m2=[]
t=0
for i in m1:
  m2.append(i)
for i in range(0,len(m1)):
  if(i%2!=0):
    m2[i-1],m2[i]=m2[i],m2[i-1]
print(*m2,sep="")
