mk=input()
b=""
t=""
for i in mk:
  if(i==i.upper()):
    b=i.lower()
    t=t+b
  else:
    b=i.upper()
    t=t+b
print(t)
