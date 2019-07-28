m,n=map(int,input().split())
mk=[]
for num in range(m,n+1):
   if(num==2):
       mk.append(num)
   elif(num > 1):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
          mk.append(num)
print(len(mk))
