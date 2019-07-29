m1=input()
m2=""
for i in m1:
  if(i=='x' or i=='X'):
    print("A",end="")
  elif(i=='y' or i=='Y'):
    print("B",end="")
  elif(i=="z" or i=='Z'):
    print("C",end="")
  else:
    print(chr(ord(i)+3),end="")
