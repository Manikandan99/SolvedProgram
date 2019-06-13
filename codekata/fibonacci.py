f=[1,1]
a=int(input())
for i in range(2,a):
  f.append(f[i-1]+f[i-2])
print(*f,sep=' ')
