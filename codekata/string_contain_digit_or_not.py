mk=input()
f=0
for i in mk:
  if(not i.isdigit()):
    f=f+1
if(f>0):
  print("no")
else:
  print("yes")
