f=[1,1]
a=int(input())
if(a==0):
  print("0")
elif(a==1):
  print("1")
else:
  for i in range(2,a):
    f.append(f[i-1]+f[i-2])
  print(*f,sep=' ')
