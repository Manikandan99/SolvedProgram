mk=int(input())
mk2=0
for i in range(2,mk):
  if(mk%i==0):
    mk2=1
    break
if(mk2==0):
  print("no")
else:
  print("yes")
