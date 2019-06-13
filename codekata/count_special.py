m=input()
c=0
for i in range(len(m)):
  if(m[i].isdigit() or m[i].isalpha() or m[i]==' '):
    continue
  else:
    c+=1
print(c)
