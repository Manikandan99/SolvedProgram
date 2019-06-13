f=[1,1]
m=int(input())
for i in range(2,m):
  f.append(f[i-1]+f[i-2])
print(*f,sep=' ')
