m1=input()
m2=[]
for i in range(len(m1)):
  m2.append(m1[i])
m3=sorted(m2,key=str.lower)
print(''.join(m3))
