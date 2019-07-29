mk=input()
l=[]
for i in mk:
  l.append(i)
if(l.count('(')==l.count(')')):
  print("yes")
else:
  print("no")
