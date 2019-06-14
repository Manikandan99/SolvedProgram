m1=input()
m2=""
m3=""
for i in range(0,len(m1)):
  if(i%2==0):
    m2=m2+m1[i]
  else:
    m3=m3+m1[i]
print(m2,m3)
