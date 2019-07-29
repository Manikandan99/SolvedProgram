mk=input()
l=[]
for i in mk:
  l.append(i)
print(l)
if(l.count('(')==l.count(')')):
  print("yes")
else:
  print("no")
