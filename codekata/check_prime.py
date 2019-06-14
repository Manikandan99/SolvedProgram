m1=int(input())
k=0
if(m1==2 or m1==3):
  print("yes")
else:
  for i in range(2,m1):
    if(m1%i==0):
      k=0
      print("no")
      break
    else:
     k=1
     continue  
  if(k!=0):
    print("yes")
