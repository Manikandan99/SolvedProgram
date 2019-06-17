mk1=int(input())
mk2=input().split()
for j in range(len(mk2)-1):
  if(mk2[j]>mk2[j+1]):
    print(j)
    break
