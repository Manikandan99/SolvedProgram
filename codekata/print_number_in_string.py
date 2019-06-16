m1=input()
m2=[]
for i in range(len(m1)):
  if(m1[i].isdigit()):
    m2.append(m1[i])
print(''.join(m2))
