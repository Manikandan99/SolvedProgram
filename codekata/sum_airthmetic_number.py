m,n,o=map(int,input().split())
if(m>=1 and o<=100000):
  print((m * (2 * n + (m - 1) * o)) // 2)
