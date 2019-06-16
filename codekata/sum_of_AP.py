m1,m2,m3=map(int,input().split())
m4=0
for i in range(1,m3+1):
  m4+=m1+(i-1)*m2
print(m4)
