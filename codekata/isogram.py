m1=input()
m2=""
for i in m1:
  if i not in m2:
    m2=m2+i
if(m1==m2):
  print("Yes")
else:
  print("No")
