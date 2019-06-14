m1=int(input())
m=0
if(m1==2 or m1==3):
  print("no")
else:
  for i in range(2,m1):
    if(m1%i==0):
      m=0
      print("yes")
      break
    else:
     m=1
     continue  
  if(m!=0):
    print("no")
