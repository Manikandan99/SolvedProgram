a=int(input())
m=0
if(a==2 or a==3):
  print("yes")
else:
  for i in range(2,a):
    if(a%i==0):
      m=0
      print("no")
      break
    else:
     m=1
     continue  
  if(m!=0):
    print("yes")
